import os
import io
import json
import logging
from typing import Optional, List, Dict, Any, Union
import pandas as pd
import boto3
from botocore.client import Config
from dotenv import load_dotenv

# Automatically load .env from project root if present
load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("DataLakeStorage")


class DataLakeStorage:
    """
    S3-Compatible Data Lake Storage Client for Supabase Storage / Cloudflare R2 / AWS S3.
    Operates on open columnar Parquet and raw JSON layers (Bronze, Silver, Gold).
    """

    def __init__(
        self,
        endpoint_url: Optional[str] = None,
        access_key_id: Optional[str] = None,
        secret_access_key: Optional[str] = None,
        default_bucket: Optional[str] = None,
        region_name: str = "us-east-1",
    ):
        self.endpoint_url = endpoint_url or os.getenv("S3_ENDPOINT_URL")
        self.access_key_id = access_key_id or os.getenv("S3_ACCESS_KEY_ID")
        self.secret_access_key = secret_access_key or os.getenv("S3_SECRET_ACCESS_KEY")
        self.default_bucket = default_bucket or os.getenv("S3_BUCKET_NAME", "wsl-data-lake")

        if not all([self.endpoint_url, self.access_key_id, self.secret_access_key]):
            raise ValueError(
                "Missing S3 Data Lake credentials. Ensure S3_ENDPOINT_URL, S3_ACCESS_KEY_ID, "
                "and S3_SECRET_ACCESS_KEY are defined in your .env file."
            )

        self.s3_client = boto3.client(
            "s3",
            endpoint_url=self.endpoint_url,
            aws_access_key_id=self.access_key_id,
            aws_secret_access_key=self.secret_access_key,
            region_name=region_name,
            config=Config(
                s3={"addressing_style": "path"},
                signature_version="s3v4",
                connect_timeout=8,
                read_timeout=15,
            ),
        )
        logger.info(f"Connected to Data Lake storage (default bucket: {self.default_bucket})")

    def _get_bucket(self, bucket: Optional[str] = None) -> str:
        b = bucket or self.default_bucket
        if not b:
            raise ValueError("No bucket specified and no default S3_BUCKET_NAME found.")
        return b

    def upload_parquet(
        self,
        df: pd.DataFrame,
        key: str,
        bucket: Optional[str] = None,
        compression: str = "snappy",
    ) -> str:
        """Upload a pandas DataFrame as a columnar Parquet file into the Data Lake."""
        target_bucket = self._get_bucket(bucket)
        buffer = io.BytesIO()
        df.to_parquet(buffer, engine="pyarrow", compression=compression, index=False)
        buffer.seek(0)

        self.s3_client.put_object(
            Bucket=target_bucket,
            Key=key,
            Body=buffer.getvalue(),
            ContentType="application/octet-stream",
        )
        logger.info(f"Successfully uploaded Parquet to {target_bucket}/{key} ({len(df)} rows)")
        return f"s3://{target_bucket}/{key}"

    def download_parquet(self, key: str, bucket: Optional[str] = None) -> pd.DataFrame:
        """Download and deserialize a Parquet file from the Data Lake into a pandas DataFrame."""
        target_bucket = self._get_bucket(bucket)
        response = self.s3_client.get_object(Bucket=target_bucket, Key=key)
        content = response["Body"].read()
        df = pd.read_parquet(io.BytesIO(content), engine="pyarrow")
        logger.info(f"Downloaded Parquet from {target_bucket}/{key} ({len(df)} rows)")
        return df

    def upload_json(
        self,
        data: Union[Dict[str, Any], List[Any]],
        key: str,
        bucket: Optional[str] = None,
    ) -> str:
        """Upload raw semi-structured JSON payload (Bronze layer dump)."""
        target_bucket = self._get_bucket(bucket)
        payload = json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8")

        self.s3_client.put_object(
            Bucket=target_bucket,
            Key=key,
            Body=payload,
            ContentType="application/json",
        )
        logger.info(f"Successfully uploaded raw JSON to {target_bucket}/{key}")
        return f"s3://{target_bucket}/{key}"

    def download_json(self, key: str, bucket: Optional[str] = None) -> Any:
        """Download raw JSON payload from the Data Lake."""
        target_bucket = self._get_bucket(bucket)
        response = self.s3_client.get_object(Bucket=target_bucket, Key=key)
        content = response["Body"].read().decode("utf-8")
        return json.loads(content)

    def list_objects(self, prefix: str = "", bucket: Optional[str] = None) -> List[str]:
        """List object keys in the Data Lake with a given prefix."""
        target_bucket = self._get_bucket(bucket)
        paginator = self.s3_client.get_paginator("list_objects_v2")
        keys = []
        for page in paginator.paginate(Bucket=target_bucket, Prefix=prefix):
            for item in page.get("Contents", []):
                keys.append(item["Key"])
        return keys

    def delete_object(self, key: str, bucket: Optional[str] = None) -> bool:
        """Delete an object from the Data Lake."""
        target_bucket = self._get_bucket(bucket)
        self.s3_client.delete_object(Bucket=target_bucket, Key=key)
        logger.info(f"Deleted object {target_bucket}/{key}")
        return True
