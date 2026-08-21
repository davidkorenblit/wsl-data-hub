---
layout: default
title: "מדריך ומילון המדדים | WSL Data Hub"
permalink: /metrics/
prev_url: /methodology/
prev_title: "מתודולוגיה ושאלות מחקר"
---

<div class="space-y-6">

  <!-- Header -->
  <div class="border-b border-neutral-200 pb-4">
    <div class="text-xs font-mono uppercase text-neutral-500 font-bold tracking-wider mb-1">
      DATA DICTIONARY & METRICS
    </div>
    <h1 class="text-2xl md:text-3xl font-bold tracking-tight text-neutral-900 mb-2">
      מילון המדדים ופירוט טכני
    </h1>
    <p class="text-sm sm:text-base text-neutral-600 leading-relaxed font-sans">
      מרוכזים כאן כל המדדים, נוסחאות החישוב והרציונל האנליטי מאחורי הניתוחים.
    </p>
  </div>

  <!-- Main Content Card -->
  <div class="rounded-md border border-neutral-200 bg-white p-6 space-y-8 text-neutral-800 leading-relaxed font-sans">

    <!-- Overview Note -->
    <div class="p-3.5 bg-neutral-50 rounded border border-neutral-200 text-xs sm:text-sm text-neutral-600">
      <strong class="text-neutral-900 font-mono uppercase text-[11px]">Data Source:</strong> מאגרי FBref / Opta לעונת ה-WSL. כל הנתונים מנורמלים ל-90 דקות משחק (Per 90) להשוואה הוגנת.
    </div>

    <!-- 1. Attack & Finishing -->
    <section class="space-y-3 pt-2">
      <div class="text-xs font-mono uppercase text-neutral-500 font-bold tracking-wider mb-1">
        CATEGORY 01
      </div>
      <h2 class="text-xl font-bold text-neutral-900">
        1. התקפה, איומים ויעילות סיומת
      </h2>
      <div class="space-y-2.5">
        <div class="p-3 bg-neutral-50 rounded border border-neutral-200 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900">GF / GF per 90 (Goals For)</span>
            <span class="text-[10px] font-mono border border-neutral-300 bg-white px-1.5 py-0.5 rounded text-neutral-600">שערים בפועל</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600">סך השערים שהבקיעה הקבוצה וממוצע השערים ל-90 דקות.</p>
        </div>

        <div class="p-3 bg-neutral-50 rounded border border-neutral-200 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900">Sh/90 (Shots per 90)</span>
            <span class="text-[10px] font-mono border border-neutral-300 bg-white px-1.5 py-0.5 rounded text-neutral-600">נפח איומים</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600">כמות הבעיטות הממוצעת שהקבוצה מייצרת לכל 90 דקות.</p>
        </div>

        <div class="p-3 bg-neutral-50 rounded border border-neutral-200 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900">SoT% (Shots on Target Percentage)</span>
            <span class="text-[10px] font-mono border border-neutral-300 bg-white px-1.5 py-0.5 rounded text-neutral-600">דיוק למסגרת</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600">אחוז הבעיטות שהלכו למסגרת מתוך סך הבעיטות.</p>
        </div>

        <div class="p-3 bg-neutral-50 rounded border border-neutral-200 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900">G/Sh (Goals per Shot)</span>
            <span class="text-[10px] font-mono border border-neutral-300 bg-white px-1.5 py-0.5 rounded text-neutral-600">יעילות סיומת</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600">יחס ההמרה של בעיטה לשער (כמה שערים נכבשים מכל בעיטה).</p>
        </div>
      </div>
    </section>

    <!-- 2. Creation & Passing -->
    <section class="space-y-3 pt-4 border-t border-neutral-200">
      <div class="text-xs font-mono uppercase text-neutral-500 font-bold tracking-wider mb-1">
        CATEGORY 02
      </div>
      <h2 class="text-xl font-bold text-neutral-900">
        2. יצירתיות, בישולים וייצור מצבים
      </h2>
      <div class="space-y-2.5">
        <div class="p-3 bg-neutral-50 rounded border border-neutral-200 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900">Ast / Ast per 90 (Assists)</span>
            <span class="text-[10px] font-mono border border-neutral-300 bg-white px-1.5 py-0.5 rounded text-neutral-600">בישולים ישירים</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600">מסירות שהובילו ישירות לשער, מנורמלות ל-90 דקות.</p>
        </div>

        <div class="p-3 bg-neutral-50 rounded border border-neutral-200 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900">Poss% (Possession Percentage)</span>
            <span class="text-[10px] font-mono border border-neutral-300 bg-white px-1.5 py-0.5 rounded text-neutral-600">החזקת כדור</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600">אחוז הזמן שהכדור ברגלי הקבוצה.</p>
        </div>
      </div>
    </section>

    <!-- 3. Defense & Goalkeeping -->
    <section class="space-y-3 pt-4 border-t border-neutral-200">
      <div class="text-xs font-mono uppercase text-neutral-500 font-bold tracking-wider mb-1">
        CATEGORY 03
      </div>
      <h2 class="text-xl font-bold text-neutral-900">
        3. הגנה, חילוצים ועבודת שוערת
      </h2>
      <div class="space-y-2.5">
        <div class="p-3 bg-neutral-50 rounded border border-neutral-200 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900">GA / GA per 90 (Goals Against)</span>
            <span class="text-[10px] font-mono border border-neutral-300 bg-white px-1.5 py-0.5 rounded text-neutral-600">ספיגת שערים</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600">כמות השערים שספגה הקבוצה וממוצע הספיגה ל-90 דקות.</p>
        </div>

        <div class="p-3 bg-neutral-50 rounded border border-neutral-200 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900">SoTA per 90 (Shots on Target Against)</span>
            <span class="text-[10px] font-mono border border-neutral-300 bg-white px-1.5 py-0.5 rounded text-neutral-600">חשיפה לאיומים</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600">בעיטות למסגרת שמגיעות לעבר שער הקבוצה בכל 90 דקות.</p>
        </div>

        <div class="p-3 bg-neutral-50 rounded border border-neutral-200 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900">Save% (Save Percentage)</span>
            <span class="text-[10px] font-mono border border-neutral-300 bg-white px-1.5 py-0.5 rounded text-neutral-600">אחוז הצלות שוערת</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600">היחס בין בעיטות שנבלמו על ידי השוערת לסך הבעיטות למסגרת.</p>
        </div>

        <div class="p-3 bg-neutral-50 rounded border border-neutral-200 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900">TklW + Int (Tackles Won + Interceptions)</span>
            <span class="text-[10px] font-mono border border-neutral-300 bg-white px-1.5 py-0.5 rounded text-neutral-600">תיקולים וחטיפות</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600">מדד מצטבר של תיקולים מוצלחים וחטיפות כדור.</p>
        </div>
      </div>
    </section>

    <!-- 4. Macro & Benchmarks -->
    <section class="space-y-3 pt-4 border-t border-neutral-200">
      <div class="text-xs font-mono uppercase text-neutral-500 font-bold tracking-wider mb-1">
        CATEGORY 04
      </div>
      <h2 class="text-xl font-bold text-neutral-900">
        4. מודל חישוב הציפיות והערכת ביצועים (Baseline Benchmarks)
      </h2>
      <p class="text-xs sm:text-sm text-neutral-600">
        מודל בנצ'מרק שמחשב מה הקבוצה הייתה "אמורה" להפיק מתוך הנתונים שלה ביחס לממוצע הליגה:
      </p>

      <div class="space-y-2.5">
        <div class="p-3.5 bg-neutral-50 rounded border border-neutral-200 space-y-1">
          <div class="font-mono text-xs font-bold text-neutral-900">1. ספיגה צפויה (Expected GA)</div>
          <p class="text-xs text-neutral-700">
            <strong>נוסחה:</strong> <code class="font-mono text-xs text-neutral-900 bg-white px-1 py-0.5 rounded border border-neutral-200">xGA = SoTA × (1 - ממוצע הצלות הליגה)</code>
          </p>
        </div>

        <div class="p-3.5 bg-neutral-50 rounded border border-neutral-200 space-y-1">
          <div class="font-mono text-xs font-bold text-neutral-900">2. הבקעה צפויה (Expected GF)</div>
          <p class="text-xs text-neutral-700">
            <strong>נוסחה:</strong> <code class="font-mono text-xs text-neutral-900 bg-white px-1 py-0.5 rounded border border-neutral-200">xGF = SoT × יחס שערים לבעיטה למסגרת בליגה</code>
          </p>
        </div>

        <div class="p-3.5 bg-neutral-50 rounded border border-neutral-200 space-y-1">
          <div class="font-mono text-xs font-bold text-neutral-900">3. בישולים צפויים (Expected Assists)</div>
          <p class="text-xs text-neutral-700">
            <strong>נוסחה:</strong> <code class="font-mono text-xs text-neutral-900 bg-white px-1 py-0.5 rounded border border-neutral-200">xAst = GF × יחס בישולים לשערים בליגה</code>
          </p>
        </div>

        <div class="p-3.5 bg-neutral-50 rounded border border-neutral-200 space-y-1">
          <div class="font-mono text-xs font-bold text-neutral-900">4. נקודות צפויות (xPTS) מרגרסיה ליניארית של הפרש שערים</div>
          <p class="text-xs text-neutral-700">
            <strong>נוסחה:</strong> <code class="font-mono text-xs text-neutral-900 bg-white px-1 py-0.5 rounded border border-neutral-200">xPTS = 0.576 × GD + 31.0</code>
          </p>
        </div>
      </div>
    </section>

  </div>

  <!-- Standardized Post Pagination -->
  {% include post_pagination.html %}

</div>
