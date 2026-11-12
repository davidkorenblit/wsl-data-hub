import json
import numpy as np

city_matches = [
    ("MW1", "City 3-1 Birmingham", "data/raw/fotmob/matches/mw1_mci_bir_5981537.json"),
    ("MW2", "Villa 1-4 City", "data/raw/fotmob/matches/mw2_avl_mci_5981640.json"),
    ("MW3", "City 4-2 Liverpool", "data/raw/fotmob/matches/mw3_mci_liv_5981641.json"),
    ("MW4", "Charlton 0-1 City", "data/raw/fotmob/matches/match_5981648.json"),
    ("MW5", "City 4-2 Arsenal", "data/raw/fotmob/matches/mw5_mci_ars_5981661.json"),
    ("MW6", "City 3-2 Brighton", "data/raw/fotmob/matches/mw6_mci_bha_5981668.json"),
    ("MW7", "Man United 1-1 City", "data/raw/fotmob/matches/mw7_mun_mci_5981669.json"),
    ("MW8", "LCL 1-2 City", "data/raw/fotmob/matches/mw8_lcl_mci_5981681.json"),
]

print("=== MANCHESTER CITY FULLBACK ROTATION (MW1 - MW8) ===")
fullback_records = []
for mw, title, fpath in city_matches:
    with open(fpath, "r", encoding="utf-8") as f:
        d = json.load(f)
    home = d.get("general", {}).get("homeTeam", {}).get("name")
    side = "homeTeam" if "Manchester City" in home else "awayTeam"
    starters = d.get("content", {}).get("lineup", {}).get(side, {}).get("starters", [])
    starter_names = [p.get("name") for p in starters]
    
    # Typically in FotMob 4-back: starters[1] is RB, starters[4] is LB (or vice versa)
    # Let's print the back 4
    print(f"\n{mw}: {title}")
    print(f"  Defenders in starters: {starter_names[1:5]}")
    fullback_records.append({
        "mw": mw,
        "match": title,
        "starters": starter_names
    })

# Now run Poisson simulation for LCL vs City:
# LCL: shots with xG
with open("scratch_lcl_mci.json", "r", encoding="utf-8") as f:
    d = json.load(f)

shots = d.get("content", {}).get("shotmap", {}).get("shots", [])
lcl_shots = [s.get("expectedGoals", 0) for s in shots if s.get("teamId") == 1075419]
mci_shots = [s.get("expectedGoals", 0) for s in shots if s.get("teamId") != 1075419]

print("\n=== MONTE CARLO SIMULATION (100,000 RUNS) ===")
print(f"LCL: {len(lcl_shots)} shots, sum xG = {sum(lcl_shots):.2f}")
print(f"MCI: {len(mci_shots)} shots, sum xG = {sum(mci_shots):.2f}")

np.random.seed(42)
N = 100000
lcl_goals = np.zeros(N)
for xg in lcl_shots:
    lcl_goals += (np.random.rand(N) < xg).astype(int)

mci_goals = np.zeros(N)
for xg in mci_shots:
    mci_goals += (np.random.rand(N) < xg).astype(int)

lcl_wins = np.sum(lcl_goals > mci_goals) / N * 100
draws = np.sum(lcl_goals == mci_goals) / N * 100
mci_wins = np.sum(mci_goals > lcl_goals) / N * 100

print(f"Simulation Outcome Probabilities:")
print(f"  LCL Win: {lcl_wins:.1f}%")
print(f"  Draw:    {draws:.1f}%")
print(f"  City Win:{mci_wins:.1f}%")
print(f"  Probability LCL gets at least a point (Win or Draw): {lcl_wins + draws:.1f}%")

