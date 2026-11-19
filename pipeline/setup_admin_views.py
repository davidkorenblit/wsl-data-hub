"""
WSL Data Platform - Admin BI Views & Permissions (Supabase PostgREST)
=====================================================================
Creates read-only views in the `public` schema over the Gold dbt marts
(`analytics_analytics.*`) and restricts access strictly to `authenticated`
users (revoking all privileges from `anon` and `PUBLIC`).

Safe to re-run after every `dbt build` (idempotent).
"""
import os
import logging
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("AdminViews")


def _get_clean_db_url() -> str:
    db_url = os.getenv("DATABASE_URL", "")
    if not db_url:
        raise ValueError("DATABASE_URL is missing in .env")
    clean_db_url = db_url.replace("?pgbouncer=true", "").replace("&pgbouncer=true", "")
    if clean_db_url.startswith("postgres://"):
        clean_db_url = clean_db_url.replace("postgres://", "postgresql+psycopg2://", 1)
    elif clean_db_url.startswith("postgresql://"):
        clean_db_url = clean_db_url.replace("postgresql://", "postgresql+psycopg2://", 1)
    if "sslmode" not in clean_db_url:
        separator = "&" if "?" in clean_db_url else "?"
        clean_db_url += f"{separator}sslmode=require"
    return clean_db_url


ADMIN_VIEWS_SQL = """
-- 1. Create Gold BI Views in public schema (exposed to Supabase PostgREST)
CREATE OR REPLACE VIEW public.v_match_player_stats AS
SELECT * FROM analytics_analytics.fct_match_player_stats;

CREATE OR REPLACE VIEW public.v_shots AS
SELECT * FROM analytics_analytics.fct_shots;

CREATE OR REPLACE VIEW public.v_league_standings AS
SELECT * FROM analytics_analytics.fct_league_standings;

-- 2. Lock down permissions: ZERO access for anonymous / public visitors
REVOKE ALL ON public.v_match_player_stats FROM PUBLIC, anon;
REVOKE ALL ON public.v_shots FROM PUBLIC, anon;
REVOKE ALL ON public.v_league_standings FROM PUBLIC, anon;

-- 3. Grant read-only SELECT strictly to authenticated admin user(s)
GRANT SELECT ON public.v_match_player_stats TO authenticated;
GRANT SELECT ON public.v_shots TO authenticated;
GRANT SELECT ON public.v_league_standings TO authenticated;
"""


def ensure_admin_views():
    """Creates/refreshes authenticated-only BI views in Supabase public schema."""
    engine = create_engine(_get_clean_db_url())
    logger.info("Creating/refreshing authenticated-only Admin BI views in public schema...")
    with engine.begin() as conn:
        conn.execute(text(ADMIN_VIEWS_SQL))
    logger.info("✅ Admin BI views ready: public.v_match_player_stats, public.v_shots, public.v_league_standings")


if __name__ == "__main__":
    ensure_admin_views()
