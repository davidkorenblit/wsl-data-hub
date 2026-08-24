---
layout: default
title: "מדריך ומילון המדדים | WSL Data Hub"
permalink: /metrics/
prev_url: /methodology/
prev_title: "מתודולוגיה ושאלות מחקר"
---

<div class="space-y-6">

  <!-- Header -->
  <div class="border-b border-neutral-200 dark:border-neutral-800 pb-4">
    <div class="text-xs font-mono uppercase text-neutral-500 dark:text-neutral-400 font-bold tracking-wider mb-1">
      DATA DICTIONARY & METRICS
    </div>
    <h1 class="text-2xl md:text-3xl font-bold tracking-tight text-neutral-900 dark:text-white mb-2">
      מילון המדדים ופירוט טכני
    </h1>
    <p class="text-sm sm:text-base text-neutral-600 dark:text-neutral-300 leading-relaxed font-sans">
      מרוכזים כאן כל המדדים, נוסחאות החישוב והרציונל האנליטי מאחורי הניתוחים.
    </p>
  </div>

  <!-- Main Content Card -->
  <div class="rounded-md border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-[#121215] p-6 space-y-8 text-neutral-800 dark:text-neutral-200 leading-relaxed font-sans">

    <!-- Overview Note -->
    <div class="p-3.5 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 text-xs sm:text-sm text-neutral-600 dark:text-neutral-300">
      <strong class="text-neutral-900 dark:text-white font-mono uppercase text-[11px]">Data Source:</strong> מאגרי FBref ואירועי Opta / FotMob לעונת ה-WSL והליגות הבכירות. כל הנתונים מנורמלים ל-90 דקות משחק (Per 90) לצורך השוואה אחידה ומדויקת.
    </div>

    <!-- 1. Attack & Finishing -->
    <section class="space-y-3 pt-2">
      <div class="text-xs font-mono uppercase text-neutral-500 dark:text-neutral-400 font-bold tracking-wider mb-1">
        CATEGORY 01
      </div>
      <h2 class="text-xl font-bold text-neutral-900 dark:text-white">
        1. התקפה, איומים ויעילות סיומת
      </h2>
      <div class="space-y-2.5">
        <div class="p-3 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900 dark:text-white">GF / GF per 90 (Goals For)</span>
            <span class="text-[10px] font-mono border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-neutral-900 px-1.5 py-0.5 rounded text-neutral-600 dark:text-neutral-300">שערים בפועל</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300">סך השערים שהבקיעה הקבוצה וממוצע השערים ל-90 דקות.</p>
        </div>

        <div class="p-3 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900 dark:text-white">Sh/90 (Shots per 90)</span>
            <span class="text-[10px] font-mono border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-neutral-900 px-1.5 py-0.5 rounded text-neutral-600 dark:text-neutral-300">נפח איומים</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300">כמות הבעיטות הממוצעת שהקבוצה מייצרת לכל 90 דקות.</p>
        </div>

        <div class="p-3 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900 dark:text-white">SoT% (Shots on Target Percentage)</span>
            <span class="text-[10px] font-mono border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-neutral-900 px-1.5 py-0.5 rounded text-neutral-600 dark:text-neutral-300">דיוק למסגרת</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300">אחוז הבעיטות שהלכו למסגרת מתוך סך הבעיטות.</p>
        </div>

        <div class="p-3 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900 dark:text-white">G/Sh (Goals per Shot)</span>
            <span class="text-[10px] font-mono border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-neutral-900 px-1.5 py-0.5 rounded text-neutral-600 dark:text-neutral-300">יעילות סיומת</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300">יחס ההמרה של בעיטה לשער (כמה שערים נכבשים מכל בעיטה).</p>
        </div>
      </div>
    </section>

    <!-- 2. Creation & Passing -->
    <section class="space-y-3 pt-4 border-t border-neutral-200 dark:border-neutral-800">
      <div class="text-xs font-mono uppercase text-neutral-500 dark:text-neutral-400 font-bold tracking-wider mb-1">
        CATEGORY 02
      </div>
      <h2 class="text-xl font-bold text-neutral-900 dark:text-white">
        2. יצירתיות, בישולים וייצור מצבים
      </h2>
      <div class="space-y-2.5">
        <div class="p-3 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900 dark:text-white">Ast / Ast per 90 (Assists)</span>
            <span class="text-[10px] font-mono border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-neutral-900 px-1.5 py-0.5 rounded text-neutral-600 dark:text-neutral-300">בישולים ישירים</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300">מסירות שהובילו ישירות לשער, מנורמלות ל-90 דקות.</p>
        </div>

        <div class="p-3 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900 dark:text-white">Poss% (Possession Percentage)</span>
            <span class="text-[10px] font-mono border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-neutral-900 px-1.5 py-0.5 rounded text-neutral-600 dark:text-neutral-300">החזקת כדור</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300">אחוז הזמן שהכדור ברגלי הקבוצה.</p>
        </div>
      </div>
    </section>

    <!-- 3. Defense & Goalkeeping -->
    <section class="space-y-3 pt-4 border-t border-neutral-200 dark:border-neutral-800">
      <div class="text-xs font-mono uppercase text-neutral-500 dark:text-neutral-400 font-bold tracking-wider mb-1">
        CATEGORY 03
      </div>
      <h2 class="text-xl font-bold text-neutral-900 dark:text-white">
        3. הגנה, מניעה ואיכות שוערות
      </h2>
      <div class="space-y-2.5">
        <div class="p-3 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900 dark:text-white">GA / GA per 90 (Goals Against)</span>
            <span class="text-[10px] font-mono border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-neutral-900 px-1.5 py-0.5 rounded text-neutral-600 dark:text-neutral-300">שערי חובה</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300">סך השערים שספגה הקבוצה וממוצע הספיגה ל-90 דקות.</p>
        </div>

        <div class="p-3 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900 dark:text-white">Save% (Save Percentage)</span>
            <span class="text-[10px] font-mono border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-neutral-900 px-1.5 py-0.5 rounded text-neutral-600 dark:text-neutral-300">אחוז הצלות</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300">אחוז ההצלות של השוערת מתוך סך הבעיטות למסגרת שנבעטו אליה.</p>
        </div>

        <div class="p-3 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900 dark:text-white">PSxG +/- (Post-Shot xG Difference)</span>
            <span class="text-[10px] font-mono border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-neutral-900 px-1.5 py-0.5 rounded text-neutral-600 dark:text-neutral-300">איכות מניעת שערים</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300">מדד מתקדם שמחשב כמה שערים השוערת מנעה ביחס למידת המסוכנות של הבעיטות שנבעטו אליה (ערך חיובי מעיד על הצלת שערים בטוחים).</p>
        </div>
      </div>
    </section>

    <!-- 4. Macro & Benchmarks -->
    <section class="space-y-3 pt-4 border-t border-neutral-200 dark:border-neutral-800">
      <div class="text-xs font-mono uppercase text-neutral-500 dark:text-neutral-400 font-bold tracking-wider mb-1">
        CATEGORY 04
      </div>
      <h2 class="text-xl font-bold text-neutral-900 dark:text-white">
        4. מודל חישוב הציפיות והערכת ביצועים (Baseline Benchmarks)
      </h2>
      <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300">
        מודל בנצ'מרק שמחשב מה הקבוצה הייתה "אמורה" להפיק מתוך הנתונים שלה ביחס לממוצע הליגה:
      </p>

      <div class="space-y-2.5">
        <div class="p-3.5 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="font-mono text-xs font-bold text-neutral-900 dark:text-white">1. ספיגה צפויה (Expected GA)</div>
          <p class="text-xs text-neutral-700 dark:text-neutral-300">
            <strong>נוסחה:</strong> <code class="font-mono text-xs text-neutral-900 dark:text-white bg-white dark:bg-neutral-900 px-1 py-0.5 rounded border border-neutral-200 dark:border-neutral-700">xGA = SoTA × (1 - ממוצע הצלות הליגה)</code>
          </p>
        </div>

        <div class="p-3.5 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="font-mono text-xs font-bold text-neutral-900 dark:text-white">2. הבקעה צפויה (Expected GF)</div>
          <p class="text-xs text-neutral-700 dark:text-neutral-300">
            <strong>נוסחה:</strong> <code class="font-mono text-xs text-neutral-900 dark:text-white bg-white dark:bg-neutral-900 px-1 py-0.5 rounded border border-neutral-200 dark:border-neutral-700">xGF = SoT × יחס שערים לבעיטה למסגרת בליגה</code>
          </p>
        </div>

        <div class="p-3.5 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="font-mono text-xs font-bold text-neutral-900 dark:text-white">3. בישולים צפויים (Expected Assists)</div>
          <p class="text-xs text-neutral-700 dark:text-neutral-300">
            <strong>נוסחה:</strong> <code class="font-mono text-xs text-neutral-900 dark:text-white bg-white dark:bg-neutral-900 px-1 py-0.5 rounded border border-neutral-200 dark:border-neutral-700">xAst = GF × יחס בישולים לשערים בליגה</code>
          </p>
        </div>

        <div class="p-3.5 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="font-mono text-xs font-bold text-neutral-900 dark:text-white">4. נקודות צפויות (xPTS) מרגרסיה ליניארית של הפרש שערים</div>
          <p class="text-xs text-neutral-700 dark:text-neutral-300">
            <strong>נוסחה (עונת 22 משחקים):</strong> <code class="font-mono text-xs text-neutral-900 dark:text-white bg-white dark:bg-neutral-900 px-1 py-0.5 rounded border border-neutral-200 dark:border-neutral-700">xPTS = 0.576 × GD + 31.0</code>
          </p>
          <p class="text-xs text-neutral-700 dark:text-neutral-300 mt-1">
            <strong>נוסחה מותאמת (עונת 26 משחקים - 14 קבוצות):</strong> <code class="font-mono text-xs text-neutral-900 dark:text-white bg-white dark:bg-neutral-900 px-1 py-0.5 rounded border border-neutral-200 dark:border-neutral-700">xPTS_26 = 0.576 × GD + 36.6</code>
          </p>
        </div>
      </div>
    </section>

    <!-- 5. Advanced Creation & Quality Metrics (Opta / FotMob) -->
    <section class="space-y-3 pt-4 border-t border-neutral-200 dark:border-neutral-800">
      <div class="text-xs font-mono uppercase text-neutral-500 dark:text-neutral-400 font-bold tracking-wider mb-1">
        CATEGORY 05
      </div>
      <h2 class="text-xl font-bold text-neutral-900 dark:text-white">
        5. מדדי יצירה, עומק ואיכות מתקדמים (Opta / FotMob)
      </h2>
      <div class="space-y-2.5">
        <div class="p-3 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900 dark:text-white">Chances Created / Big Chances</span>
            <span class="text-[10px] font-mono border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-neutral-900 px-1.5 py-0.5 rounded text-neutral-600 dark:text-neutral-300">יצירת מצבים</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300">מסירות מפתח שמובילות לבעיטה לשער (Chances), והזדמנויות של מצב ודאי מול השוערת (Big Chances Created).</p>
        </div>

        <div class="p-3 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900 dark:text-white">Touches in Opposition Box</span>
            <span class="text-[10px] font-mono border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-neutral-900 px-1.5 py-0.5 rounded text-neutral-600 dark:text-neutral-300">נוכחות ברחבה</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300">כמות הפעולות והנגיעות בכדור בתוך רחבת ה-16 של היריב — מדד קריטי לשליטה טריטוריאלית ואיום ישיר.</p>
        </div>

        <div class="p-3 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900 dark:text-white">Possession Won Final 3rd</span>
            <span class="text-[10px] font-mono border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-neutral-900 px-1.5 py-0.5 rounded text-neutral-600 dark:text-neutral-300">לחץ גבוה</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300">חטיפות וחילוצי כדור בשליש ההתקפי של המגרש — מודד את יעילות הלחץ הגבוה (High Press) וזכייה בכדורים מסוכנים.</p>
        </div>

        <div class="p-3 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900 dark:text-white">Positional Percentiles</span>
            <span class="text-[10px] font-mono border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-neutral-900 px-1.5 py-0.5 rounded text-neutral-600 dark:text-neutral-300">אחוזונים לפי עמדה</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300">דירוג השחקנית באחוזים מול כלל השחקניות באותה עמדה בדיוק בחמש הליגות הבכירות ובליגת האלופות (UWCL).</p>
        </div>
      </div>
    </section>

  </div>

  <!-- Standardized Post Pagination -->
  {% include post_pagination.html %}

</div>
