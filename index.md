---
layout: default
title: "WSL Data Hub | טבלת הליגה 2025/26"
description: "ניתוחי כדורגל נשים מבוססי דאטא – WSL עונת 2025/26"
---

<!-- Page Title & Section Header -->
<div class="mb-6">
  <div class="text-xs font-mono uppercase text-neutral-500 dark:text-neutral-400 font-bold tracking-wider mb-1">
    WSL 2025/26 · STANDINGS
  </div>
  <h1 class="text-2xl md:text-3xl font-bold tracking-tight text-neutral-900 dark:text-white mb-2">
    טבלת הליגה
  </h1>
  <p class="text-xs sm:text-sm text-neutral-500 dark:text-neutral-400 font-sans">
    לחצו על שם מועדון לצפייה בסגל, מדדי ביצוע ומחקרי עומק.
  </p>
</div>

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
      מועדון במוקד
    </div>
    <h3 class="text-lg font-bold text-neutral-900 dark:text-white mb-2">London City Lionesses</h3>
    <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300 leading-relaxed mb-3">
      קבוצת המיקוד הראשונה של הבלוג. בעמוד הקבוצה תוכלו למצוא את הסגל המלא וסדרת שאלות מחקר מבוססות דאטא.
    </p>
    <a href="{{ '/teams/london-city-lionesses/' | relative_url }}" class="text-xs font-mono font-medium text-neutral-900 dark:text-neutral-100 hover:underline">
      מעבר לניתוח LCL ←
    </a>
  </div>
</div>
