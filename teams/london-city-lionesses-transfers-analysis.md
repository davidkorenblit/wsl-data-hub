---
layout: team
title: "London City Lionesses - חלק ד': ניתוח שדרוג השוערת (Mary Earps)"
team_name: "London City Lionesses"
team_slug: "london-city-lionesses"
team_meta: "WSL 2025/26 · חלק ד': שדרוג עמדת השוערת"
permalink: /teams/london-city-lionesses/transfers-analysis/
prev_url: /teams/london-city-lionesses/transfers-intro/
prev_title: "חלק ג': חלון ההעברות והרכש"
---

<div class="space-y-6 text-neutral-800 dark:text-neutral-200 leading-relaxed text-base sm:text-lg font-sans">

  <!-- Header -->
  <div class="border-b border-neutral-200 dark:border-neutral-800 pb-3">
    <div class="text-xs font-mono uppercase text-neutral-500 dark:text-neutral-400 font-bold tracking-wider mb-1">
      חלק ד': ניתוח רכש ועמדות
    </div>
    <h1 class="text-2xl md:text-3xl font-bold tracking-tight text-neutral-900 dark:text-white mb-1">
      עמדת השוערת: מארי ארפס (Mary Earps) מול אלנה לטה (Elene Lete)
    </h1>
    <p class="text-xs sm:text-sm text-neutral-500 dark:text-neutral-400 font-sans">
      ניתוח השוואתי מעמיק: עונת 2025/26 מול כלל נתוני הקריירה בליגות המקומיות.
    </p>
  </div>

  <!-- Editorial Narrative Block -->
  <article class="rounded-md border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-[#121215] p-5 sm:p-7 space-y-4 text-neutral-900 dark:text-neutral-100 text-base sm:text-lg leading-relaxed">
    <p>
      אחד הדברים שהכי משמחים אותי כאיש שמאוהב בנתונים זה כאשר הדאטא מיישר קו עם המציאות, או עם הפרשנות שלנו אותה.
    </p>
    <p>
      הרכש של <strong>מארי ארפס (Mary Earps)</strong> היה מתבקש הן מקצועית והן זהותית. הקהל באנגליה מת עליה. האבל כשהיא פרשה מהנבחרת, האהבה שהייתה כלפיה נפגמה רק במעט אחרי הספר שהיא כתבה, ומקצועית היא ממש טובה ומנוסה.
    </p>
    <p>
      ניסיתי לנרמל את המספרים ולא לבחון רק מול עונה שעברה כי פערי הליגות, אבל זה נוקאאוט.
    </p>
    <p class="font-medium text-neutral-900 dark:text-white">
      כבר בסיקור הקודם ראינו כמה עמדת השוערת דרשה חיזוק וכנראה שהגיע החיזוק הכי מתאים שהיה זמין, ולהלן המספרים והגרפים.
    </p>
  </article>

  <!-- Radar / Spider Chart -->
  <div class="rounded-md border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-[#121215] p-4 sm:p-5 space-y-4">
    <div class="flex items-center justify-between border-b border-neutral-100 dark:border-neutral-800 pb-3">
      <div>
        <h2 class="text-lg font-bold text-neutral-900 dark:text-white">
          פרופיל שוערת: גרף רדאר (Radar Chart)
        </h2>
        <p class="text-xs text-neutral-500 dark:text-neutral-400 mt-0.5">
          השוואת ביצועים מנורמלים: מארי ארפס (ירוק) מול אלנה לטה (ורוד/אדום)
        </p>
      </div>
      <span class="text-[10px] font-mono border border-emerald-300 dark:border-emerald-700 bg-emerald-50 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-300 px-2 py-0.5 rounded font-bold">
        RADAR COMPARISON
      </span>
    </div>

    <div class="rounded border border-neutral-200 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-900 flex justify-center p-3">
      <img src="{{ '/assets/images/evaluations/earps_vs_lete_radar.png' | relative_url }}" 
           alt="Mary Earps vs Elene Lete Goalkeeper Radar Chart" 
           class="w-full max-w-xl h-auto rounded">
    </div>
  </div>

  <!-- Head-to-Head Comparison & Raw Data Tables -->
  <div class="rounded-md border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-[#121215] p-4 sm:p-5 space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-neutral-100 dark:border-neutral-800 pb-3">
      <div>
        <h2 class="text-lg font-bold text-neutral-900 dark:text-white">
          השוואת נתונים מלאה: עונת 2025/26 מול כל הקריירה
        </h2>
        <p class="text-xs text-neutral-500 dark:text-neutral-400 mt-0.5">
          השוואה בין עונת השיא בפריז סן ז'רמן / ליון לבין עונת הבכורה של אלנה ב-WSL
        </p>
      </div>

      <!-- Toggle Tabs -->
      <div class="inline-flex rounded-md p-1 bg-neutral-100 dark:bg-neutral-800 text-xs font-medium self-start sm:self-auto border border-neutral-200 dark:border-neutral-700">
        <button id="btn-tab-season" onclick="switchTableTab('season')" class="px-3 py-1.5 rounded transition-all bg-white dark:bg-neutral-900 text-neutral-900 dark:text-white shadow-sm font-bold flex items-center gap-1.5">
          <span>📅 עונת 2025/26</span>
        </button>
        <button id="btn-tab-career" onclick="switchTableTab('career')" class="px-3 py-1.5 rounded transition-all text-neutral-600 dark:text-neutral-400 hover:text-neutral-900 dark:hover:text-white flex items-center gap-1.5">
          <span>🌐 כל הקריירה</span>
        </button>
      </div>
    </div>

    <!-- Table 1: 2025/26 Single Season -->
    <div id="table-season-view" class="space-y-2">
      <div class="overflow-x-auto rounded border border-neutral-200 dark:border-neutral-800" dir="ltr">
        <table class="w-full text-left border-collapse text-xs">
          <thead>
            <tr class="bg-neutral-50 dark:bg-[#18181b] border-b border-neutral-200 dark:border-neutral-800 text-neutral-500 dark:text-neutral-400 font-mono uppercase tracking-wider">
              <th class="py-2.5 px-3 font-semibold sticky left-0 bg-neutral-50 dark:bg-[#18181b] z-10">Player</th>
              <th class="py-2.5 px-2 font-semibold">Squad</th>
              <th class="py-2.5 px-2 text-center font-semibold">MP</th>
              <th class="py-2.5 px-2 text-right font-semibold">Min</th>
              <th class="py-2.5 px-2 text-right font-semibold text-rose-600 dark:text-rose-400">GA</th>
              <th class="py-2.5 px-2 text-right font-semibold">GA90</th>
              <th class="py-2.5 px-2 text-right font-semibold">SoTA</th>
              <th class="py-2.5 px-2 text-right font-semibold">Saves</th>
              <th class="py-2.5 px-2 text-right font-semibold text-emerald-600 dark:text-emerald-400">Save%</th>
              <th class="py-2.5 px-2 text-center font-semibold">W-D-L</th>
              <th class="py-2.5 px-2 text-right font-semibold">CS</th>
              <th class="py-2.5 px-2 text-right font-semibold">CS%</th>
              <th class="py-2.5 px-2 text-right font-semibold">PPM</th>
              <th class="py-2.5 px-3 text-right font-semibold">+/-90</th>
            </tr>
          </thead>
          <tbody class="font-mono tabular-nums divide-y divide-neutral-100 dark:divide-neutral-800">
            {% assign comp_season = site.data.comparisons.gk_lete_vs_earps_2025_26.players %}
            {% for p in comp_season %}
            <tr class="hover:bg-neutral-50 dark:hover:bg-[#18181c] {% if p.player == 'Mary Earps' %}bg-emerald-500/5 font-semibold{% endif %}">
              <td class="py-2 px-3 sticky left-0 {% if p.player == 'Mary Earps' %}bg-emerald-50 dark:bg-[#0f241a] text-emerald-800 dark:text-emerald-300 font-bold{% else %}bg-white dark:bg-[#121215]{% endif %} border-r border-neutral-100 dark:border-neutral-800">
                {{ p.player }}
              </td>
              <td class="py-2 px-2 text-neutral-500">{{ p.squad }}</td>
              <td class="py-2 px-2 text-center">{{ p.mp }}</td>
              <td class="py-2 px-2 text-right">{{ p.min }}</td>
              <td class="py-2 px-2 text-right font-bold {% if p.player == 'Mary Earps' %}text-emerald-600 dark:text-emerald-400{% else %}text-rose-600 dark:text-rose-400{% endif %}">{{ p.ga }}</td>
              <td class="py-2 px-2 text-right font-bold">{{ p.ga90 }}</td>
              <td class="py-2 px-2 text-right">{{ p.sota }}</td>
              <td class="py-2 px-2 text-right">{{ p.saves }}</td>
              <td class="py-2 px-2 text-right font-bold {% if p.player == 'Mary Earps' %}text-emerald-600 dark:text-emerald-400{% else %}text-rose-600 dark:text-rose-400{% endif %}">{{ p.save_pct }}%</td>
              <td class="py-2 px-2 text-center">{{ p.w }}-{{ p.d }}-{{ p.l }}</td>
              <td class="py-2 px-2 text-right font-semibold">{{ p.cs }}</td>
              <td class="py-2 px-2 text-right font-bold {% if p.player == 'Mary Earps' %}text-emerald-600 dark:text-emerald-400{% endif %}">{{ p.cs_pct }}%</td>
              <td class="py-2 px-2 text-right">{{ p.ppm }}</td>
              <td class="py-2 px-3 text-right {% if p.plus_minus_per90 > 0 %}text-emerald-600 dark:text-emerald-400{% else %}text-rose-600 dark:text-rose-400{% endif %}">{% if p.plus_minus_per90 > 0 %}+{% endif %}{{ p.plus_minus_per90 }}</td>
            </tr>
            {% endfor %}
          </tbody>
        </table>
      </div>
    </div>

    <!-- Table 2: Career Domestic Leagues -->
    <div id="table-career-view" class="hidden space-y-2">
      <div class="overflow-x-auto rounded border border-neutral-200 dark:border-neutral-800" dir="ltr">
        <table class="w-full text-left border-collapse text-xs">
          <thead>
            <tr class="bg-neutral-50 dark:bg-[#18181b] border-b border-neutral-200 dark:border-neutral-800 text-neutral-500 dark:text-neutral-400 font-mono uppercase tracking-wider">
              <th class="py-2.5 px-3 font-semibold sticky left-0 bg-neutral-50 dark:bg-[#18181b] z-10">Player</th>
              <th class="py-2.5 px-2 font-semibold">Span</th>
              <th class="py-2.5 px-2 text-center font-semibold">MP</th>
              <th class="py-2.5 px-2 text-right font-semibold">Min</th>
              <th class="py-2.5 px-2 text-right font-semibold text-rose-600 dark:text-rose-400">GA</th>
              <th class="py-2.5 px-2 text-right font-semibold">GA90</th>
              <th class="py-2.5 px-2 text-right font-semibold">SoTA</th>
              <th class="py-2.5 px-2 text-right font-semibold">Saves</th>
              <th class="py-2.5 px-2 text-right font-semibold text-emerald-600 dark:text-emerald-400">Save%</th>
              <th class="py-2.5 px-2 text-center font-semibold">W-D-L</th>
              <th class="py-2.5 px-2 text-right font-semibold">CS</th>
              <th class="py-2.5 px-2 text-right font-semibold">CS%</th>
              <th class="py-2.5 px-2 text-right font-semibold">PPM</th>
              <th class="py-2.5 px-3 text-right font-semibold">+/-90</th>
            </tr>
          </thead>
          <tbody class="font-mono tabular-nums divide-y divide-neutral-100 dark:divide-neutral-800">
            {% assign comp_career = site.data.comparisons.gk_lete_vs_earps.players %}
            {% for p in comp_career %}
            <tr class="hover:bg-neutral-50 dark:hover:bg-[#18181c] {% if p.player == 'Mary Earps' %}bg-emerald-500/5 font-semibold{% endif %}">
              <td class="py-2 px-3 sticky left-0 {% if p.player == 'Mary Earps' %}bg-emerald-50 dark:bg-[#0f241a] text-emerald-800 dark:text-emerald-300 font-bold{% else %}bg-white dark:bg-[#121215]{% endif %} border-r border-neutral-100 dark:border-neutral-800">
                {{ p.player }}
              </td>
              <td class="py-2 px-2 text-neutral-500">{{ p.span }}</td>
              <td class="py-2 px-2 text-center">{{ p.mp }}</td>
              <td class="py-2 px-2 text-right">{{ p.min }}</td>
              <td class="py-2 px-2 text-right font-bold {% if p.player == 'Mary Earps' %}text-emerald-600 dark:text-emerald-400{% else %}text-rose-600 dark:text-rose-400{% endif %}">{{ p.ga }}</td>
              <td class="py-2 px-2 text-right font-bold">{{ p.ga90 }}</td>
              <td class="py-2 px-2 text-right">{{ p.sota }}</td>
              <td class="py-2 px-2 text-right">{{ p.saves }}</td>
              <td class="py-2 px-2 text-right font-bold {% if p.player == 'Mary Earps' %}text-emerald-600 dark:text-emerald-400{% else %}text-rose-600 dark:text-rose-400{% endif %}">{{ p.save_pct }}%</td>
              <td class="py-2 px-2 text-center">{{ p.w }}-{{ p.d }}-{{ p.l }}</td>
              <td class="py-2 px-2 text-right font-semibold">{{ p.cs }}</td>
              <td class="py-2 px-2 text-right font-bold {% if p.player == 'Mary Earps' %}text-emerald-600 dark:text-emerald-400{% endif %}">{{ p.cs_pct }}%</td>
              <td class="py-2 px-2 text-right">{{ p.ppm }}</td>
              <td class="py-2 px-3 text-right {% if p.plus_minus_per90 > 0 %}text-emerald-600 dark:text-emerald-400{% else %}text-rose-600 dark:text-rose-400{% endif %}">{% if p.plus_minus_per90 > 0 %}+{% endif %}{{ p.plus_minus_per90 }}</td>
            </tr>
            {% endfor %}
          </tbody>
        </table>
      </div>
    </div>
    
    <p class="text-[11px] font-mono text-neutral-400 dark:text-neutral-500 text-left" dir="ltr">
      Source: FBref / Stathead Official Domestic League Player Comparison
    </p>
  </div>

  <script>
    function switchTableTab(tab) {
      const seasonView = document.getElementById('table-season-view');
      const careerView = document.getElementById('table-career-view');
      const btnSeason = document.getElementById('btn-tab-season');
      const btnCareer = document.getElementById('btn-tab-career');

      if (tab === 'season') {
        seasonView.classList.remove('hidden');
        careerView.classList.add('hidden');
        btnSeason.className = 'px-3 py-1.5 rounded transition-all bg-white dark:bg-neutral-900 text-neutral-900 dark:text-white shadow-sm font-bold flex items-center gap-1.5';
        btnCareer.className = 'px-3 py-1.5 rounded transition-all text-neutral-600 dark:text-neutral-400 hover:text-neutral-900 dark:hover:text-white flex items-center gap-1.5';
      } else {
        seasonView.classList.add('hidden');
        careerView.classList.remove('hidden');
        btnCareer.className = 'px-3 py-1.5 rounded transition-all bg-white dark:bg-neutral-900 text-neutral-900 dark:text-white shadow-sm font-bold flex items-center gap-1.5';
        btnSeason.className = 'px-3 py-1.5 rounded transition-all text-neutral-600 dark:text-neutral-400 hover:text-neutral-900 dark:hover:text-white flex items-center gap-1.5';
      }
    }
  </script>

  <!-- Standardized Post Pagination -->
  {% include post_pagination.html %}

</div>
