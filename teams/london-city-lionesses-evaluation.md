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

  <!-- Chart 2: Goalkeeping Comparison with View Toggle (Chart vs Raw Table) -->
  <div class="rounded-md border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-[#121215] p-4 sm:p-5 space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-neutral-100 dark:border-neutral-800 pb-3">
      <div>
        <h2 class="text-lg font-bold text-neutral-900 dark:text-white">
          2. תמונת השוערות בליגה (ניתוח ביצועי אלנה מול ה-WSL)
        </h2>
        <p class="text-xs text-neutral-500 dark:text-neutral-400 mt-0.5">
          השוואת נתוני ספיגה, בעיטות למסגרת ואחוזי הצלה של כלל שוערות הליגה
        </p>
      </div>

      <!-- View Toggle Buttons -->
      <div class="inline-flex rounded-md p-1 bg-neutral-100 dark:bg-neutral-800 text-xs font-medium self-start sm:self-auto border border-neutral-200 dark:border-neutral-700">
        <button id="btn-gk-chart" onclick="switchGkView('chart')" class="px-3 py-1.5 rounded transition-all bg-white dark:bg-neutral-900 text-neutral-900 dark:text-white shadow-sm font-bold flex items-center gap-1.5">
          <span>📊</span>
          <span>תרשים דירוג</span>
        </button>
        <button id="btn-gk-table" onclick="switchGkView('table')" class="px-3 py-1.5 rounded transition-all text-neutral-600 dark:text-neutral-400 hover:text-neutral-900 dark:hover:text-white flex items-center gap-1.5">
          <span>📋</span>
          <span>טבלת נתונים מלאה</span>
        </button>
      </div>
    </div>

    <!-- View 1: Goalkeeper Chart View -->
    <div id="gk-chart-view" class="rounded border border-neutral-200 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-900 flex justify-center p-2">
      <img src="{{ '/assets/images/evaluations/lcl_goalkeeper_evaluation.png' | relative_url }}" 
           alt="WSL Goalkeeping Rankings and Elena Comparison Chart" 
           class="w-full max-w-3xl h-auto rounded">
    </div>

    <!-- View 2: Raw Goalkeeping Table View -->
    <div id="gk-table-view" class="hidden space-y-2">
      <div class="overflow-x-auto rounded border border-neutral-200 dark:border-neutral-800" dir="ltr">
        <table class="w-full text-left border-collapse text-xs">
          <thead>
            <tr class="bg-neutral-50 dark:bg-[#18181b] border-b border-neutral-200 dark:border-neutral-800 text-neutral-500 dark:text-neutral-400 font-mono uppercase tracking-wider">
              <th class="py-2.5 px-3 font-semibold sticky left-0 bg-neutral-50 dark:bg-[#18181b] z-10">Squad</th>
              <th class="py-2.5 px-2 text-center font-semibold"># Pl</th>
              <th class="py-2.5 px-2 text-center font-semibold">MP</th>
              <th class="py-2.5 px-2 text-center font-semibold">Starts</th>
              <th class="py-2.5 px-2 text-right font-semibold">Min</th>
              <th class="py-2.5 px-2 text-right font-semibold">90s</th>
              <th class="py-2.5 px-2 text-right font-semibold text-rose-600 dark:text-rose-400">GA</th>
              <th class="py-2.5 px-2 text-right font-semibold">GA90</th>
              <th class="py-2.5 px-2 text-right font-semibold">SoTA</th>
              <th class="py-2.5 px-2 text-right font-semibold">Saves</th>
              <th class="py-2.5 px-2 text-right font-semibold text-amber-600 dark:text-amber-400">Save%</th>
              <th class="py-2.5 px-2 text-center font-semibold">W</th>
              <th class="py-2.5 px-2 text-center font-semibold">D</th>
              <th class="py-2.5 px-2 text-center font-semibold">L</th>
              <th class="py-2.5 px-2 text-right font-semibold">CS</th>
              <th class="py-2.5 px-2 text-right font-semibold">CS%</th>
              <th class="py-2.5 px-2 text-right font-semibold">PKatt</th>
              <th class="py-2.5 px-2 text-right font-semibold">PKA</th>
              <th class="py-2.5 px-2 text-right font-semibold">PKsv</th>
              <th class="py-2.5 px-2 text-right font-semibold">PKm</th>
              <th class="py-2.5 px-3 text-right font-semibold">PK Save%</th>
            </tr>
          </thead>
          <tbody class="font-mono tabular-nums divide-y divide-neutral-100 dark:divide-neutral-800">
            {% assign gk_list = site.data.goalkeeping_squad %}
            {% if gk_list %}
              {% for row in gk_list %}
              {% assign is_lionesses = false %}
              {% if row.squad == 'Lionesses' %}
                {% assign is_lionesses = true %}
              {% endif %}
              <tr class="transition-colors {% if is_lionesses %}bg-amber-500/10 dark:bg-amber-500/15 font-bold text-amber-700 dark:text-amber-300{% else %}hover:bg-neutral-50 dark:hover:bg-[#18181c] text-neutral-800 dark:text-neutral-200{% endif %}">
                <td class="py-2 px-3 sticky left-0 {% if is_lionesses %}bg-amber-100 dark:bg-[#251d10] font-bold text-amber-700 dark:text-amber-300{% else %}bg-white dark:bg-[#121215]{% endif %} border-r border-neutral-100 dark:border-neutral-800">
                  {{ row.squad }}
                  {% if is_lionesses %} <span class="text-[10px] uppercase font-sans font-bold bg-amber-500/20 text-amber-700 dark:text-amber-300 px-1 py-0.5 rounded mr-1">Elena / LCL</span>{% endif %}
                </td>
                <td class="py-2 px-2 text-center text-neutral-500">{{ row['#_pl'] }}</td>
                <td class="py-2 px-2 text-center">{{ row.playing_time_mp }}</td>
                <td class="py-2 px-2 text-center">{{ row.playing_time_starts }}</td>
                <td class="py-2 px-2 text-right">{{ row.playing_time_min }}</td>
                <td class="py-2 px-2 text-right">{{ row.playing_time_90s }}</td>
                <td class="py-2 px-2 text-right font-semibold {% if is_lionesses %}text-rose-600 dark:text-rose-400{% endif %}">{{ row.performance_ga }}</td>
                <td class="py-2 px-2 text-right">{{ row.performance_ga90 }}</td>
                <td class="py-2 px-2 text-right">{{ row.performance_sota }}</td>
                <td class="py-2 px-2 text-right">{{ row.performance_saves }}</td>
                <td class="py-2 px-2 text-right font-bold {% if is_lionesses %}text-rose-600 dark:text-rose-400{% else %}text-emerald-600 dark:text-emerald-400{% endif %}">{{ row['performance_save%'] }}%</td>
                <td class="py-2 px-2 text-center">{{ row.performance_w }}</td>
                <td class="py-2 px-2 text-center">{{ row.performance_d }}</td>
                <td class="py-2 px-2 text-center">{{ row.performance_l }}</td>
                <td class="py-2 px-2 text-right">{{ row.performance_cs }}</td>
                <td class="py-2 px-2 text-right">{{ row['performance_cs%'] }}%</td>
                <td class="py-2 px-2 text-right text-neutral-500">{{ row.penalty_kicks_pkatt }}</td>
                <td class="py-2 px-2 text-right text-neutral-500">{{ row.penalty_kicks_pka }}</td>
                <td class="py-2 px-2 text-right text-neutral-500">{{ row.penalty_kicks_pksv }}</td>
                <td class="py-2 px-2 text-right text-neutral-500">{{ row.penalty_kicks_pkm }}</td>
                <td class="py-2 px-3 text-right text-neutral-500">{% if row['penalty_kicks_save%'] %}{{ row['penalty_kicks_save%'] }}%{% else %}-{% endif %}</td>
              </tr>
              {% endfor %}
            {% endif %}
          </tbody>
        </table>
      </div>
      <p class="text-[11px] font-mono text-neutral-400 dark:text-neutral-500 text-left" dir="ltr">
        Source: FBref / Opta WSL 2025/26 Official Goalkeeping Data
      </p>
    </div>
  </div>

  <script>
    function switchGkView(view) {
      const chartView = document.getElementById('gk-chart-view');
      const tableView = document.getElementById('gk-table-view');
      const btnChart = document.getElementById('btn-gk-chart');
      const btnTable = document.getElementById('btn-gk-table');

      if (view === 'chart') {
        chartView.classList.remove('hidden');
        tableView.classList.add('hidden');
        btnChart.className = 'px-3 py-1.5 rounded transition-all bg-white dark:bg-neutral-900 text-neutral-900 dark:text-white shadow-sm font-bold flex items-center gap-1.5';
        btnTable.className = 'px-3 py-1.5 rounded transition-all text-neutral-600 dark:text-neutral-400 hover:text-neutral-900 dark:hover:text-white flex items-center gap-1.5';
      } else {
        chartView.classList.add('hidden');
        tableView.classList.remove('hidden');
        btnTable.className = 'px-3 py-1.5 rounded transition-all bg-white dark:bg-neutral-900 text-neutral-900 dark:text-white shadow-sm font-bold flex items-center gap-1.5';
        btnChart.className = 'px-3 py-1.5 rounded transition-all text-neutral-600 dark:text-neutral-400 hover:text-neutral-900 dark:hover:text-white flex items-center gap-1.5';
      }
    }
  </script>

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
