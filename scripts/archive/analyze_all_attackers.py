import json
from pathlib import Path

# Crystal Palace attacking players
PALACE_ATTACKERS = [
    "Bethany England",
    "Annabel Blanchard",
    "Abbie Larkin",
    "Shannon O'Brien",
    "Shanade Hopcroft",
    "Lexi Lloyd-Smith",
    "Molly-Mae Sharpe",
    "Kirsty Howat"
]

# Benchmark attackers from other teams across our scratch match files
BENCHMARK_ATTACKERS = [
    "Fran Kirby",         # Brighton (possession-heavy)
    "Kiko Seike",         # Brighton
    "Lauren Hemp",        # Man City
    "Khadija Shaw",       # Man City
    "Melvine Malard",     # Chelsea
    "Aggie Beever-Jones", # Chelsea
    "Alessia Russo",      # Arsenal
    "Olivia Smith",       # Arsenal
    "Signe Gaupset",      # Tottenham
    "Cathinka Tandberg",  # Tottenham
    "Viviane Asseyi"      # West Ham (counter-attack specialist)
]

files = sorted(Path('.').glob('scratch_*.json'))

player_data = {}

def get_stat(p, stat_name):
    for grp in p.get('stats', []):
        for sname, sdata in grp.get('stats', {}).items():
            if sname == stat_name:
                v = sdata.get('stat', {}).get('value')
                return v if v is not None else 0
    return 0

for fpath in files:
    try:
        d = json.load(open(fpath, encoding='utf-8'))
        ps = d.get('content', {}).get('playerStats', {})
        if not ps:
            continue
        
        for pid, p in ps.items():
            name = p.get('name')
            tname = p.get('teamName', '')
            
            is_palace = ('Palace' in tname or 'Crystal' in tname) and name in PALACE_ATTACKERS
            is_benchmark = name in BENCHMARK_ATTACKERS
            
            if not (is_palace or is_benchmark):
                continue
                
            mins = get_stat(p, 'Minutes played')
            if not mins or mins == 0:
                continue
                
            if name not in player_data:
                player_data[name] = {
                    'team': tname,
                    'is_palace': is_palace,
                    'matches': 0,
                    'minutes': 0,
                    'goals': 0,
                    'assists': 0,
                    'shots': 0,
                    'xg': 0.0,
                    'box_touches': 0,
                    'touches': 0,
                    'passes_acc': 0,
                    'tackles_won': 0,
                    'interceptions': 0,
                    'recoveries': 0,
                    'ground_duels_won': 0,
                    'ground_duels_lost': 0,
                    'aerial_duels_won': 0,
                    'aerial_duels_lost': 0,
                    'dispossessed': 0
                }
                
            rec = player_data[name]
            rec['matches'] += 1
            rec['minutes'] += mins
            rec['goals'] += get_stat(p, 'Goals')
            rec['assists'] += get_stat(p, 'Assists')
            rec['shots'] += get_stat(p, 'Total shots')
            rec['xg'] += float(get_stat(p, 'Expected goals (xG)') or 0.0)
            rec['box_touches'] += get_stat(p, 'Touches in opposition box')
            rec['touches'] += get_stat(p, 'Touches')
            rec['passes_acc'] += get_stat(p, 'Accurate passes')
            rec['tackles_won'] += get_stat(p, 'Tackles won')
            rec['interceptions'] += get_stat(p, 'Interceptions')
            rec['recoveries'] += get_stat(p, 'Recoveries')
            rec['ground_duels_won'] += get_stat(p, 'Ground duels won')
            rec['aerial_duels_won'] += get_stat(p, 'Aerial duels won')
            rec['dispossessed'] += get_stat(p, 'Dispossessed')
            
    except Exception as e:
        continue

print("=== ALL ATTACKERS ANALYSIS: THE DEFENSIVE TAX & COGNITIVE BURDEN ===\n")
print(f"{'Player':<20} | {'Team':<22} | {'Mins':<5} | {'BoxT/90':<7} | {'DefAct/90':<9} | {'Def:Box Ratio':<13} | {'Shots/90':<8} | {'xG/Shot':<7}")
print("-" * 105)

results = []
for name, d in player_data.items():
    if d['minutes'] < 60:
        continue
    m90 = d['minutes'] / 90.0
    box_p90 = d['box_touches'] / m90
    def_act = d['interceptions'] + d['recoveries'] + d['tackles_won']
    def_p90 = def_act / m90
    shots_p90 = d['shots'] / m90
    xg_per_shot = (d['xg'] / d['shots']) if d['shots'] > 0 else 0.0
    ratio = (def_p90 / box_p90) if box_p90 > 0 else 99.0
    
    results.append({
        'name': name,
        'team': d['team'],
        'is_palace': d['is_palace'],
        'mins': d['minutes'],
        'box_p90': box_p90,
        'def_p90': def_p90,
        'ratio': ratio,
        'shots_p90': shots_p90,
        'xg_per_shot': xg_per_shot,
        'goals': d['goals'],
        'shots': d['shots'],
        'xg': d['xg'],
        'def_act': def_act,
        'box_touches': d['box_touches']
    })

# Sort by Defensive to Box Ratio descending
results.sort(key=lambda x: x['ratio'], reverse=True)

for r in results:
    tag = "🔴 PALACE" if r['is_palace'] else "⚪ BENCHMARK"
    ratio_str = f"{r['ratio']:.2f}:1" if r['ratio'] < 90 else "INF (0 box T)"
    print(f"{r['name']:<20} | {r['team'][:22]:<22} | {r['mins']:<5} | {r['box_p90']:<7.2f} | {r['def_p90']:<9.2f} | {ratio_str:<13} | {r['shots_p90']:<8.2f} | {r['xg_per_shot']:<7.2f}  {tag}")

# Save detailed json
with open('_data/attackers_defensive_tax_analysis.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\nSaved detailed metrics to _data/attackers_defensive_tax_analysis.json")

