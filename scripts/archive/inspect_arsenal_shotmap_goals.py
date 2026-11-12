import json
from pathlib import Path

ars_files = [
    ("MW3", "Man United", "data/raw/fotmob/matches/mw3_mun_ars_5981644.json", "Zigiotti"),
    ("MW4", "Chelsea", "data/raw/fotmob/matches/mw4_che_ars_5981654.json", "Thompson"),
    ("MW5", "Man City", "data/raw/fotmob/matches/mw5_mci_ars_5981661.json", "Hemp"),
    ("MW6", "Birmingham", "data/raw/fotmob/matches/mw6_ars_bir_5981663.json", "Hurtré"),
    ("MW7", "Tottenham", "data/raw/fotmob/matches/mw7_tot_ars_5981675.json", "Tandberg"),
    ("MW8", "Aston Villa", "data/raw/fotmob/matches/mw8_ars_avl_5981677.json", "Grant"),
    ("MW9", "Liverpool", "data/raw/fotmob/matches/mw9_liv_ars_5981683.json", "Olsson"),
]

for mw, opp, fpath, keyw in ars_files:
    if not Path(fpath).exists():
        continue
    with open(fpath, "r", encoding="utf-8") as fp:
        d = json.load(fp)
    shots = d.get("content", {}).get("shotmap", {}).get("shots", [])
    for s in shots:
        if s.get("eventType") == "Goal" and s.get("teamId") != 258657:
            print(f"[{mw} vs {opp}] Scorer: {s.get('playerName')} {s.get('time')}' | Sit: {s.get('situation')} | FastBreak: {s.get('isFastBreak')} | ShotType: {s.get('shotType')} | xG: {s.get('expectedGoals')} | (x, y): ({s.get('x'):.1f}, {s.get('y'):.1f})")

