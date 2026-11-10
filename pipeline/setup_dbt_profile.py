"""
WSL Data Platform - dbt Profile Generator
=========================================
Reads DATABASE_URL from .env and generates dbt_wsl/profiles.yml
so dbt connects seamlessly to Supabase PostgreSQL without manual credential editing.
"""
import os
import sys
from urllib.parse import urlparse
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DBT_DIR = PROJECT_ROOT / "dbt_wsl"
DBT_DIR.mkdir(parents=True, exist_ok=True)

db_url = os.getenv("DATABASE_URL")
if not db_url:
    print("❌ ERROR: DATABASE_URL not found in .env")
    sys.exit(1)

clean_url = db_url.replace("?pgbouncer=true", "").replace("&pgbouncer=true", "")
parsed = urlparse(clean_url)
host = parsed.hostname
port = parsed.port or 5432
user = parsed.username
password = parsed.password
dbname = parsed.path.lstrip("/").split("?")[0] or "postgres"

profile_yaml = f"""wsl_profile:
  target: dev
  outputs:
    dev:
      type: postgres
      host: "{host}"
      user: "{user}"
      password: "{password}"
      port: {port}
      dbname: "{dbname}"
      schema: "analytics"
      threads: 4
      keepalives_idle: 0
      sslmode: prefer
"""

profile_path = DBT_DIR / "profiles.yml"
with open(profile_path, "w", encoding="utf-8") as f:
    f.write(profile_yaml)

print(f"✅ Generated {profile_path} successfully from DATABASE_URL!")
