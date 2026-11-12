import json
from pathlib import Path

# Names translation map
HEBREW_NAMES = {
    "Leah Williamson": "ליאה וויליאמסון",
    "Georgia Stanway": "ג'ורג'יה סטאנוויי",
    "Alessia Russo": "אלסיה רוסו",
    "Ona Batlle": "אונה באטייה",
    "Lisa Baum": "ליסה באום",
    "Misa": "מיסה רודריגז",
    "Emily Fox": "אמילי פוקס",
    "Kyra Cooney-Cross": "קיירה קוני-קרוס",
    "Steph Catley": "סטף קאטלי",
    "Olivia Smith": "אוליביה סמית'",
    "Mariona Caldentey": "מריונה קלדנטיי",
    "Kim Little": "קים ליטל",
    "Lotte Wubben-Moy": "לוטה וובן-מוי",
    "Stina Blackstenius": "סטינה בלקסטניוס",
    "Anneke Borbe": "אנקה בורבה",
    "Taylor Hinds": "טיילור היינדס",
    "Caitlin Foord": "קייטלין פורד",
    "Chloe Kelly": "קלואי קלי",
    "Smilla Holmberg": "סמילה הולמברג",
    "Géraldine Reuteler": "ז'רלדין רויטלר",
    
    # Spurs
    "Signe Gaupset": "סיגנה גאופסט",
    "Olivia Holdt": "אוליביה הולדט",
    "Victoria Pelova": "ויקטוריה פלובה",
    "Matilda Vinberg": "מתילדה וינברג",
    "Cathinka Tandberg": "קתלין טנדברג",
    "Drew Spence": "דרו ספנס",
    "Julie Blakstad": "קתרין בלקסטד",
    "Kirsty Hanson": "קירסטי הנסן",
    "Matilda Nildén": "מתילדה נילדן",
    "Eveliina Summanen": "אוולינה סומאנן",
    "Shekiera Martinez": "שקירה מרטינז"
}

SPURS_ROLES = {
    "Signe Gaupset": "קשרית התקפית / 10",
    "Olivia Holdt": "כנף / קשרית",
    "Victoria Pelova": "עושת משחק / 8-10",
    "Matilda Vinberg": "כנף ימין",
    "Cathinka Tandberg": "חלוצה מרכזית / 9",
    "Drew Spence": "קשרית מרכזית / 8",
    "Julie Blakstad": "כנף שמאל / מגינה",
    "Kirsty Hanson": "כנף ימין/שמאל",
    "Matilda Nildén": "כנף / חלוצה מחליפה",
    "Eveliina Summanen": "קשרית אחורית / 6",
    "Shekiera Martinez": "חלוצה מחליפה"
}

# Load data files
with open("_data/arsenal_lineup_rotations_season.json", "r", encoding="utf-8") as f:
    arsenal_data = json.load(f)

with open("_data/spurs_turnovers_and_duels_season.json", "r", encoding="utf-8") as f:
    spurs_data = json.load(f)

# Build JS data payloads
ars_rounds_js = []
for m in arsenal_data["match_by_match_lineups"]:
    ars_rounds_js.append({
        "round": m["round"],
        "match": m["match"],
        "formation": m["formation"],
        "players": {
            "gk": {"name": HEBREW_NAMES.get(m["gk"], m["gk"]), "raw": m["gk"], "pos": "GK"},
            "lb": {"name": HEBREW_NAMES.get(m["lb"], m["lb"]), "raw": m["lb"], "pos": "LB"},
            "cb_left": {"name": HEBREW_NAMES.get(m["cb_left"], m["cb_left"]), "raw": m["cb_left"], "pos": "CB"},
            "cb_right": {"name": HEBREW_NAMES.get(m["cb_right"], m["cb_right"]), "raw": m["cb_right"], "pos": "CB"},
            "rb": {"name": HEBREW_NAMES.get(m["rb"], m["rb"]), "raw": m["rb"], "pos": "RB"},
            "dm1": {"name": HEBREW_NAMES.get(m["dm1"], m["dm1"]), "raw": m["dm1"], "pos": "DM"},
            "dm2": {"name": HEBREW_NAMES.get(m["dm2"], m["dm2"]), "raw": m["dm2"], "pos": "DM"},
            "lw": {"name": HEBREW_NAMES.get(m["lw"], m["lw"]), "raw": m["lw"], "pos": "LW"},
            "am": {"name": HEBREW_NAMES.get(m["am"], m["am"]), "raw": m["am"], "pos": "AM"},
            "rw": {"name": HEBREW_NAMES.get(m["rw"], m["rw"]), "raw": m["rw"], "pos": "RW"},
            "cf": {"name": HEBREW_NAMES.get(m["cf"], m["cf"]), "raw": m["cf"], "pos": "CF"}
        }
    })

# Format notes for each round
ars_notes_map = {
    "MW1": "פתיחת העונה מול ברייטון (0:1). פוקס ובאטייה כמגינות, סטאנוויי וליטל בקישור, רוסו ב-9.",
    "MW2": "תיקו 0:0 מול פאלאס. וובן-מוי פותחת כבלמית במקום קאטלי; קוני-קרוס מחליפה את ליטל; קלי בכנף.",
    "MW3": "תיקו 1:1 מול יונייטד. בלקסטניוס פותחת ב-9! רוסו מוסטת לעמדה 10; קלדנטיי בקישור האחורי לצד סטאנוויי.",
    "MW4": "הפסד 0:1 לצ'לסי. אנקה בורבה נזרקת לשער במקום מיסה; ליטל חוזרת ל-10; רוסו מוחזרת ל-9.",
    "MW5": "הפסד 2:4 לסיטי. שוב בורבה בשער; וובן-מוי מחליפה את קאטלי כבלמית; סלגרס סופגת רביעייה.",
    "MW6": "תיקו 1:1 מול ברמינגהאם. מיסה חוזרת לשער; סמילה הולמברג פותחת לראשונה כמגן ימני; בלקסטניוס שוב ב-9 ורוסו ב-10.",
    "MW7": "ניצחון 1:2 בדרבי מול ספרס. טיילור היינדס פותחת לראשונה כמגן שמאלי, באטייה בספסל! רוסו ב-10, סמית' מוקפצת לחוד.",
    "MW8": "תיקו 1:1 מול וילה (28 בעיטות, 2.61 xG מול 0.07). באטייה מועברת כמגן ימני; פוקס בספסל; רויטלר בהופעת בכורה ב-RW; רוסו שוב ב-10 וסמית' ב-9."
}

ars_summary_js = arsenal_data["player_starts_summary"]

# Spurs players JS payload
spurs_players_js = []
for p in spurs_data["season_summary_attack_and_midfield"]:
    pname = p["player"]
    # category: 'high' vs 'clean'
    is_high = p["dispossessed_per_90"] >= 1.0
    spurs_players_js.append({
        "name": HEBREW_NAMES.get(pname, pname),
        "raw_name": pname,
        "role": SPURS_ROLES.get(pname, "התקפה/קישור"),
        "minutes": p["total_minutes"],
        "appearances": p["appearances"],
        "disp_total": p["dispossessed_total"],
        "disp_per_90": p["dispossessed_per_90"],
        "duels_won": p["duels_won_total"],
        "duels_total": p["total_duels"],
        "duels_pct": p["duels_win_pct"],
        "duels_lost_per_90": p["duels_lost_per_90"],
        "category": "high" if is_high else "clean",
        "match_log": p.get("match_log", [])
    })

print(f"Processed {len(ars_rounds_js)} Arsenal rounds and {len(spurs_players_js)} Spurs players.")
