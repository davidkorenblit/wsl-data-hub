---
layout: default
title: "WSL Data Hub | טבלת הליגה 2025/26"
description: "ניתוחי כדורגל נשים מבוססי דאטא – WSL עונת 2025/26"
---

<!-- Page Title & Section Header -->
<div class="mb-6">
  <div class="text-xs uppercase font-mono font-bold tracking-wider text-neutral-500 mb-1">
    WSL 2025/26 · STANDINGS
  </div>
  <h1 class="font-serif text-2xl md:text-3xl font-semibold tracking-tight text-neutral-900 mb-2">
    טבלת הליגה
  </h1>
  <p class="text-xs sm:text-sm text-neutral-500 font-sans">
    לחצו על שם מועדון לצפייה בסגל, מדדי ביצוע ומחקרי עומק.
  </p>
</div>

<!-- Strict Clean Editorial League Table Container -->
<div class="overflow-x-auto rounded-md border border-neutral-200 bg-white mb-8" dir="ltr">
  <table class="w-full text-left border-collapse">
    <thead>
      <tr>
        <th class="text-xs uppercase font-mono font-medium text-neutral-400 bg-neutral-50 py-2.5 px-3 border-b border-neutral-200 text-left w-10">#</th>
        <th class="text-xs uppercase font-mono font-medium text-neutral-400 bg-neutral-50 py-2.5 px-3 border-b border-neutral-200 text-left">Club</th>
        <th class="text-xs uppercase font-mono font-medium text-neutral-400 bg-neutral-50 py-2.5 px-3 border-b border-neutral-200 text-right">MP</th>
        <th class="text-xs uppercase font-mono font-medium text-neutral-400 bg-neutral-50 py-2.5 px-3 border-b border-neutral-200 text-right">W</th>
        <th class="text-xs uppercase font-mono font-medium text-neutral-400 bg-neutral-50 py-2.5 px-3 border-b border-neutral-200 text-right">D</th>
        <th class="text-xs uppercase font-mono font-medium text-neutral-400 bg-neutral-50 py-2.5 px-3 border-b border-neutral-200 text-right">L</th>
        <th class="text-xs uppercase font-mono font-medium text-neutral-400 bg-neutral-50 py-2.5 px-3 border-b border-neutral-200 text-right">GF</th>
        <th class="text-xs uppercase font-mono font-medium text-neutral-400 bg-neutral-50 py-2.5 px-3 border-b border-neutral-200 text-right">GA</th>
        <th class="text-xs uppercase font-mono font-medium text-neutral-400 bg-neutral-50 py-2.5 px-3 border-b border-neutral-200 text-right">GD</th>
        <th class="text-xs uppercase font-mono font-bold text-neutral-700 bg-neutral-100/70 py-2.5 px-3 border-b border-neutral-200 text-right w-14">PTS</th>
      </tr>
    </thead>
    <tbody>
      {% assign teams = site.data.league_table %}
      {% for team in teams %}
      {% assign is_lcl = (team.slug == 'london-city-lionesses') %}
      <tr class="hover:bg-neutral-50 {% if is_lcl %}bg-neutral-50/60 font-medium{% endif %}">
        
        <!-- Rank -->
        <td class="text-xs font-mono text-neutral-400 py-2 px-3 border-b border-neutral-100 text-left">
          {{ team.rk }}
        </td>
        
        <!-- Team Name -->
        <td class="text-sm font-sans font-medium text-neutral-900 py-2 px-3 border-b border-neutral-100 text-left">
          <a href="{{ '/teams/' | append: team.slug | relative_url }}" class="hover:underline hover:text-neutral-950 flex items-center gap-2">
            {% if is_lcl %}
            <span class="w-1.5 h-1.5 rounded-full bg-neutral-900"></span>
            {% endif %}
            <span>{{ team.squad }}</span>
          </a>
        </td>
        
        <!-- Numeric Columns (Strictly Right Aligned, Monospace) -->
        <td class="text-sm font-mono tabular-nums text-neutral-500 py-2 px-3 border-b border-neutral-100 text-right">{{ team.mp }}</td>
        <td class="text-sm font-mono tabular-nums text-neutral-800 py-2 px-3 border-b border-neutral-100 text-right">{{ team.w }}</td>
        <td class="text-sm font-mono tabular-nums text-neutral-500 py-2 px-3 border-b border-neutral-100 text-right">{{ team.d }}</td>
        <td class="text-sm font-mono tabular-nums text-neutral-500 py-2 px-3 border-b border-neutral-100 text-right">{{ team.l }}</td>
        <td class="text-sm font-mono tabular-nums text-neutral-800 py-2 px-3 border-b border-neutral-100 text-right">{{ team.gf }}</td>
        <td class="text-sm font-mono tabular-nums text-neutral-500 py-2 px-3 border-b border-neutral-100 text-right">{{ team.ga }}</td>
        <td class="text-sm font-mono tabular-nums text-neutral-800 py-2 px-3 border-b border-neutral-100 text-right">
          {% if team.gd > 0 %}+{% endif %}{{ team.gd }}
        </td>
        <td class="text-sm font-mono tabular-nums font-bold text-neutral-950 py-2 px-3 border-b border-neutral-100 text-right bg-neutral-50/50">
          {{ team.pts }}
        </td>

      </tr>
      {% endfor %}
    </tbody>
  </table>
</div>

<!-- Strict Clean Editorial Cards -->
<div class="grid md:grid-cols-2 gap-4" dir="rtl">
  <div class="rounded-md border border-neutral-200 bg-white p-5">
    <div class="text-xs uppercase font-mono font-bold tracking-wider text-neutral-500 mb-2">
      מתודולוגיה ומודלים
    </div>
    <h3 class="font-serif text-lg font-semibold text-neutral-900 mb-2">מודלים וניתוחי עומק</h3>
    <p class="text-xs sm:text-sm text-neutral-600 leading-relaxed mb-3">
      מדדי xG, פעולות יצירת בעיטה (SCA), איכות מסירות וזמני משחק מ-FBref לניתוח ביצועי הקבוצות והשחקניות.
    </p>
    <a href="{{ '/methodology/' | relative_url }}" class="text-xs font-mono font-medium text-neutral-900 hover:underline">
      מתודולוגיית הניתוח ←
    </a>
  </div>

  <div class="rounded-md border border-neutral-200 bg-white p-5">
    <div class="text-xs uppercase font-mono font-bold tracking-wider text-neutral-500 mb-2">
      מועדון במוקד
    </div>
    <h3 class="font-serif text-lg font-semibold text-neutral-900 mb-2">London City Lionesses</h3>
    <p class="text-xs sm:text-sm text-neutral-600 leading-relaxed mb-3">
      קבוצת המיקוד הראשונה של הבלוג. בעמוד הקבוצה תוכלו למצוא את הסגל המלא וסדרת שאלות מחקר מבוססות דאטא.
    </p>
    <a href="{{ '/teams/london-city-lionesses/' | relative_url }}" class="text-xs font-mono font-medium text-neutral-900 hover:underline">
      מעבר לניתוח LCL ←
    </a>
  </div>
</div>
