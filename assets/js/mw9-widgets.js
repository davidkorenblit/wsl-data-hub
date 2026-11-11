/**
 * MW9 Interactive Widgets:
 * 1. Arsenal Transition Goals Simulator (לוח טקטי מונפש של השערים החוזרים במעבר)
 * 2. Victoria Pelova Involvement Collapse Chart (גרף צניחת הנגיעות והיצירה)
 * 3. Chelsea Chance Creators Table (טבלת יוצרות המצבים והדילמה הטקטית)
 */

(function() {
  'use strict';

  // =========================================================================
  // 1. ARSENAL TRANSITION GOALS SIMULATION DATA & LOGIC
  // =========================================================================
  const ARSENAL_GOALS = [
    {
      id: "olsson",
      tabLabel: "אולסון (ליברפול, מ' 9)",
      round: "מחזור 9 · אנפילד / פרנטון פארק",
      match: "ליברפול 1 – 2 ארסנל",
      scorer: "אוליביה אולסון (דקה 15')",
      xg: "0.48 xG",
      passer: "ספירי קוברלי (כדור ארוך מחצי המגרש)",
      defender: "ליאה וויליאמסון",
      distance: "38 מטרים בשטח פתוח",
      oppTeam: "ליברפול",
      oppColor: "#DC2626", // Red
      oppTextColor: "#FFFFFF",
      desc: "ארסנל לוחצת גבוה באנפילד, קו ההגנה עומד 40 מטר מהשער שלה. איבוד כדור במעבר מוביל להקשת כדור ישירה מעל וויליאמסון. אולסון רצה קדימה כשוויליאמסון רצה לאחור ללא חיפוי, 1 על 1 נקי מול מיסה וסיומת מדויקת לרשת.",
      // Pitch coordinates (0..800, 0..520) - Arsenal defends LEFT (x: 20..150)
      turnover: { x: 490, y: 190 },
      passTarget: { x: 230, y: 180 },
      strikerStart: { x: 420, y: 170 },
      strikerFinish: { x: 75, y: 245 },
      defenderStart: { x: 340, y: 210 },
      defenderMid: { x: 230, y: 215 },
      defenderEnd: { x: 110, y: 235 },
      gkStart: { x: 45, y: 260 },
      gkEnd: { x: 58, y: 252 },
      goalTarget: { x: 22, y: 250 }
    },
    {
      id: "grant",
      tabLabel: "גרנט (וילה, מ' 8)",
      round: "מחזור 8 · אמירויות",
      match: "ארסנל 1 – 1 אסטון וילה",
      scorer: "צ'סיטי גרנט (דקה 25')",
      xg: "0.52 xG",
      passer: "ג'ורדן נובס (מסירת סרגל במעבר מהיר)",
      defender: "ליאה וויליאמסון וסטף קאטלי",
      distance: "42 מטרים בספרינט אלכסוני",
      oppTeam: "אסטון וילה",
      oppColor: "#0284C7", // Villa sky blue
      oppTextColor: "#FFFFFF",
      desc: "ארסנל שלחה 8 שחקניות קדימה לחצי של וילה. חילוץ כדור סמוך לרחבה, כדור ארוך אחד מוצא את גרנט בספרינט מסחרר באגף הימני. וויליאמסון וקאטלי מנסות לרדוף אך נמצאות בפיגור מובנה של 6–7 מטרים, גרנט חודרת ובועטת פנימה.",
      turnover: { x: 570, y: 350 },
      passTarget: { x: 260, y: 370 },
      strikerStart: { x: 440, y: 360 },
      strikerFinish: { x: 80, y: 290 },
      defenderStart: { x: 350, y: 300 },
      defenderMid: { x: 240, y: 320 },
      defenderEnd: { x: 120, y: 295 },
      gkStart: { x: 45, y: 260 },
      gkEnd: { x: 60, y: 275 },
      goalTarget: { x: 22, y: 280 }
    },
    {
      id: "hurtre",
      tabLabel: "הרטרה (ברמינגהאם, מ' 6)",
      round: "מחזור 6 · אמירויות",
      match: "ארסנל 1 – 1 ברמינגהאם סיטי",
      scorer: "לורי הרטרה (דקה 53')",
      xg: "0.59 xG (Opta Fast Break)",
      passer: "צ'ו סו-היון (שחרור כדור מהיר מקרן)",
      defender: "ליאה וויליאמסון",
      distance: "40 מטרים בספרינט בודד",
      oppTeam: "ברמינגהאם סיטי",
      oppColor: "#2563EB", // Royal blue
      oppTextColor: "#FFFFFF",
      desc: "מתפרצת מהסרטים של ברמינגהאם (מוגדרת רשמית כ-Fast Break על פי אופטה). וויליאמסון נשארת בלמית אחרונה סביב קו האמצע, הרטרה עוקפת אותה בריצה חיצונית ונשארת לבדה לחלוטין מול מיסה רודריגז.",
      turnover: { x: 600, y: 140 },
      passTarget: { x: 270, y: 150 },
      strikerStart: { x: 430, y: 150 },
      strikerFinish: { x: 75, y: 235 },
      defenderStart: { x: 340, y: 190 },
      defenderMid: { x: 240, y: 195 },
      defenderEnd: { x: 115, y: 220 },
      gkStart: { x: 45, y: 260 },
      gkEnd: { x: 55, y: 248 },
      goalTarget: { x: 22, y: 242 }
    },
    {
      id: "shaw",
      tabLabel: "באני שאו (סיטי, מ' 5)",
      round: "מחזור 5 · ג'ובי סטדיום",
      match: "מנצ'סטר סיטי 4 – 2 ארסנל",
      scorer: "קאדיג'ה 'באני' שאו (דקה 84')",
      xg: "0.23 xG (Opta Fast Break)",
      passer: "אאובה פוג'ינו (בישול רשמי בהתקפת מעבר)",
      defender: "ליאה וויליאמסון",
      distance: "35 מטרים במרכז הרחבה",
      oppTeam: "מנצ'סטר סיטי",
      oppColor: "#38BDF8", // City blue
      oppTextColor: "#0F172A",
      desc: "דקה 84, ארסנל שולחת את כל הקבוצה קדימה לנסות להשוות ומפקירה את קו האמצע. פוג'ינו חוטפת ומשגרת את שאו במתפרצת ישירה (מוגדרת רשמית כ-Fast Break על פי אופטה). שאו גוברת על וויליאמסון וסוגרת עניין.",
      turnover: { x: 460, y: 250 },
      passTarget: { x: 220, y: 255 },
      strikerStart: { x: 380, y: 255 },
      strikerFinish: { x: 80, y: 255 },
      defenderStart: { x: 320, y: 255 },
      defenderMid: { x: 220, y: 255 },
      defenderEnd: { x: 110, y: 255 },
      gkStart: { x: 45, y: 260 },
      gkEnd: { x: 60, y: 258 },
      goalTarget: { x: 22, y: 255 }
    },
    {
      id: "zigiotti",
      tabLabel: "זיגיוטי (יונייטד, מ' 3)",
      round: "מחזור 3 · אמירויות",
      match: "ארסנל 1 – 1 מנצ'סטר יונייטד",
      scorer: "ג'וליה זיגיוטי אולמה (דקה 67')",
      xg: "0.50 xG",
      passer: "חטיפת כדור במעבר ישיר לתוך הרחבה",
      defender: "וויליאמסון וקאטלי",
      distance: "32 מטרים חדירה ישירה",
      oppTeam: "מנצ'סטר יונייטד",
      oppColor: "#B91C1C", // United red
      oppTextColor: "#FFFFFF",
      desc: "איבוד כדור של ארסנל במעבר לאחר עלייה של כל הקישור קדימה. כדור עומק שמבתר את קו ההגנה מגיע לזיגיוטי בריצה מקו שני, חודרת מול שער חשוף (מצב ענק של 0.50 xG) וקובעת 1:1 באמירויות.",
      turnover: { x: 500, y: 230 },
      passTarget: { x: 240, y: 250 },
      strikerStart: { x: 410, y: 240 },
      strikerFinish: { x: 80, y: 265 },
      defenderStart: { x: 340, y: 250 },
      defenderMid: { x: 240, y: 255 },
      defenderEnd: { x: 120, y: 260 },
      gkStart: { x: 45, y: 260 },
      gkEnd: { x: 58, y: 262 },
      goalTarget: { x: 22, y: 268 }
    }
  ];

  let currentGoalIdx = 0;
  let isPlaying = false;
  let progress = 0; // 0..1
  let animFrameId = null;
  let animSpeed = 1.0;
  let lastTimestamp = 0;
  const DURATION_MS = 6000; // 6 seconds per simulation run

  function lerp(a, b, t) {
    return a + (b - a) * t;
  }

  function lerpPoint(p1, p2, t) {
    return {
      x: lerp(p1.x, p2.x, t),
      y: lerp(p1.y, p2.y, t)
    };
  }

  window.selectArsenalGoal = function(idx) {
    currentGoalIdx = idx;
    progress = 0;
    renderArsenalTabs();
    updateGoalDetails();
    drawPitchFrame(0);
    if (!isPlaying) {
      playSimulation();
    }
  };

  window.toggleSimPlay = function() {
    if (isPlaying) {
      pauseSimulation();
    } else {
      if (progress >= 1) progress = 0;
      playSimulation();
    }
  };

  window.replaySim = function() {
    progress = 0;
    playSimulation();
  };

  window.setSimSpeed = function(speed) {
    animSpeed = speed;
    const btn1 = document.getElementById("sim-speed-1x");
    const btn15 = document.getElementById("sim-speed-15x");
    if (btn1 && btn15) {
      if (speed === 1.0) {
        btn1.className = "px-2 py-1 text-xs font-mono font-bold rounded bg-primary-600 text-white";
        btn15.className = "px-2 py-1 text-xs font-mono rounded bg-neutral-800 text-neutral-400 hover:text-white";
      } else {
        btn1.className = "px-2 py-1 text-xs font-mono rounded bg-neutral-800 text-neutral-400 hover:text-white";
        btn15.className = "px-2 py-1 text-xs font-mono font-bold rounded bg-primary-600 text-white";
      }
    }
  };

  window.handleScrub = function(val) {
    pauseSimulation();
    progress = val / 100;
    drawPitchFrame(progress);
  };

  function playSimulation() {
    isPlaying = true;
    lastTimestamp = performance.now();
    updatePlayBtnIcon();
    if (animFrameId) cancelAnimationFrame(animFrameId);
    animFrameId = requestAnimationFrame(animLoop);
  }

  function pauseSimulation() {
    isPlaying = false;
    updatePlayBtnIcon();
    if (animFrameId) cancelAnimationFrame(animFrameId);
  }

  function updatePlayBtnIcon() {
    const btn = document.getElementById("sim-play-btn");
    if (!btn) return;
    btn.innerHTML = isPlaying 
      ? '<span class="inline-block w-3 text-center">⏸</span><span>השהה</span>' 
      : '<span class="inline-block w-3 text-center">▶</span><span>נגן הדמיה</span>';
  }

  function animLoop(timestamp) {
    if (!isPlaying) return;
    const delta = timestamp - lastTimestamp;
    lastTimestamp = timestamp;

    progress += (delta / DURATION_MS) * animSpeed;
    if (progress >= 1.0) {
      progress = 1.0;
      drawPitchFrame(1.0);
      pauseSimulation();
      return;
    }

    drawPitchFrame(progress);
    animFrameId = requestAnimationFrame(animLoop);
  }

  function renderArsenalTabs() {
    const container = document.getElementById("ars-sim-tabs");
    if (!container) return;

    let html = "";
    ARSENAL_GOALS.forEach((g, idx) => {
      const active = idx === currentGoalIdx;
      const cls = active
        ? "bg-red-600 text-white font-bold border-red-500 shadow-md ring-2 ring-red-400/50"
        : "bg-neutral-800/90 text-neutral-300 hover:bg-neutral-700 border-neutral-700";
      html += '<button type="button" onclick="selectArsenalGoal(' + idx + ')" class="px-3 py-1.5 rounded-lg border text-xs sm:text-sm transition-all whitespace-nowrap ' + cls + '">';
      html += '<span>⚽ ' + g.tabLabel + '</span>';
      html += '</button>';
    });
    container.innerHTML = html;
  }

  function updateGoalDetails() {
    const g = ARSENAL_GOALS[currentGoalIdx];
    const elMatch = document.getElementById("sim-detail-match");
    const elScorer = document.getElementById("sim-detail-scorer");
    const elXg = document.getElementById("sim-detail-xg");
    const elPasser = document.getElementById("sim-detail-passer");
    const elDefender = document.getElementById("sim-detail-defender");
    const elDistance = document.getElementById("sim-detail-distance");
    const elDesc = document.getElementById("sim-detail-desc");

    if (elMatch) elMatch.innerText = g.match + " (" + g.round + ")";
    if (elScorer) elScorer.innerText = g.scorer;
    if (elXg) elXg.innerText = g.xg;
    if (elPasser) elPasser.innerText = g.passer;
    if (elDefender) elDefender.innerText = g.defender;
    if (elDistance) elDistance.innerText = g.distance;
    if (elDesc) elDesc.innerText = g.desc;
  }

  function drawPitchFrame(t) {
    const g = ARSENAL_GOALS[currentGoalIdx];
    const scrub = document.getElementById("sim-scrubber");
    const phaseLabel = document.getElementById("sim-phase-label");
    if (scrub) scrub.value = Math.round(t * 100);

    // Phases:
    // 0.00..0.20: Phase 1 - High Line & Turnover (קו הגנה גבוה ואיבוד כדור)
    // 0.20..0.50: Phase 2 - Through Ball over the top (מסירת עומק מעל ההגנה)
    // 0.50..0.85: Phase 3 - Footrace into 40m open turf (ספרינט 1 על 1 מול וויליאמסון)
    // 0.85..1.00: Phase 4 - Shot & Goal (סיומת מול השוערת ושער)

    let phaseText = "";
    if (t < 0.20) {
      phaseText = "שלב 1: קו הגנה גבוה של ארסנל (40 מ' מהשער) · איבוד כדור במעבר";
    } else if (t < 0.50) {
      phaseText = "שלב 2: כדור עומק ארוך מוקפץ מעל קו ההגנה לשטח הריק מאחור";
    } else if (t < 0.85) {
      phaseText = "שלב 3: ספרינט 1 על 1 ב-40 מטר פנויים · וויליאמסון במרדף לאחור";
    } else {
      phaseText = "שלב 4: חדירה לרחבה, בעיטה נקייה לפינה וכיבוש!";
    }
    if (phaseLabel) phaseLabel.innerText = phaseText;

    // Elements
    const turnoverEl = document.getElementById("sim-elem-turnover");
    const passLineEl = document.getElementById("sim-elem-passline");
    const ballEl = document.getElementById("sim-elem-ball");
    const strikerEl = document.getElementById("sim-elem-striker");
    const defenderEl = document.getElementById("sim-elem-defender");
    const gkEl = document.getElementById("sim-elem-gk");
    const goalBannerEl = document.getElementById("sim-elem-goal-banner");

    // 1. Turnover point
    if (turnoverEl) {
      turnoverEl.setAttribute("cx", g.turnover.x);
      turnoverEl.setAttribute("cy", g.turnover.y);
      turnoverEl.style.display = t > 0.05 ? "block" : "none";
      // Pulse size
      const pulseR = 8 + Math.sin(t * 20) * 3;
      turnoverEl.setAttribute("r", pulseR);
    }

    // 2. Ball & Pass Vector
    let ballPos = { x: g.turnover.x, y: g.turnover.y };
    if (t < 0.20) {
      ballPos = g.turnover;
      if (passLineEl) passLineEl.setAttribute("d", "");
    } else if (t < 0.50) {
      const pT = (t - 0.20) / 0.30;
      ballPos = lerpPoint(g.turnover, g.passTarget, pT);
      if (passLineEl) {
        passLineEl.setAttribute("d", "M " + g.turnover.x + " " + g.turnover.y + " Q " + ((g.turnover.x + g.passTarget.x)/2) + " " + (Math.min(g.turnover.y, g.passTarget.y) - 40) + " " + ballPos.x + " " + ballPos.y);
      }
    } else if (t < 0.85) {
      const sT = (t - 0.50) / 0.35;
      ballPos = lerpPoint(g.passTarget, g.strikerFinish, sT);
      if (passLineEl) {
        passLineEl.setAttribute("d", "M " + g.turnover.x + " " + g.turnover.y + " Q " + ((g.turnover.x + g.passTarget.x)/2) + " " + (Math.min(g.turnover.y, g.passTarget.y) - 40) + " " + g.passTarget.x + " " + g.passTarget.y);
      }
    } else {
      const gT = (t - 0.85) / 0.15;
      ballPos = lerpPoint(g.strikerFinish, g.goalTarget, gT);
    }

    if (ballEl) {
      ballEl.setAttribute("cx", ballPos.x);
      ballEl.setAttribute("cy", ballPos.y);
    }

    // 3. Striker
    let strikerPos = g.strikerStart;
    if (t < 0.20) {
      strikerPos = g.strikerStart;
    } else if (t < 0.50) {
      const pT = (t - 0.20) / 0.30;
      strikerPos = lerpPoint(g.strikerStart, g.passTarget, pT);
    } else if (t < 0.85) {
      const sT = (t - 0.50) / 0.35;
      strikerPos = lerpPoint(g.passTarget, g.strikerFinish, sT);
    } else {
      strikerPos = g.strikerFinish;
    }

    if (strikerEl) {
      strikerEl.setAttribute("transform", "translate(" + strikerPos.x + "," + strikerPos.y + ")");
      const circle = strikerEl.querySelector("circle");
      if (circle) circle.setAttribute("fill", g.oppColor);
      const txt = strikerEl.querySelector("text");
      if (txt) {
        txt.setAttribute("fill", g.oppTextColor);
        txt.textContent = g.scorer.split(" ")[0];
      }
    }

    // 4. Leah Williamson / Defender
    let defPos = g.defenderStart;
    if (t < 0.20) {
      defPos = g.defenderStart;
    } else if (t < 0.50) {
      const pT = (t - 0.20) / 0.30;
      defPos = lerpPoint(g.defenderStart, g.defenderMid, pT * 0.85); // Defender is slower to react
    } else if (t < 0.85) {
      const sT = (t - 0.50) / 0.35;
      defPos = lerpPoint(g.defenderMid, g.defenderEnd, sT);
    } else {
      defPos = g.defenderEnd;
    }

    if (defenderEl) {
      defenderEl.setAttribute("transform", "translate(" + defPos.x + "," + defPos.y + ")");
    }

    // 5. Goalkeeper
    let gkPos = g.gkStart;
    if (t > 0.60) {
      const gkT = Math.min(1.0, (t - 0.60) / 0.35);
      gkPos = lerpPoint(g.gkStart, g.gkEnd, gkT);
    }
    if (gkEl) {
      gkEl.setAttribute("transform", "translate(" + gkPos.x + "," + gkPos.y + ")");
    }

    // 6. Goal Banner
    if (goalBannerEl) {
      goalBannerEl.style.display = t > 0.90 ? "block" : "none";
    }
  }


  // =========================================================================
  // 2. VICTORIA PELOVA INVOLVEMENT COLLAPSE CHART
  // =========================================================================
  const PELOVA_DATA = [
    {
      round: "MW3",
      match: "פאלאס (חוץ)",
      score: "0–7 ניצחון",
      type: "open",
      minutes: 90,
      touches: 73,
      passes: 47,
      chances: 4,
      rating: 9.44,
      desc: "משחק פתוח לחלוטין מול קו הגנה מפורק. פאלובה שולטת לחלוטין בקצב ומחלקת כדורים בחופשיות."
    },
    {
      round: "MW4",
      match: "וילה (בית)",
      score: "0–4 ניצחון",
      type: "open",
      minutes: 90,
      touches: 86,
      passes: 58,
      chances: 2,
      rating: 9.25,
      desc: "שיא עונתי של נגיעות ומסירות מדויקות. ספרס שולטת ב-65% בכדור ופאלובה מנהלת את כל מרכז השדה."
    },
    {
      round: "MW8",
      match: "ברמינגהאם (חוץ)",
      score: "1–4 ניצחון",
      type: "open",
      minutes: 90,
      touches: 74,
      passes: 46,
      chances: 5,
      rating: 9.08,
      desc: "5 מצבים שיוצרו (שיא משחק) מול יריבה שמתגוננת עמוק ומאפשרת לפאלובה לקבל כדור עם הפנים לשער."
    },
    {
      round: "MW7",
      match: "ארסנל (בית)",
      score: "2–1 הפסד",
      type: "tight",
      minutes: 90,
      touches: 54,
      passes: 18,
      chances: 2,
      rating: 8.05,
      desc: "הדרבי של צפון לונדון: ארסנל מפעילה לחץ אגרסיבי, פאלובה מוגבלת ל-18 מסירות בלבד ב-90 דקות."
    },
    {
      round: "MW6",
      match: "צ'לסי (חוץ)",
      score: "6–2 תבוסה",
      type: "tight",
      minutes: 71,
      touches: 47,
      passes: 22,
      chances: 3,
      rating: 7.28,
      desc: "צ'לסי חונקת את הקישור. פאלובה מאבדת 3 כדורים מסוכנים ומוחלפת בדקה ה-71."
    },
    {
      round: "MW9",
      match: "ברייטון (בית)",
      score: "1–2 ניצחון",
      type: "tight",
      minutes: 90,
      touches: 42,
      passes: 22,
      chances: 0,
      rating: 6.91,
      desc: "נורת אזהרה בוהקת: 90 דקות מלאות, ופאלובה עם 42 נגיעות בלבד ו-0 מצבים שייצרה! ברייטון ניטרלה אותה."
    },
    {
      round: "MW5",
      match: "ליונסס (בית)",
      score: "6–1 תבוסה",
      type: "tight",
      minutes: 68,
      touches: 30,
      passes: 8,
      chances: 1,
      rating: 6.84,
      desc: "קריסה מוחלטת: 30 נגיעות ב-68 דקות, 8 מסירות בלבד ו-5 איבודי כדור תחת מכבש הלחץ של לס\"ל."
    }
  ];

  function renderPelovaChart() {
    const container = document.getElementById("pelova-chart-container");
    if (!container) return;

    const maxTouches = 100;
    let html = "";

    PELOVA_DATA.forEach((item, idx) => {
      const isOpen = item.type === "open";
      const barColor = isOpen 
        ? "bg-gradient-to-r from-emerald-500 to-teal-400" 
        : (item.round === "MW9" ? "bg-gradient-to-r from-red-600 to-rose-500 ring-2 ring-red-400" : "bg-gradient-to-r from-rose-500 to-red-400");
      const badgeCls = isOpen 
        ? "bg-emerald-100 text-emerald-800 dark:bg-emerald-950/60 dark:text-emerald-300 border-emerald-300 dark:border-emerald-800" 
        : "bg-rose-100 text-rose-800 dark:bg-rose-950/60 dark:text-rose-300 border-rose-300 dark:border-rose-800";
      const widthPct = (item.touches / maxTouches) * 100;

      html += '<div class="space-y-1.5 p-3 rounded-lg bg-white dark:bg-[#181820] border border-neutral-200 dark:border-neutral-800/80 hover:border-primary-400 dark:hover:border-primary-600 transition-colors shadow-2xs">';
      html += '  <div class="flex items-center justify-between text-xs sm:text-sm font-sans flex-wrap gap-2">';
      html += '    <div class="flex items-center gap-2">';
      html += '      <span class="font-mono font-bold text-neutral-900 dark:text-white px-2 py-0.5 rounded bg-neutral-100 dark:bg-[#252530] border border-neutral-200 dark:border-neutral-700">' + item.round + '</span>';
      html += '      <span class="font-bold text-neutral-800 dark:text-neutral-100">' + item.match + '</span>';
      html += '      <span class="text-xs text-neutral-500 font-mono">(' + item.minutes + " דק')</span>";
      html += '    </div>';
      html += '    <div class="flex items-center gap-3 font-mono text-xs">';
      html += '      <span class="px-2 py-0.5 rounded text-[11px] font-bold border ' + badgeCls + '">' + (isOpen ? "משחק פתוח / נחותה" : "לחץ אינטנסיבי / צמרת") + '</span>';
      html += '      <span class="font-bold text-neutral-900 dark:text-white">' + item.touches + ' נגיעות</span>';
      html += '      <span class="text-neutral-500 dark:text-neutral-400">(' + item.chances + ' מצבים)</span>';
      html += '    </div>';
      html += '  </div>';

      // Bar
      html += '  <div class="w-full bg-neutral-100 dark:bg-[#22222c] h-3.5 rounded-full overflow-hidden flex items-center relative">';
      html += '    <div class="h-full rounded-full transition-all duration-700 ' + barColor + '" style="width: ' + widthPct + '%"></div>';
      html += '    <span class="absolute left-3 text-[10px] font-mono font-bold text-white drop-shadow-xs">' + item.touches + '</span>';
      html += '  </div>';

      // Explanation
      html += '  <p class="text-[11px] sm:text-xs text-neutral-600 dark:text-neutral-400 font-sans leading-relaxed pt-0.5">' + item.desc + '</p>';
      html += '</div>';
    });

    container.innerHTML = html;
  }


  // =========================================================================
  // 3. CHELSEA CHANCE CREATORS TABLE
  // =========================================================================
  const CHELSEA_CREATORS = [
    { name: "ארין קאת'ברט", raw: "Erin Cuthbert", pos: "קשרית מרכזית (8/10)", mins: 293, chances: 17, p90: 5.22, assists: 0, highlight: true },
    { name: "קייטי מקייב", raw: "Katie McCabe", pos: "כנף שמאל / מגינה", mins: 462, chances: 21, p90: 4.09, assists: 2, highlight: true },
    { name: "אליסה תומפסון", raw: "Alyssa Thompson", pos: "כנף ימין", mins: 390, chances: 12, p90: 2.77, assists: 3, highlight: false },
    { name: "סנדי בולטימור", raw: "Sandy Baltimore", pos: "כנף שמאל", mins: 256, chances: 6, p90: 2.11, assists: 1, highlight: false },
    { name: "קיירה וולש", raw: "Keira Walsh", pos: "עושת משחק (6/8)", mins: 511, chances: 12, p90: 2.11, assists: 3, highlight: true, note: "מקום 2 בליגה בבישולים" },
    { name: "ויקה קאפטיין", raw: "Wieke Kaptein", pos: "קשרית מרכזית", mins: 420, chances: 9, p90: 1.93, assists: 1, highlight: false },
    { name: "אלי קארפנטר", raw: "Ellie Carpenter", pos: "מגינה ימנית", mins: 629, chances: 12, p90: 1.72, assists: 1, highlight: false },
    { name: "אגי ביבר-ג'ונס", raw: "Agnes Beever-Jones", pos: "חלוצה מחליפה", mins: 213, chances: 4, p90: 1.69, assists: 0, highlight: false },
    { name: "מלווין מאלארד", raw: "Melvine Malard", pos: "חלוצה פותחת (9)", mins: 424, chances: 6, p90: 1.27, assists: 0, highlight: false },
    { name: "אלכסיה פוטר", raw: "Alexia Potter", pos: "קשרית אחורית (6)", mins: 331, chances: 3, p90: 0.82, assists: 0, highlight: true, note: "העוגן שמאפשר לוולש לעלות" },
    { name: "לורן ג'יימס", raw: "Lauren James", pos: "עושת משחק (פצועה)", mins: 174, chances: 2, p90: 1.03, assists: 0, highlight: false, note: "נעדרת מאז מחזור 4" }
  ];

  function renderChelseaTable() {
    const tbody = document.getElementById("che-creators-tbody");
    if (!tbody) return;

    let html = "";
    CHELSEA_CREATORS.forEach((p, idx) => {
      const isTop = idx < 2;
      const rowBg = p.highlight 
        ? "bg-primary-50/50 dark:bg-primary-950/20 font-medium" 
        : (idx % 2 === 0 ? "bg-white dark:bg-[#121217]" : "bg-neutral-50/60 dark:bg-[#16161c]");

      html += '<tr class="border-b border-neutral-100 dark:border-neutral-800/80 transition-colors hover:bg-neutral-100/70 dark:hover:bg-[#1e1e26] ' + rowBg + '">';
      html += '  <td class="p-3 text-right font-sans font-bold text-neutral-900 dark:text-white flex items-center gap-2">';
      if (isTop) html += '    <span class="text-amber-500 text-xs">⭐</span>';
      html += '    <span>' + p.name + '</span>';
      if (p.note) html += '    <span class="text-[10px] font-mono px-1.5 py-0.5 rounded bg-neutral-200/80 dark:bg-neutral-800 text-neutral-600 dark:text-neutral-400 font-normal">' + p.note + '</span>';
      html += '  </td>';
      html += '  <td class="p-3 text-right text-xs text-neutral-600 dark:text-neutral-400 font-sans">' + p.pos + '</td>';
      html += '  <td class="p-3 text-center font-mono text-neutral-700 dark:text-neutral-300">' + p.mins + " דק'</td>";
      html += '  <td class="p-3 text-center font-mono font-bold text-neutral-900 dark:text-white">' + p.chances + '</td>';
      html += '  <td class="p-3 text-center font-mono font-bold ' + (p.p90 >= 4.0 ? 'text-emerald-600 dark:text-emerald-400 text-sm' : 'text-neutral-800 dark:text-neutral-200') + '">' + p.p90.toFixed(2) + '</td>';
      html += '  <td class="p-3 text-center font-mono text-neutral-700 dark:text-neutral-300">' + p.assists + '</td>';
      html += '</tr>';
    });

    tbody.innerHTML = html;
  }


  // =========================================================================
  // INITIALIZATION ON DOM READY
  // =========================================================================
  function initWidgets() {
    renderArsenalTabs();
    updateGoalDetails();
    drawPitchFrame(0);
    renderPelovaChart();
    renderChelseaTable();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initWidgets);
  } else {
    initWidgets();
  }

})();

