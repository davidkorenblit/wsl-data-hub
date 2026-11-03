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

with open("_data/arsenal_lineup_rotations_season.json", "r", encoding="utf-8") as f:
    arsenal_data = json.load(f)

with open("_data/spurs_turnovers_and_duels_season.json", "r", encoding="utf-8") as f:
    spurs_data = json.load(f)

ars_rounds = []
for m in arsenal_data["match_by_match_lineups"]:
    ars_rounds.append({
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

ars_notes = {
    "MW1": "פתיחת העונה מול ברייטון (0:1). פוקס ובאטייה כמגינות, סטאנוויי וליטל בקישור, רוסו ב-9.",
    "MW2": "תיקו 0:0 מול פאלאס. וובן-מוי פותחת כבלמית במקום קאטלי; קוני-קרוס מחליפה את ליטל; קלי בכנף.",
    "MW3": "תיקו 1:1 מול יונייטד. בלקסטניוס פותחת ב-9! רוסו מוסטת לעמדה 10; קלדנטיי בקישור האחורי לצד סטאנוויי.",
    "MW4": "הפסד 0:1 לצ'לסי. אנקה בורבה נזרקת לשער במקום מיסה; ליטל חוזרת ל-10; רוסו מוחזרת ל-9.",
    "MW5": "הפסד 2:4 לסיטי. שוב בורבה בשער; וובן-מוי מחליפה את קאטלי כבלמית; סלגרס סופגת רביעייה.",
    "MW6": "תיקו 1:1 מול ברמינגהאם. מיסה חוזרת לשער; סמילה הולמברג פותחת לראשונה כמגן ימני; בלקסטניוס שוב ב-9 ורוסו ב-10.",
    "MW7": "ניצחון 1:2 בדרבי מול ספרס. טיילור היינדס פותחת לראשונה כמגן שמאלי, באטייה בספסל! רוסו ב-10, סמית' מוקפצת לחוד.",
    "MW8": "תיקו 1:1 מול וילה (28 בעיטות, 2.61 xG מול 0.07). באטייה מועברת כמגן ימני; פוקס בספסל; רויטלר בהופעת בכורה ב-RW; רוסו שוב ב-10 וסמית' ב-9."
}

spurs_players = []
for p in spurs_data["season_summary_attack_and_midfield"]:
    pname = p["player"]
    is_high = p["dispossessed_per_90"] >= 1.0
    spurs_players.append({
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

# Write assets/js/mw8-widgets.js
js_code = f"""/**
 * MW8 Interactive Widgets: Arsenal Tactical Pitch, Spurs Turnover Table, West Ham Transitions
 */
(function() {{
  const ARSENAL_ROUNDS = {json.dumps(ars_rounds, ensure_ascii=False)};
  const ARSENAL_NOTES = {json.dumps(ars_notes, ensure_ascii=False)};
  const SPURS_PLAYERS = {json.dumps(spurs_players, ensure_ascii=False)};

  const POS_COORDS = {{
    "cf": {{ top: "13%", left: "50%" }},
    "lw": {{ top: "30%", left: "18%" }},
    "am": {{ top: "33%", left: "50%" }},
    "rw": {{ top: "30%", left: "82%" }},
    "dm1": {{ top: "52%", left: "34%" }},
    "dm2": {{ top: "52%", left: "66%" }},
    "lb": {{ top: "72%", left: "16%" }},
    "cb_left": {{ top: "74%", left: "38%" }},
    "cb_right": {{ top: "74%", left: "62%" }},
    "rb": {{ top: "72%", left: "84%" }},
    "gk": {{ top: "88%", left: "50%" }}
  }};

  // 1. ARSENAL CONTROLLER
  let currentArsenalMode = "chaos"; // "chaos" (default Migration Board) or 0..7

  window.setArsenalRound = function(idx) {{
    currentArsenalMode = idx;
    renderArsenalControls();
    if (idx === "chaos") {{
      renderArsenalChaosMap();
    }} else {{
      renderArsenalSingleRound(idx);
    }}
  }};

  function renderArsenalControls() {{
    const container = document.getElementById("ars-tabs-container");
    if (!container) return;

    let html = "";
    const isChaos = currentArsenalMode === "chaos";
    const chaosCls = isChaos
      ? "bg-red-600 text-white font-bold border-red-500 shadow-md ring-2 ring-red-400"
      : "bg-neutral-800 text-red-300 hover:bg-neutral-700 border-neutral-700";
    html += '<button type="button" onclick="setArsenalRound(\\'chaos\\')" class="px-2.5 py-1 rounded border transition-colors flex items-center gap-1 ' + chaosCls + '"><span>⚡</span><span>מפת התוהו ובוהו</span></button>';

    ARSENAL_ROUNDS.forEach((r, idx) => {{
      const isActive = currentArsenalMode === idx;
      const activeCls = isActive
        ? "bg-primary-600 text-white font-bold border-primary-500 shadow-xs"
        : "bg-neutral-800 text-neutral-300 hover:bg-neutral-700 border-neutral-700";
      html += '<button type="button" onclick="setArsenalRound(' + idx + ')" class="px-2 py-1 rounded border transition-colors ' + activeCls + '">' + r.round + '</button>';
    }});

    container.innerHTML = html;
  }}

  // RENDER THE MIGRATION & CHAOS MAP (DEFAULT VIEW)
  function renderArsenalChaosMap() {{
    const nodesLayer = document.getElementById("ars-pitch-nodes");
    const pRound = document.getElementById("ars-panel-round");
    const pFormation = document.getElementById("ars-panel-formation");
    const pMatch = document.getElementById("ars-panel-match");
    const pNotes = document.getElementById("ars-panel-notes");
    const subTitle = document.getElementById("ars-widget-subtitle");

    if (!nodesLayer || !pRound) return;

    pRound.innerText = "עונת 2026/27 (מחזורים 1–8)";
    pFormation.innerText = "מפת הפיצולים והנדידה";
    pMatch.innerText = "סחרחרת ההרכבים: 0% המשכיות, 8 הרכבים שונים";
    subTitle.innerText = "מפת התוהו ובוהו: רואים ממש על המגרש את השחקניות הנודדות והפיצולים";

    pNotes.innerHTML = `
      <div class="space-y-2 text-xs">
        <div class="p-2 rounded bg-red-950/40 border border-red-800/60 text-red-200">
          <strong class="text-red-400">⚡ פיצול רוסו (חוד ⟷ 10):</strong> 4 פעמים כחלוצה בודדת (מחזורים 1, 2, 4, 5), 4 פעמים כקשרית התקפית (מחזורים 3, 6, 7, 8).
        </div>
        <div class="p-2 rounded bg-blue-950/40 border border-blue-800/60 text-blue-200">
          <strong class="text-blue-400">🔄 סחרחרת המגינות (שמאל ⟷ ימין):</strong> באטייה שיחקה 6 פעמים בשמאל, והוסטה לימין מול וילה. היינדס פתחה בשמאל פעמיים. פוקס סופסלה.
        </div>
        <div class="p-2 rounded bg-purple-950/40 border border-purple-800/60 text-purple-200">
          <strong class="text-purple-400">🔀 אוליביה סמית' הנודדת:</strong> נדדה בין כנף שמאל (3), כנף ימין וחלוצת חוד מול לסטר ווילה (2).
        </div>
        <div class="p-2 rounded bg-emerald-950/40 border border-emerald-800/60 text-emerald-200">
          <strong class="text-emerald-400">🟢 עוגני ברזל יחידים:</strong> ליאה וויליאמסון (8/8), ג'ורג'יה סטאנוויי (8/8) וקייטלין פורד.
        </div>
      </div>
    `;

    // Visual nodes on pitch showing the chaos & split
    nodesLayer.innerHTML = `
      <!-- Connecting Migration Arrow: Russo between 9 and 10 -->
      <div class="absolute w-1 bg-gradient-to-b from-amber-400 via-red-500 to-amber-400 shadow-md pointer-events-none -translate-x-1/2"
           style="top: 17%; bottom: 64%; left: 50%;"></div>
      <div class="absolute -translate-x-1/2 -translate-y-1/2 pointer-events-none px-2 py-0.5 rounded bg-amber-500 text-black font-mono font-bold text-[9px] shadow-lg border border-amber-300"
           style="top: 23%; left: 50%;">
        רוסו (4 ב-9 ⟷ 4 ב-10)
      </div>

      <!-- Connecting Migration Arrow: Batlle crossing LB to RB -->
      <div class="absolute h-0.5 bg-gradient-to-r from-blue-400 via-indigo-500 to-blue-400 pointer-events-none"
           style="top: 71%; left: 24%; right: 24%;"></div>
      <div class="absolute -translate-x-1/2 -translate-y-1/2 pointer-events-none px-2 py-0.5 rounded bg-blue-600 text-white font-mono font-bold text-[9px] shadow-lg border border-blue-400"
           style="top: 67%; left: 50%;">
        באטייה (6 בשמאל ⟷ 1 בימין)
      </div>

      <!-- Position 9 (CF) Split -->
      <div class="absolute -translate-x-1/2 -translate-y-1/2 flex flex-col items-center pointer-events-none" style="top: 12%; left: 50%;">
        <div class="px-2 py-1 rounded-lg bg-black/90 border border-red-500 text-center shadow-lg">
          <div class="text-[9px] font-mono text-red-400 font-bold uppercase">עמדה 9 (חוד)</div>
          <div class="text-[10px] font-bold text-white whitespace-nowrap">רוסו (4) | סמית' (2) | בלקסטניוס (2)</div>
        </div>
      </div>

      <!-- Position 10 (AM) Split -->
      <div class="absolute -translate-x-1/2 -translate-y-1/2 flex flex-col items-center pointer-events-none" style="top: 34%; left: 50%;">
        <div class="px-2 py-1 rounded-lg bg-black/90 border border-amber-500 text-center shadow-lg">
          <div class="text-[9px] font-mono text-amber-400 font-bold uppercase">עמדה 10 (פליימייקר)</div>
          <div class="text-[10px] font-bold text-white whitespace-nowrap">רוסו (4) | קלדנטיי (3) | ליטל (1)</div>
        </div>
      </div>

      <!-- Wings: Left and Right -->
      <div class="absolute -translate-x-1/2 -translate-y-1/2 flex flex-col items-center pointer-events-none" style="top: 31%; left: 16%;">
        <div class="px-2 py-1 rounded-lg bg-black/90 border border-neutral-600 text-center shadow-lg">
          <div class="text-[8px] font-mono text-purple-400 font-bold">כנף שמאל</div>
          <div class="text-[9px] font-bold text-neutral-200 whitespace-nowrap">סמית' (3) | פורד (2) | קלדנטיי (1) | קלי (1)</div>
        </div>
      </div>
      <div class="absolute -translate-x-1/2 -translate-y-1/2 flex flex-col items-center pointer-events-none" style="top: 31%; left: 84%;">
        <div class="px-2 py-1 rounded-lg bg-black/90 border border-neutral-600 text-center shadow-lg">
          <div class="text-[8px] font-mono text-neutral-400 font-bold">כנף ימין</div>
          <div class="text-[10px] font-bold text-neutral-200 whitespace-nowrap">באום (7) | רויטלר (1)</div>
        </div>
      </div>

      <!-- Double Pivot -->
      <div class="absolute -translate-x-1/2 -translate-y-1/2 flex flex-col items-center pointer-events-none" style="top: 52%; left: 34%;">
        <div class="px-2 py-1 rounded bg-black/90 border border-neutral-700 text-center shadow-md">
          <div class="text-[8px] font-mono text-neutral-400">קישור</div>
          <div class="text-[10px] font-bold text-white whitespace-nowrap">קוני-קרוס (6) | ליטל (2)</div>
        </div>
      </div>
      <div class="absolute -translate-x-1/2 -translate-y-1/2 flex flex-col items-center pointer-events-none" style="top: 52%; left: 66%;">
        <div class="px-2 py-1 rounded bg-emerald-950/90 border-2 border-emerald-400 text-center shadow-md">
          <div class="text-[8px] font-mono text-emerald-400 font-bold">עוגן 100%</div>
          <div class="text-[10px] font-bold text-white whitespace-nowrap">סטאנוויי (8/8)</div>
        </div>
      </div>

      <!-- Fullbacks: LB & RB -->
      <div class="absolute -translate-x-1/2 -translate-y-1/2 flex flex-col items-center pointer-events-none" style="top: 74%; left: 16%;">
        <div class="px-2 py-1 rounded-lg bg-black/90 border border-blue-500 text-center shadow-lg">
          <div class="text-[8px] font-mono text-blue-400 font-bold">מגן שמאל</div>
          <div class="text-[10px] font-bold text-white whitespace-nowrap">באטייה (6) | היינדס (2)</div>
        </div>
      </div>
      <div class="absolute -translate-x-1/2 -translate-y-1/2 flex flex-col items-center pointer-events-none" style="top: 74%; left: 84%;">
        <div class="px-2 py-1 rounded-lg bg-black/90 border border-blue-500 text-center shadow-lg">
          <div class="text-[8px] font-mono text-blue-400 font-bold">מגן ימין</div>
          <div class="text-[10px] font-bold text-white whitespace-nowrap">פוקס (6) | באטייה (1) | הולמברג (1)</div>
        </div>
      </div>

      <!-- Center Backs -->
      <div class="absolute -translate-x-1/2 -translate-y-1/2 flex flex-col items-center pointer-events-none" style="top: 76%; left: 38%;">
        <div class="px-2 py-1 rounded bg-black/90 border border-neutral-700 text-center shadow-md">
          <div class="text-[8px] font-mono text-neutral-400">בלמית שמאל</div>
          <div class="text-[10px] font-bold text-white whitespace-nowrap">קאטלי (5) | וובן-מוי (3)</div>
        </div>
      </div>
      <div class="absolute -translate-x-1/2 -translate-y-1/2 flex flex-col items-center pointer-events-none" style="top: 76%; left: 62%;">
        <div class="px-2 py-1 rounded bg-emerald-950/90 border-2 border-emerald-400 text-center shadow-md">
          <div class="text-[8px] font-mono text-emerald-400 font-bold">עוגן 100%</div>
          <div class="text-[10px] font-bold text-white whitespace-nowrap">וויליאמסון (8/8)</div>
        </div>
      </div>

      <!-- Goalkeeper -->
      <div class="absolute -translate-x-1/2 -translate-y-1/2 flex flex-col items-center pointer-events-none" style="top: 89%; left: 50%;">
        <div class="px-2 py-1 rounded bg-black/90 border border-neutral-600 text-center shadow-md">
          <div class="text-[8px] font-mono text-neutral-400">שוערת</div>
          <div class="text-[10px] font-bold text-white whitespace-nowrap">מיסה (6) | בורבה (2)</div>
        </div>
      </div>
    `;
  }}

  // RENDER INDIVIDUAL MATCHWEEK (MW1..MW8)
  function renderArsenalSingleRound(idx) {{
    const nodesLayer = document.getElementById("ars-pitch-nodes");
    const pRound = document.getElementById("ars-panel-round");
    const pFormation = document.getElementById("ars-panel-formation");
    const pMatch = document.getElementById("ars-panel-match");
    const pNotes = document.getElementById("ars-panel-notes");
    const subTitle = document.getElementById("ars-widget-subtitle");

    const r = ARSENAL_ROUNDS[idx];
    if (!r) return;

    pRound.innerText = r.round;
    pFormation.innerText = r.formation;
    pMatch.innerText = r.match;
    pNotes.innerText = ARSENAL_NOTES[r.round] || "";
    subTitle.innerText = "הרכב פותח: " + r.match + " (מערך " + r.formation + ")";

    let nodesHtml = "";
    for (const [posKey, p] of Object.entries(r.players)) {{
      const coords = POS_COORDS[posKey] || {{ top: "50%", left: "50%" }};
      
      let tagBadge = "";
      if (p.raw === "Alessia Russo") {{
        tagBadge = posKey === "am" 
          ? '<span class="text-[8px] font-mono bg-amber-500 text-black px-1 rounded font-bold">הוסטה ל-10</span>' 
          : '<span class="text-[8px] font-mono bg-red-500 text-white px-1 rounded font-bold">חלוצה 9</span>';
      }} else if (p.raw === "Ona Batlle") {{
        tagBadge = posKey === "rb"
          ? '<span class="text-[8px] font-mono bg-blue-500 text-white px-1 rounded font-bold">הוסטה לימין</span>'
          : '<span class="text-[8px] font-mono bg-neutral-700 text-neutral-200 px-1 rounded">מגן שמאל</span>';
      }} else if (p.raw === "Taylor Hinds") {{
        tagBadge = '<span class="text-[8px] font-mono bg-emerald-500 text-white px-1 rounded font-bold">פתיחה בשמאל</span>';
      }} else if (p.raw === "Olivia Smith" && posKey === "cf") {{
        tagBadge = '<span class="text-[8px] font-mono bg-purple-500 text-white px-1 rounded font-bold">הוקפצה ל-9</span>';
      }}

      nodesHtml += '<div class="absolute -translate-x-1/2 -translate-y-1/2 flex flex-col items-center pointer-events-none transition-all duration-300" style="top: ' + coords.top + '; left: ' + coords.left + ';"><div class="w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-red-600 border border-white/80 shadow-md flex items-center justify-center text-[10px] font-mono font-bold text-white">' + p.pos + '</div><div class="mt-1 px-1.5 py-0.5 rounded bg-black/85 text-white font-sans text-[10px] sm:text-[11px] font-bold whitespace-nowrap shadow-xs border border-white/10">' + p.name + '</div>' + (tagBadge ? '<div class="mt-0.5">' + tagBadge + '</div>' : '') + '</div>';
    }}
    nodesLayer.innerHTML = nodesHtml;
  }}

  // 2. SPURS TABLE CONTROLLER
  let currentSpursFilter = "all";

  window.filterSpursTable = function(category) {{
    currentSpursFilter = category;
    
    ["all", "high", "clean"].forEach(c => {{
      const btn = document.getElementById("btn-spurs-" + c);
      if (!btn) return;
      if (c === category) {{
        btn.className = "px-2.5 py-1 rounded border border-primary-500 bg-primary-600 text-white font-bold transition-colors";
      }} else {{
        btn.className = "px-2.5 py-1 rounded border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-[#202028] text-neutral-700 dark:text-neutral-300 hover:border-neutral-400 transition-colors";
      }}
    }});

    renderSpursTable();
  }};

  window.toggleSpursPlayerLog = function(rawName) {{
    const cleanId = "log-row-" + rawName.replace(/\\s+/g, '-');
    const row = document.getElementById(cleanId);
    if (!row) return;
    row.classList.toggle("hidden");
  }};

  function renderSpursTable() {{
    const tbody = document.getElementById("spurs-table-body");
    if (!tbody) return;

    let filtered = SPURS_PLAYERS.slice();
    if (currentSpursFilter === "high") {{
      filtered = filtered.filter(p => p.disp_per_90 >= 1.0);
    }} else if (currentSpursFilter === "clean") {{
      filtered = filtered.filter(p => p.disp_per_90 < 1.0);
    }}

    filtered.sort((a, b) => b.disp_per_90 - a.disp_per_90);

    let html = "";
    filtered.forEach(p => {{
      const rowId = "log-row-" + p.raw_name.replace(/\\s+/g, '-');
      
      let barColor = "bg-emerald-500";
      let textColor = "text-emerald-600 dark:text-emerald-400";
      if (p.disp_per_90 >= 2.0) {{
        barColor = "bg-red-500";
        textColor = "text-red-600 dark:text-red-400 font-bold";
      }} else if (p.disp_per_90 >= 1.0) {{
        barColor = "bg-amber-500";
        textColor = "text-amber-600 dark:text-amber-400 font-bold";
      }}

      let logHtml = "";
      if (p.match_log && p.match_log.length > 0) {{
        const matchCards = p.match_log.map(m => {{
          const isHighDisp = m.dispossessed > 1;
          const dispCls = isHighDisp ? 'text-red-500 font-bold' : 'text-neutral-700 dark:text-neutral-300';
          return '<div class="p-1.5 rounded bg-white dark:bg-[#202028] border border-neutral-200 dark:border-neutral-700">' +
            '<div class="font-bold text-neutral-800 dark:text-neutral-200">' + m.round + ' (' + m.minutes + ' דק\\')</div>' +
            '<div class="text-neutral-500">' + m.match + '</div>' +
            '<div class="flex justify-between mt-1 pt-1 border-t border-neutral-100 dark:border-neutral-700/60">' +
            '<span>איבודים: <strong class="' + dispCls + '">' + m.dispossessed + '</strong></span>' +
            '<span>מאבקים: ' + m.duels_won + '/' + m.total_duels + '</span>' +
            '</div></div>';
        }}).join('');

        logHtml = '<tr id="' + rowId + '" class="hidden bg-neutral-50/80 dark:bg-[#181822]"><td colspan="7" class="p-3 text-[11px] font-sans"><div class="font-bold text-neutral-800 dark:text-neutral-200 mb-1.5 flex items-center gap-1.5"><span>📋</span><span>פירוט 8 מחזורי הליגה של ' + p.name + ' (' + p.role + '):</span></div><div class="grid grid-cols-2 sm:grid-cols-4 gap-2 font-mono text-[10px]">' + matchCards + '</div></td></tr>';
      }}

      html += '<tr onclick="toggleSpursPlayerLog(\\'' + p.raw_name + '\\')" class="hover:bg-neutral-50 dark:hover:bg-[#1c1c24] cursor-pointer transition-colors">' +
        '<td class="p-3"><div class="font-bold text-neutral-900 dark:text-white">' + p.name + '</div><div class="text-[10px] text-neutral-500 dark:text-neutral-400 font-sans">' + p.role + '</div></td>' +
        '<td class="p-3 text-center text-neutral-700 dark:text-neutral-300">' + p.minutes + '\\' <span class="text-neutral-400 text-[10px]">(' + p.appearances + ')</span></td>' +
        '<td class="p-3 text-center font-bold text-neutral-900 dark:text-white">' + p.disp_total + '</td>' +
        '<td class="p-3 text-center"><span class="' + textColor + '">' + p.disp_per_90.toFixed(2) + '</span><div class="w-16 h-1.5 bg-neutral-200 dark:bg-neutral-700 rounded-full mx-auto mt-1 overflow-hidden"><div class="' + barColor + ' h-full rounded-full" style="width: ' + Math.min(100, (p.disp_per_90 / 2.5) * 100) + '%"></div></div></td>' +
        '<td class="p-3 text-center text-neutral-700 dark:text-neutral-300">' + p.duels_won + ' / ' + p.duels_total + '</td>' +
        '<td class="p-3 text-center"><span class="font-bold text-neutral-800 dark:text-neutral-200">' + p.duels_pct + '%</span><div class="w-14 h-1.5 bg-neutral-200 dark:bg-neutral-700 rounded-full mx-auto mt-1 overflow-hidden"><div class="bg-indigo-500 h-full rounded-full" style="width: ' + p.duels_pct + '%"></div></div></td>' +
        '<td class="p-3 text-center text-neutral-600 dark:text-neutral-400">' + p.duels_lost_per_90.toFixed(1) + '</td>' +
        '</tr>' + logHtml;
    }});

    tbody.innerHTML = html;
  }}

  // 3. WEST HAM TRANSITION BLUEPRINT CONTROLLER
  window.setWestHamView = function(view) {{
    const container = document.getElementById("whu-dynamic-content");
    const btnMw2 = document.getElementById("btn-whu-mw2");
    const btnMw8 = document.getElementById("btn-whu-mw8");
    const btnCompare = document.getElementById("btn-whu-compare");

    if (!container) return;

    [btnMw2, btnMw8, btnCompare].forEach(btn => {{
      if (btn) btn.className = "px-2.5 py-1 rounded border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-[#202028] text-neutral-700 dark:text-neutral-300 hover:border-amber-400 transition-colors";
    }});

    if (view === "mw2") {{
      if (btnMw2) btnMw2.className = "px-2.5 py-1 rounded border border-amber-500 bg-amber-500 text-white font-bold transition-colors";
      container.innerHTML = '<div class="space-y-4"><div class="flex items-center justify-between border-b border-neutral-200 dark:border-neutral-800 pb-2"><div><span class="text-xs font-mono font-bold text-amber-600 dark:text-amber-400">מחזור 2 בחוץ:</span><span class="text-sm font-bold text-neutral-900 dark:text-white mr-1.5">לונדון סיטי ליונסס 1 – 2 ווסטהאם</span></div><span class="text-xs font-mono font-bold px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-300">ניצחון מעברים</span></div><div class="grid grid-cols-2 sm:grid-cols-4 gap-3 text-center font-sans"><div class="p-3 rounded-lg bg-neutral-50 dark:bg-[#1a1a22] border border-neutral-200 dark:border-neutral-800"><div class="text-[11px] font-mono text-neutral-500">החזקת כדור</div><div class="text-lg font-bold text-neutral-900 dark:text-white mt-0.5">38%</div><div class="text-[10px] font-mono text-neutral-400">62 מסירות בחצי היריבה בלבד</div></div><div class="p-3 rounded-lg bg-neutral-50 dark:bg-[#1a1a22] border border-neutral-200 dark:border-neutral-800"><div class="text-[11px] font-mono text-neutral-500">בעיטות ו-xG</div><div class="text-lg font-bold text-amber-600 dark:text-amber-400 mt-0.5">8 בעיטות (1.34)</div><div class="text-[10px] font-mono text-neutral-400">3 מצבי ענק במעברים</div></div><div class="p-3 rounded-lg bg-neutral-50 dark:bg-[#1a1a22] border border-neutral-200 dark:border-neutral-800"><div class="text-[11px] font-mono text-neutral-500">פיוּבל (המנוע)</div><div class="text-lg font-bold text-indigo-600 dark:text-indigo-400 mt-0.5">בישול (11\\')</div><div class="text-[10px] font-mono text-neutral-400">כדור עומק לגאגו</div></div><div class="p-3 rounded-lg bg-neutral-50 dark:bg-[#1a1a22] border border-neutral-200 dark:border-neutral-800"><div class="text-[11px] font-mono text-neutral-500">אסיי (הסיומת)</div><div class="text-lg font-bold text-emerald-600 dark:text-emerald-400 mt-0.5">שער ניצחון (84\\')</div><div class="text-[10px] font-mono text-neutral-400">עקיצה קטלנית בדקה ה-84</div></div></div><p class="text-xs text-neutral-600 dark:text-neutral-400 leading-relaxed font-sans">הניצחון בברומלי היה שיעור מופתי: לס"ל לחצה גבוה, ווסטהאם כמעט לא החזיקה בכדור אבל השאירה את ארפס חסרת אונים (1.05- שערים שנמנעו) ב-3 התקפות מעבר ישירות.</p></div>';
    }} else if (view === "mw8") {{
      if (btnMw8) btnMw8.className = "px-2.5 py-1 rounded border border-amber-500 bg-amber-500 text-white font-bold transition-colors";
      container.innerHTML = '<div class="space-y-4"><div class="flex items-center justify-between border-b border-neutral-200 dark:border-neutral-800 pb-2"><div><span class="text-xs font-mono font-bold text-amber-600 dark:text-amber-400">מחזור 8 בבית:</span><span class="text-sm font-bold text-neutral-900 dark:text-white mr-1.5">ווסטהאם 4 – 1 ליברפול</span></div><span class="text-xs font-mono font-bold px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-300">התפרקות ליברפול</span></div><div class="grid grid-cols-2 sm:grid-cols-4 gap-3 text-center font-sans"><div class="p-3 rounded-lg bg-neutral-50 dark:bg-[#1a1a22] border border-neutral-200 dark:border-neutral-800"><div class="text-[11px] font-mono text-neutral-500">החזקת כדור</div><div class="text-lg font-bold text-neutral-900 dark:text-white mt-0.5">40%</div><div class="text-[10px] font-mono text-neutral-400">74 מסירות בחצי ליברפול בלבד</div></div><div class="p-3 rounded-lg bg-neutral-50 dark:bg-[#1a1a22] border border-neutral-200 dark:border-neutral-800"><div class="text-[11px] font-mono text-neutral-500">בעיטות ו-xG</div><div class="text-lg font-bold text-amber-600 dark:text-amber-400 mt-0.5">16 בעיטות (1.99)</div><div class="text-[10px] font-mono text-neutral-400">3 מצבי ענק מול 0 של ליברפול</div></div><div class="p-3 rounded-lg bg-neutral-50 dark:bg-[#1a1a22] border border-neutral-200 dark:border-neutral-800"><div class="text-[11px] font-mono text-neutral-500">פיוּבל (האדריכלית)</div><div class="text-lg font-bold text-indigo-600 dark:text-indigo-400 mt-0.5">צמד בישולים</div><div class="text-[10px] font-mono text-neutral-400">לוונדלר (15\\') ולקודינה (44\\')</div></div><div class="p-3 rounded-lg bg-neutral-50 dark:bg-[#1a1a22] border border-neutral-200 dark:border-neutral-800"><div class="text-[11px] font-mono text-neutral-500">אסיי (שחקנית המחזור)</div><div class="text-lg font-bold text-emerald-600 dark:text-emerald-400 mt-0.5">צמד + פנדל</div><div class="text-[10px] font-mono text-neutral-400">ציון 9.40 · 10 מאבקי קרקע</div></div></div><p class="text-xs text-neutral-600 dark:text-neutral-400 leading-relaxed font-sans">שכפול מושלם של אותה תוכנית: ליברפול שלטה בכדור ללא שום תכלית (491 מסירות מדויקות ו-0 מצבי ענק), קיארה קיטינג קרסה (2.04- שערים שנמנעו), ו-ווסטהאם חגגה רביעייה.</p></div>';
    }} else {{
      if (btnCompare) btnCompare.className = "px-2.5 py-1 rounded border border-amber-500 bg-amber-500 text-white font-bold transition-colors";
      container.innerHTML = '<div class="space-y-4"><div class="text-xs font-bold text-neutral-800 dark:text-neutral-200 mb-1">השוואת תבנית ראש-בראש: ה-Blueprint שהביס את לונדון סיטי ואת ליברפול</div><div class="overflow-x-auto"><table class="w-full text-right text-xs font-mono"><thead class="bg-neutral-100 dark:bg-[#181820] text-neutral-500 dark:text-neutral-400 text-[11px] border-b border-neutral-200 dark:border-neutral-800"><tr><th class="p-2.5">פרמטר</th><th class="p-2.5 text-center">מחזור 2 (1:2 מול ליונסס)</th><th class="p-2.5 text-center">מחזור 8 (1:4 מול ליברפול)</th><th class="p-2.5 text-center">התבנית הטקטית</th></tr></thead><tbody class="divide-y divide-neutral-200 dark:divide-neutral-800 text-[11px]"><tr><td class="p-2.5 font-bold text-neutral-900 dark:text-white">החזקת כדור</td><td class="p-2.5 text-center text-amber-600 dark:text-amber-400 font-bold">38%</td><td class="p-2.5 text-center text-amber-600 dark:text-amber-400 font-bold">40%</td><td class="p-2.5 text-center text-neutral-500">ויתור מודע על פוזשן עקר</td></tr><tr><td class="p-2.5 font-bold text-neutral-900 dark:text-white">מסירות בחצי היריבה</td><td class="p-2.5 text-center">62 מסירות</td><td class="p-2.5 text-center">74 מסירות</td><td class="p-2.5 text-center text-neutral-500">מינימום נגיעות, מהירות שיא</td></tr><tr><td class="p-2.5 font-bold text-neutral-900 dark:text-white">מצבי ענק במעברים</td><td class="p-2.5 text-center text-emerald-600 dark:text-emerald-400 font-bold">3 מצבי ענק</td><td class="p-2.5 text-center text-emerald-600 dark:text-emerald-400 font-bold">3 מצבי ענק</td><td class="p-2.5 text-center text-neutral-500">100% מהמצבים הגיעו במעבר</td></tr><tr><td class="p-2.5 font-bold text-neutral-900 dark:text-white">סריינה פיוּבל</td><td class="p-2.5 text-center">בישול (11\\')</td><td class="p-2.5 text-center">צמד בישולים (15\\', 44\\')</td><td class="p-2.5 text-center text-neutral-500">מהנדסת המעברים הראשית</td></tr><tr><td class="p-2.5 font-bold text-neutral-900 dark:text-white">ויויאן אסיי</td><td class="p-2.5 text-center">שער ניצחון (84\\')</td><td class="p-2.5 text-center font-bold text-emerald-500">צמד + סחיטת פנדל</td><td class="p-2.5 text-center text-neutral-500">מטרה קטלנית ברחבה</td></tr><tr><td class="p-2.5 font-bold text-neutral-900 dark:text-white">שוערת יריבה שספגה עונש</td><td class="p-2.5 text-center text-red-500">ארפס (1.05- שנמנעו)</td><td class="p-2.5 text-center text-red-500 font-bold">קיטינג (2.04- שנמנעו)</td><td class="p-2.5 text-center text-neutral-500">חשיפה מוחלטת של השוערת</td></tr></tbody></table></div></div>';
    }}
  }};

  // INITIALIZE ON LOAD
  function init() {{
    setArsenalRound("chaos");
    renderSpursTable();
    setWestHamView("compare");
  }}

  if (document.readyState === "loading") {{
    document.addEventListener("DOMContentLoaded", init);
  }} else {{
    init();
  }}
}})();
"""

out_js = Path("assets/js/mw8-widgets.js")
out_js.parent.mkdir(parents=True, exist_ok=True)
with open(out_js, "w", encoding="utf-8") as f:
    f.write(js_code)

print(f"Generated {out_js} cleanly.")
