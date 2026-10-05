# פייפליין עדכון מחזור משחקים (Gameweek Sync Pipeline)

מדריך תמציתי ומהיר לעדכון שוטף של תוצאות המחזור, לוח המשחקים וטבלת הליגה באתר בסיום כל מחזור ב-WSL.

---

## 1. פקודת ההרצה (One-Liner)

בסיום משחקי המחזור, מריצים מהטרמינל (שורש הפרויקט):

```bash
python scripts/sync_matchweek.py
```

> **בדיקה מקדימה (Dry-Run):** להצגת התוצאות והטבלה בטרמינל ללא שינוי קבצים:
> `python scripts/sync_matchweek.py --dry-run`

---

## 2. קבצים שמתעדכנים אוטומטית

הסקריפט שואב את נתוני ה-WSL העדכניים מ-FotMob (`league_id = 9227`) ומעדכן 4 קבצי ליבה:

| קובץ יעד | תפקיד |
| :--- | :--- |
| `_data/league_table.json` | טבלת הליגה המעודכנת (נקודות, שערים, מיקום ו-slugs) |
| `assets/data/league_table.json` | עותק טבלה לשימוש צד-לקוח / API פנימי |
| `_data/wsl_recent_results.json` | תוצאות כל המשחקים שהסתיימו במחזור האחרון |
| `_data/wsl_matches.json` | מאגר כל משחקי העונה המלא (הסתיימו, מתוכננים ותוצאות) |
| `data/raw/fotmob/leagues/league_9227_wsl_overview.json` | Snapshot גולמי מ-FotMob לגיבוי ומעקב |

---

## 3. אימות ודחיפה ל-GitHub (Deploy)

לאחר הריצה, מאמתים ודוחפים את העדכון לאתר החי:

```bash
# 1. בדיקת הקבצים שהשתנו
git status

# 2. הוספה, קומיט ודחיפה
git add _data/ assets/data/
git commit -m "feat(pipeline): sync matchweek X standings and results"
git push origin main
```

---

## 4. משיכת נתוני עומק למשחקי המחזור (עבור הטור השבועי)

לניתוח טקטי, xG, בעיטות והרכבים לקראת כתיבת הטור:

```bash
# משיכת פרטי המשחקים הגולמיים למחזור הרלוונטי (לדוגמה מחזור 5)
python scripts/fetch_round5_matches.py

# הדפסת סיכום xG, בעיטות, מצבי ענק ומבקיעות
python scripts/inspect_round5_summary.py
```
