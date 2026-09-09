---
layout: team
title: "London City Lionesses - Part II: Squad Baseline & Data Analysis"
team_name: "London City Lionesses"
team_slug: "london-city-lionesses"
team_meta: "WSL 2026/27 · Part II: Squad Baseline & Data Analysis"
hide_sidebar: true
permalink: /en/teams/london-city-lionesses/analysis/
prev_url: /en/teams/london-city-lionesses/
prev_title: "Part I: Culture & Identity"
lang: en
alt_url: /teams/london-city-lionesses/analysis/
---

<div class="space-y-5 text-neutral-800 dark:text-neutral-200 leading-relaxed text-base sm:text-lg font-sans">

  <div class="border-b border-neutral-200 dark:border-neutral-800 pb-3">
    <div class="text-xs font-mono uppercase text-neutral-500 dark:text-neutral-400 font-bold tracking-wider mb-1">
      Question 1: Squad Baseline & Historical Data
    </div>
    <h1 class="text-2xl md:text-3xl font-bold tracking-tight text-neutral-900 dark:text-white">
      London City Lionesses: The Debut Top-Flight Benchmark
    </h1>
  </div>

  <p>
    A first glance at the underlying data from LCL's inaugural top-flight campaign reveals several tactical conclusions that might surprise casual WSL followers.
  </p>

  <p>
    Looking at the attacking metrics we track (explained in our <a href="{{ '/en/methodology/' | relative_url }}" class="text-neutral-900 dark:text-white underline font-medium">Methodology</a> guide), several telling patterns emerge. They scored relatively few goals—even relative to league averages: 26 goals (ranking 8th in the league, against a WSL average of 31.2). They also generated modest shot volume: 10.95 shots per 90 minutes (ranking 7th). Conversely, their shot accuracy on target was 3rd-best in the league at 38.2% (Brighton led the WSL at 40.9%).
  </p>

  <p>
    Their overall shot conversion rate ranked 7th at 0.11 goals per shot. In other words, their baseline offensive output was essentially lower-middle tier.
  </p>

  <p>
    However, on defensive disruption metrics, LCL were exceptional: they finished tied for 1st in the entire league in successful combined tackles and interceptions—racking up 536 total defensive actions.
  </p>

  <p>
    Furthermore, in terms of suppressing shots on target, LCL's backline performed comfortably above league average: conceding just 3.73 shots on target per match (5th-best in the league, against a league average of 4.30; Arsenal led the category at 2.41).
  </p>

  <p>
    Yet here lies the paradox: the goalkeeper save percentage was among the lowest in the division—just 57.3% (ranking 11th of 12 clubs, compared to Chelsea's 74.4%). That stark difference highlights why upgrading between the sticks was essential: the defensive unit did its job limiting high-danger volume, but routine chances resulted in goals too often.
  </p>

  <p>
    Possession-wise, LCL hovered right around the median at 49.8% (6th in the WSL). Even though they held substantial possession compared to the bottom tier, it rarely translated into incisive final-third penetration.
  </p>

  <p>
    Excluding the "Big Three" of Chelsea (60.0%), Arsenal (59.0%), and Manchester City (56.6%), who average 58.5% together, the remaining 9 clubs averaged only 47.2%. Outside that elite tier, LCL was 3rd in territorial control.
  </p>

  <p>
    Still, this didn't translate into high-end chance creation: LCL produced only 18 assists—0.82 per 90, 9th in the division.
  </p>

  <p>
    Looking at advanced Opta/FotMob metrics: the club produced 49 Big Chances created (5th in WSL) and 30.1 Expected Goals (xG, 6th). For a debut season resulting in a 6th-place finish, these are respectable numbers. But the gap to the absolute summit is vast (Manchester City generated 102 Big Chances and 58.6 xG). Furthermore, limited touches in the opponent's penalty box (487, 7th in the league compared to ~890 for Arsenal and City) and modest passing volume (335.2 accurate passes per game, 8th) proved that midfield progression was the critical bottleneck.
  </p>

  <!-- Scatter Plot Chart: Possession vs Box Touches -->
  <div class="rounded-md border border-neutral-200 dark:border-neutral-800 bg-[#0b1329] p-3 sm:p-5 my-6">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
      <div>
        <h3 class="text-sm sm:text-base font-bold text-white">
          Possession vs. Opponent Box Touches (WSL 2024/25)
        </h3>
        <p class="text-xs text-slate-400 font-sans">
          Decent midfield share (#6 WSL) vs. difficulty penetrating the penalty area (#7 WSL)
        </p>
      </div>
      <span class="text-[10px] font-mono border border-sky-500/40 bg-sky-950/40 text-sky-400 px-2 py-0.5 rounded font-bold">
        SCATTER PLOT
      </span>
    </div>
    <img 
      src="{{ '/assets/images/evaluations/lcl_possession_vs_box_touches.png' | relative_url }}" 
      alt="WSL 2024/25 Possession vs Box Touches Scatter Plot" 
      class="w-full h-auto rounded shadow"
      loading="lazy"
    />
  </div>

  <!-- Detailed Benchmark Table (Expandable for deeper drill-down) -->
  <details class="group rounded-md border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-[#121215] p-4 sm:p-5 my-6">
    <summary class="cursor-pointer font-bold text-base text-neutral-900 dark:text-white flex items-center justify-between select-none">
      <div class="space-y-0.5">
        <span class="flex items-center gap-2">
          <span>📊 Full Comparative League Benchmark Table</span>
        </span>
        <p class="text-xs text-neutral-500 dark:text-neutral-400 font-normal">
          Click to inspect the complete 10-metric statistical breakdown across the WSL
        </p>
      </div>
      <span class="text-xs font-mono text-neutral-700 dark:text-neutral-300 px-2.5 py-1 rounded bg-neutral-100 dark:bg-neutral-800 border border-neutral-200 dark:border-neutral-700">
        Show / Hide Table
      </span>
    </summary>

    <div class="pt-4 overflow-x-auto rounded" dir="ltr">
      <table class="w-full text-left border-collapse text-xs sm:text-sm">
        <thead>
          <tr class="bg-neutral-50 dark:bg-[#18181b] border-b border-neutral-200 dark:border-neutral-800 text-neutral-600 dark:text-neutral-400 font-mono text-xs">
            <th class="py-2.5 px-3 font-semibold">Metric</th>
            <th class="py-2.5 px-3 font-semibold text-center text-neutral-900 dark:text-white">LCL Value</th>
            <th class="py-2.5 px-3 font-semibold text-center">WSL Rank</th>
            <th class="py-2.5 px-3 font-semibold text-center">League Avg</th>
            <th class="py-2.5 px-3 font-semibold">League Leader</th>
            <th class="py-2.5 px-3 font-semibold text-center">Gap to Summit</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-neutral-100 dark:divide-neutral-800">
          <tr class="hover:bg-neutral-50 dark:hover:bg-[#18181c] bg-emerald-50/40 dark:bg-emerald-950/20 font-medium">
            <td class="py-2 px-3">Interceptions + Tackles (Defensive Volume)</td>
            <td class="py-2 px-3 text-center font-bold font-mono text-emerald-600 dark:text-emerald-400">536</td>
            <td class="py-2 px-3 text-center font-mono font-bold">#1 🥇</td>
            <td class="py-2 px-3 text-center font-mono text-neutral-500">459.1</td>
            <td class="py-2 px-3">Lionesses (536)</td>
            <td class="py-2 px-3 text-center font-mono text-emerald-600 dark:text-emerald-400">Leader</td>
          </tr>
          <tr class="hover:bg-neutral-50 dark:hover:bg-[#18181c]">
            <td class="py-2 px-3">Accurate Long Balls / 90 min</td>
            <td class="py-2 px-3 text-center font-mono font-semibold">20.3</td>
            <td class="py-2 px-3 text-center font-mono">#4</td>
            <td class="py-2 px-3 text-center font-mono text-neutral-500">19.9</td>
            <td class="py-2 px-3">Chelsea (23.5)</td>
            <td class="py-2 px-3 text-center font-mono text-neutral-600 dark:text-neutral-400">-3.2</td>
          </tr>
          <tr class="hover:bg-neutral-50 dark:hover:bg-[#18181c]">
            <td class="py-2 px-3">Big Chances Created</td>
            <td class="py-2 px-3 text-center font-mono font-semibold">49.0</td>
            <td class="py-2 px-3 text-center font-mono">#5</td>
            <td class="py-2 px-3 text-center font-mono text-neutral-500">48.5</td>
            <td class="py-2 px-3">Man City (102.0)</td>
            <td class="py-2 px-3 text-center font-mono text-rose-600 dark:text-rose-400">-53.0</td>
          </tr>
          <tr class="hover:bg-neutral-50 dark:hover:bg-[#18181c]">
            <td class="py-2 px-3">Expected Goals (xG)</td>
            <td class="py-2 px-3 text-center font-mono font-semibold">30.1</td>
            <td class="py-2 px-3 text-center font-mono">#6</td>
            <td class="py-2 px-3 text-center font-mono text-neutral-500">32.1</td>
            <td class="py-2 px-3">Man City (58.6)</td>
            <td class="py-2 px-3 text-center font-mono text-neutral-600 dark:text-neutral-400">-28.5</td>
          </tr>
          <tr class="hover:bg-neutral-50 dark:hover:bg-[#18181c]">
            <td class="py-2 px-3">Average Possession (%)</td>
            <td class="py-2 px-3 text-center font-mono font-semibold">49.8%</td>
            <td class="py-2 px-3 text-center font-mono">#6</td>
            <td class="py-2 px-3 text-center font-mono text-neutral-500">50.1%</td>
            <td class="py-2 px-3">Chelsea (60.0%)</td>
            <td class="py-2 px-3 text-center font-mono text-neutral-600 dark:text-neutral-400">-10.2%</td>
          </tr>
          <tr class="hover:bg-neutral-50 dark:hover:bg-[#18181c]">
            <td class="py-2 px-3">Touches in Opponent Box</td>
            <td class="py-2 px-3 text-center font-mono font-semibold">487</td>
            <td class="py-2 px-3 text-center font-mono">#7</td>
            <td class="py-2 px-3 text-center font-mono text-neutral-500">547.6</td>
            <td class="py-2 px-3">Arsenal (897)</td>
            <td class="py-2 px-3 text-center font-mono text-rose-600 dark:text-rose-400">-410</td>
          </tr>
          <tr class="hover:bg-neutral-50 dark:hover:bg-[#18181c]">
            <td class="py-2 px-3">Goals For (GF)</td>
            <td class="py-2 px-3 text-center font-mono font-semibold">26</td>
            <td class="py-2 px-3 text-center font-mono">#8</td>
            <td class="py-2 px-3 text-center font-mono text-neutral-500">31.2</td>
            <td class="py-2 px-3">Man City (60)</td>
            <td class="py-2 px-3 text-center font-mono text-neutral-600 dark:text-neutral-400">-34</td>
          </tr>
          <tr class="hover:bg-neutral-50 dark:hover:bg-[#18181c]">
            <td class="py-2 px-3">Accurate Passes / 90 min</td>
            <td class="py-2 px-3 text-center font-mono font-semibold">335.2</td>
            <td class="py-2 px-3 text-center font-mono">#8</td>
            <td class="py-2 px-3 text-center font-mono text-neutral-500">354.2</td>
            <td class="py-2 px-3">Arsenal (452.1)</td>
            <td class="py-2 px-3 text-center font-mono text-rose-600 dark:text-rose-400">-116.9</td>
          </tr>
          <tr class="hover:bg-neutral-50 dark:hover:bg-[#18181c]">
            <td class="py-2 px-3">Goals Conceded (GA)</td>
            <td class="py-2 px-3 text-center font-mono font-semibold text-rose-600 dark:text-rose-400">35</td>
            <td class="py-2 px-3 text-center font-mono">#8</td>
            <td class="py-2 px-3 text-center font-mono text-neutral-500">31.2</td>
            <td class="py-2 px-3">Arsenal (12)</td>
            <td class="py-2 px-3 text-center font-mono text-rose-600 dark:text-rose-400">+23</td>
          </tr>
          <tr class="hover:bg-neutral-50 dark:hover:bg-[#18181c]">
            <td class="py-2 px-3">Assists</td>
            <td class="py-2 px-3 text-center font-mono font-semibold">18</td>
            <td class="py-2 px-3 text-center font-mono">#9</td>
            <td class="py-2 px-3 text-center font-mono text-neutral-500">22.7</td>
            <td class="py-2 px-3">Arsenal (45)</td>
            <td class="py-2 px-3 text-center font-mono text-neutral-600 dark:text-neutral-400">-27</td>
          </tr>
          <tr class="hover:bg-neutral-50 dark:hover:bg-[#18181c] bg-rose-50/30 dark:bg-rose-950/20">
            <td class="py-2 px-3">Goalkeeper Save Rate (%)</td>
            <td class="py-2 px-3 text-center font-mono font-bold text-rose-600 dark:text-rose-400">57.3%</td>
            <td class="py-2 px-3 text-center font-mono font-bold text-rose-600 dark:text-rose-400">#11</td>
            <td class="py-2 px-3 text-center font-mono text-neutral-500">66.2%</td>
            <td class="py-2 px-3">Chelsea (74.4%)</td>
            <td class="py-2 px-3 text-center font-mono text-rose-600 dark:text-rose-400">-17.1%</td>
          </tr>
        </tbody>
      </table>
    </div>
  </details>

  <div class="p-4 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 my-4 space-y-2">
    <div class="text-xs font-mono uppercase text-neutral-500 dark:text-neutral-400 font-bold tracking-wider">
      Section Summary
    </div>
    <h3 class="font-bold text-neutral-900 dark:text-white text-base">What Does This Data Tell Us?</h3>
    <p class="text-sm text-neutral-700 dark:text-neutral-300">
      The numbers immediately justified investing heavily in an elite goalkeeper (Mary Earps) and creative attacking midfield reinforcements.
    </p>
    <p class="text-sm text-neutral-700 dark:text-neutral-300">
      Pairing Mapi León with an already formidable defensive engine transforms London City Lionesses into a powerhouse capable of dictating tempo from the back, laying the groundwork for a genuine top-three challenge.
    </p>
  </div>

  <!-- Outro & Forward Links -->
  <div class="pt-4 flex items-center justify-between border-t border-neutral-200 dark:border-neutral-800 text-sm font-mono">
    <a href="{{ '/en/teams/london-city-lionesses/' | relative_url }}" class="text-neutral-600 dark:text-neutral-400 hover:text-neutral-900 dark:hover:text-white">
      ← Part I: Culture & Identity
    </a>
    <a href="{{ '/en/weekly/' | relative_url }}" class="text-neutral-900 dark:text-white font-bold hover:underline">
      Matchweek 1 Column Review →
    </a>
  </div>

  <!-- Standardized Post Pagination -->
  {% include post_pagination.html %}

</div>
