---
layout: team
title: "Liverpool - מקבוצה לחוצה לקבוצה לוחצת"
team_name: "Liverpool"
team_slug: "liverpool"
team_meta: "WSL 2026/27 · מיקום: 6 (7 נק', הפרש שערים +3) · דוח מצב מעודכן: מחזור 5"
permalink: /teams/liverpool/
lang: he
alt_url: /en/teams/liverpool/
---

<div class="space-y-8 text-neutral-800 dark:text-neutral-200 leading-relaxed text-base sm:text-lg font-sans">

  <!-- Header Section -->
  <div class="border-b border-neutral-200 dark:border-neutral-800 pb-4">
    <div class="flex flex-wrap items-center gap-2 mb-2">
      <span class="text-xs font-mono font-bold px-2 py-0.5 rounded bg-red-100 dark:bg-red-950/50 text-red-800 dark:text-red-300 border border-red-200 dark:border-red-800">
        דוח מצב מעודכן
      </span>
      <span class="text-xs font-mono font-bold px-2 py-0.5 rounded bg-neutral-100 dark:bg-neutral-800 text-neutral-700 dark:text-neutral-300 border border-neutral-200 dark:border-neutral-700">
        מחזור 5 · אוקטובר 2026
      </span>
      <span class="text-xs font-mono text-neutral-400 dark:text-neutral-500">
        גארת' טיילור · עונה ראשונה מלאה
      </span>
    </div>
    <h1 class="text-2xl sm:text-3xl md:text-4xl font-extrabold tracking-tight text-neutral-900 dark:text-white">
      מקבוצה לחוצה לקבוצה לוחצת
    </h1>
    <p class="text-sm sm:text-base text-neutral-600 dark:text-neutral-400 font-sans mt-1">
      הזהות החדשה של ליברפול: רצפת בטון שמפרקת את מרבית הליגה מול תקרת זכוכית שנשברת מול קבוצות העילית.
    </p>
  </div>

  <!-- Module 1: Editorial Raw Text -->
  <div class="rounded-xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/70 dark:bg-neutral-900/50 p-5 sm:p-7 space-y-4 shadow-sm">
    <div class="flex items-center gap-2">
      <span class="w-2.5 h-2.5 rounded-full bg-red-600"></span>
      <h2 class="text-lg sm:text-xl font-bold text-neutral-900 dark:text-white font-sans">
        טור דעה וניתוח: הסלוגן שמגדיר את ליברפול
      </h2>
    </div>

    <div class="space-y-4 text-neutral-800 dark:text-neutral-200 font-sans text-base sm:text-lg leading-relaxed">
      <p>
        ליברפול לוחצת, וזה שינוי מרענן. אם תרצו למתג את זה הסלוגן יהיה <strong>"מקבוצה לחוצה לקבוצה לוחצת"</strong>.
      </p>

      <p>
        סגנון המשחק של טיילור מוכר. זאת לא העונה הראשונה שלו בליגה, הוא אחד מהמאמנים הכי מוערכים בליגה. בעונה הקודמת זה פחות עבד, גם כי באמצע העונה הייתה אותה הטרגדיה במותו של <strong>מאט בירד (Matt Beard)</strong>.
      </p>

      <p>
        לשיטה הזאת של ליברפול יש מגרעות ומעלות. המעלה המרכזית, הרצפה שלה מאוד גבוהה בליגה. אתפלא לראות אותה מתחת למקומות 7-10, כי בחלק גדול מהמשחקים, הלחץ שהן מפעילות בשליש עליון פשוט יפרק את רוב הקבוצות בליגה. גם מול קבוצות הביניים.
      </p>

      <p>
        המגרעות, פציעות פוטנציאליות, קיבעון טקטי ובעיקר קריסה מול קבוצות טופ.
      </p>

      <p class="font-bold text-neutral-900 dark:text-white pt-1">
        להלן המספרים שמראים את מה שדיברנו עליו:
      </p>
    </div>
  </div>

  <!-- Module 2: The Interactive 3D Coin Flip -->
  <div class="rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-[#121215] p-5 sm:p-8 space-y-6 shadow-sm overflow-hidden">
    
    <div class="text-center space-y-1.5">
      <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-mono font-bold bg-amber-100 dark:bg-amber-950/60 text-amber-800 dark:text-amber-300 border border-amber-300 dark:border-amber-700/60">
        <span>🪙 פרדוקס הלחץ של טיילור</span>
      </div>
      <h2 class="text-xl sm:text-2xl font-black text-neutral-900 dark:text-white">
        שני הצדדים של המטבע: הרצפה מול התקרה
      </h2>
      <p class="text-xs sm:text-sm text-neutral-500 dark:text-neutral-400 max-w-lg mx-auto">
        הקליקו על המטבע או על הכפתור למטה כדי להפוך צד ולראות את שני הקצוות של שיטת המשחק.
      </p>
    </div>

    <!-- Coin 3D Container -->
    <div class="py-4">
      <div class="coin-container relative max-w-md mx-auto w-72 h-72 sm:w-88 sm:h-88 md:w-96 md:h-96" style="perspective: 1200px;">
        <div id="liverpool-coin-inner" class="coin-inner w-full h-full relative cursor-pointer select-none transition-transform duration-700 ease-out" style="transform-style: preserve-3d;" onclick="toggleLiverpoolCoin()" role="button" tabindex="0" onkeydown="if(event.key==='Enter'||event.key===' ')toggleLiverpoolCoin()" aria-label="הפוך מטבע">
          
          <!-- Front Face: עץ (Heads) - The High Floor -->
          <div class="coin-face coin-front absolute inset-0 rounded-full p-6 sm:p-8 flex flex-col items-center justify-between text-center bg-gradient-to-br from-red-800 via-rose-950 to-neutral-950 text-white shadow-2xl border-4 border-amber-400/70 ring-8 ring-amber-500/20" style="-webkit-backface-visibility: hidden; backface-visibility: hidden;">
            
            <div class="pt-1">
              <span class="inline-block px-3 py-0.5 rounded-full text-[11px] font-mono font-bold tracking-wider uppercase bg-amber-400/20 text-amber-300 border border-amber-400/40">
                צד א' · עץ
              </span>
              <h3 class="text-lg sm:text-xl font-black tracking-tight text-amber-200 mt-1">
                הרצפה הגבוהה: כתישת הליגה
              </h3>
            </div>

            <!-- Stats Cluster Inside Coin -->
            <div class="space-y-2.5 sm:space-y-3 w-full my-auto">
              <div class="bg-black/40 backdrop-blur-sm rounded-lg py-1.5 px-3 border border-amber-400/20">
                <div class="text-2xl sm:text-3xl font-black text-amber-300 font-mono">45 חילוצים</div>
                <div class="text-[11px] sm:text-xs text-neutral-300">ב-0:4 המוחץ על צ'רלטון (כדורגל במעמד צד אחד)</div>
              </div>

              <div class="bg-black/40 backdrop-blur-sm rounded-lg py-1.5 px-3 border border-amber-400/20">
                <div class="text-2xl sm:text-3xl font-black text-emerald-400 font-mono">53 חילוצים + 17 תיקולים</div>
                <div class="text-[11px] sm:text-xs text-neutral-300">ב-1:1 מול ספרס (חנקו את הנעת הכדור)</div>
              </div>

              <div class="bg-black/40 backdrop-blur-sm rounded-lg py-1.5 px-3 border border-amber-400/20">
                <div class="text-2xl sm:text-3xl font-black text-white font-mono">17 בעיטות בדרבי</div>
                <div class="text-[11px] sm:text-xs text-neutral-300">0:2 מוחלט על אברטון באנפילד</div>
              </div>
            </div>

            <div class="pb-1 text-[11px] sm:text-xs text-amber-300/80 font-mono flex items-center gap-1">
              <span>↻ לחצו כדי לחשוף את הפאלי</span>
            </div>
          </div>

          <!-- Back Face: פאלי (Tails) - The Brittle Ceiling -->
          <div class="coin-face coin-back absolute inset-0 rounded-full p-6 sm:p-8 flex flex-col items-center justify-between text-center bg-gradient-to-br from-neutral-950 via-zinc-900 to-red-950 text-white shadow-2xl border-4 border-rose-500/70 ring-8 ring-rose-500/20" style="-webkit-backface-visibility: hidden; backface-visibility: hidden; transform: rotateY(180deg);">
            
            <div class="pt-1">
              <span class="inline-block px-3 py-0.5 rounded-full text-[11px] font-mono font-bold tracking-wider uppercase bg-rose-500/20 text-rose-300 border border-rose-500/40">
                צד ב' · פאלי
              </span>
              <h3 class="text-lg sm:text-xl font-black tracking-tight text-rose-300 mt-1">
                התקרה השבירה: שבירת קו הלחץ
              </h3>
            </div>

            <!-- Stats Cluster Inside Back Coin -->
            <div class="space-y-2.5 sm:space-y-3 w-full my-auto">
              <div class="bg-black/50 backdrop-blur-sm rounded-lg py-1.5 px-3 border border-rose-500/30">
                <div class="text-2xl sm:text-3xl font-black text-rose-400 font-mono">4.27 xG לחובתה</div>
                <div class="text-[11px] sm:text-xs text-rose-200">מול מנצ'סטר סיטי (4:2) — שיא עונתי שלילי ב-WSL</div>
              </div>

              <div class="bg-black/50 backdrop-blur-sm rounded-lg py-1.5 px-3 border border-rose-500/30">
                <div class="text-2xl sm:text-3xl font-black text-amber-400 font-mono">1.47 xG ו-15 בעיטות</div>
                <div class="text-[11px] sm:text-xs text-neutral-300">אפס שערים מול הבלוק הנמוך של יונייטד (0:1)</div>
              </div>

              <div class="bg-black/50 backdrop-blur-sm rounded-lg py-1.5 px-3 border border-rose-500/30">
                <div class="text-xl sm:text-2xl font-bold text-white font-mono">הפקרות בשטח פתוח</div>
                <div class="text-[11px] sm:text-xs text-neutral-300">שבירת הגל הראשון חושפת את צמד הבלמיות לחלוטין</div>
              </div>
            </div>

            <div class="pb-1 text-[11px] sm:text-xs text-rose-300/80 font-mono flex items-center gap-1">
              <span>↻ לחצו כדי לחזור לעץ</span>
            </div>
          </div>

        </div>
      </div>
    </div>

    <!-- Coin Controls & Status -->
    <div class="flex flex-col items-center justify-center gap-3 pt-2">
      <button onclick="toggleLiverpoolCoin()" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-full font-bold text-sm bg-neutral-900 hover:bg-neutral-800 text-white dark:bg-neutral-100 dark:hover:bg-neutral-200 dark:text-neutral-900 transition-colors shadow-md active:scale-95">
        <span>🪙 הפוך את המטבע (עץ / פאלי)</span>
      </button>
      <div id="coin-side-label" class="text-xs sm:text-sm font-sans font-medium text-neutral-600 dark:text-neutral-400 text-center">
        מציג כעת: <span class="text-emerald-600 dark:text-emerald-400 font-bold">עץ (הרצפה הגבוהה: כתישת קבוצות הביניים)</span>
      </div>
    </div>

  </div>

  <!-- Module 3: The Mathematical Floor (PPG Formulas & Historical Thresholds) -->
  <div class="rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-[#121215] p-5 sm:p-7 space-y-5 shadow-sm">
    <div class="border-b border-neutral-100 dark:border-neutral-800 pb-3">
      <span class="text-xs font-mono font-bold text-primary-600 dark:text-primary-400 uppercase tracking-wider">
        מתמטיקה של נקודות · ליגה בת 14 קבוצות (26 מחזורים)
      </span>
      <h2 class="text-xl sm:text-2xl font-black text-neutral-900 dark:text-white mt-1">
        מחשבון הרצפה ההיסטורית: למה ליברפול לא תרד מתחת למקום 7?
      </h2>
      <p class="text-sm text-neutral-600 dark:text-neutral-400 mt-1">
        במקום לנחש, הצבנו את נוסחאות צבירת הנקודות לקצב משחק (PPG) בתרחיש המחמיר ביותר.
      </p>
    </div>

    <!-- Formula Banner -->
    <div class="p-4 rounded-xl bg-neutral-50 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 text-center space-y-1">
      <div class="text-xs font-mono text-neutral-500 uppercase tracking-wider">נוסחת הרצפה בתרחיש קיצון שמרני</div>
      <div class="text-base sm:text-xl font-mono font-extrabold text-neutral-900 dark:text-white dir-ltr">
        PPG<sub>floor</sub> = [(16 × 1.75) + (10 × 0.40)] / 26 = <span class="text-emerald-600 dark:text-emerald-400">1.23 PPG</span> (32 נקודות)
      </div>
    </div>

    <!-- Breakdown Grid -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      
      <!-- Bucket 1: Mid & Bottom Tier -->
      <div class="p-4 rounded-xl border border-emerald-200 dark:border-emerald-900/50 bg-emerald-50/50 dark:bg-emerald-950/20 space-y-2">
        <div class="flex items-center justify-between">
          <span class="text-xs font-bold font-mono px-2 py-0.5 rounded bg-emerald-200 dark:bg-emerald-900 text-emerald-900 dark:text-emerald-200">
            16 משחקים
          </span>
          <span class="text-lg font-black font-mono text-emerald-700 dark:text-emerald-400">
            28 נק'
          </span>
        </div>
        <h4 class="font-bold text-neutral-900 dark:text-white text-sm">מול מקומות 7–14 (החצי התחתון)</h4>
        <p class="text-xs text-neutral-600 dark:text-neutral-400 leading-normal">
          קבוצות שלא מסוגלות לשבור לחץ בשליש מרכזי (צ'רלטון, אברטון, ברמינגהאם, וילה). קצב צבירה היסטורי שמרני של <strong>1.75 PPG</strong> (מתוך פוטנציאל של 2.20+).
        </p>
      </div>

      <!-- Bucket 2: Top 6 -->
      <div class="p-4 rounded-xl border border-rose-200 dark:border-rose-900/50 bg-rose-50/50 dark:bg-rose-950/20 space-y-2">
        <div class="flex items-center justify-between">
          <span class="text-xs font-bold font-mono px-2 py-0.5 rounded bg-rose-200 dark:bg-rose-900 text-rose-900 dark:text-rose-200">
            10 משחקים
          </span>
          <span class="text-lg font-black font-mono text-rose-700 dark:text-rose-400">
            4 נק'
          </span>
        </div>
        <h4 class="font-bold text-neutral-900 dark:text-white text-sm">מול הטופ-6 (איכות עילית)</h4>
        <p class="text-xs text-neutral-600 dark:text-neutral-400 leading-normal">
          תרחיש קריסה טקטית קיצוני: ליברפול מפסידה ב-8 מתוך 10 המשחקים הללו ומחלצת 4 תוצאות תיקו בלבד (קצב של <strong>0.40 PPG</strong> בלבד).
        </p>
      </div>

      <!-- Bucket 3: The WSL Baseline Threshold -->
      <div class="p-4 rounded-xl border border-blue-200 dark:border-blue-900/50 bg-blue-50/50 dark:bg-blue-950/20 space-y-2">
        <div class="flex items-center justify-between">
          <span class="text-xs font-bold font-mono px-2 py-0.5 rounded bg-blue-200 dark:bg-blue-900 text-blue-900 dark:text-blue-200">
            סף היסטורי
          </span>
          <span class="text-lg font-black font-mono text-blue-700 dark:text-blue-400">
            0.95–1.15
          </span>
        </div>
        <h4 class="font-bold text-neutral-900 dark:text-white text-sm">רף מקומות 7–10 ב-WSL</h4>
        <p class="text-xs text-neutral-600 dark:text-neutral-400 leading-normal">
          מקומות 7–10 מסיימים היסטורית עם <strong>25 עד 30 נקודות</strong>. 32 הנקודות של ליברפול ברצפה השמרנית משאירות אותה בוודאות מעל הרף הזה.
        </p>
      </div>

    </div>

    <!-- Visual Comparison Gauge -->
    <div class="pt-2 space-y-2">
      <div class="flex justify-between text-xs font-mono text-neutral-500">
        <span>קו ירידה (18 נק')</span>
        <span>מקומות 8–10 (25–30 נק')</span>
        <span class="font-bold text-emerald-600 dark:text-emerald-400">רצפת ליברפול (32 נק')</span>
        <span>יעד טופ-5 (38+ נק')</span>
      </div>
      <div class="w-full h-3 rounded-full bg-neutral-200 dark:bg-neutral-800 relative overflow-hidden">
        <div class="h-full bg-neutral-400 dark:bg-neutral-600 w-[35%] absolute"></div>
        <div class="h-full bg-amber-400 w-[55%] absolute"></div>
        <div class="h-full bg-emerald-500 w-[63%] absolute"></div>
      </div>
      <p class="text-xs text-neutral-500 dark:text-neutral-400 text-center font-sans">
        מסקנה: גם אם ליברפול תיכשל טוטאלית מול אריות הליגה, משחק הלחץ מול 8 קבוצות התחתית מעניק לה כרטיס ביטוח שמבטיח מתמטית את המקום ה-5–6.
      </p>
    </div>

  </div>

  <!-- Module 4: New Signings Upgrade Grid -->
  <div class="rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-[#121215] p-5 sm:p-7 space-y-5 shadow-sm">
    <div class="border-b border-neutral-100 dark:border-neutral-800 pb-3">
      <div class="flex items-center gap-2">
        <span class="text-xs font-mono font-bold px-2 py-0.5 rounded bg-primary-100 dark:bg-primary-950/50 text-primary-800 dark:text-primary-300 border border-primary-200 dark:border-primary-800">
          שדרוגי סגל 2026/27
        </span>
      </div>
      <h2 class="text-xl sm:text-2xl font-black text-neutral-900 dark:text-white mt-1">
        שחקניות הרכש: למה השיטה של טיילור עובדת השנה?
      </h2>
      <p class="text-sm text-neutral-600 dark:text-neutral-400">
        ארבע שחקניות מפתח שנרכשו בקיץ ומספקות את הכלים הפיזיים והטקטיים לביצוע הלחץ הגבוה.
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      
      <!-- Player 1: Endemann -->
      <div class="p-4 rounded-xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/50 dark:bg-neutral-900/30 flex flex-col justify-between space-y-3">
        <div>
          <div class="flex items-center justify-between">
            <span class="text-xs font-mono font-bold px-2 py-0.5 rounded bg-red-100 dark:bg-red-950/60 text-red-800 dark:text-red-300">
              חלוצה / כנף · #9
            </span>
            <span class="text-xs font-mono text-neutral-400">מוולפסבורג (גרמניה)</span>
          </div>
          <h3 class="text-lg font-bold text-neutral-900 dark:text-white mt-1">
            ויוויאן אנדמן (Vivien Endemann)
          </h3>
          <p class="text-xs text-neutral-600 dark:text-neutral-400 mt-1">
            <strong>טריגר הלחץ הראשי:</strong> מפלצת מעברים שלוחצת ראשונה. מדורגת ב<strong>אחוזון ה-92 באירופה</strong> בחטיפות כדור בשליש ההתקפי (Possession won final 3rd).
          </p>
        </div>
        <div class="pt-2 border-t border-neutral-200 dark:border-neutral-800/60 flex items-center justify-between text-xs font-mono">
          <span class="text-neutral-500">תפוקה בוולפסבורג:</span>
          <span class="font-bold text-red-600 dark:text-red-400">0.62 שערים+בישולים ל-90 דק'</span>
        </div>
      </div>

      <!-- Player 2: Kapocs -->
      <div class="p-4 rounded-xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/50 dark:bg-neutral-900/30 flex flex-col justify-between space-y-3">
        <div>
          <div class="flex items-center justify-between">
            <span class="text-xs font-mono font-bold px-2 py-0.5 rounded bg-blue-100 dark:bg-blue-950/60 text-blue-800 dark:text-blue-300">
              כנף / התקפה · #7
            </span>
            <span class="text-xs font-mono text-neutral-400">מלינקופינג (שוודיה)</span>
          </div>
          <h3 class="text-lg font-bold text-neutral-900 dark:text-white mt-1">
            קורנליה קפוטש (Cornelia Kapocs)
          </h3>
          <p class="text-xs text-neutral-600 dark:text-neutral-400 mt-1">
            <strong>הסיומת במעברים:</strong> מספקת עומק התקפי שמונע נפילת אינטנסיביות בדקות 60+. כבשה את השער המכריע ב-0:2 בדרבי מול אברטון באנפילד.
          </p>
        </div>
        <div class="pt-2 border-t border-neutral-200 dark:border-neutral-800/60 flex items-center justify-between text-xs font-mono">
          <span class="text-neutral-500">רגע שיא העונה:</span>
          <span class="font-bold text-blue-600 dark:text-blue-400">שער דרבי באנפילד (מחזור 4)</span>
        </div>
      </div>

      <!-- Player 3: Keating -->
      <div class="p-4 rounded-xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/50 dark:bg-neutral-900/30 flex flex-col justify-between space-y-3">
        <div>
          <div class="flex items-center justify-between">
            <span class="text-xs font-mono font-bold px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950/60 text-emerald-800 dark:text-emerald-300">
              שוערת · #12
            </span>
            <span class="text-xs font-mono text-neutral-400">ממנצ'סטר סיטי</span>
          </div>
          <h3 class="text-lg font-bold text-neutral-900 dark:text-white mt-1">
            קיארה קיטינג (Khiara Keating)
          </h3>
          <p class="text-xs text-neutral-600 dark:text-neutral-400 mt-1">
            <strong>מפתחת ה-Sweeper-Keeper:</strong> מכירה את שיטת טיילור לעומק. היציאות האגרסיביות שלה מחוץ לרחבה מאפשרות לקו ההגנה לעלות ב-10 מטרים מעונה שעברה.
          </p>
        </div>
        <div class="pt-2 border-t border-neutral-200 dark:border-neutral-800/60 flex items-center justify-between text-xs font-mono">
          <span class="text-neutral-500">השפעה טקטית:</span>
          <span class="font-bold text-emerald-600 dark:text-emerald-400">+10 מטרים בקו ההגנה</span>
        </div>
      </div>

      <!-- Player 4: Bernabé -->
      <div class="p-4 rounded-xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/50 dark:bg-neutral-900/30 flex flex-col justify-between space-y-3">
        <div>
          <div class="flex items-center justify-between">
            <span class="text-xs font-mono font-bold px-2 py-0.5 rounded bg-purple-100 dark:bg-purple-950/60 text-purple-800 dark:text-purple-300">
              מגינה שמאלית · #29
            </span>
            <span class="text-xs font-mono text-neutral-400">ריאל סוסיאדד / צ'לסי</span>
          </div>
          <h3 class="text-lg font-bold text-neutral-900 dark:text-white mt-1">
            אלחנדרה ברנאבה (Alejandra Bernabé)
          </h3>
          <p class="text-xs text-neutral-600 dark:text-neutral-400 mt-1">
            <strong>דחיפה פרוגרסיבית מאגף שמאל:</strong> מונעת תקיעות בהנעת כדור אחורית. דוחפת את המשחק קדימה עם חדירות מהאגף ומסירות עומק מדויקות.
          </p>
        </div>
        <div class="pt-2 border-t border-neutral-200 dark:border-neutral-800/60 flex items-center justify-between text-xs font-mono">
          <span class="text-neutral-500">מסירות פרוגרסיביות:</span>
          <span class="font-bold text-purple-600 dark:text-purple-400">4.6 ל-90 דקות</span>
        </div>
      </div>

    </div>
  </div>

</div>

<!-- Interactive 3D Coin Script -->
<script>
  function toggleLiverpoolCoin() {
    const coin = document.getElementById('liverpool-coin-inner');
    const label = document.getElementById('coin-side-label');
    if (!coin) return;
    
    coin.classList.toggle('flipped');
    const isFlipped = coin.classList.contains('flipped');
    
    if (isFlipped) {
      coin.style.transform = 'rotateY(180deg)';
      if (label) {
        label.innerHTML = 'מציג כעת: <span class="text-rose-600 dark:text-rose-400 font-bold">פאלי (התקרה השבירה: שבירת קו הלחץ מול קבוצות העילית)</span>';
      }
    } else {
      coin.style.transform = 'rotateY(0deg)';
      if (label) {
        label.innerHTML = 'מציג כעת: <span class="text-emerald-600 dark:text-emerald-400 font-bold">עץ (הרצפה הגבוהה: כתישת קבוצות הביניים)</span>';
      }
    }
  }
</script>
