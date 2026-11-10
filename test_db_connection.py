"""
Test Postgres connection from terminal
"""
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()
url = os.getenv("DATABASE_URL")

print("Testing connection to PostgreSQL...")
try:
    conn = psycopg2.connect(url, connect_timeout=8)
    print("✅ SUCCESS: Connected to Supabase PostgreSQL Database!")
    conn.close()
except Exception as e:
    print("❌ Connection Error:")
    print(e)
