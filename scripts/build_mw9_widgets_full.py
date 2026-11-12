import json

with open('assets/js/mw9-widgets.js', 'r', encoding='utf-8') as f:
    orig_code = f.read()

parts = orig_code.split("// 2. VICTORIA PELOVA INVOLVEMENT COLLAPSE CHART")
pelova_and_chelsea_section = "// 2. VICTORIA PELOVA INVOLVEMENT COLLAPSE CHART" + parts[1]

arsenal_section = """/**
 * MW9 Interactive Widgets:
 * 1. Arsenal Transition Goals Simulator & Broadcast Telestrator (לוח טקטי מונפש והדמיית פריימים מהשידור)
 * 2. Victoria Pelova Involvement Collapse Chart (גרף צניחת הנגיעות והיצירה)
 * 3. Chelsea Chance Creators Table (טבלת יוצרות המצבים והדילמה הטקטית)
 */

(function() {
  'use strict';

  // Base URL helper for GitHub Pages vs Localhost
  function getAssetUrl(path) {
    if (!path) return '';
    const base = window.location.pathname.startsWith('/wsl-data-hub') ? '/wsl-data-hub' : '';
    return base + path;
  }

  // =========================================================================
  // 1. ARSENAL TRANSITION GOALS: DATA WITH 2D PITCH & BROADCAST TELESTRATOR
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
      // 2D Pitch coordinates (0..800, 0..520) - Arsenal defends LEFT (x: 20..150)
      turnover: { x: 490, y: 190 },
      passTarget: { x: 230, y: 180 },
      strikerStart: { x: 420, y: 170 },
      strikerFinish: { x: 75, y: 245 },
      defenderStart: { x: 340, y: 210 },
      defenderMid: { x: 230, y: 215 },
      defenderEnd: { x: 110, y: 235 },
      gkStart: { x: 45, y: 260 },
      gkEnd: { x: 58, y: 252 },
      goalTarget: { x: 22, y: 250 },
      // Broadcast Telestrator Frames (1920x1080)
      telestrator: {
        buildupImg: "/assets/images/arsenal_conceded/mw9_olsson_buildup.jpg",
        sprintImg: "/assets/images/arsenal_conceded/mw9_olsson_sprint.jpg",
        buildup: {
          stepTitle: "שלב 1: שחרור המסירה באנפילד (קו הגנה גבוה)",
          desc: "ארסנל לוחצת גבוה באנפילד סביב קו האמצע. כדור ארוך מוקפץ מעל הראש של ליאה וויליאמסון לתוך 38 מטרים של דשא פנוי לחלוטין.",
          highLine: { x1: 1100, y1: 220, x2: 1240, y2: 740, label: "קו הגנה גבוה (40 מ' מהשער)" },
          defender: { x: 1240, y: 420, label: "ליאה וויליאמסון #6" },
          attacker: { x: 1380, y: 890, label: "אוליביה אולסון #9" },
          ball: { x: 995, y: 275 },
          passPath: "M 600 330 Q 995 230 1400 320",
          spacePoly: "1000,180 1820,180 1820,860 1150,760",
          spaceLabel: "38 מטרים שטח פנוי ללא חיפוי",
          spaceLabelPos: { x: 1460, y: 550 }
        },
        sprint: {
          stepTitle: "שלב 2: ספרינט 1v1 מול וויליאמסון וסיומת מול מיסה",
          desc: "אולסון רצה קדימה כשליאה וויליאמסון רודפת לאחור ואינה מצליחה לסגור. אולסון משתלטת, מגיעה לאחד על אחד מול מיסה רודריגז וכובשת.",
          defender: { x: 990, y: 420, label: "וויליאמסון (במרדף לאחור)" },
          attacker: { x: 1045, y: 405, label: "אולסון (ספרינט 1v1)" },
          gk: { x: 120, y: 390, label: "מיסה רודריגז #1" },
          runPath: "M 1045 405 L 250 400",
          spaceLabel: "1 על 1 נקי מול השוערת",
          spaceLabelPos: { x: 600, y: 370 }
        }
      }
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
      goalTarget: { x: 22, y: 280 },
      telestrator: {
        buildupImg: "/assets/images/arsenal_conceded/mw8_grant_buildup.jpg",
        sprintImg: "/assets/images/arsenal_conceded/mw8_grant_sprint.jpg",
        buildup: {
          stepTitle: "שלב 1: שחרור המסירה באמירויות (איבוד כדור בחצי של וילה)",
          desc: "ארסנל ישבה על הרחבה של וילה (28 בעיטות במשחק). איבוד כדור וכדור עומק ארוך של לין וילמס משגר את גרנט ב-42 מטר של שטח פנוי באגף.",
          highLine: { x1: 520, y1: 430, x2: 740, y2: 720, label: "קו הגנה מופקר" },
          defender: { x: 580, y: 440, label: "וויליאמסון וקאטלי" },
          attacker: { x: 630, y: 380, label: "צ'סיטי גרנט #11" },
          ball: { x: 570, y: 345 },
          passPath: "M 350 480 Q 570 300 850 380",
          spacePoly: "600,260 1450,260 1450,650 700,650",
          spaceLabel: "42 מטרים שטח פנוי באגף ימין",
          spaceLabelPos: { x: 1000, y: 450 }
        },
        sprint: {
          stepTitle: "שלב 2: כניסה לרחבה בפיגור בלתי ניתן לסגירה",
          desc: "גרנט משתלטת, מנצלת את הפיגור המובנה של הבלמיות, חודרת לפינה הימנית של הרחבה ומכניעה את מיסה.",
          defender: { x: 1050, y: 400, label: "בלמית בפיגור 6 מטרים" },
          attacker: { x: 980, y: 380, label: "צ'סיטי גרנט (חודרת לרחבה)" },
          gk: { x: 170, y: 420, label: "מיסה רודריגז #1" },
          runPath: "M 980 380 L 300 420",
          spaceLabel: "בעיטה חדה לפינה הרחוקה",
          spaceLabelPos: { x: 580, y: 400 }
        }
      }
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
      goalTarget: { x: 22, y: 242 },
      telestrator: {
        buildupImg: "/assets/images/arsenal_conceded/mw6_hurtre_buildup.jpg",
        sprintImg: "/assets/images/arsenal_conceded/mw6_hurtre_sprint.jpg",
        buildup: {
          stepTitle: "שלב 1: פריצת קו האמצע במתפרצת רשמית (Opta Fast Break)",
          desc: "שחרור מהיר אחרי כדור קרן של ארסנל. נב הרון שולחת את הרטרה, וויליאמסון נשארת אחרונה ומתחילה מרדף נואש מאחור.",
          highLine: { x1: 750, y1: 200, x2: 750, y2: 850, label: "קו אמצע המגרש" },
          defender: { x: 1150, y: 630, label: "וויליאמסון במרדף" },
          attacker: { x: 1280, y: 660, label: "לורי הרטרה #11" },
          ball: { x: 1320, y: 680 },
          passPath: "M 1520 700 L 1280 660",
          spacePoly: "200,300 1100,300 1100,750 200,750",
          spaceLabel: "Opta Fast Break · 45 מטר דשא פתוח",
          spaceLabelPos: { x: 650, y: 520 }
        },
        sprint: {
          stepTitle: "שלב 2: ספרינט בודד מול השער (מצב ענק של 0.59 xG)",
          desc: "הרטרה דוהר ללא מענה אל תוך הרחבה, כשוויליאמסון רודפת 4 מטרים מאחוריה. סיומת נקייה לרשת.",
          defender: { x: 960, y: 610, label: "וויליאמסון בפיגור" },
          attacker: { x: 1010, y: 590, label: "לורי הרטרה (0.59 xG)" },
          gk: { x: 150, y: 500, label: "מיסה רודריגז #1" },
          runPath: "M 1010 590 L 300 500",
          spaceLabel: "חדירה ללא הפרעה",
          spaceLabelPos: { x: 620, y: 530 }
        }
      }
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
      desc: "דקה 84, ארסנל בפיגור שולחת את כל הקבוצה קדימה לנסות להשוות ומפקירה את קו האמצע. פוג'ינו חוטפת ומשגרת את שאו באחד-על-אחד פיזי מול וויליאמסון. שאו גוברת על ליאה בכוח ובמהירות וסוגרת עניין.",
      turnover: { x: 460, y: 250 },
      passTarget: { x: 220, y: 255 },
      strikerStart: { x: 380, y: 255 },
      strikerFinish: { x: 80, y: 255 },
      defenderStart: { x: 320, y: 255 },
      defenderMid: { x: 220, y: 255 },
      defenderEnd: { x: 110, y: 255 },
      gkStart: { x: 45, y: 260 },
      gkEnd: { x: 60, y: 258 },
      goalTarget: { x: 22, y: 255 },
      telestrator: {
        buildupImg: "/assets/images/arsenal_conceded/mw5_shaw_buildup.jpg",
        sprintImg: "/assets/images/arsenal_conceded/mw5_shaw_sprint.jpg",
        buildup: {
          stepTitle: "שלב 1: איבוד כדור של ארסנל בחצי של סיטי ומסירת עומק של פוג'ינו",
          desc: "דקה 84 בג'ובי סטדיום, כל ארסנל בחצי של סיטי. פוג'ינו מובילה מעבר ומשגרת את באני שאו מעבר לקו ההגנה.",
          highLine: { x1: 700, y1: 200, x2: 700, y2: 800, label: "קו אמצע המגרש" },
          defender: { x: 380, y: 480, label: "ליאה וויליאמסון" },
          attacker: { x: 420, y: 460, label: "באני שאו #21" },
          passer: { x: 860, y: 425, label: "אאובה פוג'ינו (מבשלת)" },
          ball: { x: 860, y: 425 },
          passPath: "M 860 425 Q 600 400 430 460",
          spacePoly: "100,300 500,300 500,700 100,700",
          spaceLabel: "מסירת עומק חותכת במעבר",
          spaceLabelPos: { x: 300, y: 380 }
        },
        sprint: {
          stepTitle: "שלב 2: מאבק 1v1 פיזי מול וויליאמסון",
          desc: "שאו מנצלת את העוצמה והמהירות, גוברת על וויליאמסון ומגלגלת פנימה את שער הניצחון הסופי.",
          defender: { x: 640, y: 480, label: "וויליאמסון (במאבק)" },
          attacker: { x: 700, y: 460, label: "באני שאו (1v1 פיזי)" },
          gk: { x: 100, y: 450, label: "אנקה בורבה #1" },
          runPath: "M 700 460 L 250 450",
          spaceLabel: "סיומת אכזרית לרשת",
          spaceLabelPos: { x: 450, y: 430 }
        }
      }
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
      goalTarget: { x: 22, y: 268 },
      telestrator: {
        buildupImg: "/assets/images/arsenal_conceded/mw3_zigiotti_buildup.jpg",
        sprintImg: "/assets/images/arsenal_conceded/mw3_zigiotti_sprint.jpg",
        buildup: {
          stepTitle: "שלב 1: איבוד כדור בקישור וחדירה מול הגנה מפורקת",
          desc: "איבוד כדור כפול של ארסנל במרכז המגרש. זיגיוטי מקבלת את הכדור בדהירה מקו שני לתוך שטח חופשי לחלוטין מול שער חשוף.",
          attacker: { x: 1130, y: 330, label: "ג'וליה זיגיוטי #16" },
          ball: { x: 1185, y: 365 },
          spacePoly: "400,200 1200,200 1200,600 400,600",
          spaceLabel: "איבוד כדור במעבר · שטח פנוי מול שער חשוף",
          spaceLabelPos: { x: 750, y: 350 }
        },
        sprint: {
          stepTitle: "שלב 2: סיומת של 0.50 xG ללא הפרעה",
          desc: "זיגיוטי חודרת מול הרשת כשהבלמיות של ארסנל נותרות מאחור ואינן מצליחות להגיע לחסימה.",
          attacker: { x: 1060, y: 420, label: "זיגיוטי (0.50 xG)" },
          defender: { x: 870, y: 560, label: "הגנת ארסנל בפיגור" },
          gk: { x: 1480, y: 270, label: "מיסה רודריגז #1" },
          runPath: "M 1060 420 L 1400 300",
          spaceLabel: "סיומת מול שער ריק כמעט",
          spaceLabelPos: { x: 1250, y: 380 }
        }
      }
    }
  ];

  let currentGoalIdx = 0;
  let currentViewMode = "telestrator"; // "telestrator" (default) or "tactical"
  let currentTeleStep = "buildup"; // "buildup" or "sprint"
  let teleAutoplayTimer = null;
  let isTeleAutoplaying = false;

  // 2D Tactical pitch state
  let isPlaying = false;
  let progress = 0; // 0..1
  let animFrameId = null;
  let animSpeed = 1.0;
  let lastTimestamp = 0;
  const DURATION_MS = 6000;

  function lerp(a, b, t) {
    return a + (b - a) * t;
  }

  function lerpPoint(p1, p2, t) {
    return {
      x: lerp(p1.x, p2.x, t),
      y: lerp(p1.y, p2.y, t)
    };
  }

  // View Mode Controller (Telestrator vs Tactical 2D Pitch)
  window.setArsenalViewMode = function(mode) {
    currentViewMode = mode;
    const btnTele = document.getElementById("view-mode-telestrator");
    const btnTact = document.getElementById("view-mode-tactical");
    const containerTele = document.getElementById("ars-telestrator-container");
    const containerTact = document.getElementById("ars-tactical-container");
    const stepControls = document.getElementById("telestrator-step-controls");

    if (mode === "telestrator") {
      if (btnTele) btnTele.className = "px-3 py-1.5 rounded-md text-xs font-sans font-bold transition-all bg-primary-600 text-white shadow-xs flex items-center gap-1.5";
      if (btnTact) btnTact.className = "px-3 py-1.5 rounded-md text-xs font-sans text-neutral-400 hover:text-white transition-all flex items-center gap-1.5";
      if (containerTele) containerTele.style.display = "block";
      if (containerTact) containerTact.style.display = "none";
      if (stepControls) stepControls.style.display = "flex";
      pauseSimulation();
      renderTelestrator();
    } else {
      if (btnTele) btnTele.className = "px-3 py-1.5 rounded-md text-xs font-sans text-neutral-400 hover:text-white transition-all flex items-center gap-1.5";
      if (btnTact) btnTact.className = "px-3 py-1.5 rounded-md text-xs font-sans font-bold transition-all bg-primary-600 text-white shadow-xs flex items-center gap-1.5";
      if (containerTele) containerTele.style.display = "none";
      if (containerTact) containerTact.style.display = "block";
      if (stepControls) stepControls.style.display = "none";
      stopTelestratorAutoplay();
      drawPitchFrame(progress);
      if (!isPlaying) playSimulation();
    }
  };

  // Telestrator Step Controller (Buildup vs Sprint)
  window.setTelestratorStep = function(step) {
    currentTeleStep = step;
    const btnBuildup = document.getElementById("tele-step-buildup");
    const btnSprint = document.getElementById("tele-step-sprint");

    if (btnBuildup && btnSprint) {
      if (step === "buildup") {
        btnBuildup.className = "px-2.5 py-1 text-xs font-sans font-bold rounded bg-amber-500 text-black border border-amber-400";
        btnSprint.className = "px-2.5 py-1 text-xs font-sans rounded bg-neutral-800 text-neutral-300 hover:text-white border border-neutral-700";
      } else {
        btnBuildup.className = "px-2.5 py-1 text-xs font-sans rounded bg-neutral-800 text-neutral-300 hover:text-white border border-neutral-700";
        btnSprint.className = "px-2.5 py-1 text-xs font-sans font-bold rounded bg-amber-500 text-black border border-amber-400";
      }
    }
    renderTelestrator();
  };

  window.toggleTelestratorAutoplay = function() {
    if (isTeleAutoplaying) {
      stopTelestratorAutoplay();
    } else {
      startTelestratorAutoplay();
    }
  };

  function startTelestratorAutoplay() {
    isTeleAutoplaying = true;
    const btn = document.getElementById("tele-autoplay-btn");
    if (btn) btn.innerHTML = '<span>⏸</span><span>השהה מעבר</span>';
    runTeleAutoplayStep();
  }

  function stopTelestratorAutoplay() {
    isTeleAutoplaying = false;
    if (teleAutoplayTimer) clearTimeout(teleAutoplayTimer);
    const btn = document.getElementById("tele-autoplay-btn");
    if (btn) btn.innerHTML = '<span>▶</span><span>נגן שלבים</span>';
  }

  function runTeleAutoplayStep() {
    if (!isTeleAutoplaying) return;
    const nextStep = currentTeleStep === "buildup" ? "sprint" : "buildup";
    window.setTelestratorStep(nextStep);
    teleAutoplayTimer = setTimeout(runTeleAutoplayStep, 3500);
  }

  // RENDER TELESTRATOR (Image + SVG Overlay)
  function renderTelestrator() {
    const g = ARSENAL_GOALS[currentGoalIdx];
    if (!g || !g.telestrator) return;

    const imgEl = document.getElementById("tele-frame-img");
    const svgOverlay = document.getElementById("tele-svg-overlay");
    const descEl = document.getElementById("tele-step-desc");
    const titleEl = document.getElementById("tele-step-title");

    const tData = g.telestrator[currentTeleStep];
    const imgSrc = currentTeleStep === "buildup" ? g.telestrator.buildupImg : g.telestrator.sprintImg;

    if (imgEl) {
      imgEl.src = getAssetUrl(imgSrc);
    }
    if (titleEl && tData) {
      titleEl.innerText = tData.stepTitle || '';
    }
    if (descEl && tData) {
      descEl.innerText = tData.desc || '';
    }

    if (!svgOverlay || !tData) return;

    let svgHtml = `
      <defs>
        <marker id="tele-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#FBBF24" />
        </marker>
        <filter id="tele-glow" x="-20%" y="-20%" width="140%" height="140%">
          <feGaussianBlur stdDeviation="4" result="blur" />
          <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
      </defs>
    `;

    // 1. Shaded Space Polygon
    if (tData.spacePoly) {
      svgHtml += `<polygon points="${tData.spacePoly}" fill="rgba(239, 68, 68, 0.18)" stroke="#EF4444" stroke-width="2" stroke-dasharray="8 6" />`;
    }
    if (tData.spaceLabel && tData.spaceLabelPos) {
      svgHtml += `
        <g transform="translate(${tData.spaceLabelPos.x}, ${tData.spaceLabelPos.y})">
          <rect x="-180" y="-18" width="360" height="36" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#EF4444" stroke-width="2" />
          <text y="6" fill="#FCA5A5" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">
            ⚠️ ${tData.spaceLabel}
          </text>
        </g>
      `;
    }

    // 2. High Defensive Line
    if (tData.highLine) {
      const hl = tData.highLine;
      svgHtml += `
        <line x1="${hl.x1}" y1="${hl.y1}" x2="${hl.x2}" y2="${hl.y2}" stroke="#EF4444" stroke-width="4" stroke-dasharray="10 8" filter="url(#tele-glow)" />
        <g transform="translate(${(hl.x1 + hl.x2)/2}, ${Math.min(hl.y1, hl.y2) + 20})">
          <rect x="-140" y="-16" width="280" height="32" rx="6" fill="rgba(239, 68, 68, 0.95)" />
          <text y="5" fill="#FFFFFF" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">
            🛡️ ${hl.label}
          </text>
        </g>
      `;
    }

    // 3. Pass / Run Vector Path
    if (tData.passPath) {
      svgHtml += `<path d="${tData.passPath}" fill="none" stroke="#FBBF24" stroke-width="5" stroke-dasharray="10 6" marker-end="url(#tele-arrow)" filter="url(#tele-glow)" />`;
    }
    if (tData.runPath) {
      svgHtml += `<path d="${tData.runPath}" fill="none" stroke="#38BDF8" stroke-width="5" stroke-dasharray="10 6" marker-end="url(#tele-arrow)" filter="url(#tele-glow)" />`;
    }

    // 4. Defender Node
    if (tData.defender) {
      const d = tData.defender;
      svgHtml += `
        <g transform="translate(${d.x}, ${d.y})">
          <ellipse rx="28" ry="14" fill="none" stroke="#EF4444" stroke-width="4" filter="url(#tele-glow)" />
          <circle r="6" fill="#EF4444" />
          <rect x="-85" y="-45" width="170" height="28" rx="6" fill="rgba(15, 23, 42, 0.9)" stroke="#EF4444" stroke-width="1.5" />
          <text y="-26" fill="#FFFFFF" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">
            ${d.label}
          </text>
        </g>
      `;
    }

    // 5. Attacker Node
    if (tData.attacker) {
      const a = tData.attacker;
      svgHtml += `
        <g transform="translate(${a.x}, ${a.y})">
          <ellipse rx="28" ry="14" fill="none" stroke="#38BDF8" stroke-width="4" filter="url(#tele-glow)" />
          <circle r="6" fill="#38BDF8" />
          <rect x="-85" y="-45" width="170" height="28" rx="6" fill="rgba(15, 23, 42, 0.9)" stroke="#38BDF8" stroke-width="1.5" />
          <text y="-26" fill="#38BDF8" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">
            ⚡ ${a.label}
          </text>
        </g>
      `;
    }

    // 6. Goalkeeper / Passer Node
    if (tData.gk) {
      const gk = tData.gk;
      svgHtml += `
        <g transform="translate(${gk.x}, ${gk.y})">
          <circle r="8" fill="#EAB308" stroke="#000" stroke-width="2" />
          <rect x="-70" y="-35" width="140" height="24" rx="5" fill="rgba(15, 23, 42, 0.85)" stroke="#EAB308" stroke-width="1" />
          <text y="-18" fill="#EAB308" font-size="12" font-family="sans-serif" font-weight="bold" text-anchor="middle">
            🧤 ${gk.label}
          </text>
        </g>
      `;
    }
    if (tData.passer) {
      const p = tData.passer;
      svgHtml += `
        <g transform="translate(${p.x}, ${p.y})">
          <circle r="7" fill="#FBBF24" stroke="#000" stroke-width="1.5" />
          <rect x="-70" y="-35" width="140" height="24" rx="5" fill="rgba(15, 23, 42, 0.85)" stroke="#FBBF24" stroke-width="1" />
          <text y="-18" fill="#FBBF24" font-size="12" font-family="sans-serif" font-weight="bold" text-anchor="middle">
            🎯 ${p.label}
          </text>
        </g>
      `;
    }

    svgOverlay.innerHTML = svgHtml;
  }

  // Goal Selector Controller
  window.selectArsenalGoal = function(idx) {
    currentGoalIdx = idx;
    progress = 0;
    renderArsenalTabs();
    updateGoalDetails();
    if (currentViewMode === "telestrator") {
      renderTelestrator();
    } else {
      drawPitchFrame(0);
      if (!isPlaying) playSimulation();
    }
  };

  // 2D Tactical Pitch Controls
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

    const turnoverEl = document.getElementById("sim-elem-turnover");
    const passLineEl = document.getElementById("sim-elem-passline");
    const ballEl = document.getElementById("sim-elem-ball");
    const strikerEl = document.getElementById("sim-elem-striker");
    const defenderEl = document.getElementById("sim-elem-defender");
    const gkEl = document.getElementById("sim-elem-gk");
    const goalBannerEl = document.getElementById("sim-elem-goal-banner");

    if (turnoverEl) {
      turnoverEl.setAttribute("cx", g.turnover.x);
      turnoverEl.setAttribute("cy", g.turnover.y);
      turnoverEl.style.display = t > 0.05 ? "block" : "none";
      const pulseR = 8 + Math.sin(t * 20) * 3;
      turnoverEl.setAttribute("r", pulseR);
    }

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

    let defPos = g.defenderStart;
    if (t < 0.20) {
      defPos = g.defenderStart;
    } else if (t < 0.50) {
      const pT = (t - 0.20) / 0.30;
      defPos = lerpPoint(g.defenderStart, g.defenderMid, pT * 0.85);
    } else if (t < 0.85) {
      const sT = (t - 0.50) / 0.35;
      defPos = lerpPoint(g.defenderMid, g.defenderEnd, sT);
    } else {
      defPos = g.defenderEnd;
    }

    if (defenderEl) {
      defenderEl.setAttribute("transform", "translate(" + defPos.x + "," + defPos.y + ")");
    }

    let gkPos = g.gkStart;
    if (t > 0.60) {
      const gkT = Math.min(1.0, (t - 0.60) / 0.35);
      gkPos = lerpPoint(g.gkStart, g.gkEnd, gkT);
    }
    if (gkEl) {
      gkEl.setAttribute("transform", "translate(" + gkPos.x + "," + gkPos.y + ")");
    }

    if (goalBannerEl) {
      goalBannerEl.style.display = t > 0.90 ? "block" : "none";
    }
  }

"""

full_code = arsenal_section + "\n  " + pelova_and_chelsea_section

# Update initWidgets in full_code to include renderTelestrator
full_code = full_code.replace("drawPitchFrame(0);", "drawPitchFrame(0);\n    renderTelestrator();")

with open('assets/js/mw9-widgets.js', 'w', encoding='utf-8') as f:
    f.write(full_code)

print("Updated assets/js/mw9-widgets.js successfully!")
