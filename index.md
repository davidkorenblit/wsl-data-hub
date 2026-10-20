---
layout: default
title: "WSL Data Hub | טבלת הליגה 2026/27"
description: "ניתוחי כדורגל נשים מבוססי דאטא – WSL עונת 2026/27"
lang: he
alt_url: /en/
---

<!-- Page Title & Section Header -->
<div class="mb-6">
  <div class="text-xs font-mono uppercase text-neutral-500 dark:text-neutral-400 font-bold tracking-wider mb-1">
    WSL 2026/27 · STANDINGS
  </div>
  <h1 class="text-2xl md:text-3xl font-bold tracking-tight text-neutral-900 dark:text-white mb-2">
    טבלת הליגה
  </h1>
  <p class="text-xs sm:text-sm text-neutral-500 dark:text-neutral-400 font-sans">
    לחצו על שם מועדון לצפייה בסגל, מדדי ביצוע ומחקרי עומק.
  </p>
</div>

<!-- Matchweek Results Widget (משבצת תוצאות מחזור אחרון) -->
<section class="mb-8" dir="rtl">
  <!-- Widget Header -->
  <div class="flex flex-wrap items-center justify-between gap-3 mb-3">
    <div class="flex items-center gap-2">
      <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-mono font-semibold bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20">
        <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
        <span>מחזור {{ site.data.wsl_recent_results.first.round }} · תוצאות סיום</span>
      </span>
      <span class="text-xs text-neutral-500 dark:text-neutral-400 font-mono hidden sm:inline">
        (7 משחקים)
      </span>
    </div>

    <!-- Controls -->
    <div class="flex items-center gap-2 text-xs font-mono">
      <button id="toggle-match-details" type="button" class="px-2.5 py-1 rounded border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-[#121215] text-neutral-700 dark:text-neutral-300 hover:border-neutral-300 dark:hover:border-neutral-700 hover:text-neutral-950 dark:hover:text-white transition-all flex items-center gap-1.5 shadow-sm">
        <span id="toggle-details-icon">📊</span>
        <span id="toggle-details-text">הצג פירוט xG ומבקיעות</span>
      </button>
      <a href="{{ '/weekly/' | relative_url }}" class="hidden sm:inline-flex items-center gap-1 text-neutral-500 hover:text-neutral-900 dark:text-neutral-400 dark:hover:text-white transition-colors">
        <span>לטור השבועי ←</span>
      </a>
    </div>
  </div>

  <!-- Match Cards Grid -->
  <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-3">
    {% for match in site.data.wsl_recent_results %}
    {% assign is_home_win = (match.winner == 'home') %}
    {% assign is_away_win = (match.winner == 'away') %}
    <div class="rounded-lg border {% if match.is_lcl %}border-pink-500/40 dark:border-pink-500/30 bg-gradient-to-b from-pink-500/[0.03] to-transparent shadow-sm{% else %}border-neutral-200 dark:border-neutral-800 bg-white dark:bg-[#121215]{% endif %} p-3.5 hover:border-neutral-300 dark:hover:border-neutral-700 hover:shadow-md transition-all duration-200 flex flex-col justify-between group">
      
      <!-- Card Top: Date & FT Badge -->
      <div class="flex items-center justify-between text-[11px] font-mono text-neutral-400 dark:text-neutral-500 pb-2 mb-2 border-b border-neutral-100 dark:border-neutral-800/80">
        <span class="truncate">{{ match.date_formatted_he }}</span>
        <div class="flex items-center gap-1.5">
          {% if match.is_lcl %}
          <span class="text-[10px] font-bold text-pink-600 dark:text-pink-400 bg-pink-50 dark:bg-pink-950/40 px-1.5 py-0.2 rounded border border-pink-200 dark:border-pink-800/50">LCL</span>
          {% endif %}
          <span class="font-bold text-neutral-600 dark:text-neutral-400 bg-neutral-100 dark:bg-neutral-800/60 px-1.5 py-0.2 rounded text-[10px]">FT</span>
        </div>
      </div>

      <!-- Teams & Score Container -->
      <div class="space-y-2 mb-2">
        <!-- Home Team -->
        <div class="flex items-center justify-between gap-2">
          <div class="flex items-center gap-2 min-w-0">
            <img src="{{ match.home_crest }}" alt="{{ match.home_name }}" class="w-5 h-5 object-contain flex-shrink-0" loading="lazy" onerror="this.style.display='none'">
            <a href="{{ '/teams/' | append: match.home_slug | relative_url }}" class="text-sm truncate hover:underline {% if is_home_win %}font-bold text-neutral-900 dark:text-white{% else %}font-medium text-neutral-600 dark:text-neutral-300{% endif %}">
              {{ match.home_name_he }}
            </a>
          </div>
          <span class="font-mono text-base tabular-nums {% if is_home_win %}font-bold text-neutral-950 dark:text-white{% else %}text-neutral-500 dark:text-neutral-400{% endif %}">
            {{ match.home_score }}
          </span>
        </div>

        <!-- Away Team -->
        <div class="flex items-center justify-between gap-2">
          <div class="flex items-center gap-2 min-w-0">
            <img src="{{ match.away_crest }}" alt="{{ match.away_name }}" class="w-5 h-5 object-contain flex-shrink-0" loading="lazy" onerror="this.style.display='none'">
            <a href="{{ '/teams/' | append: match.away_slug | relative_url }}" class="text-sm truncate hover:underline {% if is_away_win %}font-bold text-neutral-900 dark:text-white{% else %}font-medium text-neutral-600 dark:text-neutral-300{% endif %}">
              {{ match.away_name_he }}
            </a>
          </div>
          <span class="font-mono text-base tabular-nums {% if is_away_win %}font-bold text-neutral-950 dark:text-white{% else %}text-neutral-500 dark:text-neutral-400{% endif %}">
            {{ match.away_score }}
          </span>
        </div>
      </div>

      <!-- Expandable Deep Stats Section (xG & Scorers) -->
      {% if match.has_deep_stats %}
      <div class="match-detail-drawer hidden pt-2.5 mt-auto border-t border-dashed border-neutral-200 dark:border-neutral-800/80 text-[11px] font-mono transition-all">
        
        <!-- xG Comparison -->
        {% if match.home_xg and match.away_xg %}
        <div class="mb-2">
          <div class="flex items-center justify-between text-[10px] text-neutral-400 dark:text-neutral-500 mb-1">
            <span>xG: {{ match.home_xg }}</span>
            <span class="text-neutral-400">איומים</span>
            <span>xG: {{ match.away_xg }}</span>
          </div>
          <div class="w-full h-1 bg-neutral-100 dark:bg-neutral-800 rounded-full overflow-hidden flex">
            <div style="width: {{ match.home_xg | times: 100 | divided_by: 4.0 | at_most: 85 | at_least: 15 }}%; background-color: {{ match.home_color }};" class="h-full"></div>
            <div class="flex-1 bg-transparent"></div>
            <div style="width: {{ match.away_xg | times: 100 | divided_by: 4.0 | at_most: 85 | at_least: 15 }}%; background-color: {{ match.away_color }};" class="h-full"></div>
          </div>
        </div>
        {% endif %}

        <!-- Goalscorers -->
        {% if match.home_scorers.size > 0 or match.away_scorers.size > 0 %}
        <div class="space-y-1 text-[11px] text-neutral-600 dark:text-neutral-300 pt-1">
          {% for g in match.home_scorers %}
          <div class="flex items-center gap-1.5 text-neutral-700 dark:text-neutral-300 truncate">
            <span class="text-[9px]">⚽</span>
            <span class="font-medium truncate">{{ g.name }}</span>
            <span class="text-neutral-400 text-[10px]">({{ g.minute }})</span>
          </div>
          {% endfor %}
          {% for g in match.away_scorers %}
          <div class="flex items-center gap-1.5 text-neutral-500 dark:text-neutral-400 truncate">
            <span class="text-[9px]">⚽</span>
            <span class="font-medium truncate">{{ g.name }}</span>
            <span class="text-neutral-400 text-[10px]">({{ g.minute }})</span>
          </div>
          {% endfor %}
        </div>
        {% endif %}
      </div>
      {% endif %}

    </div>
    {% endfor %}
  </div>
</section>

<!-- Script for Interactive Details Drawer -->
<script>
  document.getElementById('toggle-match-details')?.addEventListener('click', function() {
    const drawers = document.querySelectorAll('.match-detail-drawer');
    const textSpan = document.getElementById('toggle-details-text');
    let isCurrentlyHidden = false;
    
    drawers.forEach(el => {
      if (el.classList.contains('hidden')) {
        isCurrentlyHidden = true;
        el.classList.remove('hidden');
      } else {
        el.classList.add('hidden');
      }
    });
    
    if (textSpan) {
      textSpan.textContent = isCurrentlyHidden ? 'הסתר פירוט xG ומבקיעות' : 'הצג פירוט xG ומבקיעות';
    }
  });
</script>

<!-- Strict Clean Editorial League Table Container -->
<div class="overflow-x-auto rounded-md border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-[#121215] mb-8" dir="ltr">
  <table class="w-full text-left border-collapse">
    <thead>
      <tr>
        <th class="text-xs uppercase font-mono font-medium text-neutral-400 dark:text-neutral-500 bg-neutral-50 dark:bg-[#18181b] py-2.5 px-3 border-b border-neutral-200 dark:border-neutral-800 text-left w-10">#</th>
        <th class="text-xs uppercase font-mono font-medium text-neutral-400 dark:text-neutral-500 bg-neutral-50 dark:bg-[#18181b] py-2.5 px-3 border-b border-neutral-200 dark:border-neutral-800 text-left">Club</th>
        <th class="text-xs uppercase font-mono font-medium text-neutral-400 dark:text-neutral-500 bg-neutral-50 dark:bg-[#18181b] py-2.5 px-3 border-b border-neutral-200 dark:border-neutral-800 text-right">MP</th>
        <th class="text-xs uppercase font-mono font-medium text-neutral-400 dark:text-neutral-500 bg-neutral-50 dark:bg-[#18181b] py-2.5 px-3 border-b border-neutral-200 dark:border-neutral-800 text-right">W</th>
        <th class="text-xs uppercase font-mono font-medium text-neutral-400 dark:text-neutral-500 bg-neutral-50 dark:bg-[#18181b] py-2.5 px-3 border-b border-neutral-200 dark:border-neutral-800 text-right">D</th>
        <th class="text-xs uppercase font-mono font-medium text-neutral-400 dark:text-neutral-500 bg-neutral-50 dark:bg-[#18181b] py-2.5 px-3 border-b border-neutral-200 dark:border-neutral-800 text-right">L</th>
        <th class="text-xs uppercase font-mono font-medium text-neutral-400 dark:text-neutral-500 bg-neutral-50 dark:bg-[#18181b] py-2.5 px-3 border-b border-neutral-200 dark:border-neutral-800 text-right">GF</th>
        <th class="text-xs uppercase font-mono font-medium text-neutral-400 dark:text-neutral-500 bg-neutral-50 dark:bg-[#18181b] py-2.5 px-3 border-b border-neutral-200 dark:border-neutral-800 text-right">GA</th>
        <th class="text-xs uppercase font-mono font-medium text-neutral-400 dark:text-neutral-500 bg-neutral-50 dark:bg-[#18181b] py-2.5 px-3 border-b border-neutral-200 dark:border-neutral-800 text-right">GD</th>
        <th class="text-xs uppercase font-mono font-bold text-neutral-700 dark:text-neutral-200 bg-neutral-100/70 dark:bg-[#1c1c22] py-2.5 px-3 border-b border-neutral-200 dark:border-neutral-800 text-right w-14">PTS</th>
      </tr>
    </thead>
    <tbody>
      {% assign teams = site.data.league_table %}
      {% for team in teams %}
      {% assign is_lcl = (team.slug == 'london-city-lionesses') %}
      <tr class="hover:bg-neutral-50 dark:hover:bg-[#18181c] {% if is_lcl %}bg-neutral-50/60 dark:bg-[#18181b]/60 font-medium{% endif %}">
        
        <!-- Rank -->
        <td class="text-xs font-mono text-neutral-400 dark:text-neutral-500 py-2 px-3 border-b border-neutral-100 dark:border-neutral-800 text-left">
          {{ team.rk }}
        </td>
        
        <!-- Team Name -->
        <td class="text-sm font-sans font-medium text-neutral-900 dark:text-white py-2 px-3 border-b border-neutral-100 dark:border-neutral-800 text-left">
          <a href="{{ '/teams/' | append: team.slug | relative_url }}" class="hover:underline hover:text-neutral-950 dark:hover:text-neutral-200 flex items-center gap-2">
            {% if is_lcl %}
            <span class="w-1.5 h-1.5 rounded-full bg-neutral-900 dark:bg-white"></span>
            {% endif %}
            <span>{{ team.squad }}</span>
          </a>
        </td>
        
        <!-- Numeric Columns (Strictly Right Aligned, Monospace) -->
        <td class="text-sm font-mono tabular-nums text-neutral-500 dark:text-neutral-400 py-2 px-3 border-b border-neutral-100 dark:border-neutral-800 text-right">{{ team.mp }}</td>
        <td class="text-sm font-mono tabular-nums text-neutral-800 dark:text-neutral-200 py-2 px-3 border-b border-neutral-100 dark:border-neutral-800 text-right">{{ team.w }}</td>
        <td class="text-sm font-mono tabular-nums text-neutral-500 dark:text-neutral-400 py-2 px-3 border-b border-neutral-100 dark:border-neutral-800 text-right">{{ team.d }}</td>
        <td class="text-sm font-mono tabular-nums text-neutral-500 dark:text-neutral-400 py-2 px-3 border-b border-neutral-100 dark:border-neutral-800 text-right">{{ team.l }}</td>
        <td class="text-sm font-mono tabular-nums text-neutral-800 dark:text-neutral-200 py-2 px-3 border-b border-neutral-100 dark:border-neutral-800 text-right">{{ team.gf }}</td>
        <td class="text-sm font-mono tabular-nums text-neutral-500 dark:text-neutral-400 py-2 px-3 border-b border-neutral-100 dark:border-neutral-800 text-right">{{ team.ga }}</td>
        <td class="text-sm font-mono tabular-nums text-neutral-800 dark:text-neutral-200 py-2 px-3 border-b border-neutral-100 dark:border-neutral-800 text-right">
          {% if team.gd > 0 %}+{% endif %}{{ team.gd }}
        </td>
        <td class="text-sm font-mono tabular-nums font-bold text-neutral-950 dark:text-white py-2 px-3 border-b border-neutral-100 dark:border-neutral-800 text-right bg-neutral-50/50 dark:bg-[#18181b]/50">
          {{ team.pts }}
        </td>

      </tr>
      {% endfor %}
    </tbody>
  </table>
</div>

<!-- Strict Clean Editorial Cards -->
<div class="grid md:grid-cols-2 gap-4" dir="rtl">
  <div class="rounded-md border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-[#121215] p-5">
    <div class="text-xs font-mono uppercase text-neutral-500 dark:text-neutral-400 font-bold tracking-wider mb-2">
      מתודולוגיה ומודלים
    </div>
    <h3 class="text-lg font-bold text-neutral-900 dark:text-white mb-2">מודלים וניתוחי עומק</h3>
    <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300 leading-relaxed mb-3">
      מדדי xG, פעולות יצירת בעיטה (SCA), איכות מסירות וזמני משחק מ-FBref לניתוח ביצועי הקבוצות והשחקניות.
    </p>
    <a href="{{ '/methodology/' | relative_url }}" class="text-xs font-mono font-medium text-neutral-900 dark:text-neutral-100 hover:underline">
      מתודולוגיית הניתוח ←
    </a>
  </div>

  <div class="rounded-md border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-[#121215] p-5">
    <div class="text-xs font-mono uppercase text-neutral-500 dark:text-neutral-400 font-bold tracking-wider mb-2">
      הטור השבועי
    </div>
    <h3 class="text-lg font-bold text-neutral-900 dark:text-white mb-2">סיכומי מחזור וטורי דעה</h3>
    <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300 leading-relaxed mb-3">
      נבחן עבור חלק מהקבוצות את התיאוריות שדיברנו עליהן, נלמד להכיר את הקבוצות החדשות ועוד.
    </p>
    <a href="{{ '/weekly/' | relative_url }}" class="text-xs font-mono font-medium text-neutral-900 dark:text-neutral-100 hover:underline">
      מעבר לטור השבועי ←
    </a>
  </div>
</div>
