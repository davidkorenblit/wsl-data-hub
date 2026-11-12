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
      round: "מחזור 9 · אנפילד",
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
  // 2. VICTORIA PELOVA INVOLVEMENT COLLAPSE CHART (CARTESIAN COORDINATE GRAPH)
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
      desc: "משחק פתוח לחלוטין מול קו הגנה מפורק. פאלובה שולטת לחלוטין בקצב ומחלקת כדורים בחופשיות ללא כל לחץ על מובילת הכדור."
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
      desc: "שיא עונתי של נגיעות (86) ומסירות מדויקות (58). ספרס שולטת ב-65% בכדור ופאלובה מנהלת את כל מרכז השדה מעמדה קדמית."
    },
    {
      round: "MW5",
      match: "לס\"ל (בית)",
      score: "6–1 תבוסה",
      type: "tight",
      minutes: 68,
      touches: 30,
      passes: 8,
      chances: 1,
      rating: 6.84,
      desc: "קריסה מוחלטת תחת לחץ: 30 נגיעות ב-68 דקות, 8 מסירות בלבד ו-5 איבודי כדור תחת מכבש הלחץ האגרסיבי של לונדון סיטי ליונסס."
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
      desc: "צ'לסי חונקת את הקישור וסוגרת נתיבי מסירה. פאלובה מאבדת 3 כדורים מסוכנים בחצי שלה ומוחלפת בדקה ה-71."
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
      desc: "הדרבי של צפון לונדון: ארסנל לוחצת גבוה ואגרסיבי. למרות בישול קרן לטנדברג, פאלובה מוגבלת ל-18 מסירות בלבד ב-90 דקות שלמות."
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
      desc: "שיא יצירה עונתי של 5 מצבים שהסתיימו בבעיטה מול יריבה מתגוננת עמוק, שמאפשרת לפאלובה לקבל כדור חופשי עם הפנים לשער."
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
      desc: "נורת אזהרה בוהקת: 90 דקות מלאות על הדשא, ופאלובה עם 42 נגיעות בלבד ו-0 מצבים שייצרה! ברייטון חנקה אותה וספרס ניצחה בשיניים."
    }
  ];

  let activePelovaMatchIdx = 6; // default to MW9 (Brighton)

  window.selectPelovaMatch = function(idx) {
    activePelovaMatchIdx = idx;
    renderPelovaChart();
  };

  function computeMonotoneSpline(pts) {
    const n = pts.length;
    if (n < 2) return '';
    const x = pts.map(p => p.x);
    const y = pts.map(p => p.y);
    const dx = [], dy = [], m = [];
    for (let i = 0; i < n - 1; i++) {
      dx.push(x[i+1] - x[i]);
      dy.push(y[i+1] - y[i]);
      m.push(dy[i] / dx[i]);
    }
    const tangents = [m[0]];
    for (let i = 1; i < n - 1; i++) {
      if (m[i-1] * m[i] <= 0) {
        tangents.push(0);
      } else {
        tangents.push((dx[i-1] * m[i] + dx[i] * m[i-1]) / (dx[i-1] + dx[i]));
      }
    }
    tangents.push(m[n - 2]);

    for (let i = 0; i < n - 1; i++) {
      if (dy[i] === 0) {
        tangents[i] = 0;
        tangents[i+1] = 0;
      } else {
        const alpha = tangents[i] / m[i];
        const beta = tangents[i+1] / m[i];
        const h = Math.hypot(alpha, beta);
        if (h > 3) {
          tangents[i] = (3 / h) * alpha * m[i];
          tangents[i+1] = (3 / h) * beta * m[i];
        }
      }
    }

    let curveD = 'M ' + x[0].toFixed(1) + ' ' + y[0].toFixed(1);
    for (let i = 0; i < n - 1; i++) {
      const cp1x = x[i] + dx[i] / 3;
      const cp1y = y[i] + tangents[i] * dx[i] / 3;
      const cp2x = x[i+1] - dx[i] / 3;
      const cp2y = y[i+1] - tangents[i+1] * dx[i] / 3;
      curveD += ' C ' + cp1x.toFixed(1) + ',' + cp1y.toFixed(1) + ' ' + cp2x.toFixed(1) + ',' + cp2y.toFixed(1) + ' ' + x[i+1].toFixed(1) + ',' + y[i+1].toFixed(1);
    }
    return curveD;
  }

  function renderPelovaChart() {
    const container = document.getElementById("pelova-chart-container");
    if (!container) return;

    const width = 800;
    const height = 370;
    const padLeft = 70;
    const padRight = 45;
    const padTop = 50;
    const padBottom = 65;
    const plotW = width - padLeft - padRight;
    const plotH = height - padTop - padBottom;

    const pts = PELOVA_DATA.map((d, i) => ({
      x: padLeft + i * (plotW / (PELOVA_DATA.length - 1)),
      y: padTop + (100 - d.touches) * (plotH / 100),
      data: d,
      idx: i
    }));

    const curveD = computeMonotoneSpline(pts);
    const baselineY = padTop + plotH;
    const areaD = curveD + ' L ' + pts[pts.length - 1].x.toFixed(1) + ' ' + baselineY.toFixed(1) + ' L ' + pts[0].x.toFixed(1) + ' ' + baselineY.toFixed(1) + ' Z';
    const benchY = padTop + (100 - 50) * (plotH / 100);

    let html = '';

    // Summary comparison cards
    html += '<div class="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-2 font-sans">';
    html += '  <div class="p-3 rounded-lg bg-emerald-50/70 dark:bg-emerald-950/20 border border-emerald-200 dark:border-emerald-800/60 flex items-center justify-between">';
    html += '    <div>';
    html += '      <div class="text-[11px] font-mono text-emerald-800 dark:text-emerald-300 font-bold">משחקים פתוחים (פאלאס, וילה, ברמינגהאם)</div>';
    html += '      <div class="text-xs text-neutral-600 dark:text-neutral-400 mt-0.5">ספרס שולטת בקצב ללא לחץ</div>';
    html += '    </div>';
    html += '    <div class="text-left font-mono">';
    html += '      <div class="text-base font-bold text-emerald-600 dark:text-emerald-400">77.7 נגיעות</div>';
    html += '      <div class="text-[11px] text-emerald-700 dark:text-emerald-300">3.7 מצבים שיוצרו</div>';
    html += '    </div>';
    html += '  </div>';

    html += '  <div class="p-3 rounded-lg bg-rose-50/70 dark:bg-rose-950/20 border border-rose-200 dark:border-rose-800/60 flex items-center justify-between">';
    html += '    <div>';
    html += '      <div class="text-[11px] font-mono text-rose-800 dark:text-rose-300 font-bold">לחץ אינטנסיבי (לס"ל, צ\'לסי, ארסנל, ברייטון)</div>';
    html += '      <div class="text-xs text-neutral-600 dark:text-neutral-400 mt-0.5">צניחה של 45% בנגיעות ו-59% ביצירה</div>';
    html += '    </div>';
    html += '    <div class="text-left font-mono">';
    html += '      <div class="text-base font-bold text-rose-600 dark:text-rose-400">43.2 נגיעות</div>';
    html += '      <div class="text-[11px] text-rose-700 dark:text-rose-300">1.5 מצבים שיוצרו</div>';
    html += '    </div>';
    html += '  </div>';
    html += '</div>';

    // SVG Cartesian Graph Container
    html += '<div class="relative w-full overflow-hidden rounded-xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-[#16161f] shadow-inner p-2 sm:p-4">';
    html += '  <svg viewBox="0 0 800 370" class="w-full h-auto block select-none font-sans" xmlns="http://www.w3.org/2000/svg">';
    html += '    <defs>';
    html += '      <linearGradient id="pelova-area-grad" x1="0" y1="0" x2="0" y2="1">';
    html += '        <stop offset="0%" stop-color="#6366F1" stop-opacity="0.30" />';
    html += '        <stop offset="70%" stop-color="#6366F1" stop-opacity="0.06" />';
    html += '        <stop offset="100%" stop-color="#6366F1" stop-opacity="0.0" />';
    html += '      </linearGradient>';
    html += '      <marker id="axis-arrow-y" viewBox="0 0 10 10" refX="5" refY="3" markerWidth="6" markerHeight="6" orient="auto">';
    html += '        <path d="M 1 9 L 5 1 L 9 9 z" fill="#64748B" />';
    html += '      </marker>';
    html += '      <marker id="axis-arrow-x" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto">';
    html += '        <path d="M 1 1 L 9 5 L 1 9 z" fill="#64748B" />';
    html += '      </marker>';
    html += '      <filter id="pelova-glow" x="-30%" y="-30%" width="160%" height="160%">';
    html += '        <feDropShadow dx="0" dy="1.5" stdDeviation="2.5" flood-opacity="0.3" />';
    html += '      </filter>';
    html += '    </defs>';

    // Zone Shading
    html += '    <!-- Zone 1: Control & Dominance (>50) -->';
    html += '    <rect x="' + padLeft + '" y="' + padTop + '" width="' + plotW + '" height="' + (benchY - padTop) + '" fill="#10B981" fill-opacity="0.05" rx="3" />';
    html += '    <text x="' + (padLeft + plotW - 8) + '" y="' + (padTop + 18) + '" text-anchor="end" font-size="10.5" font-weight="bold" fill="#10B981" opacity="0.85">▲ אזור שליטה ודומיננטיות (משחקים פתוחים · 50–100 נגיעות)</text>';

    html += '    <!-- Zone 2: Suffocation & Drop (<50) -->';
    html += '    <rect x="' + padLeft + '" y="' + benchY + '" width="' + plotW + '" height="' + (baselineY - benchY) + '" fill="#F43F5E" fill-opacity="0.05" rx="3" />';
    html += '    <text x="' + (padLeft + plotW - 8) + '" y="' + (baselineY - 12) + '" text-anchor="end" font-size="10.5" font-weight="bold" fill="#F43F5E" opacity="0.85">▼ אזור חנק וצניחה תחת לחץ (קבוצות אגרסיביות · 0–50 נגיעות)</text>';

    // Horizontal Grid Lines at 100, 80, 60, 40, 20
    [100, 80, 60, 40, 20].forEach(v => {
      const gy = padTop + (100 - v) * (plotH / 100);
      html += '    <line x1="' + padLeft + '" y1="' + gy + '" x2="' + (padLeft + plotW) + '" y2="' + gy + '" stroke="rgba(148, 163, 184, 0.22)" stroke-dasharray="3,3" stroke-width="1" />';
      html += '    <text x="' + (padLeft - 10) + '" y="' + (gy + 4) + '" text-anchor="end" font-family="monospace" font-size="11" font-weight="600" fill="#64748B">' + v + '</text>';
    });

    // Benchmark Line at 50
    html += '    <!-- Benchmark Line 50 Touches -->';
    html += '    <line x1="' + padLeft + '" y1="' + benchY + '" x2="' + (padLeft + plotW) + '" y2="' + benchY + '" stroke="#F59E0B" stroke-width="1.8" stroke-dasharray="6,4" />';
    html += '    <g transform="translate(' + (padLeft + 6) + ', ' + (benchY - 12) + ')">';
    html += '      <rect width="162" height="23" rx="5" fill="#FEF3C7" stroke="#F59E0B" stroke-width="1" />';
    html += '      <text x="81" y="15" text-anchor="middle" font-size="11" font-weight="bold" fill="#B45309">סף שליטה ומעורבות (50 נגיעות)</text>';
    html += '    </g>';

    // Axes
    html += '    <!-- Cartesian Axes -->';
    html += '    <line x1="' + padLeft + '" y1="' + (baselineY + 6) + '" x2="' + padLeft + '" y2="' + (padTop - 25) + '" stroke="#64748B" stroke-width="2" marker-end="url(#axis-arrow-y)" />';
    html += '    <text x="' + (padLeft + 6) + '" y="' + (padTop - 20) + '" text-anchor="start" font-size="11" font-weight="bold" fill="#64748B">נגיעות בכדור (ציר Y)</text>';

    html += '    <line x1="' + (padLeft - 5) + '" y1="' + baselineY + '" x2="' + (padLeft + plotW + 24) + '" y2="' + baselineY + '" stroke="#64748B" stroke-width="2" marker-end="url(#axis-arrow-x)" />';
    html += '    <text x="' + (padLeft + plotW + 20) + '" y="' + (baselineY + 22) + '" text-anchor="end" font-size="11" font-weight="bold" fill="#64748B">רצף מחזורים (ציר X) →</text>';

    // Curve and Area
    html += '    <!-- Continuous Smooth Curve -->';
    html += '    <path d="' + areaD + '" fill="url(#pelova-area-grad)" />';
    html += '    <path d="' + curveD + '" fill="none" stroke="#6366F1" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" />';

    // Points & Labels
    pts.forEach((p, i) => {
      const isSel = (i === activePelovaMatchIdx);
      const isOpen = (p.data.type === "open");
      const color = isOpen ? "#10B981" : (p.data.round === "MW9" ? "#DC2626" : "#F43F5E");
      const textColor = isOpen ? "#059669" : (p.data.round === "MW9" ? "#991B1B" : "#E11D48");

      // X Axis ticks & texts
      html += '    <!-- Point ' + p.data.round + ' -->';
      html += '    <line x1="' + p.x.toFixed(1) + '" y1="' + baselineY + '" x2="' + p.x.toFixed(1) + '" y2="' + (baselineY + 6) + '" stroke="#64748B" stroke-width="1.5" />';
      html += '    <text x="' + p.x.toFixed(1) + '" y="' + (baselineY + 20) + '" text-anchor="middle" font-family="monospace" font-weight="bold" font-size="12" fill="' + (isSel ? "#6366F1" : "#0F172A") + '">' + p.data.round + '</text>';
      html += '    <text x="' + p.x.toFixed(1) + '" y="' + (baselineY + 34) + '" text-anchor="middle" font-size="10.5" fill="#475569">' + p.data.match.split(" ")[0] + '</text>';
      html += '    <text x="' + p.x.toFixed(1) + '" y="' + (baselineY + 47) + '" text-anchor="middle" font-family="monospace" font-size="9.5" fill="#94A3B8">' + p.data.score.split(" ")[0] + '</text>';

      // Point Halo and Core
      html += '    <circle cx="' + p.x.toFixed(1) + '" cy="' + p.y.toFixed(1) + '" r="' + (isSel ? 11 : 8.5) + '" fill="' + color + '" fill-opacity="0.25" stroke="' + color + '" stroke-width="' + (isSel ? 2.5 : 1.5) + '" filter="url(#pelova-glow)" />';
      html += '    <circle cx="' + p.x.toFixed(1) + '" cy="' + p.y.toFixed(1) + '" r="' + (isSel ? 5.5 : 4) + '" fill="' + color + '" stroke="#FFFFFF" stroke-width="1.8" />';

      // Point direct labels
      let badgeX = p.x;
      let badgeY = p.y - 28;
      let badgeW = 76;
      let badgeH = 28;
      let titleText = p.data.touches + " נגיעות";
      let subText = p.data.chances + (p.data.chances === 1 ? " מצב" : " מצבים");

      if (p.data.round === "MW3") {
        badgeX = p.x + 18;
        badgeY = p.y - 34;
      } else if (p.data.round === "MW4") {
        badgeW = 86;
        badgeH = 30;
        badgeY = p.y - 36;
        titleText = p.data.touches + " · שיא ⭐";
      } else if (p.data.round === "MW5") {
        badgeW = 88;
        badgeH = 30;
        badgeY = p.y + 12;
        titleText = p.data.touches + " · שפל ⚠️";
      } else if (p.data.round === "MW6") {
        badgeY = p.y + 12;
      } else if (p.data.round === "MW7") {
        badgeY = p.y - 34;
      } else if (p.data.round === "MW8") {
        badgeW = 90;
        badgeH = 30;
        badgeY = p.y - 36;
        titleText = p.data.touches + " · יצירה ⭐";
      } else if (p.data.round === "MW9") {
        badgeX = p.x - 38;
        badgeY = p.y + 10;
        badgeW = 98;
        badgeH = 32;
        titleText = p.data.touches + " · צניחה ⚠️";
        subText = "0 מצבים ב-90'!";
      }

      html += '    <g transform="translate(' + (badgeX - badgeW / 2).toFixed(1) + ', ' + badgeY.toFixed(1) + ')" style="cursor: pointer;" onclick="window.selectPelovaMatch(' + i + ')">';
      html += '      <rect width="' + badgeW + '" height="' + badgeH + '" rx="5" fill="' + color + '" fill-opacity="0.14" stroke="' + color + '" stroke-width="' + (isSel ? 1.8 : 1) + '" />';
      html += '      <text x="' + (badgeW / 2) + '" y="13" text-anchor="middle" font-family="monospace" font-weight="bold" font-size="11" fill="' + textColor + '">' + titleText + '</text>';
      html += '      <text x="' + (badgeW / 2) + '" y="' + (badgeH - 4) + '" text-anchor="middle" font-size="9.5" font-weight="' + (p.data.round === "MW9" ? "bold" : "normal") + '" fill="' + textColor + '">' + subText + '</text>';
      html += '    </g>';

      // Click hitbox
      html += '    <circle cx="' + p.x.toFixed(1) + '" cy="' + p.y.toFixed(1) + '" r="' + 22 + '" fill="transparent" style="cursor: pointer;" onclick="window.selectPelovaMatch(' + i + ')">';
      html += '      <title>' + p.data.round + ': ' + p.data.match + ' - ' + p.data.touches + ' נגיעות, ' + p.data.chances + ' מצבים</title>';
      html += '    </circle>';
    });

    html += '  </svg>';
    html += '</div>';

    // Interactive Round Switcher Buttons
    html += '<div class="pt-2">';
    html += '  <div class="text-xs font-sans text-neutral-500 dark:text-neutral-400 mb-2 font-medium">בחר מחזור לבחינת הנתונים והניתוח הטקטי:</div>';
    html += '  <div class="flex items-center gap-1.5 overflow-x-auto pb-1 scrollbar-thin">';
    PELOVA_DATA.forEach((item, idx) => {
      const isSel = (idx === activePelovaMatchIdx);
      const isOpen = (item.type === "open");
      const btnBorder = isSel 
        ? "border-primary-600 bg-primary-50 dark:bg-primary-950/40 text-primary-700 dark:text-primary-300 font-bold shadow-xs" 
        : "border-neutral-200 dark:border-neutral-800 bg-white dark:bg-[#181820] text-neutral-700 dark:text-neutral-300 hover:border-neutral-300 dark:hover:border-neutral-700";
      const dotColor = isOpen ? "bg-emerald-500" : (item.round === "MW9" ? "bg-red-600" : "bg-rose-500");

      html += '    <button type="button" onclick="window.selectPelovaMatch(' + idx + ')" class="px-2.5 py-1.5 rounded-lg border text-xs font-mono transition-all flex items-center gap-1.5 whitespace-nowrap ' + btnBorder + '">';
      html += '      <span class="w-2 h-2 rounded-full ' + dotColor + '"></span>';
      html += '      <span>' + item.round + '</span>';
      html += '      <span class="text-[11px] font-sans opacity-80">(' + item.touches + ' נג\')</span>';
      html += '    </button>';
    });
    html += '  </div>';
    html += '</div>';

    // Active Match Detail Card
    const activeItem = PELOVA_DATA[activePelovaMatchIdx];
    const isOpen = activeItem.type === "open";
    const badgeCls = isOpen 
      ? "bg-emerald-100 text-emerald-800 dark:bg-emerald-950/60 dark:text-emerald-300 border-emerald-300 dark:border-emerald-800" 
      : "bg-rose-100 text-rose-800 dark:bg-rose-950/60 dark:text-rose-300 border-rose-300 dark:border-rose-800";

    html += '<div class="p-4 rounded-xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/70 dark:bg-[#181822] space-y-3 font-sans shadow-2xs">';
    html += '  <div class="flex items-center justify-between flex-wrap gap-2 border-b border-neutral-200/70 dark:border-neutral-800 pb-2.5">';
    html += '    <div class="flex items-center gap-2">';
    html += '      <span class="px-2 py-0.5 rounded font-mono font-bold text-xs bg-neutral-200/80 dark:bg-neutral-800 text-neutral-800 dark:text-neutral-200">' + activeItem.round + '</span>';
    html += '      <span class="font-bold text-neutral-900 dark:text-white text-sm sm:text-base">' + activeItem.match + ' (' + activeItem.score + ')</span>';
    html += '    </div>';
    html += '    <div class="flex items-center gap-2">';
    html += '      <span class="px-2 py-0.5 rounded text-[11px] font-bold border ' + badgeCls + '">' + (isOpen ? "משחק פתוח / נחותה" : "לחץ אינטנסיבי / יריבה אגרסיבית") + '</span>';
    html += '      <span class="text-xs font-mono font-bold px-2 py-0.5 rounded bg-primary-100 dark:bg-primary-950/60 text-primary-800 dark:text-primary-300">ציון ' + activeItem.rating + '</span>';
    html += '    </div>';
    html += '  </div>';

    // 4 Stats Grid
    html += '  <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center font-mono">';
    html += '    <div class="p-2 rounded-lg bg-white dark:bg-[#121218] border border-neutral-200/80 dark:border-neutral-800">';
    html += '      <div class="text-[10px] text-neutral-500 uppercase">נגיעות בכדור</div>';
    html += '      <div class="text-base sm:text-lg font-bold ' + (activeItem.touches >= 50 ? 'text-emerald-600 dark:text-emerald-400' : 'text-rose-600 dark:text-rose-400') + '">' + activeItem.touches + '</div>';
    html += '    </div>';
    html += '    <div class="p-2 rounded-lg bg-white dark:bg-[#121218] border border-neutral-200/80 dark:border-neutral-800">';
    html += '      <div class="text-[10px] text-neutral-500 uppercase">מצבים שיוצרו</div>';
    html += '      <div class="text-base sm:text-lg font-bold ' + (activeItem.chances > 0 ? 'text-emerald-600 dark:text-emerald-400' : 'text-neutral-400') + '">' + activeItem.chances + '</div>';
    html += '    </div>';
    html += '    <div class="p-2 rounded-lg bg-white dark:bg-[#121218] border border-neutral-200/80 dark:border-neutral-800">';
    html += '      <div class="text-[10px] text-neutral-500 uppercase">מסירות מדויקות</div>';
    html += '      <div class="text-base sm:text-lg font-bold text-neutral-900 dark:text-white">' + activeItem.passes + '</div>';
    html += '    </div>';
    html += '    <div class="p-2 rounded-lg bg-white dark:bg-[#121218] border border-neutral-200/80 dark:border-neutral-800">';
    html += '      <div class="text-[10px] text-neutral-500 uppercase">דקות משחק</div>';
    html += '      <div class="text-base sm:text-lg font-bold text-neutral-900 dark:text-white">' + activeItem.minutes + '\'</div>';
    html += '    </div>';
    html += '  </div>';

    // Description
    html += '  <p class="text-xs sm:text-sm text-neutral-700 dark:text-neutral-300 leading-relaxed pt-1">' + activeItem.desc + '</p>';
    html += '</div>';

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

