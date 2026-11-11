# ⚽ WSL Data Hub · Data Platform Roadmap
> **סטטוס פרויקט:** End-to-End ELT Pipeline הושלם ומאומת במלואו בענן! 🚀  
> **ארכיטקטורה:** Lakehouse (Supabase S3 Data Lake + Postgres Data Warehouse + dbt Core + GitHub Actions Automation).

---

## 📍 מה הושלם בפועל? (Done ✅)

| שלב | רכיב | מה בוצע? | סטטוס |
| :--- | :--- | :--- | :--- |
| **תשתית** | **S3 Data Lake** | הקמת Bucket `wsl-data-lake`, הגדרת S3 Credentials, מודול `wsl_lake` | ✅ מאומת ופעיל |
| **תשתית** | **PostgreSQL DW** | יצירת סכמות `raw` ו-`analytics`, חיבור דרך Pooler (IPv4) | ✅ מחובר ופעיל |
| **שלב 1 (E&L)** | **Ingestion Engine** | `pipeline/ingest.py` עם חוזי Pydantic (`MatchRecord`, `StandingRecord`) | ✅ שואב ושומר ל-Lake |
| **שלב 2 (Raw)** | **Warehouse Loader** | `pipeline/load_raw.py` טוען Parquet מה-Lake לתוך סכמת `raw` ב-DB | ✅ 182 משחקים + 14 קבוצות |
| **שלב 3 (T)** | **dbt Transformations** | מודלי Staging, Dims (`dim_teams`), Facts (`fct_league_standings`) | ✅ 12/12 טסטים עברו |
| **שלב 4 (Serving)**| **Site Exporter** | `pipeline/export_to_site.py` מושך מטבלת ה-Gold ומעדכן את האתר | ✅ מעדכן `_data/` אוטומטית |
| **אוטומציה** | **Master Runner** | `run_pipeline.py` מריץ את כל 4 השלבים ברצף בפקודה אחת | ✅ מוכן להרצה |
| **מיגרציה** | **Lake Backfill** | `pipeline/backfill_lake.py` ממיר 146 קבצי JSON ו-CSV ל-Parquet ב-Lake | ✅ מוכן להרצה |
| **CI/CD** | **GitHub Actions** | `.github/workflows/data_pipeline.yml` תזמון שבועי אוטומטי (Monday 04:00) | ✅ מוכן לפריסה |

---

## 🎯 איך הדאטה הישן מאוחסן ומסודר?

```mermaid
flowchart TD
    subgraph Local["מחשב מקומי (146 קבצי JSON ו-29 CSV)"]
        L1["data/raw/squads/*.csv"]
        L2["data/raw/players/*.csv"]
        L3["data/raw/fotmob/teams/*.json"]
        L4["data/raw/fotmob/players/cache/*.json"]
    end

    subgraph Lake["Cloud Data Lake (Supabase S3)"]
        B1["bronze/squad_stats/*.parquet"]
        B2["bronze/player_stats/*.parquet"]
        B3["bronze/fotmob/teams/*.json"]
        B4["bronze/fotmob/players/*.json"]
    end

    subgraph Warehouse["Supabase PostgreSQL (dbt)"]
        W1["raw schema (טבלאות גולמיות)"]
        W2["analytics schema (dim_players, dim_teams, fct_player_stats)"]
    end

    Local -->|"pipeline/backfill_lake.py"| Lake
    Lake -->|"pipeline/load_raw.py"| W1
    W1 -->|"dbt build"| W2
```

---

## 🔮 משימה להמשך: פתרון גנרי לנתוני מיקרו (Micro-Data Ingestion & Serving)

### 1. האתגר הקיים (The Problem)
* **פער ברמת הרזולוציה:** הפייפליין האוטומטי וה-Data Lake מטפלים כרגע מצוין בנתוני **מאקרו** (טבלת ליגה, תוצאות משחקים ולוח זמנים).
* **התלות השבועית בכתיבת הטורים:** הטורים והניתוחים הטקטיים נשענים על **נתוני מיקרו עמוקים** (נגיעות ברחבת היריב, פעולות הגנה/חילוצים, מפות בעיטות עם קואורדינטות, עמדות ממוצעות, ומאבקי קרקע/אוויר).
* **צוואר הבקבוק:** כיום, בכל שבוע מחדש נוצר צורך לייצר סקריפטים אד-הוק וספציפיים (`fetch_roundX_matches.py`, `inspect_palace_whu.py`, `inspect_bha_cry_players.py` וכדומה), במקום שהמידע יהיה זמין ושלִיף ישירות מתוך שכבת הנתונים.

### 2. כיוון הפתרון שנבחן (Concept & Vision)
* **מיפוי מכנה משותף של סקריפטי העבר:** לעבור על כל סקריפטי ה-`inspect_*` וה-`fetch_*` ההיסטוריים בפרויקט, לזהות את הליבה (כ-80%–90% מהמדדים הנפוצים שחוזרים בכל שבוע), ולחלץ מהם סכמה קבועה.
* **מנוע Ingestion גנרי לפרטי משחק:** הפיכת משיכת ה-`matchDetails` מ-FotMob לחלק מובנה מהפייפליין הראשי, כך שכל משחק יפורק אוטומטית ל:
  * מפות בעיטות (Shotmaps) מובנות.
  * סטטיסטיקות שחקניות פר-משחק (`fct_match_player_stats` ב-Parquet/Warehouse).
* **גמישות לחריגים (Extensibility):** המנגנון יספק את רוב הנתונים הסטנדרטיים "מהקופסה", תוך שמירה על ה-Raw JSON ב-Lake למקרים שבהם נרצה לתחקר חריגות או זוויות אנליטיות מיוחדות.

> **סטטוס:** 📌 מתוכנן לתעדוף ולתכנון ארכיטקטוני לאחר השלמת הטורים השוטפים.

