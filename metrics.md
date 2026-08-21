---
layout: default
title: "מדריך ומילון המדדים | WSL Data Hub"
permalink: /metrics/
---

<div class="max-w-4xl mx-auto space-y-6">

  <!-- Header Card -->
  <div class="bg-surface-900 rounded-xl border border-surface-700/80 p-6 sm:p-8">
    <div class="flex items-center gap-2 mb-2.5">
      <span class="px-2 py-0.5 border border-surface-700 bg-surface-850 text-neutral-400 text-[11px] font-mono rounded">
        DATA DICTIONARY & METRICS
      </span>
      <span class="text-xs font-mono text-neutral-500">WSL 2025/26</span>
    </div>
    <h1 class="font-serif text-3xl sm:text-4xl font-bold text-white mb-3 tracking-tight">
      מילון המדדים ופירוט טכני
    </h1>
    <p class="text-neutral-300 text-base sm:text-lg leading-relaxed font-sans">
      עבור מי שרוצה לצלול עמוק יותר אל תוך הקרביים של הדאטא: כאן מרוכזים כל המדדים, נוסחאות החישוב והרציונל האנליטי מאחורי הניתוחים שלנו.
    </p>
  </div>

  <!-- Main Content Card -->
  <div class="bg-surface-900 rounded-xl border border-surface-700/80 p-6 sm:p-8 space-y-8 text-neutral-300 leading-relaxed font-sans">

    <!-- Overview Note -->
    <div class="p-3.5 bg-surface-850 rounded-lg border border-surface-700/80 text-xs sm:text-sm text-neutral-300">
      <strong class="text-white font-mono uppercase text-[11px]">Data Source:</strong> מאגרי FBref / Opta לעונת ה-WSL. כל הנתונים מנורמלים ל-90 דקות משחק (Per 90) כדי לאפשר השוואה הוגנת ונטולת הטיות של דקות משחק.
    </div>

    <!-- 1. Attack & Finishing -->
    <section class="space-y-3.5 pt-2">
      <h2 class="font-serif text-xl font-bold text-white flex items-center gap-2">
        <span>⚡</span>
        <span>1. התקפה, איומים ויעילות סיומת</span>
      </h2>
      <div class="space-y-2.5">
        <div class="p-3.5 bg-surface-850 rounded-lg border border-surface-700/80 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-brand-400">GF / GF per 90 (Goals For)</span>
            <span class="text-[10px] font-mono border border-surface-700 bg-surface-800 px-2 py-0.5 rounded text-neutral-400">שערים בפועל</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-300">סך השערים שהבקיעה הקבוצה וממוצע השערים ל-90 דקות. מייצג את התפוקה ההתקפית המוחלטת.</p>
        </div>

        <div class="p-3.5 bg-surface-850 rounded-lg border border-surface-700/80 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-brand-400">Sh/90 (Shots per 90)</span>
            <span class="text-[10px] font-mono border border-surface-700 bg-surface-800 px-2 py-0.5 rounded text-neutral-400">נפח איומים</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-300">כמות הבעיטות הממוצעת שהקבוצה מייצרת לכל 90 דקות. מודד את תדירות ההגעה למצבי בעיטה ללא קשר לדיוק.</p>
        </div>

        <div class="p-3.5 bg-surface-850 rounded-lg border border-surface-700/80 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-brand-400">SoT% (Shots on Target Percentage)</span>
            <span class="text-[10px] font-mono border border-surface-700 bg-surface-800 px-2 py-0.5 rounded text-neutral-400">דיוק למסגרת</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-300">אחוז הבעיטות שהלכו למסגרת מתוך סך הבעיטות. מודד את איכות הכיוון והיכולת של שחקניות ההתקפה לאלץ את שוערת היריבה לפעול.</p>
        </div>

        <div class="p-3.5 bg-surface-850 rounded-lg border border-surface-700/80 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-brand-400">G/Sh (Goals per Shot)</span>
            <span class="text-[10px] font-mono border border-surface-700 bg-surface-800 px-2 py-0.5 rounded text-neutral-400">יעילות סיומת</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-300">יחס ההמרה של בעיטה לשער (כמה שערים נכבשים בממוצע מכל בעיטה). מדד הממחיש חדות וניצול הזדמנויות.</p>
        </div>
      </div>
    </section>

    <!-- 2. Creation & Passing -->
    <section class="space-y-3.5 pt-4 border-t border-surface-700/80">
      <h2 class="font-serif text-xl font-bold text-white flex items-center gap-2">
        <span>🪄</span>
        <span>2. יצירתיות, בישולים וייצור מצבים</span>
      </h2>
      <div class="space-y-2.5">
        <div class="p-3.5 bg-surface-850 rounded-lg border border-surface-700/80 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-brand-400">Ast / Ast per 90 (Assists)</span>
            <span class="text-[10px] font-mono border border-surface-700 bg-surface-800 px-2 py-0.5 rounded text-neutral-400">בישולים ישירים</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-300">מסירות שהובילו ישירות לשער. בהיעדר נתוני xA/SCA מלאים לכלל הליגה, קצב האסיסטים ל-90 דקות בשילוב עם החזקת כדור משמש כאינדיקטור מרכזי לרמת הפרגון והאיכות במסירה האחרונה.</p>
        </div>

        <div class="p-3.5 bg-surface-850 rounded-lg border border-surface-700/80 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-brand-400">Poss% (Possession Percentage)</span>
            <span class="text-[10px] font-mono border border-surface-700 bg-surface-800 px-2 py-0.5 rounded text-neutral-400">החזקת כדור ושליטה</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-300">אחוז הזמן שהכדור ברגלי הקבוצה. הניתוח מחלק את הליגה לטופ-3 (המחזיקות מעל 56%) מול יתר 9 הקבוצות כדי לאפיין סגנון יוזם מול מתפרץ.</p>
        </div>
      </div>
    </section>

    <!-- 3. Defense & Goalkeeping -->
    <section class="space-y-3.5 pt-4 border-t border-surface-700/80">
      <h2 class="font-serif text-xl font-bold text-white flex items-center gap-2">
        <span>🛡️</span>
        <span>3. הגנה, חילוצים ועבודת שוערת</span>
      </h2>
      <div class="space-y-2.5">
        <div class="p-3.5 bg-surface-850 rounded-lg border border-surface-700/80 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-brand-400">GA / GA per 90 (Goals Against)</span>
            <span class="text-[10px] font-mono border border-surface-700 bg-surface-800 px-2 py-0.5 rounded text-neutral-400">ספיגת שערים</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-300">כמות השערים שספגה הקבוצה מסך משחקיה, וממוצע הספיגה ל-90 דקות.</p>
        </div>

        <div class="p-3.5 bg-surface-850 rounded-lg border border-surface-700/80 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-brand-400">SoTA per 90 (Shots on Target Against)</span>
            <span class="text-[10px] font-mono border border-surface-700 bg-surface-800 px-2 py-0.5 rounded text-neutral-400">חשיפה לאיומים</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-300">כמה בעיטות למסגרת מגיעות לעבר שער הקבוצה בכל 90 דקות. מודד את איכות קו ההגנה במניעת איומים מסוכנים.</p>
        </div>

        <div class="p-3.5 bg-surface-850 rounded-lg border border-surface-700/80 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-brand-400">Save% (Save Percentage)</span>
            <span class="text-[10px] font-mono border border-surface-700 bg-surface-800 px-2 py-0.5 rounded text-neutral-400">אחוז הצלות שוערת</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-300">היחס בין בעיטות שנבלמו על ידי השוערת לסך הבעיטות למסגרת. מבודד את ביצועי עמדת השוערת מאיכות חוליית ההגנה שעומדת לפניה.</p>
        </div>

        <div class="p-3.5 bg-surface-850 rounded-lg border border-surface-700/80 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-brand-400">TklW + Int (Tackles Won + Interceptions)</span>
            <span class="text-[10px] font-mono border border-surface-700 bg-surface-800 px-2 py-0.5 rounded text-neutral-400">אגרסיביות וחילוצים</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-300">מדד מצטבר של תיקולים מוצלחים וחטיפות כדור. ממחיש את רמת הלחץ והאינטנסיביות ההגנתית של שחקניות השדה.</p>
        </div>
      </div>
    </section>

    <!-- 4. Macro & Goal Difference -->
    <section class="space-y-3.5 pt-4 border-t border-surface-700/80">
      <h2 class="font-serif text-xl font-bold text-white flex items-center gap-2">
        <span>⚖️</span>
        <span>4. מדדי מאקרו ויחסי כוחות</span>
      </h2>
      <div class="p-3.5 bg-surface-850 rounded-lg border border-surface-700/80 space-y-1">
        <div class="flex items-center justify-between">
          <span class="font-mono text-xs font-bold text-brand-400">GD (Goal Difference)</span>
          <span class="text-[10px] font-mono border border-surface-700 bg-surface-800 px-2 py-0.5 rounded text-neutral-400">הפרש שערים</span>
        </div>
        <p class="text-xs sm:text-sm text-neutral-300">הפער בין סך השערים שנכבשו לסך השערים שנספגו. מדד העוגן שמסביר לאורך זמן את מיקום הקבוצה בטבלה ואת הבסיס לחיזוי נקודות עתידי.</p>
      </div>
    </section>

    <!-- 5. Mathematical Expectations & Over/Under Benchmarks -->
    <section class="space-y-4 pt-4 border-t border-surface-700/80">
      <h2 class="font-serif text-xl font-bold text-white flex items-center gap-2">
        <span>📐</span>
        <span>5. מודל חישוב הציפיות (Baseline Benchmarks) והערכת ביצועים</span>
      </h2>
      <p class="text-xs sm:text-sm text-neutral-300">
        כדי לקבוע האם קבוצה עמדה ב-<strong>Overperformance</strong> (ביצוע עודף) או <strong>Underperformance</strong> (ביצוע חסר), פיתחנו מודל בנצ'מרק גנרי שמחשב מה הקבוצה הייתה "אמורה" להפיק מתוך הנתונים שלה ביחס לממוצע הליגה:
      </p>

      <div class="space-y-3">
        <div class="p-4 bg-surface-850 rounded-lg border border-surface-700/80 space-y-1.5">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-brand-400">1. ספיגה צפויה (Expected GA) מתוך איומי היריבה</span>
            <span class="text-[10px] font-mono border border-surface-700 bg-surface-800 px-2 py-0.5 rounded text-neutral-400">שוערות והגנה</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-200">
            <strong>הנוסחה:</strong> <code class="font-mono text-xs text-brand-400 bg-surface-800 px-1.5 py-0.5 rounded border border-surface-700">xGA = SoTA × (1 - ממוצע הצלות הליגה)</code>
          </p>
          <p class="text-xs text-neutral-400">
            ממוצע הליגה עומד על כ-65.5% הצלות. הכפלת כמות הבעיטות למסגרת שספגה הקבוצה (SoTA) באחוז הספיגה הליגתי הממוצע (34.5%) מבודדת את תפקוד השוערת: האם ספגה יותר או פחות ממה ששוערת ממוצעת הייתה סופגת מאותם איומים בדיוק.
          </p>
        </div>

        <div class="p-4 bg-surface-850 rounded-lg border border-surface-700/80 space-y-1.5">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-brand-400">2. הבקעה צפויה (Expected GF) מתוך בעיטות למסגרת</span>
            <span class="text-[10px] font-mono border border-surface-700 bg-surface-800 px-2 py-0.5 rounded text-neutral-400">התקפה וסיומת</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-200">
            <strong>הנוסחה:</strong> <code class="font-mono text-xs text-brand-400 bg-surface-800 px-1.5 py-0.5 rounded border border-surface-700">xGF = SoT × יחס שערים לבעיטה למסגרת בליגה</code>
          </p>
          <p class="text-xs text-neutral-400">
            יחס ההמרה הליגתי עומד על כ-0.315 שערים לכל בעיטה למסגרת. חישוב זה מודד האם חדות הסיומת של שחקניות ההתקפה הניבה יותר שערים ממה שנפח הבעיטות למסגרת אמור לספק.
          </p>
        </div>

        <div class="p-4 bg-surface-850 rounded-lg border border-surface-700/80 space-y-1.5">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-brand-400">3. בישולים צפויים (Expected Assists)</span>
            <span class="text-[10px] font-mono border border-surface-700 bg-surface-800 px-2 py-0.5 rounded text-neutral-400">יצירתיות ושיתוף</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-200">
            <strong>הנוסחה:</strong> <code class="font-mono text-xs text-brand-400 bg-surface-800 px-1.5 py-0.5 rounded border border-surface-700">xAst = GF × יחס בישולים לשערים בליגה</code>
          </p>
          <p class="text-xs text-neutral-400">
            בליגה, כ-73% מהשערים מובקעים לאחר בישול ישיר. המדד בודק האם השערים של הקבוצה נבעו ממהלכים קבוצתיים מתוכננים ומסירות מפתח, או מטעויות יריב ומהלכים אישיים מבודדים.
          </p>
        </div>

        <div class="p-4 bg-surface-850 rounded-lg border border-surface-700/80 space-y-1.5">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-brand-400">4. נקודות צפויות (xPTS) מרגרסיה ליניארית של הפרש שערים</span>
            <span class="text-[10px] font-mono border border-surface-700 bg-surface-800 px-2 py-0.5 rounded text-neutral-400">מאקרו ויעילות טבלה</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-200">
            <strong>הנוסחה:</strong> <code class="font-mono text-xs text-brand-400 bg-surface-800 px-1.5 py-0.5 rounded border border-surface-700">xPTS = 0.576 × GD + 31.0</code> (משוואת קו המגמה הליגתי)
          </p>
          <p class="text-xs text-neutral-400">
            מכיוון שהפרש שערים יכול להיות שלילי (בניגוד לנקודות), הרגרסיה הליניארית מודדת את תוחלת הנקודות שכל שער בהפרש השערים מייצר בעונת 22 משחקים. פער חיובי (Pts > xPTS) ממחיש יכולת "סחיטת נקודות" וניצחונות צמודים.
          </p>
        </div>
      </div>
    </section>

    <!-- Navigation links -->
    <div class="pt-4 border-t border-surface-700/80 flex flex-wrap justify-between items-center text-xs text-neutral-400 gap-4">
      <a href="{{ '/methodology/' | relative_url }}" class="hover:text-white font-medium flex items-center gap-1">
        → חזרה למתודולוגיה ושאלות המחקר
      </a>
      <a href="{{ '/' | relative_url }}" class="text-neutral-300 hover:text-white font-medium flex items-center gap-1">
        לטבלת הליגה והקבוצות ←
      </a>
    </div>

  </div>

</div>
