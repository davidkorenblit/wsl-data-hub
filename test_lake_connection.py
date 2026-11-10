"""
WSL Data Hub - Data Lake Smoke Test
===================================
Tests connectivity and round-trip Parquet serialization against the Supabase S3 Data Lake.
"""
import sys
import pandas as pd
from wsl_lake.storage import DataLakeStorage

def main():
    print("=" * 60)
    print("  🚀 Starting Data Lake Smoke Test (Supabase Storage)")
    print("=" * 60)

    try:
        lake = DataLakeStorage()
    except Exception as e:
        print(f"\n❌ FAILED TO INITIALIZE DATA LAKE CLIENT:")
        print(f"   {e}")
        print("\nPlease check your .env file keys (S3_ENDPOINT_URL, S3_ACCESS_KEY_ID, S3_SECRET_ACCESS_KEY).")
        sys.exit(1)

    test_key = "smoke_test/connection_test.parquet"
    test_df = pd.DataFrame([
        {"team": "Chelsea Women", "season": "2026/27", "status": "Data Lake Online", "points": 18},
        {"team": "Arsenal Women", "season": "2026/27", "status": "Data Lake Online", "points": 15},
        {"team": "Tottenham Hotspur Women", "season": "2026/27", "status": "Data Lake Online", "points": 12},
    ])

    print(f"\n1. Uploading test Parquet file to: {test_key}...")
    try:
        s3_uri = lake.upload_parquet(test_df, key=test_key)
        print(f"   ✅ Upload successful! URI: {s3_uri}")
    except Exception as e:
        print(f"   ❌ Upload failed: {e}")
        sys.exit(1)

    print(f"\n2. Downloading and verifying test Parquet file...")
    try:
        downloaded_df = lake.download_parquet(key=test_key)
        assert len(downloaded_df) == len(test_df), "Row count mismatch!"
        assert list(downloaded_df["team"]) == list(test_df["team"]), "Data content mismatch!"
        print(f"   ✅ Download & verification successful! ({len(downloaded_df)} rows matched)")
    except Exception as e:
        print(f"   ❌ Download verification failed: {e}")
        sys.exit(1)

    print(f"\n3. Cleaning up test object from lake...")
    try:
        lake.delete_object(key=test_key)
        print(f"   ✅ Cleaned up {test_key}")
    except Exception as e:
        print(f"   ⚠️ Warning during cleanup: {e}")

    print("\n" + "=" * 60)
    print("  🎉 DATA LAKE IS FULLY OPERATIONAL!")
    print("=" * 60)

if __name__ == "__main__":
    main()
