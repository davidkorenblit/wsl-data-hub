# WSL Data Hub — Agent Rules

## DB Query & SQL Practice Protocol

Whenever a session requires **pulling existing data from the database** or **checking whether data exists in the database** (e.g., querying Supabase/PostgreSQL tables such as `analytics.fct_match_player_stats`, `analytics.fct_shots`, `analytics.fct_league_standings`, `analytics.dim_teams`, or `raw.*`) — and **not** during general brainstorming:

1. **Always pause and ask first:**  
   "האם המטרה כרגע היא השלמת הניתוח בלבד, או גם תרגול SQL?"
2. **If the user chooses analysis only:** pull/check the data directly from the DB and continue building the analysis or website.
3. **If the user chooses SQL practice:** **do not write the SQL query for them.** Instead, work in one of two modes as requested:
   - **Guided Exercise Mode:** translate the user's analytical idea into a clear SQL exercise (tables, filters, expected output schema) so the user writes the SQL manually.
   - **Independent Thinking Mode:** let the user draft both the pseudo-logic and the SQL query themselves; provide review, hints, and refinements only when asked.

## SQL Review Rubric (User-Written SQL)

When reviewing SQL written manually by the user, always evaluate across three dimensions:
1. **Correctness & Grain:** check that `JOIN`s and aggregations do not accidentally duplicate rows or distort totals.
2. **Edge Cases:** verify safe division (`NULLIF(..., 0)`), `NULL` handling (`COALESCE`), and explicit minimum-minutes filters where relevant.
3. **Readability & Idiomatic PostgreSQL:** favor clear CTEs over deeply nested subqueries, meaningful aliases, and clean formatting.

## Data Integrity

- **Never fabricate or estimate stats:** every published metric, score, minute count, or xG figure must trace back to a verified query against the database or an existing file in `_data/` or `data/`.
- **Safe calculations:** always guard Per-90 and percentage formulas against division by zero and state the minimum-minutes threshold when comparing players.

## Site Architecture, RTL & Verification

- **Hebrew-first RTL + English mirror:** the site is Hebrew-first (RTL) with English pages under `en/`. Before creating a new page or section, confirm whether an `en/` counterpart is needed right away or Hebrew-only for now.
- **Single source of truth:** build on `dbt_wsl/` and `pipeline/` rather than reviving legacy one-off scripts in `scripts/archive/`.
- **Lightweight verification:** run `dbt test` after modifying dbt models, and verify JSON/image paths and RTL layout before wrapping up site changes.

## Secrets & Security

- Never echo, hardcode, or commit credentials, API keys, or `.env` values.
