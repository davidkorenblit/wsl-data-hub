---
layout: team
title: "London City Lionesses - שלב ביניים: ביצועים מול ציפיות"
team_name: "London City Lionesses"
team_slug: "london-city-lionesses"
team_meta: "WSL 2025/26 · שלב ביניים: מודל הערכת ביצועים"
hide_sidebar: true
permalink: /teams/london-city-lionesses/evaluation/
prev_url: /teams/london-city-lionesses/analysis/
prev_title: "חלק ב': ניתוח נתונים"
next_url: /teams/london-city-lionesses/transfers-intro/
next_title: "חלק ג': חלון ההעברות והרכש"
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

  <!-- Chart 1: Performance Deltas (Pure Responsive Vector Lollipop Component) -->
  <div class="rounded-md border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-[#121215] p-4 sm:p-5 space-y-4">
    <div class="flex items-center justify-between border-b border-neutral-100 dark:border-neutral-800 pb-3">
      <div>
        <h2 class="text-lg font-bold text-neutral-900 dark:text-white">
          1. מפת הפערים מול הציפיות (Performance Deltas)
        </h2>
        <p class="text-xs text-neutral-500 dark:text-neutral-400 mt-0.5">
          סטיית LCL מקו האפס (הבנצ'מרק הליגתי הצפוי)
        </p>
      </div>
      <span class="text-[10px] font-mono border border-neutral-200 dark:border-neutral-700 bg-neutral-50 dark:bg-neutral-800 px-2 py-0.5 rounded text-neutral-600 dark:text-neutral-300">
        DELTA vs BASELINE
      </span>
    </div>

    <!-- Pure CSS/HTML Vector Lollipop Dashboard -->
    <div class="bg-[#0b1329] border border-[#1e293b] rounded-lg p-4 sm:p-6 text-white font-sans space-y-5" dir="ltr">
      <div class="text-center pb-2 border-b border-[#1e293b]/60">
        <h3 class="text-sm sm:text-base font-bold text-slate-100">London City Lionesses · Performance vs Expected Baseline</h3>
        <p class="text-[11px] text-slate-400 font-mono">Deviation in points, goals, assists and conceded goals</p>
      </div>

      <!-- 4 Metric Rows with Strict Zero Centerline -->
      <div class="space-y-4">
        
        <!-- Row 1: Points -->
        <div class="space-y-1">
          <div class="flex justify-between text-xs font-medium">
            <span class="text-slate-200 font-semibold">Points (xPTS) <span class="text-slate-400 font-normal text-[11px]">· Winning close games</span></span>
            <span class="font-mono font-bold text-emerald-400 text-xs sm:text-sm">+1.2 Pts (Overperformed)</span>
          </div>
          <div class="relative h-7 bg-[#131f3d] rounded flex items-center px-1 overflow-hidden">
            <div class="absolute left-1/2 top-0 bottom-0 w-0.5 bg-slate-400 z-10"></div>
            <!-- Lollipop Line & Head -->
            <div class="absolute left-1/2 h-1 bg-emerald-500 rounded-r z-0 flex items-center" style="width: 14%;">
              <div class="absolute -right-2 w-4 h-4 rounded-full bg-emerald-400 ring-2 ring-[#0b1329] shadow"></div>
            </div>
          </div>
        </div>

        <!-- Row 2: Goals Scored -->
        <div class="space-y-1">
          <div class="flex justify-between text-xs font-medium">
            <span class="text-slate-200 font-semibold">Goals Scored (GF) <span class="text-slate-400 font-normal text-[11px]">· Finishing vs shot volume</span></span>
            <span class="font-mono font-bold text-rose-400 text-xs sm:text-sm">-3.7 Goals (Underperformed)</span>
          </div>
          <div class="relative h-7 bg-[#131f3d] rounded flex items-center px-1 overflow-hidden">
            <div class="absolute left-1/2 top-0 bottom-0 w-0.5 bg-slate-400 z-10"></div>
            <!-- Lollipop Line & Head -->
            <div class="absolute right-1/2 h-1 bg-rose-500 rounded-l z-0 flex items-center justify-start" style="width: 37%;">
              <div class="absolute -left-2 w-4 h-4 rounded-full bg-rose-400 ring-2 ring-[#0b1329] shadow"></div>
            </div>
          </div>
        </div>

        <!-- Row 3: Assists -->
        <div class="space-y-1">
          <div class="flex justify-between text-xs font-medium">
            <span class="text-slate-200 font-semibold">Assists (Ast) <span class="text-slate-400 font-normal text-[11px]">· Direct chance conversion</span></span>
            <span class="font-mono font-bold text-rose-400 text-xs sm:text-sm">-0.9 Ast (Underperformed)</span>
          </div>
          <div class="relative h-7 bg-[#131f3d] rounded flex items-center px-1 overflow-hidden">
            <div class="absolute left-1/2 top-0 bottom-0 w-0.5 bg-slate-400 z-10"></div>
            <!-- Lollipop Line & Head -->
            <div class="absolute right-1/2 h-1 bg-rose-500 rounded-l z-0 flex items-center justify-start" style="width: 10%;">
              <div class="absolute -left-2 w-4 h-4 rounded-full bg-rose-400 ring-2 ring-[#0b1329] shadow"></div>
            </div>
          </div>
        </div>

        <!-- Row 4: Goals Conceded -->
        <div class="space-y-1">
          <div class="flex justify-between text-xs font-medium">
            <span class="text-slate-200 font-semibold">Goals Conceded (GA) <span class="text-slate-400 font-normal text-[11px]">· Excess goals allowed</span></span>
            <span class="font-mono font-bold text-rose-400 text-xs sm:text-sm">+6.7 GA (Weak Goalkeeping)</span>
          </div>
          <div class="relative h-7 bg-[#131f3d] rounded flex items-center px-1 overflow-hidden">
            <div class="absolute left-1/2 top-0 bottom-0 w-0.5 bg-slate-400 z-10"></div>
            <!-- Lollipop Line & Head -->
            <div class="absolute left-1/2 h-1 bg-rose-500 rounded-r z-0 flex items-center" style="width: 67%;">
              <div class="absolute -right-2 w-4 h-4 rounded-full bg-rose-400 ring-2 ring-[#0b1329] shadow"></div>
            </div>
          </div>
        </div>

        <!-- Row 5: Defensive Work Rate (PAdj) -->
        <div class="space-y-1">
          <div class="flex justify-between text-xs font-medium">
            <span class="text-slate-200 font-semibold">Defensive Work Rate (PAdj Tkl+Int) <span class="text-slate-400 font-normal text-[11px]">· Pressing & ball recovery</span></span>
            <span class="font-mono font-bold text-emerald-400 text-xs sm:text-sm">+70.8 Actions (Overperformed · #1 in WSL)</span>
          </div>
          <div class="relative h-7 bg-[#131f3d] rounded flex items-center px-1 overflow-hidden">
            <div class="absolute left-1/2 top-0 bottom-0 w-0.5 bg-slate-400 z-10"></div>
            <!-- Lollipop Line & Head -->
            <div class="absolute left-1/2 h-1 bg-emerald-500 rounded-r z-0 flex items-center" style="width: 71%;">
              <div class="absolute -right-2 w-4 h-4 rounded-full bg-emerald-400 ring-2 ring-[#0b1329] shadow"></div>
            </div>
          </div>
        </div>

      </div>

      <!-- Axis Labels -->
      <div class="flex justify-between text-[11px] font-mono text-slate-400 border-t border-[#1e293b] pt-2 px-1">
        <span>◀ Underperformed (-10 / Negative)</span>
        <span class="text-slate-200 font-bold">Expected Baseline (0)</span>
        <span>Overperformed (+10 / Positive) ▶</span>
      </div>
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

  <!-- Section 3: Defensive Actions & Work Rate Table -->
  <div class="rounded-md border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-[#121215] p-4 sm:p-5 space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-neutral-100 dark:border-neutral-800 pb-3">
      <div>
        <h2 class="text-lg font-bold text-neutral-900 dark:text-white">
          3. פעולות הגנה ועצימות שדה (תיקולים, חטיפות ונירמול החזקה)
        </h2>
        <p class="text-xs text-neutral-500 dark:text-neutral-400 mt-0.5">
          בדיקת עבודת ההגנה בשדה: נפח תיקולים וחטיפות מנוכה אחוזי החזקה בכדור (PAdj)
        </p>
      </div>
      <span class="text-[10px] font-mono border border-emerald-300 dark:border-emerald-700 bg-emerald-50 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-300 px-2 py-0.5 rounded font-bold self-start sm:self-auto">
        LCL RANK #1 IN LEAGUE
      </span>
    </div>

    <div class="overflow-x-auto rounded border border-neutral-200 dark:border-neutral-800" dir="ltr">
      <table class="w-full text-left border-collapse text-xs">
        <thead>
          <tr class="bg-neutral-50 dark:bg-[#18181b] border-b border-neutral-200 dark:border-neutral-800 text-neutral-500 dark:text-neutral-400 font-mono uppercase tracking-wider">
            <th class="py-2.5 px-3 font-semibold sticky left-0 bg-neutral-50 dark:bg-[#18181b] z-10">Squad</th>
            <th class="py-2.5 px-2 text-right font-semibold">Tackles Won (TklW)</th>
            <th class="py-2.5 px-2 text-right font-semibold">Interceptions (Int)</th>
            <th class="py-2.5 px-2 text-right font-semibold">Total Actions (Tkl+Int)</th>
            <th class="py-2.5 px-2 text-right font-semibold text-emerald-600 dark:text-emerald-400">PAdj Actions (50% Poss)</th>
            <th class="py-2.5 px-3 text-right font-semibold">Delta vs Avg</th>
          </tr>
        </thead>
        <tbody class="font-mono tabular-nums divide-y divide-neutral-100 dark:divide-neutral-800">
          {% assign def_list = site.data.defensive_squad %}
          {% if def_list %}
            {% for row in def_list %}
            {% assign is_lionesses = false %}
            {% if row.squad == 'Lionesses' %}
              {% assign is_lionesses = true %}
            {% endif %}
            <tr class="transition-colors {% if is_lionesses %}bg-emerald-500/10 dark:bg-emerald-500/15 font-bold text-emerald-800 dark:text-emerald-200{% else %}hover:bg-neutral-50 dark:hover:bg-[#18181c] text-neutral-800 dark:text-neutral-200{% endif %}">
              <td class="py-2 px-3 sticky left-0 {% if is_lionesses %}bg-emerald-100 dark:bg-[#0f241a] font-bold text-emerald-800 dark:text-emerald-200{% else %}bg-white dark:bg-[#121215]{% endif %} border-r border-neutral-100 dark:border-neutral-800">
                {{ row.squad }}
                {% if is_lionesses %} <span class="text-[10px] uppercase font-sans font-bold bg-emerald-500/20 text-emerald-700 dark:text-emerald-300 px-1 py-0.5 rounded mr-1">#1 WSL Leader</span>{% endif %}
              </td>
              <td class="py-2 px-2 text-right">{{ row.tackles_tklw }}</td>
              <td class="py-2 px-2 text-right">{{ row.int }}</td>
              <td class="py-2 px-2 text-right font-semibold">{{ row.tkl_plus_int }}</td>
              <td class="py-2 px-2 text-right font-bold {% if is_lionesses %}text-emerald-600 dark:text-emerald-400{% endif %}">
                {% if row.squad == 'Lionesses' %}533.9{% elsif row.squad == 'Chelsea' %}528.8{% elsif row.squad == 'Arsenal' %}481.7{% elsif row.squad == 'Manchester City' %}481.6{% elsif row.squad == 'Manchester Utd' %}480.0{% elsif row.squad == 'Tottenham' %}467.8{% elsif row.squad == 'West Ham' %}456.3{% elsif row.squad == 'Liverpool' %}443.3{% elsif row.squad == 'Brighton' %}430.8{% elsif row.squad == 'Leicester City' %}425.4{% elsif row.squad == 'Aston Villa' %}418.9{% else %}408.8{% endif %}
              </td>
              <td class="py-2 px-3 text-right font-semibold {% if is_lionesses %}text-emerald-600 dark:text-emerald-400{% endif %}">
                {% if row.squad == 'Lionesses' %}+70.8{% elsif row.squad == 'Chelsea' %}+65.7{% elsif row.squad == 'Arsenal' %}+18.6{% elsif row.squad == 'Manchester City' %}+18.5{% elsif row.squad == 'Manchester Utd' %}+16.9{% elsif row.squad == 'Tottenham' %}+4.7{% elsif row.squad == 'West Ham' %}-6.8{% elsif row.squad == 'Liverpool' %}-19.8{% elsif row.squad == 'Brighton' %}-32.3{% elsif row.squad == 'Leicester City' %}-37.7{% elsif row.squad == 'Aston Villa' %}-44.2{% else %}-54.3{% endif %}
              </td>
            </tr>
            {% endfor %}
          {% endif %}
        </tbody>
      </table>
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
        גם נתוני ההתקפה של הקבוצה לא מזהירים אבל גם לא מחרידים. Under performance במה שקשור בכיבוש שערים ובבישול שלהם, אך בכל הנוגע להגנה, לחץ ותיקולים – כשמנרמלים לאחוזי החזקה בכדור מתברר ש-LCL במקום ה-1 בכל הליגה בנפח פעולות הגנה (70.8+ פעולות מעל הממוצע הליגתי). זה מדגיש עוד יותר: שחקניות השדה עבדו ללא הפסקה, והבעיה המרכזית הייתה מה שקרה ברגע שהכדור עבר אותן ונבעט למסגרת השער.
      </p>
      <p>
        אין נוסחה מוסכמת (לפחות אני לא מצאתי) איך לחשב אופי וניסיון של קבוצה. אם יורשה לי להתיימר וזו חתיכת יומרה, המדד שאני אסתכל עליו הוא האם הקבוצה השיגה יותר נקודות ממה שהיא אמורה הייתה להשיג. ואם התשובה היא כן, ובטח כשאין לי כלים לבודד ולהבין מה גרם לזה לקרות, אני נוטה ללכת ולדבר על אופי. ו-LCL הביאה כבר בעונה שעברה אופי ו-character (אין לזה תרגום טוב לעברית) כמו ניקיטה פאריס וג'נה הרננדז שיעזרו לקבוצה צעירה (בגיל ובליגה) לפתח איזושהי זהות ואופי. חלון ההעברות הזה, משפר אותן גם שם.
      </p>
    </div>
  </div>

  <!-- Standardized Post Pagination -->
  {% include post_pagination.html %}

</div>
