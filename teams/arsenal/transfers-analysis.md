---
layout: team
title: "Arsenal - חלק ה': קומבינציות טקטיות ועומק הסגל"
team_name: "Arsenal Women"
team_slug: "arsenal"
team_meta: "WSL 2026/27 · חלק ה': לוח מגנטים טקטי וקומבינציות הסגל"
sidebar: transfers
permalink: /teams/arsenal/transfers-analysis/
prev_url: /teams/arsenal/transfers-intro/
prev_title: "חלק ד': חלון ההעברות ואונה באטייה"
next_url: /teams/arsenal/projections/
next_title: "חלק ו': תחזית העונה המורחבת"
---

<div class="space-y-6 text-neutral-800 dark:text-neutral-200 leading-relaxed text-base sm:text-lg font-sans">

  <!-- Header Section -->
  <div class="border-b border-neutral-200 dark:border-neutral-800 pb-3">
    <div class="text-xs font-mono uppercase text-neutral-500 dark:text-neutral-400 font-bold tracking-wider mb-1">
      חלק ה': ורסטיליות, קומבינציות ולוח מגנטים טקטי
    </div>
    <h1 class="text-2xl md:text-3xl font-bold tracking-tight text-neutral-900 dark:text-white">
      3 הפרצופים של ארסנל: הלוח הטקטי של רנה סלחרס
    </h1>
  </div>

  <!-- Opening Placeholder -->
  <div class="p-4 rounded border border-amber-500/30 bg-amber-500/10 text-amber-600 dark:text-amber-400 font-mono text-sm">
    כפרה עובדים (פסקת פתיחה על ורסטיליות, עומק ולוח המגנטים של סלחרס)
  </div>

  <!-- Interactive Tactical Board Section -->
  <div class="rounded-md border border-neutral-200 dark:border-neutral-800 bg-[#0b1329] p-4 sm:p-6 my-6 shadow-xl" id="tactical-board-app">
    
    <!-- Header & Controls -->
    <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 border-b border-slate-800 pb-4 mb-4">
      <div>
        <div class="flex items-center gap-2">
          <span class="text-xl">📋</span>
          <h3 class="text-base sm:text-lg font-bold text-white">לוח מגנטים טקטי אינטראקטיבי</h3>
          <span class="text-[10px] font-mono bg-sky-500/20 text-sky-400 px-2 py-0.5 rounded border border-sky-500/30">LAB</span>
        </div>
        <p class="text-xs text-slate-400 font-sans mt-0.5">
          בחרו פריסט קומבינציה מוכן או גררו/החליפו שחקניות מהספסל למגרש
        </p>
      </div>

      <!-- Presets Buttons -->
      <div class="flex flex-wrap gap-1.5 font-mono text-xs">
        <button onclick="setPreset('combo1')" id="btn-combo1" class="px-2.5 py-1.5 rounded font-bold transition-all bg-sky-600 text-white shadow">
          1. פיצוח בלוק (4-2-3-1)
        </button>
        <button onclick="setPreset('combo2')" id="btn-combo2" class="px-2.5 py-1.5 rounded font-bold transition-all bg-slate-800 hover:bg-slate-700 text-slate-300">
          2. מכבש לחץ (4-3-3)
        </button>
        <button onclick="setPreset('combo3')" id="btn-combo3" class="px-2.5 py-1.5 rounded font-bold transition-all bg-slate-800 hover:bg-slate-700 text-slate-300">
          3. שליטה ואירופה (4-3-3)
        </button>
      </div>
    </div>

    <!-- Active Preset Description Card -->
    <div id="preset-info-box" class="mb-4 p-3 rounded bg-slate-900/90 border border-slate-800 text-xs font-sans text-slate-300">
      <!-- Injected via JS -->
    </div>

    <!-- The 2D Tactical Football Pitch -->
    <div class="relative w-full max-w-2xl mx-auto rounded-lg overflow-hidden border border-emerald-500/30 shadow-inner" style="height: 480px; background: radial-gradient(circle at center, #064e3b 0%, #022c22 100%);">
      
      <!-- Pitch Lines -->
      <div class="absolute inset-2 border-2 border-white/20 rounded pointer-events-none"></div>
      <div class="absolute top-1/2 left-0 right-0 h-0.5 bg-white/20 -translate-y-1/2 pointer-events-none"></div>
      <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-28 h-28 border-2 border-white/20 rounded-full pointer-events-none"></div>
      <!-- Top Box (Opponent) -->
      <div class="absolute top-2 left-1/2 -translate-x-1/2 w-48 h-20 border-2 border-white/20 border-t-0 pointer-events-none"></div>
      <div class="absolute top-2 left-1/2 -translate-x-1/2 w-24 h-8 border-2 border-white/20 border-t-0 pointer-events-none"></div>
      <!-- Bottom Box (Arsenal Goal) -->
      <div class="absolute bottom-2 left-1/2 -translate-x-1/2 w-48 h-20 border-2 border-white/20 border-b-0 pointer-events-none"></div>
      <div class="absolute bottom-2 left-1/2 -translate-x-1/2 w-24 h-8 border-2 border-white/20 border-b-0 pointer-events-none"></div>

      <!-- 11 On-Pitch Magnet Slots -->
      <div id="pitch-slots-container" class="absolute inset-0">
        <!-- Rendered by JS -->
      </div>
    </div>

    <!-- Squad Bench / Pool -->
    <div class="mt-5 pt-4 border-t border-slate-800">
      <div class="flex items-center justify-between mb-2">
        <span class="text-xs font-mono font-bold text-slate-300 uppercase tracking-wider">
          מאגר שחקניות הסגל (לחצו על שחקנית במגרש ושחקנית בספסל להחלפה)
        </span>
        <span class="text-[11px] font-mono text-slate-500" id="selected-indicator">לא נבחרה שחקנית להחלפה</span>
      </div>
      
      <div class="flex flex-wrap gap-1.5" id="bench-container">
        <!-- Rendered by JS -->
      </div>
    </div>

  </div>

  <!-- Combination 1 Analysis Narrative -->
  <article class="space-y-3 pt-2">
    <h2 class="text-xl font-bold text-neutral-900 dark:text-white flex items-center gap-2">
      <span>1. קומבינציה א': מפרקת הבלוקים והעומס האסימטרי (4-2-3-1)</span>
    </h2>
    <div class="p-4 rounded border border-amber-500/30 bg-amber-500/10 text-amber-600 dark:text-amber-400 font-mono text-sm">
      כפרה עובדים (אלסיה רוסו בעמדת ה-10 החופשית, סטינה בלקסטניוס / מישל אג'ימאן בשפיץ, מריונה בימין שנכנסת פנימה ומפנה את כל הקו לסמילה הולמברג, ליטל ו-G בשתי שישיות)
    </div>
  </article>

  <!-- Combination 2 Analysis Narrative -->
  <article class="space-y-3 pt-2">
    <h2 class="text-xl font-bold text-neutral-900 dark:text-white flex items-center gap-2">
      <span>2. קומבינציה ב': מכבש הלחץ הגבוה ומעברים מהירים (4-3-3)</span>
    </h2>
    <div class="p-4 rounded border border-amber-500/30 bg-amber-500/10 text-amber-600 dark:text-amber-400 font-mono text-sm">
      כפרה עובדים סבלנות (מריונה מנהלת מעברים, רוסו וסטינה לוחצות גבוה, סטאנוויי חונקת את הקישור מול צ'לסי וסיטי)
    </div>
  </article>

  <!-- Combination 3 Analysis Narrative -->
  <article class="space-y-3 pt-2">
    <h2 class="text-xl font-bold text-neutral-900 dark:text-white flex items-center gap-2">
      <span>3. קומבינציה ג': שליטה סבלנית, הגנה וניהול קצב (4-3-3)</span>
    </h2>
    <div class="p-4 rounded border border-amber-500/30 bg-amber-500/10 text-amber-600 dark:text-amber-400 font-mono text-sm">
      כפרה עובדים (קישור מעובה, משחקי חוץ בצ'מפיונס ליג ונעילת משחק)
    </div>
  </article>

  <!-- Standardized Post Pagination -->
  {% include post_pagination.html %}

</div>

<!-- Interactive Tactical Board JavaScript Logic -->
<script>
(function() {
  const SQUAD_POOL = [
    { id: "vandomselaar", name: "Daphne van Domselaar", nameHe: "ואן דומסלאר", pos: "GK", no: "1" },
    { id: "misa", name: "Misa Rodríguez", nameHe: "מיסה", pos: "GK", no: "13" },
    { id: "williamson", name: "Leah Williamson", nameHe: "ויליאמסון", pos: "DF", no: "6" },
    { id: "wubbenmoy", name: "Lotte Wubben-Moy", nameHe: "וובן-מוי", pos: "DF", no: "3" },
    { id: "fox", name: "Emily Fox", nameHe: "פוקס", pos: "DF", no: "2" },
    { id: "catley", name: "Steph Catley", nameHe: "קאטלי", pos: "DF", no: "7" },
    { id: "batlle", name: "Ona Batlle", nameHe: "באטייה", pos: "DF", no: "22" },
    { id: "hinds", name: "Taylor Hinds", nameHe: "היינדס", pos: "DF", no: "12" },
    { id: "holmberg", name: "Smilla Holmberg", nameHe: "הולמברג", pos: "DF", no: "25" },
    { id: "little", name: "Kim Little", nameHe: "ליטל", pos: "MF", no: "10" },
    { id: "stanway", name: "Georgia Stanway", nameHe: "סטאנוויי (G)", pos: "MF", no: "8" },
    { id: "maanum", name: "Frida Maanum", nameHe: "מאנום", pos: "MF", no: "12" },
    { id: "reuteler", name: "Géraldine Reuteler", nameHe: "רויטלר", pos: "MF", no: "14" },
    { id: "baum", name: "Lisa Baum", nameHe: "ליסה באום", pos: "MF", no: "19" },
    { id: "cooneycross", name: "Kyra Cooney-Cross", nameHe: "קוני-קרוס", pos: "MF", no: "32" },
    { id: "russo", name: "Alessia Russo", nameHe: "רוסו", pos: "FW", no: "23" },
    { id: "blackstenius", name: "Stina Blackstenius", nameHe: "סטינה", pos: "FW", no: "25" },
    { id: "agyemang", name: "Michelle Agyemang", nameHe: "מיש", pos: "FW", no: "27" },
    { id: "mariona", name: "Mariona Caldentey", nameHe: "מריונה", pos: "FW", no: "8" },
    { id: "kelly", name: "Chloe Kelly", nameHe: "קלי", pos: "FW", no: "18" },
    { id: "smith", name: "Olivia Smith", nameHe: "סמית'", pos: "FW", no: "20" },
    { id: "cerci", name: "Selina Cerci", nameHe: "צ'רצ'י", pos: "FW", no: "9" },
    { id: "kafaji", name: "Rosa Kafaji", nameHe: "קפאג'י", pos: "FW", no: "16" }
  ];

  const PRESETS = {
    combo1: {
      name: "1. פיצוח בלוק נמוך ועומס אסימטרי (4-2-3-1)",
      desc: "<strong>טקטיקת מפתח:</strong> רוסו משחקת ב-10 חופשית, סטינה/מיש כ-9 פיזית ברחבה. מריונה נכנסת פנימה מימין ומשאירה את כל הקו לסמילה הולמברג שרצה קדימה, כשליטל ו-G סוגרות את האמצע.",
      lineup: [
        { slot: 0, x: 50, y: 88, player: "vandomselaar", role: "GK" },
        { slot: 1, x: 82, y: 72, player: "holmberg", role: "RB (קו מלא)" },
        { slot: 2, x: 62, y: 76, player: "williamson", role: "CB" },
        { slot: 3, x: 38, y: 76, player: "wubbenmoy", role: "CB" },
        { slot: 4, x: 18, y: 72, player: "batlle", role: "LB" },
        { slot: 5, x: 60, y: 55, player: "stanway", role: "DM (G)" },
        { slot: 6, x: 40, y: 55, player: "little", role: "DM (C)" },
        { slot: 7, x: 75, y: 36, player: "mariona", role: "RW (Inverted)" },
        { slot: 8, x: 50, y: 35, player: "russo", role: "AM (#10)" },
        { slot: 9, x: 25, y: 36, player: "smith", role: "LW" },
        { slot: 10, x: 50, y: 15, player: "blackstenius", role: "ST (#9)" }
      ]
    },
    combo2: {
      name: "2. מכבש לחץ גבוה ומעברים מהירים (4-3-3)",
      desc: "<strong>טקטיקת מפתח:</strong> רוסו וסטינה לוחצות יחד את קו ההגנה, מריונה מנהלת מעברים מהאגף/אמצע, וסטאנוויי חונקת התקפות יריב עם 7.9 חילוצים בשליש ההתקפי.",
      lineup: [
        { slot: 0, x: 50, y: 88, player: "vandomselaar", role: "GK" },
        { slot: 1, x: 80, y: 74, player: "fox", role: "RB" },
        { slot: 2, x: 60, y: 76, player: "williamson", role: "CB" },
        { slot: 3, x: 40, y: 76, player: "wubbenmoy", role: "CB" },
        { slot: 4, x: 20, y: 74, player: "batlle", role: "LB" },
        { slot: 5, x: 50, y: 58, player: "little", role: "DM" },
        { slot: 6, x: 68, y: 48, player: "stanway", role: "CM (Press)" },
        { slot: 7, x: 32, y: 48, player: "maanum", role: "CM (Box)" },
        { slot: 8, x: 75, y: 25, player: "kelly", role: "RW" },
        { slot: 9, x: 25, y: 25, player: "mariona", role: "LW" },
        { slot: 10, x: 50, y: 16, player: "russo", role: "ST (Press #1)" }
      ]
    },
    combo3: {
      name: "3. שליטה סבלנית, הגנה וניהול קצב (4-3-3)",
      desc: "<strong>טקטיקת מפתח:</strong> הרכב משחקי חוץ באירופה. קישור מעובה וטכני עם ליטל, סטאנוויי ורויטלר, באטייה ופוקס סוגרות הרמטית את האגפים ורוסו מכריעה במאבקים.",
      lineup: [
        { slot: 0, x: 50, y: 88, player: "misa", role: "GK" },
        { slot: 1, x: 80, y: 74, player: "fox", role: "RB" },
        { slot: 2, x: 60, y: 76, player: "williamson", role: "CB" },
        { slot: 3, x: 40, y: 76, player: "catley", role: "CB" },
        { slot: 4, x: 20, y: 74, player: "batlle", role: "LB" },
        { slot: 5, x: 50, y: 60, player: "stanway", role: "DM (Anchor)" },
        { slot: 6, x: 68, y: 48, player: "little", role: "CM" },
        { slot: 7, x: 32, y: 48, player: "reuteler", role: "CM" },
        { slot: 8, x: 75, y: 26, player: "mariona", role: "RW" },
        { slot: 9, x: 25, y: 26, player: "baum", role: "LW" },
        { slot: 10, x: 50, y: 16, player: "russo", role: "ST" }
      ]
    }
  };

  let currentLineup = JSON.parse(JSON.stringify(PRESETS.combo1.lineup));
  let selectedSlotIndex = null;

  function renderPitch() {
    const container = document.getElementById("pitch-slots-container");
    if (!container) return;
    container.innerHTML = "";

    currentLineup.forEach((slot, idx) => {
      const pData = SQUAD_POOL.find(p => p.id === slot.player) || { nameHe: slot.player, pos: slot.role, no: "--" };
      const isSelected = selectedSlotIndex === idx;

      const slotEl = document.createElement("div");
      slotEl.className = "absolute -translate-x-1/2 -translate-y-1/2 cursor-pointer flex flex-col items-center group transition-transform duration-150";
      slotEl.style.left = slot.x + "%";
      slotEl.style.top = slot.y + "%";
      slotEl.onclick = () => onPitchSlotClick(idx);

      slotEl.innerHTML = `
        <div class="relative flex items-center justify-center w-9 h-9 sm:w-10 sm:h-10 rounded-full shadow-lg border-2 font-mono font-bold text-xs transition-all ${
          isSelected 
            ? "border-amber-400 bg-amber-500 text-slate-950 scale-110 ring-4 ring-amber-400/40 z-20" 
            : "border-sky-300 bg-slate-900 text-sky-200 group-hover:scale-105 group-hover:border-white z-10"
        }">
          <span>${pData.no ? '#' + pData.no : pData.pos}</span>
        </div>
        <div class="mt-1 px-1.5 py-0.5 rounded bg-slate-950/80 backdrop-blur border border-slate-700/80 text-[10px] sm:text-[11px] font-bold text-white whitespace-nowrap shadow pointer-events-none">
          ${pData.nameHe}
        </div>
        <div class="text-[9px] font-mono text-sky-300 -mt-0.5 pointer-events-none">
          ${slot.role}
        </div>
      `;
      container.appendChild(slotEl);
    });
  }

  function renderBench() {
    const container = document.getElementById("bench-container");
    if (!container) return;
    container.innerHTML = "";

    const onPitchIds = currentLineup.map(s => s.player);

    SQUAD_POOL.forEach(p => {
      const isOnPitch = onPitchIds.includes(p.id);
      const chip = document.createElement("button");
      chip.className = `px-2 py-1 rounded font-sans text-xs flex items-center gap-1.5 transition-all border ${
        isOnPitch 
          ? "bg-slate-900/40 text-slate-500 border-slate-800 opacity-60" 
          : "bg-slate-900 hover:bg-slate-800 text-slate-200 border-slate-700 hover:border-sky-400 shadow-sm"
      }`;
      chip.onclick = () => onBenchClick(p.id);

      chip.innerHTML = `
        <span class="font-mono text-[10px] text-sky-400">#${p.no || '-'}</span>
        <span class="font-medium">${p.nameHe}</span>
        <span class="text-[9px] font-mono px-1 rounded bg-slate-800 text-slate-400">${p.pos}</span>
      `;
      container.appendChild(chip);
    });
  }

  function onPitchSlotClick(idx) {
    if (selectedSlotIndex === idx) {
      selectedSlotIndex = null;
    } else {
      selectedSlotIndex = idx;
    }
    updateIndicator();
    renderPitch();
  }

  function onBenchClick(playerId) {
    if (selectedSlotIndex === null) {
      // Find first slot of matching or free
      alert("בחרו תחילה עמדה במגרש כדי להחליף שחקנית.");
      return;
    }
    currentLineup[selectedSlotIndex].player = playerId;
    selectedSlotIndex = null;
    updateIndicator();
    renderPitch();
    renderBench();
  }

  function updateIndicator() {
    const ind = document.getElementById("selected-indicator");
    if (!ind) return;
    if (selectedSlotIndex !== null) {
      const slot = currentLineup[selectedSlotIndex];
      const p = SQUAD_POOL.find(p => p.id === slot.player);
      ind.innerHTML = `<span class="text-amber-400 font-bold">עמדה נבחרת: ${slot.role} (${p ? p.nameHe : ''}) - לחצו על שחקנית בספסל להחלפה</span>`;
    } else {
      ind.textContent = "לא נבחרה עמדה להחלפה";
    }
  }

  window.setPreset = function(presetKey) {
    const p = PRESETS[presetKey];
    if (!p) return;
    currentLineup = JSON.parse(JSON.stringify(p.lineup));
    selectedSlotIndex = null;

    // Update buttons
    ['combo1', 'combo2', 'combo3'].forEach(k => {
      const b = document.getElementById('btn-' + k);
      if (b) {
        if (k === presetKey) {
          b.className = "px-2.5 py-1.5 rounded font-bold transition-all bg-sky-600 text-white shadow";
        } else {
          b.className = "px-2.5 py-1.5 rounded font-bold transition-all bg-slate-800 hover:bg-slate-700 text-slate-300";
        }
      }
    });

    const infoBox = document.getElementById("preset-info-box");
    if (infoBox) {
      infoBox.innerHTML = `
        <div class="font-bold text-sky-400 mb-1">${p.name}</div>
        <div>${p.desc}</div>
      `;
    }

    updateIndicator();
    renderPitch();
    renderBench();
  };

  // Init
  document.addEventListener("DOMContentLoaded", () => {
    window.setPreset('combo1');
  });
  if (document.readyState === "complete" || document.readyState === "interactive") {
    window.setPreset('combo1');
  }
})();
</script>
