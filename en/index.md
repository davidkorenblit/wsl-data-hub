---
layout: default
title: "WSL Data Hub | 2026/27 Standings"
description: "Data-driven women's football analytics & deep dives – FA WSL 2026/27"
permalink: /en/
lang: en
alt_url: /
---

<!-- Page Title & Section Header -->
<div class="mb-6">
  <div class="text-xs font-mono uppercase text-neutral-500 dark:text-neutral-400 font-bold tracking-wider mb-1">
    WSL 2026/27 · STANDINGS
  </div>
  <h1 class="text-2xl md:text-3xl font-bold tracking-tight text-neutral-900 dark:text-white mb-2">
    League Table
  </h1>
  <p class="text-xs sm:text-sm text-neutral-500 dark:text-neutral-400 font-sans">
    Click on any club to view squad details, advanced metrics, and in-depth tactical analysis.
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
          {% assign en_teams = "tottenham,chelsea,arsenal,manchester-city,manchester-utd,london-city-lionesses,brighton" | split: "," %}
          {% if en_teams contains team.slug %}
          <a href="{{ '/en/teams/' | append: team.slug | append: '/' | relative_url }}" class="hover:underline hover:text-neutral-950 dark:hover:text-neutral-200 flex items-center gap-2">
            {% if is_lcl %}
            <span class="w-1.5 h-1.5 rounded-full bg-neutral-900 dark:bg-white"></span>
            {% endif %}
            <span>{{ team.squad }}</span>
          </a>
          {% else %}
          <a href="{{ '/teams/' | append: team.slug | relative_url }}" class="hover:underline hover:text-neutral-950 dark:hover:text-neutral-200 flex items-center gap-2">
            {% if is_lcl %}
            <span class="w-1.5 h-1.5 rounded-full bg-neutral-900 dark:bg-white"></span>
            {% endif %}
            <span>{{ team.squad }}</span>
          </a>
          {% endif %}
        </td>
        
        <!-- Numeric Columns -->
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

<!-- Clean Editorial Cards -->
<div class="grid md:grid-cols-2 gap-4" dir="ltr">
  <div class="rounded-md border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-[#121215] p-5">
    <div class="text-xs font-mono uppercase text-neutral-500 dark:text-neutral-400 font-bold tracking-wider mb-2">
      Methodology & Models
    </div>
    <h3 class="text-lg font-bold text-neutral-900 dark:text-white mb-2">Data Science & Metrics</h3>
    <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300 leading-relaxed mb-3">
      xG models, Shot-Creating Actions (SCA), passing progression quality, and possession metrics powered by FBref and FotMob data.
    </p>
    <a href="{{ '/methodology/' | relative_url }}" class="text-xs font-mono font-medium text-neutral-900 dark:text-neutral-100 hover:underline">
      Explore Methodology →
    </a>
  </div>

  <div class="rounded-md border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-[#121215] p-5">
    <div class="text-xs font-mono uppercase text-neutral-500 dark:text-neutral-400 font-bold tracking-wider mb-2">
      Weekly Column
    </div>
    <h3 class="text-lg font-bold text-neutral-900 dark:text-white mb-2">Matchweek Reviews & Insights</h3>
    <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300 leading-relaxed mb-3">
      Tactical takeaways, eye-test verifications, expected vs actual performance, and deep dives across the league.
    </p>
    <a href="{{ '/en/weekly/' | relative_url }}" class="text-xs font-mono font-medium text-neutral-900 dark:text-neutral-100 hover:underline">
      Read MW1 Column →
    </a>
  </div>
</div>
