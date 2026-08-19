---
layout: default
title: "WSL Data Hub | טבלת הליגה 2025/26"
description: "ניתוחי כדורגל נשים מבוססי דאטא – WSL עונת 2025/26"
---

<!-- Hero intro -->
<div class="mb-10">
  <h2 class="text-3xl font-bold text-white mb-2">טבלת הליגה 🏆</h2>
  <p class="text-slate-400 text-sm">Women's Super League · עונת 2025/26 · נתוני בסיס (הליגה טרם החלה)</p>
</div>

<!-- League Table -->
<div class="bg-surface-800 rounded-2xl shadow-xl overflow-hidden border border-surface-700">
  <div class="overflow-x-auto">
    <table class="w-full text-sm text-right">
      <thead>
        <tr class="bg-surface-700 text-slate-400 uppercase text-xs tracking-wider">
          <th class="px-4 py-3 text-center w-10">#</th>
          <th class="px-4 py-3">קבוצה</th>
          <th class="px-4 py-3 text-center">מש'</th>
          <th class="px-4 py-3 text-center">נצ'</th>
          <th class="px-4 py-3 text-center">תיק'</th>
          <th class="px-4 py-3 text-center">הפ'</th>
          <th class="px-4 py-3 text-center">שש'</th>
          <th class="px-4 py-3 text-center">ספ'</th>
          <th class="px-4 py-3 text-center">הפרש</th>
          <th class="px-4 py-3 text-center font-bold text-white">נק'</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-surface-700">
        {% assign teams = site.data.league_table %}
        {% for team in teams %}
        <tr class="hover:bg-surface-700 transition-colors duration-150 {% if team.slug == 'lionesses' %}bg-brand-900 bg-opacity-20{% endif %}">
          <td class="px-4 py-3 text-center text-slate-500 font-mono text-xs">{{ team.rk }}</td>
          <td class="px-4 py-3">
            <a href="{{ '/teams/' | append: team.slug | relative_url }}"
               class="font-semibold text-white hover:text-brand-500 transition-colors flex items-center gap-2">
              {% if team.slug == 'lionesses' %}
              <span class="inline-block w-2 h-2 rounded-full bg-brand-500 flex-shrink-0"></span>
              {% else %}
              <span class="inline-block w-2 h-2 rounded-full bg-surface-600 flex-shrink-0"></span>
              {% endif %}
              {{ team.squad }}
            </a>
          </td>
          <td class="px-4 py-3 text-center text-slate-300">{{ team.mp }}</td>
          <td class="px-4 py-3 text-center text-emerald-400">{{ team.w }}</td>
          <td class="px-4 py-3 text-center text-slate-300">{{ team.d }}</td>
          <td class="px-4 py-3 text-center text-red-400">{{ team.l }}</td>
          <td class="px-4 py-3 text-center text-slate-300">{{ team.gf }}</td>
          <td class="px-4 py-3 text-center text-slate-300">{{ team.ga }}</td>
          <td class="px-4 py-3 text-center {% if team.gd > 0 %}text-emerald-400{% elsif team.gd < 0 %}text-red-400{% else %}text-slate-400{% endif %}">
            {% if team.gd > 0 %}+{% endif %}{{ team.gd }}
          </td>
          <td class="px-4 py-3 text-center font-bold text-white text-base">{{ team.pts }}</td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
  </div>
</div>

<!-- Footnote -->
<p class="text-xs text-slate-600 mt-4 text-center">
  * הליגה טרם החלה · עמודות יעודכנו עם פתיחת העונה · נתונים: FBref / Sports-Reference
</p>

<!-- About section -->
<div class="mt-16 grid md:grid-cols-2 gap-6">
  <div class="bg-surface-800 rounded-xl p-6 border border-surface-700">
    <h3 class="text-lg font-semibold text-white mb-2">על הפרויקט</h3>
    <p class="text-slate-400 text-sm leading-relaxed">
      WSL Data Hub הוא בלוג ניתוח כדורגל נשים מבוסס-נתונים, בעברית.
      הנתונים נשאבים מ-FBref ומעובדים באמצעות Python, ומוצגים כאן בצורה נגישה וויזואלית.
    </p>
  </div>
  <div class="bg-surface-800 rounded-xl p-6 border border-surface-700">
    <h3 class="text-lg font-semibold text-white mb-2">קבוצת המיקוד</h3>
    <p class="text-slate-400 text-sm leading-relaxed">
      הניתוח המרכזי בפרויקט מתמקד ב-<a href="{{ '/teams/lionesses' | relative_url }}" class="text-brand-500 hover:underline">London City Lionesses</a>,
      עם השוואות לשאר קבוצות ה-WSL לאורך העונה.
    </p>
  </div>
</div>
