"""
Test Script: Fetching FotMob Data (Option A vs Option B)
=======================================================
Target Player: Mapi León (Barcelona / London City Lionesses)
"""

import json
import requests

# -------------------------------------------------------------
# OPTION B: Direct Internal API (requests + headers)
# -------------------------------------------------------------
def fetch_fotmob_direct_api(player_name: str = "Mapi Leon"):
    print(f"\n--- Testing Option B (Direct API for '{player_name}') ---")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json",
        "Referer": "https://www.fotmob.com/"
    }

    # 1. Search player to get ID
    search_url = f"https://www.fotmob.com/api/data/search/suggest?term={requests.utils.quote(player_name)}"
    try:
        search_res = requests.get(search_url, headers=headers, timeout=10)
        search_res.raise_for_status()
        search_data = search_res.json()
        
        player_id = None
        for group in search_data:
            for item in group.get("suggestions", []):
                if item.get("type") == "player":
                    player_id = item.get("id")
                    print(f"[Option B] Found player: {item.get('name')} (ID: {player_id}, Team: {item.get('teamName')})")
                    break
            if player_id:
                break

        if not player_id:
            print("[Option B] Player not found in search suggestions.")
            return None

        # 2. Fetch full Player Data profile
        player_url = f"https://www.fotmob.com/api/data/playerData?id={player_id}"
        player_res = requests.get(player_url, headers=headers, timeout=10)
        player_res.raise_for_status()
        player_data = player_res.json()

        print(f"[Option B] Success! Retrieved profile for: {player_data.get('name')}")
        print(f"[Option B] Position: {player_data.get('positionDescription', {}).get('primaryPosition', {}).get('label')}")
        
        # Display Traits / Radar Percentiles vs other Center-Backs
        traits = player_data.get("traits", {})
        if traits:
            print(f"[Option B] Percentile Traits ({traits.get('title')}):")
            for t in traits.get("items", []):
                pct = int(t.get("value", 0) * 100)
                print(f"   - {t.get('title')}: {pct}th Percentile")

        return player_data

    except Exception as e:
        print(f"[Option B] Error during direct API call: {e}")
        return None


# -------------------------------------------------------------
# OPTION A: Wrapper Library (pyfotmob / fotmob-wrapper fallback)
# -------------------------------------------------------------
def fetch_fotmob_wrapper(player_name: str = "Mapi Leon"):
    print(f"\n--- Testing Option A (Wrapper Library) ---")
    try:
        import pyfotmob
        print("[Option A] `pyfotmob` package loaded.")
        client = pyfotmob.Fotmob()
        # Test basic search / fetch
        res = client.get_player(829862)
        print(f"[Option A] Success via pyfotmob! Name: {res.get('name')}")
        return res
    except ImportError:
        print("[Option A] `pyfotmob` not pre-installed. Wrapper libraries add extra dependency overhead.")
        return None
    except Exception as e:
        print(f"[Option A] Wrapper error: {e}")
        return None


if __name__ == "__main__":
    direct_data = fetch_fotmob_direct_api("Mapi Leon")
    wrapper_data = fetch_fotmob_wrapper("Mapi Leon")
