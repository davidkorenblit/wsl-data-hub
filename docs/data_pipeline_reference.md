# מדריך ומתודולוגיית משיכת נתונים (Data Fetching Reference)

מסמך זה מרכז את **המתודה הקבועה והגנרית** למשיכת נתוני קבוצות, סגלים, פרופילי שחקניות, מדדי אחוזונים והעברות ממאגרי הנתונים (בדגש על ממשק FotMob הפנימי).

---

## 1. הגדרת עונות ומוסכמות זמן
בכל פוסט ועיבוד נתונים בפרויקט, מוגדרים שני צירי זמן ברורים:
* **עונת הבסיס / העונה החולפת (Completed Baseline): `2025/2026`**
  * משמשת לניתוח ביצועים, מפות נגיעות, שערים, בישולים, xG/xA ומדדים מתקדמים.
* **העונה החדשה / פעילה (Target Season): `2026/2027`**
  * משמשת להרכב הסגל המעודכן, ניתוח חלון ההעברות (רכש נכנס ויוצא) ותחזיות.

---

## 2. מאגר מזהי קבוצות וליגות (Registry)

### קבוצות WSL
| קבוצה (Slug) | שם מלא | FotMob Team ID |
| :--- | :--- | :--- |
| `tottenham` | Tottenham Hotspur Women | `628117` |
| `arsenal` | Arsenal Women | `258657` |
| `chelsea` | Chelsea Women | `258661` |
| `manchester_city` | Manchester City Women | `231488` |
| `manchester_united` | Manchester United Women | `954396` |
| `liverpool` | Liverpool Women | `258665` |
| `brighton` | Brighton & Hove Albion Women | `231505` |
| `aston_villa` | Aston Villa Women | `231494` |
| `everton` | Everton Women | `258663` |
| `west_ham` | West Ham United Women | `231497` |
| `crystal_palace` | Crystal Palace Women | `614828` |
| `london_city` | London City Lionesses | `1075419` |

### שחקניות מפתח נבחרות (Key Player IDs)
| שחקנית | קבוצת מקור 25/26 | קבוצה נוכחית 26/27 | FotMob ID |
| :--- | :--- | :--- | :--- |
| **Victoria Pelova** | Arsenal | Tottenham Hotspur | `1055898` |
| **Olivia Holdt** | Tottenham | Tottenham Hotspur | `1030313` |
| **Signe Gaupset** | Tottenham / Brann | Tottenham Hotspur | `1285343` |
| **Cathinka Tandberg**| Tottenham | Tottenham Hotspur | `1140227` |
| **Julie Blakstad** | Tottenham | Tottenham Hotspur | `1031793` |
| **Caitlin Dijkstra** | Wolfsburg | Tottenham Hotspur | `1215012` |
| **Alice Sombath** | Lyon | Tottenham Hotspur | `1214575` |
| **Kirsty Hanson** | Aston Villa | Tottenham Hotspur | `1082557` |

---

## 3. מבנה ה-Endpoints וה-Headers

כל הבקשות מתבצעות בפורמט JSON ישיר ללא צורך ב-Scraping של HTML:

### Headers נדרשים:
```python
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.fotmob.com/"
}
```

### Endpoints מרכזיים:
1. **מידע קבוצתי, סגל והעברות:**
   `GET https://www.fotmob.com/api/data/teams?id={team_id}`
   * `squad.squad`: חלוקת שחקניות לפי תפקידים (Keeper, Defender, Midfielder, Attacker).
   * `transfers.data`: העברות נכנסות (`in`) ויוצאות (`out`).
2. **פרופיל שחקנית, תכונות (Traits) ומדדי Per 90:**
   `GET https://www.fotmob.com/api/data/playerData?id={player_id}`
   * `traits.items`: תכונות ליבה ואחוזון ביחס לעמדה (0–100%).
   * `firstSeasonStats.statsSection.items`: קטגוריות Shooting, Passing, Possession, Defending.
3. **טבלאות ומדדים מובילים לליגה (TopStats):**
   `GET https://data.fotmob.com/stats/{league_id}/season/{season_id}/topstats.json`
   * ליגת WSL: `league_id = 9227`, עונת 2025/2026: `season_id = 27506`.

---

## 4. שימוש במודול הגנרי (`scripts/fotmob_api_client.py`)

נבנה כלי CLI גנרי קבוע ב-Python. דוגמאות להפעלה:

```bash
# 1. משיכת סגל של קבוצה ושמירתו כקובץ JSON
python scripts/fotmob_api_client.py --team tottenham --save-squad

# 2. שליפת מדדים מתקדמים של שחקנית לפי ID
python scripts/fotmob_api_client.py --player-id 1055898
```

או בייבוא ישיר בסקריפטים:
```python
from fotmob_api_client import FotMobAPIClient, WSL_TEAMS

client = FotMobAPIClient()
team_data = client.fetch_team_raw(WSL_TEAMS["tottenham"]["id"])
squad = client.parse_squad(team_data)
```

---

## 5. מיפוי קבצים ב-Jekyll (`_data/`)
* סגלים מעודכנים: `_data/squads/{team_slug}_2026_27.json`
* העברות: `_data/transfers/{team_slug}.json`
* נתונים מתקדמים לניתוחים: `_data/{team_slug}_advanced_attack.json`
