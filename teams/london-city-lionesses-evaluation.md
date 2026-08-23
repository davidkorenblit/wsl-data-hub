---
layout: team
title: "London City Lionesses - שלב ביניים: ביצועים מול ציפיות"
team_name: "London City Lionesses"
team_slug: "london-city-lionesses"
team_meta: "WSL 2025/26 · שלב ביניים: מודל הערכת ביצועים"
permalink: /teams/london-city-lionesses/evaluation/
prev_url: /teams/london-city-lionesses/analysis/
prev_title: "חלק ב': ניתוח נתונים"
---

<div class="space-y-6 text-neutral-800 dark:text-neutral-200 leading-relaxed text-base sm:text-lg font-sans">

  <!-- Header -->
  <div class="border-b border-neutral-200 dark:border-neutral-800 pb-3">
    <div class="text-xs font-mono uppercase text-neutral-500 dark:text-neutral-400 font-bold tracking-wider mb-1">
      שלב ביניים: מודל הערכת ביצועים
    </div>
    <h1 class="text-2xl md:text-3xl font-bold tracking-tight text-neutral-900 dark:text-white mb-1">
      בפועל מול על הנייר: תמונת ה-Over / Under Performance של LCL
    </h1>
    <p class="text-xs sm:text-sm text-neutral-500 dark:text-neutral-400 font-sans">
      השוואה מתמטית בין הביצועים בפועל של הקבוצה לבין הבנצ'מרק הליגתי הצפוי מתוך הנתונים.
    </p>
  </div>

  <!-- Chart 1: Performance Deltas -->
  <div class="rounded-md border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-[#121215] p-4 sm:p-5 space-y-3">
    <div class="flex items-center justify-between">
      <h2 class="text-lg font-bold text-neutral-900 dark:text-white">
        1. מפת הפערים מול הציפיות (Performance Deltas)
      </h2>
      <span class="text-[10px] font-mono border border-neutral-200 dark:border-neutral-700 bg-neutral-50 dark:bg-neutral-800 px-2 py-0.5 rounded text-neutral-600 dark:text-neutral-300">
        DELTA vs BASELINE
      </span>
    </div>

    <div class="rounded border border-neutral-200 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-900 flex justify-center p-2">
      <img src="{{ '/assets/images/evaluations/lcl_performance_deltas.png' | relative_url }}" 
           alt="London City Lionesses Performance Deltas Chart" 
           class="w-full max-w-3xl h-auto rounded">
    </div>
  </div>

  <!-- Chart 2: Goalkeeping Comparison -->
  <div class="rounded-md border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-[#121215] p-4 sm:p-5 space-y-3">
    <div class="flex items-center justify-between">
      <h2 class="text-lg font-bold text-neutral-900 dark:text-white">
        2. תמונת השוערות בליגה (ניתוח ביצועי אלנה מול ה-WSL)
      </h2>
      <span class="text-[10px] font-mono border border-neutral-200 dark:border-neutral-700 bg-neutral-50 dark:bg-neutral-800 px-2 py-0.5 rounded text-neutral-600 dark:text-neutral-300">
        GOALKEEPING RANKINGS
      </span>
    </div>

    <div class="rounded border border-neutral-200 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-900 flex justify-center p-2">
      <img src="{{ '/assets/images/evaluations/lcl_goalkeeper_evaluation.png' | relative_url }}" 
           alt="WSL Goalkeeping Rankings and Elena Comparison Chart" 
           class="w-full max-w-3xl h-auto rounded">
    </div>
  </div>

  <!-- User Conclusion Card -->
  <div class="rounded-md border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-[#121215] p-6 space-y-4">
    <div class="flex items-center gap-2 text-primary-600 dark:text-primary-400 font-bold text-sm uppercase tracking-wider">
      <span class="w-2 h-2 rounded-full bg-primary-500"></span>
      סיכום והערכת ביצועים
    </div>
    
    <div class="text-neutral-800 dark:text-neutral-200 text-sm sm:text-base leading-relaxed space-y-3">
      <p>
        הגרפים למעלה, המספרים קודם, ובמידה מסוימת גם ההשקעה בחלון העברות מספרות לנו במידה רבה גם את הסיפור של העונה הקודמת.
      </p>
      <p>
        LCL ספגה יותר ממה שהיא הייתה "אמורה" לספוג, והצצה לנתונים של אלנה מספרת שהיא השוערת הכי גרועה בליגה בחלק מהקטוגריות (יחד עם השוערות של לסטר שירדה ווסטהאם) - וזה כבר ספויילר לשאלת האם מארי ארפס היא רכש טוב.
      </p>
      <p>
        גם נתוני ההתקפה של הקבוצה לא מזהירים אבל גם לא מחרידים. Under performance במה שקשור בכיבוש שערים ובבישול שלהם, בשאר המדדים שדיברנו עליהם (הגנה ותיקולים) עדיין לא יודע כי לא בדקתי.
      </p>
    </div>
  </div>

  <!-- Standardized Post Pagination -->
  {% include post_pagination.html %}

</div>
