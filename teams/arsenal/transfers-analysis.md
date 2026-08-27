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

  <!-- Opening Narrative Section (User Drafting Area) -->
  <div class="p-4 rounded border border-amber-500/30 bg-amber-500/10 text-amber-600 dark:text-amber-400 font-mono text-sm">
    כפרה עובדים (פסקת פתיחה על ורסטיליות, עומק ולוח המגנטים של סלחרס)
  </div>

  <!-- Collapsible Interactive Tactical Lab -->
  <details class="group rounded-md border border-neutral-200 dark:border-neutral-800 bg-[#0b1329] p-4 sm:p-5 my-6 shadow-xl" open>
    <summary class="cursor-pointer font-bold text-base text-neutral-900 dark:text-white flex items-center justify-between select-none list-none">
      <div class="space-y-0.5">
        <span class="flex items-center gap-2">
          <span>🧪 מעבדה טקטית אינטראקטיבית: לוח המגנטים של ארסנל</span>
          <span class="text-[10px] font-mono bg-sky-500/20 text-sky-400 px-2 py-0.5 rounded border border-sky-500/30">LAB</span>
        </span>
        <p class="text-xs text-slate-400 font-normal">
          לחצו כאן כדי להציג/להסתיר את המגרש, להתנסות בהרכבים שונים ולגרור מגנטים בחופשיות
        </p>
      </div>
      <span class="text-xs font-mono text-primary-600 dark:text-primary-400 px-2.5 py-1 rounded bg-neutral-100 dark:bg-neutral-800 border border-neutral-200 dark:border-neutral-700">
        הצג / הסתר מעבדה
      </span>
    </summary>

    <div class="pt-4 border-t border-slate-800 mt-4 select-none" id="tactical-board-app">
      <!-- Header & Controls -->
      <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 pb-3 mb-3 border-b border-slate-800/80">
        <div>
          <div class="flex items-center gap-2">
            <span class="text-sm font-bold text-white">לוח מגנטים חופשי</span>
            <span id="player-count-badge" class="text-[11px] font-mono px-2 py-0.5 rounded font-bold border border-emerald-500/40 bg-emerald-950/60 text-emerald-400">
              11 / 11 שחקניות במגרש
            </span>
          </div>
          <p class="text-xs text-slate-400 font-sans mt-0.5">
            גררו מגנטים בחופשיות לכל נקודה, הוסיפו מהספסל או מחקו מגנט בלחיצה (✖)
          </p>
        </div>

        <!-- Presets & Reset Buttons -->
        <div class="flex flex-wrap items-center gap-1.5 font-mono text-xs">
          <button onclick="setFormation('combo1')" id="btn-combo1" class="px-2.5 py-1.5 rounded font-bold transition-all bg-sky-600 text-white shadow">
            4-2-3-1 (בלוק נמוך)
          </button>
          <button onclick="setFormation('combo2')" id="btn-combo2" class="px-2.5 py-1.5 rounded font-bold transition-all bg-slate-800 hover:bg-slate-700 text-slate-300">
            4-2-3-1 (קבוצות טופ)
          </button>
          <button onclick="setFormation('combo3')" id="btn-combo3" class="px-2.5 py-1.5 rounded font-bold transition-all bg-slate-800 hover:bg-slate-700 text-slate-300">
            4-3-3 (אירופה ומעברים)
          </button>
          <button onclick="clearPitch()" class="px-2 py-1.5 rounded font-bold transition-all bg-rose-950/40 text-rose-400 border border-rose-800/60 hover:bg-rose-900/60">
            נקה לוח
          </button>
        </div>
      </div>

      <!-- Active Preset Description Box -->
      <div id="preset-info-box" class="mb-4 p-3 rounded bg-slate-900/90 border border-slate-800 text-xs font-sans text-slate-300">
        <strong class="text-sky-400">קומבינציה א' (4-2-3-1 אסימטרי):</strong> רוסו ב-10 חופשית, סטינה/מיש כ-9 פיזית. מריונה בימין נכנסת פנימה ומפנה את כל הקו לסמילה הולמברג שעולה בספרינטים, כשליטל וסטאנוויי סוגרות את האמצע.
      </div>

      <!-- The 2D Tactical Football Pitch (Free Drag Surface) -->
      <div id="pitch-container" class="relative w-full max-w-2xl mx-auto rounded-lg overflow-hidden border-2 border-emerald-500/40 shadow-2xl touch-none" style="height: 520px; background: radial-gradient(circle at center, #064e3b 0%, #022c22 100%);">
        
        <!-- Pitch Markings -->
        <div class="absolute inset-2 border-2 border-white/20 rounded pointer-events-none"></div>
        <div class="absolute top-1/2 left-0 right-0 h-0.5 bg-white/20 -translate-y-1/2 pointer-events-none"></div>
        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-32 h-32 border-2 border-white/20 rounded-full pointer-events-none"></div>
        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-2 h-2 bg-white/40 rounded-full pointer-events-none"></div>

        <!-- Top Goal Area (Opponent Box) -->
        <div class="absolute top-2 left-1/2 -translate-x-1/2 w-56 h-24 border-2 border-white/20 border-t-0 pointer-events-none"></div>
        <div class="absolute top-2 left-1/2 -translate-x-1/2 w-28 h-10 border-2 border-white/20 border-t-0 pointer-events-none"></div>

        <!-- Bottom Goal Area (Arsenal Box) -->
        <div class="absolute bottom-2 left-1/2 -translate-x-1/2 w-56 h-24 border-2 border-white/20 border-b-0 pointer-events-none"></div>
        <div class="absolute bottom-2 left-1/2 -translate-x-1/2 w-28 h-10 border-2 border-white/20 border-b-0 pointer-events-none"></div>

        <!-- Pitch Drop Target / Magnets Area -->
        <div id="pitch-magnets-layer" class="absolute inset-0">
          <!-- Draggable magnets injected here -->
        </div>
      </div>

      <!-- Bench / Player Magnet Pool -->
      <div class="mt-5 pt-4 border-t border-slate-800">
        <div class="flex items-center justify-between mb-2.5">
          <span class="text-xs font-mono font-bold text-slate-300 uppercase tracking-wider">
            מאגר שחקניות (לחצו על שחקנית להוספה למגרש):
          </span>
          <span class="text-[11px] font-mono text-slate-400">ניתן להציב עד 11 שחקניות</span>
        </div>
        
        <div class="flex flex-wrap gap-1.5" id="bench-container">
          <!-- Rendered by JS -->
        </div>
      </div>
    </div>
  </details>

  <!-- Combination 1 Analysis Narrative -->
  <article class="space-y-3 pt-2">
    <h2 class="text-xl font-bold text-neutral-900 dark:text-white flex items-center gap-2">
      <span>1. קומבינציה א': מפרקת הבלוקים והעומס האסימטרי (4-2-3-1)</span>
    </h2>
    <div class="p-4 rounded border border-amber-500/30 bg-amber-500/10 text-amber-600 dark:text-amber-400 font-mono text-sm">
      כפרה עובדים (אלסיה רוסו בעמדת ה-10 החופשית, סטינה בלקסטניוס / מישל אג'ימאן בשפיץ, מריונה בימין שנכנסת פנימה ומפנה את כל הקו לסמילה הולמברג, ליטל וסטאנוויי בשתי שישיות)
    </div>
  </article>

  <!-- Combination 2 Analysis Narrative -->
  <article class="space-y-3 pt-2">
    <h2 class="text-xl font-bold text-neutral-900 dark:text-white flex items-center gap-2">
      <span>2. קומבינציה ב': מול קבוצות הטופ ותקיפת שטחים פנויים (4-2-3-1)</span>
    </h2>
    <div class="p-4 rounded border border-amber-500/30 bg-amber-500/10 text-amber-600 dark:text-amber-400 font-mono text-sm">
      כפרה עובדים סבלנות (רוסו ב-10, סטינה/מיש בשפיץ, מריונה וסמית' באגפים, G וליטל בדאבל פיבוט של שליטה ועוצמה מול צ'לסי וסיטי)
    </div>
  </article>

  <!-- Combination 3 Analysis Narrative -->
  <article class="space-y-3 pt-2">
    <h2 class="text-xl font-bold text-neutral-900 dark:text-white flex items-center gap-2">
      <span>3. קומבינציה ג': מול אריות אירופה ומעברים מהירים (4-3-3)</span>
    </h2>
    <div class="p-4 rounded border border-amber-500/30 bg-amber-500/10 text-amber-600 dark:text-amber-400 font-mono text-sm">
      כפרה עובדים (כשאין לארסנל את הכדור מול ברצלונה/אירופה – הגנה קומפקטית, סטאנוויי-רויטלר-ליטל באמצע, ויציאה מהירה לרוסו, סטינה וקלי)
    </div>
  </article>

  <!-- Combination 4 Analysis Narrative (Chasing Goal / Edge Case) -->
  <article class="space-y-3 pt-2">
    <h2 class="text-xl font-bold text-neutral-900 dark:text-white flex items-center gap-2">
      <span>4. קומבינציה ד': מקרה קצה – "חייבים גול בדקה ה-80" (3-2-4-1 / 3-2-2-3)</span>
    </h2>
    <div class="p-4 rounded border border-amber-500/30 bg-amber-500/10 text-amber-600 dark:text-amber-400 font-mono text-sm">
      כפרה עובדים (באטייה נכנסת כפיבוט שני, סמילה וסמית' רוחב מקסימלי, דאבל 10 של רוסו ומריונה וצמד חלוצות ברחבה)
    </div>
  </article>

  <!-- Standardized Post Pagination -->
  {% include post_pagination.html %}

</div>

<!-- Free Drag-and-Drop Tactical Pitch Script -->
<script>
(function() {
  const SQUAD = [
    { id: "vandomselaar", name: "Daphne van Domselaar", nameHe: "ואן דומסלאר", pos: "GK", no: "1" },
    { id: "misa", name: "Misa Rodríguez", nameHe: "מיסה רודריגז", pos: "GK", no: "13" },
    { id: "williamson", name: "Leah Williamson", nameHe: "ויליאמסון", pos: "DF", no: "6" },
    { id: "wubbenmoy", name: "Lotte Wubben-Moy", nameHe: "וובן-מוי", pos: "DF", no: "3" },
    { id: "fox", name: "Emily Fox", nameHe: "פוקס", pos: "DF", no: "2" },
    { id: "catley", name: "Steph Catley", nameHe: "קאטלי", pos: "DF", no: "7" },
    { id: "batlle", name: "Ona Batlle", nameHe: "באטייה", pos: "DF", no: "22" },
    { id: "hinds", name: "Taylor Hinds", nameHe: "היינדס", pos: "DF", no: "12" },
    { id: "holmberg", name: "Smilla Holmberg", nameHe: "הולמברג", pos: "DF", no: "25" },
    { id: "little", name: "Kim Little", nameHe: "ליטל", pos: "MF", no: "10" },
    { id: "stanway", name: "Georgia Stanway", nameHe: "סטאנוויי", pos: "MF", no: "8" },
    { id: "maanum", name: "Frida Maanum", nameHe: "מאנום", pos: "MF", no: "12" },
    { id: "reuteler", name: "Géraldine Reuteler", nameHe: "רויטלר", pos: "MF", no: "14" },
    { id: "baum", name: "Lisa Baum", nameHe: "ליסה באום", pos: "MF", no: "19" },
    { id: "cooneycross", name: "Kyra Cooney-Cross", nameHe: "קוני-קרוס", pos: "MF", no: "32" },
    { id: "russo", name: "Alessia Russo", nameHe: "רוסו", pos: "FW", no: "23" },
    { id: "blackstenius", name: "Stina Blackstenius", nameHe: "סטינה", pos: "FW", no: "25" },
    { id: "agyemang", name: "Michelle Agyemang", nameHe: "אג'ימאן", pos: "FW", no: "27" },
    { id: "mariona", name: "Mariona Caldentey", nameHe: "מריונה", pos: "FW", no: "8" },
    { id: "kelly", name: "Chloe Kelly", nameHe: "קלי", pos: "FW", no: "18" },
    { id: "smith", name: "Olivia Smith", nameHe: "סמית'", pos: "FW", no: "20" },
    { id: "cerci", name: "Selina Cerci", nameHe: "צ'רצ'י", pos: "FW", no: "9" },
    { id: "kafaji", name: "Rosa Kafaji", nameHe: "קפאג'י", pos: "FW", no: "16" }
  ];

  const FORMATIONS = {
    combo1: {
      name: "1. פיצוח בלוק נמוך ועומס אסימטרי (4-2-3-1)",
      desc: "<strong>טקטיקת מפתח:</strong> רוסו ב-10 חופשית, סטינה כ-9 פיזית ברחבה. מריונה נכנסת פנימה מימין ומשאירה את כל הקו לסמילה הולמברג שעולה בספרינטים, כשליטל וסטאנוויי בפיבוט אחורי.",
      players: [
        { id: "vandomselaar", x: 50, y: 88, role: "GK" },
        { id: "holmberg", x: 82, y: 68, role: "RB" },
        { id: "williamson", x: 62, y: 76, role: "CB" },
        { id: "wubbenmoy", x: 38, y: 76, role: "CB" },
        { id: "batlle", x: 18, y: 72, role: "LB" },
        { id: "stanway", x: 60, y: 55, role: "DM" },
        { id: "little", x: 40, y: 55, role: "DM" },
        { id: "mariona", x: 74, y: 36, role: "RW" },
        { id: "russo", x: 50, y: 35, role: "AM" },
        { id: "smith", x: 26, y: 36, role: "LW" },
        { id: "blackstenius", x: 50, y: 15, role: "ST" }
      ]
    },
    combo2: {
      name: "2. מול קבוצות הטופ ותקיפת שטחים (4-2-3-1)",
      desc: "<strong>טקטיקת מפתח:</strong> רוסו ב-10 מייצרת שטח, סטינה ב-9 מאיימת לעומק, מריונה וסמית' באגפים, וסטאנוויי (G) וליטל תוקפות שטח פנוי מקו שני ומאזנות את הקישור.",
      players: [
        { id: "vandomselaar", x: 50, y: 88, role: "GK" },
        { id: "fox", x: 80, y: 74, role: "RB" },
        { id: "williamson", x: 60, y: 76, role: "CB" },
        { id: "wubbenmoy", x: 40, y: 76, role: "CB" },
        { id: "batlle", x: 20, y: 74, role: "LB" },
        { id: "stanway", x: 62, y: 56, role: "DM (G)" },
        { id: "little", x: 38, y: 56, role: "DM (C)" },
        { id: "mariona", x: 75, y: 36, role: "RW" },
        { id: "russo", x: 50, y: 35, role: "AM (#10)" },
        { id: "smith", x: 25, y: 36, role: "LW" },
        { id: "blackstenius", x: 50, y: 15, role: "ST (#9)" }
      ]
    },
    combo3: {
      name: "3. מול אריות אירופה ומעברים מהירים (4-3-3)",
      desc: "<strong>טקטיקת מפתח:</strong> כשאין לארסנל את הכדור מול ברצלונה/אירופה – הגנה קומפקטית, סטאנוויי-רויטלר-ליטל באמצע, ויציאה מהירה לרוסו, סטינה וקלי.",
      players: [
        { id: "misa", x: 50, y: 88, role: "GK" },
        { id: "fox", x: 80, y: 74, role: "RB" },
        { id: "williamson", x: 60, y: 76, role: "CB" },
        { id: "catley", x: 40, y: 76, role: "CB" },
        { id: "batlle", x: 20, y: 74, role: "LB" },
        { id: "stanway", x: 50, y: 60, role: "DM (Anchor)" },
        { id: "little", x: 68, y: 48, role: "CM" },
        { id: "reuteler", x: 32, y: 48, role: "CM" },
        { id: "kelly", x: 75, y: 26, role: "RW" },
        { id: "mariona", x: 25, y: 26, role: "LW" },
        { id: "russo", x: 50, y: 16, role: "ST" }
      ]
    }
  };

  let pitchPlayers = JSON.parse(JSON.stringify(FORMATIONS.combo1.players));

  function renderPitch() {
    const layer = document.getElementById("pitch-magnets-layer");
    if (!layer) return;
    layer.innerHTML = "";

    pitchPlayers.forEach((pObj) => {
      const pData = SQUAD.find(p => p.id === pObj.id) || { nameHe: pObj.id, no: "--", pos: pObj.role };
      
      const magnet = document.createElement("div");
      magnet.className = "absolute -translate-x-1/2 -translate-y-1/2 cursor-grab active:cursor-grabbing flex flex-col items-center group touch-none";
      magnet.style.left = pObj.x + "%";
      magnet.style.top = pObj.y + "%";
      magnet.dataset.id = pObj.id;

      magnet.innerHTML = `
        <div class="relative flex items-center justify-center w-10 h-10 rounded-full shadow-2xl border-2 border-sky-300 bg-slate-900 text-sky-200 font-mono font-bold text-xs group-hover:scale-110 group-hover:border-white transition-transform">
          <span>${pData.no ? '#' + pData.no : pData.pos}</span>
          <button onclick="removePlayer('${pObj.id}', event)" class="absolute -top-1 -right-1 w-4 h-4 rounded-full bg-rose-600 hover:bg-rose-500 text-white flex items-center justify-center text-[10px] shadow font-sans leading-none z-30">
            &times;
          </button>
        </div>
        <div class="mt-1 px-1.5 py-0.5 rounded bg-slate-950/90 backdrop-blur border border-slate-700/80 text-[10px] sm:text-[11px] font-bold text-white whitespace-nowrap shadow pointer-events-none">
          ${pData.nameHe}
        </div>
      `;

      attachDragEvents(magnet, pObj);
      layer.appendChild(magnet);
    });

    updateCounters();
    renderBench();
  }

  function renderBench() {
    const container = document.getElementById("bench-container");
    if (!container) return;
    container.innerHTML = "";

    const onPitchIds = pitchPlayers.map(p => p.id);

    SQUAD.forEach(p => {
      const isOnPitch = onPitchIds.includes(p.id);
      const btn = document.createElement("button");
      btn.className = `px-2 py-1 rounded font-sans text-xs flex items-center gap-1.5 transition-all border ${
        isOnPitch 
          ? "bg-slate-900/40 text-slate-500 border-slate-800 opacity-50 cursor-not-allowed" 
          : "bg-slate-900 hover:bg-slate-800 text-slate-200 border-slate-700 hover:border-sky-400 shadow-sm"
      }`;

      if (!isOnPitch) {
        btn.onclick = () => addPlayerToPitch(p.id);
      }

      btn.innerHTML = `
        <span class="font-mono text-[10px] text-sky-400">#${p.no || '-'}</span>
        <span class="font-medium">${p.nameHe}</span>
        <span class="text-[9px] font-mono px-1 rounded bg-slate-800 text-slate-400">${p.pos}</span>
      `;
      container.appendChild(btn);
    });
  }

  function attachDragEvents(el, pObj) {
    let startX, startY, origX, origY;
    const pitch = document.getElementById("pitch-container");

    const onPointerDown = (e) => {
      if (e.target.tagName === 'BUTTON') return;
      e.preventDefault();
      const rect = pitch.getBoundingClientRect();
      startX = e.clientX || (e.touches && e.touches[0].clientX);
      startY = e.clientY || (e.touches && e.touches[0].clientY);
      origX = pObj.x;
      origY = pObj.y;
      el.style.zIndex = "100";

      const onPointerMove = (moveEvt) => {
        const cx = moveEvt.clientX || (moveEvt.touches && moveEvt.touches[0].clientX);
        const cy = moveEvt.clientY || (moveEvt.touches && moveEvt.touches[0].clientY);
        const deltaX = ((cx - startX) / rect.width) * 100;
        const deltaY = ((cy - startY) / rect.height) * 100;

        let newX = Math.max(5, Math.min(95, origX + deltaX));
        let newY = Math.max(5, Math.min(95, origY + deltaY));

        pObj.x = Math.round(newX);
        pObj.y = Math.round(newY);

        el.style.left = pObj.x + "%";
        el.style.top = pObj.y + "%";
      };

      const onPointerUp = () => {
        document.removeEventListener("pointermove", onPointerMove);
        document.removeEventListener("pointerup", onPointerUp);
        document.removeEventListener("touchmove", onPointerMove);
        document.removeEventListener("touchend", onPointerUp);
        el.style.zIndex = "10";
      };

      document.addEventListener("pointermove", onPointerMove);
      document.addEventListener("pointerup", onPointerUp);
      document.addEventListener("touchmove", onPointerMove, { passive: false });
      document.addEventListener("touchend", onPointerUp);
    };

    el.addEventListener("pointerdown", onPointerDown);
    el.addEventListener("touchstart", onPointerDown, { passive: false });
  }

  function addPlayerToPitch(playerId) {
    if (pitchPlayers.length >= 11) {
      alert("יש כבר 11 שחקניות על המגרש. מחקו שחקנית (✖) כדי לפנות מקום.");
      return;
    }
    pitchPlayers.push({
      id: playerId,
      x: 50,
      y: 50,
      role: "MF"
    });
    renderPitch();
  }

  window.removePlayer = function(playerId, e) {
    if (e) e.stopPropagation();
    pitchPlayers = pitchPlayers.filter(p => p.id !== playerId);
    renderPitch();
  };

  window.clearPitch = function() {
    pitchPlayers = [];
    renderPitch();
  };

  window.setFormation = function(comboKey) {
    const f = FORMATIONS[comboKey];
    if (!f) return;
    pitchPlayers = JSON.parse(JSON.stringify(f.players));

    ['combo1', 'combo2', 'combo3'].forEach(k => {
      const b = document.getElementById('btn-' + k);
      if (b) {
        if (k === comboKey) {
          b.className = "px-2.5 py-1.5 rounded font-bold transition-all bg-sky-600 text-white shadow";
        } else {
          b.className = "px-2.5 py-1.5 rounded font-bold transition-all bg-slate-800 hover:bg-slate-700 text-slate-300";
        }
      }
    });

    const infoBox = document.getElementById("preset-info-box");
    if (infoBox) {
      infoBox.innerHTML = `
        <div class="font-bold text-sky-400 mb-1">${f.name}</div>
        <div>${f.desc}</div>
      `;
    }

    renderPitch();
  };

  function updateCounters() {
    const countBadge = document.getElementById("player-count-badge");
    if (!countBadge) return;
    const len = pitchPlayers.length;
    countBadge.textContent = `${len} / 11 שחקניות במגרש`;
    if (len === 11) {
      countBadge.className = "text-[11px] font-mono px-2 py-0.5 rounded font-bold border border-emerald-500/40 bg-emerald-950/60 text-emerald-400";
    } else {
      countBadge.className = "text-[11px] font-mono px-2 py-0.5 rounded font-bold border border-amber-500/40 bg-amber-950/60 text-amber-400";
    }
  }

  // Init
  document.addEventListener("DOMContentLoaded", () => {
    window.setFormation('combo1');
  });
  if (document.readyState === "complete" || document.readyState === "interactive") {
    window.setFormation('combo1');
  }
})();
</script>
