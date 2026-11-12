import json
from pathlib import Path

fp = Path('data/raw/fotmob/players/player_1414896_michelle_agyemang.json')
with open(fp, 'r', encoding='utf-8') as f:
    d = json.load(f)

print("=== SEARCHING FOR EURO / WOMEN EURO IN AGYEMANG DATA ===")

def search_dict(obj, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            search_dict(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            search_dict(item, f"{path}[{i}]")
    elif isinstance(obj, str):
        if "euro" in obj.lower() or "switzerland" in obj.lower() or "england" in obj.lower():
            print(f"Found match at {path}: {obj}")

search_dict(d)
