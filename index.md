---
layout: default
title: "WSL Data Hub | טבלת הליגה 2025/26"
description: "ניתוחי כדורגל נשים מבוססי דאטא – WSL עונת 2025/26"
---

<!-- Hero Section -->
<div class="mb-8">
  <div class="flex flex-wrap items-center justify-between gap-4">
    <div>
      <div class="flex items-center gap-2 mb-2">
        <span class="px-2.5 py-0.5 bg-brand-500/10 border border-brand-500/30 text-brand-400 text-xs font-semibold rounded-full">
          עונת 2025/26
        </span>
        <span class="text-xs text-slate-500">Women's Super League</span>
      </div>
      <h2 class="text-3xl font-bold text-white tracking-tight">טבלת הליגה 🏆</h2>
    </div>
    <p class="text-xs text-slate-400 max-w-xs text-left sm:text-right">
      לחצו על כל קבוצה כדי לצפות בסגל המלא ובניתוחים הטקטיים
    </p>
  </div>
</div>

<!-- League Table Card -->
<div class="bg-surface-800 rounded-2xl shadow-xl overflow-hidden border border-surface-700">
  <div class="overflow-x-auto">
    <table class="w-full text-sm text-right">
      <thead>
        <tr class="bg-surface-700/80 text-slate-400 text-xs font-semibold border-b border-surface-600">
          <th class="px-4 py-3 text-center w-12">#</th>
          <th class="px-4 py-3 text-right">מועדון</th>
          <th class="px-3 py-3 text-center">מש'</th>
          <th class="px-3 py-3 text-center">נצ'</th>
          <th class="px-3 py-3 text-center">תיקו</th>
          <th class="px-3 py-3 text-center">הפ'</th>
          <th class="px-3 py-3 text-center">זכות</th>
          <th class="px-3 py-3 text-center">חובה</th>
          <th class="px-3 py-3 text-center">הפרש</th>
          <th class="px-4 py-3 text-center bg-surface-600/40 text-white font-bold w-16">נק'</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-surface-700">
        {% assign teams = site.data.league_table %}
        {% for team in teams %}
        <tr class="hover:bg-surface-700/60 transition-colors duration-150 {% if team.slug == 'london-city-lionesses' %}bg-brand-900/30 font-medium{% endif %}">
          
          <!-- Rank -->
          <td class="px-4 py-3.5 text-center text-slate-400 font-mono text-xs">{{ team.rk }}</td>
          
          <!-- Team Name -->
          <td class="px-4 py-3.5">
            <a href="{{ '/teams/' | append: team.slug | relative_url }}"
               class="font-semibold text-white hover:text-brand-400 transition-colors flex items-center gap-2.5">
              {% if team.slug == 'london-city-lionesses' %}
              <span class="w-2.5 h-2.5 rounded-full bg-brand-400 flex-shrink-0 animate-pulse"></span>
              {% else %}
              <span class="w-2 h-2 rounded-full bg-surface-600 flex-shrink-0"></span>
              {% endif %}
              <span dir="ltr">{{ team.squad }}</span>
            </a>
          </td>
          
          <!-- Stats -->
          <td class="px-3 py-3.5 text-center text-slate-300">{{ team.mp }}</td>
          <td class="px-3 py-3.5 text-center text-emerald-400 font-mono">{{ team.w }}</td>
          <td class="px-3 py-3.5 text-center text-slate-400 font-mono">{{ team.d }}</td>
          <td class="px-3 py-3.5 text-center text-rose-400 font-mono">{{ team.l }}</td>
          <td class="px-3 py-3.5 text-center text-slate-300 font-mono">{{ team.gf }}</td>
          <td class="px-3 py-3.5 text-center text-slate-400 font-mono">{{ team.ga }}</td>
          <td class="px-3 py-3.5 text-center font-mono {% if team.gd > 0 %}text-emerald-400{% elsif team.gd < 0 %}text-rose-400{% else %}text-slate-400{% endif %}">
            {% if team.gd > 0 %}+{% endif %}{{ team.gd }}
          </td>
          
          <!-- Points (Highlighted) -->
          <td class="px-4 py-3.5 text-center font-bold text-white text-base bg-surface-700/40">
            <span class="inline-block min-w-[24px] px-1.5 py-0.5 rounded bg-brand-500/20 text-brand-300 border border-brand-500/30">
              {{ team.pts }}
            </span>
          </td>

        </tr>
        {% endfor %}
      </tbody>
    </table>
  </div>
</div>

<!-- Info Cards (Like Kashar / Modern sports portal) -->
<div class="mt-12 grid md:grid-cols-2 gap-6">
  <div class="bg-surface-800 rounded-2xl p-6 border border-surface-700 shadow-lg">
    <div class="flex items-center gap-2 mb-3">
      <span class="text-xl">📊</span>
      <h3 class="text-lg font-bold text-white">מודלים וניתוחי עומק</h3>
    </div>
    <p class="text-slate-400 text-sm leading-relaxed mb-4">
      אנחנו משתמשים במדדי $xG$, פעולות יצירת בעיטה ($SCA$), איכות מסירות וזמני משחק מ-FBref כדי לנתח את ביצועי הקבוצות והשחקניות לעומק.
    </p>
    <a href="{{ '/about/' | relative_url }}" class="text-xs text-brand-400 hover:text-brand-300 font-medium">
      קראו עוד על מתודולוגיית הניתוח ←
    </a>
  </div>

  <div class="bg-surface-800 rounded-2xl p-6 border border-surface-700 shadow-lg">
    <div class="flex items-center gap-2 mb-3">
      <span class="text-xl">🦁</span>
      <h3 class="text-lg font-bold text-white">פוקוס: London City Lionesses</h3>
    </div>
    <p class="text-slate-400 text-sm leading-relaxed mb-4">
      קבוצת המיקוד הראשונה של הבלוג. בעמוד הקבוצה תוכלו למצוא את הסגל המלא וסדרת שאלות מחקר מבוססות דאטא.
    </p>
    <a href="{{ '/teams/london-city-lionesses/' | relative_url }}" class="text-xs text-brand-400 hover:text-brand-300 font-medium">
      מעבר לעמוד London City Lionesses ←
    </a>
  </div>
</div>
