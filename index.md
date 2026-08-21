---
layout: default
title: "WSL Data Hub | טבלת הליגה 2025/26"
description: "ניתוחי כדורגל נשים מבוססי דאטא – WSL עונת 2025/26"
---

<!-- Editorial Hero Section -->
<div class="mb-6">
  <div class="flex flex-wrap items-end justify-between gap-4 border-b border-surface-700/80 pb-4">
    <div>
      <div class="flex items-center gap-2 mb-1.5">
        <span class="px-2 py-0.5 border border-surface-700 bg-surface-850 text-neutral-400 text-[11px] font-mono rounded">
          WSL 2025/26
        </span>
        <span class="text-xs text-neutral-500 font-mono">STANDINGS & METRICS</span>
      </div>
      <h1 class="font-serif text-3xl sm:text-4xl font-bold text-white tracking-tight">טבלת הליגה</h1>
    </div>
    <p class="text-xs text-neutral-400 font-sans max-w-sm text-right">
      לחצו על שם מועדון לצפייה בסגל השחקניות, מדדי ביצוע ומחקרי עומק טקטיים.
    </p>
  </div>
</div>

<!-- League Table Card - High Density Editorial Standard -->
<div class="bg-surface-900 rounded-xl overflow-hidden border border-surface-700/80">
  <div class="overflow-x-auto" dir="ltr">
    <table class="w-full text-xs text-left border-collapse">
      <thead>
        <tr class="bg-surface-850 text-neutral-400 text-[11px] font-mono uppercase tracking-wider border-b border-surface-700/80">
          <th class="px-3 py-2.5 text-center w-10 sticky-col bg-surface-850">#</th>
          <th class="px-3 py-2.5 text-left">Club</th>
          <th class="px-2.5 py-2.5 text-right">MP</th>
          <th class="px-2.5 py-2.5 text-right">W</th>
          <th class="px-2.5 py-2.5 text-right">D</th>
          <th class="px-2.5 py-2.5 text-right">L</th>
          <th class="px-2.5 py-2.5 text-right">GF</th>
          <th class="px-2.5 py-2.5 text-right">GA</th>
          <th class="px-2.5 py-2.5 text-right">GD</th>
          <th class="px-3 py-2.5 text-right font-bold text-neutral-200 bg-surface-800/60 w-14">PTS</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-surface-700/40">
        {% assign teams = site.data.league_table %}
        {% for team in teams %}
        {% assign is_lcl = (team.slug == 'london-city-lionesses') %}
        <tr class="hover:bg-surface-800/70 transition-colors {% if is_lcl %}bg-surface-850/60{% endif %}" {% if is_lcl %}style="border-left: 3px solid #E91E63;"{% endif %}>
          
          <!-- Rank (Sticky) -->
          <td class="px-3 py-2 text-center text-neutral-400 font-mono text-xs sticky-col {% if is_lcl %}bg-surface-850{% else %}bg-surface-900{% endif %}">
            {{ team.rk }}
          </td>
          
          <!-- Team Name -->
          <td class="px-3 py-2">
            <a href="{{ '/teams/' | append: team.slug | relative_url }}"
               class="font-medium text-neutral-100 hover:text-brand-400 transition-colors flex items-center gap-2">
              {% if is_lcl %}
              <span class="w-2 h-2 rounded-full bg-[#E91E63] flex-shrink-0"></span>
              {% else %}
              <span class="w-1.5 h-1.5 rounded-full bg-neutral-600 flex-shrink-0"></span>
              {% endif %}
              <span class="font-sans text-xs sm:text-sm">{{ team.squad }}</span>
            </a>
          </td>
          
          <!-- Monospace Numeric Metrics (Strictly Right Aligned) -->
          <td class="px-2.5 py-2 text-right text-neutral-400 font-mono tabular-nums tracking-tight">{{ team.mp }}</td>
          <td class="px-2.5 py-2 text-right text-emerald-400 font-mono tabular-nums tracking-tight">{{ team.w }}</td>
          <td class="px-2.5 py-2 text-right text-neutral-400 font-mono tabular-nums tracking-tight">{{ team.d }}</td>
          <td class="px-2.5 py-2 text-right text-rose-400 font-mono tabular-nums tracking-tight">{{ team.l }}</td>
          <td class="px-2.5 py-2 text-right text-neutral-300 font-mono tabular-nums tracking-tight">{{ team.gf }}</td>
          <td class="px-2.5 py-2 text-right text-neutral-400 font-mono tabular-nums tracking-tight">{{ team.ga }}</td>
          <td class="px-2.5 py-2 text-right font-mono tabular-nums tracking-tight {% if team.gd > 0 %}text-emerald-400{% elsif team.gd < 0 %}text-rose-400{% else %}text-neutral-400{% endif %}">
            {% if team.gd > 0 %}+{% endif %}{{ team.gd }}
          </td>
          
          <!-- Points -->
          <td class="px-3 py-2 text-right font-bold text-white font-mono tabular-nums tracking-tight text-xs sm:text-sm bg-surface-800/40">
            {{ team.pts }}
          </td>

        </tr>
        {% endfor %}
      </tbody>
    </table>
  </div>
</div>

<!-- Editorial Info Cards -->
<div class="mt-10 grid md:grid-cols-2 gap-5" dir="rtl">
  <div class="bg-surface-900 rounded-xl p-5 sm:p-6 border border-surface-700/80" style="border-right: 3px solid #38bdf8;">
    <div class="flex items-center gap-2.5 mb-2.5">
      <span class="text-lg">📊</span>
      <h3 class="font-serif text-lg font-bold text-white">מודלים וניתוחי עומק</h3>
    </div>
    <p class="text-neutral-400 text-xs sm:text-sm leading-relaxed mb-4">
      אנחנו משתמשים במדדי xG, פעולות יצירת בעיטה (SCA), איכות מסירות וזמני משחק מ-FBref כדי לנתח את ביצועי הקבוצות והשחקניות לעומק.
    </p>
    <a href="{{ '/methodology/' | relative_url }}" class="text-xs font-medium text-brand-400 hover:text-brand-300 flex items-center gap-1">
      <span>קראו עוד על מתודולוגיית הניתוח</span>
      <span>←</span>
    </a>
  </div>

  <div class="bg-surface-900 rounded-xl p-5 sm:p-6 border border-surface-700/80" style="border-right: 3px solid #E91E63;">
    <div class="flex items-center gap-2.5 mb-2.5">
      <span class="text-lg">🦁</span>
      <h3 class="font-serif text-lg font-bold text-white">פוקוס: London City Lionesses</h3>
    </div>
    <p class="text-neutral-400 text-xs sm:text-sm leading-relaxed mb-4">
      קבוצת המיקוד הראשונה של הבלוג. בעמוד הקבוצה תוכלו למצוא את הסגל המלא וסדרת שאלות מחקר מבוססות דאטא.
    </p>
    <a href="{{ '/teams/london-city-lionesses/' | relative_url }}" class="text-xs font-medium text-brand-400 hover:text-brand-300 flex items-center gap-1">
      <span>מעבר לעמוד London City Lionesses</span>
      <span>←</span>
    </a>
  </div>
</div>
