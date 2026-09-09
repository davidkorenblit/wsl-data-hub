---
layout: team
title: "Tottenham Hotspur - Part II: Data Analysis & Tactical Baseline"
team_name: "Tottenham Hotspur"
team_slug: "tottenham"
team_meta: "WSL 2026/27 · Part II: Data Analysis & Tactical Baseline"
permalink: /en/teams/tottenham/analysis/
prev_url: /en/teams/tottenham/
prev_title: "Part I: Identity, Leadership & Heart"
next_url: /en/teams/tottenham/defense/
next_title: "Part III: Defensive Unit & The Search for Koga's Partners"
lang: en
alt_url: /teams/tottenham/analysis/
---

<div class="space-y-6 text-neutral-800 dark:text-neutral-200 leading-relaxed text-base sm:text-lg font-sans">

  <!-- Header -->
  <div class="border-b border-neutral-200 dark:border-neutral-800 pb-3">
    <div class="text-xs font-mono uppercase text-neutral-500 dark:text-neutral-400 font-bold tracking-wider mb-1">
      Part II: Data Analysis & Tactical Baseline
    </div>
    <h1 class="text-2xl md:text-3xl font-bold tracking-tight text-neutral-900 dark:text-white">
      Tottenham Hotspur: Formations, Positionless Play & Data
    </h1>
  </div>

  <!-- Intro -->
  <p class="text-lg">
    The concept of <strong>"positionless" play</strong> originates from basketball, but hearing it repeated so frequently by Spurs players and Robert Vilahamn forced me to verify it against the underlying data from last season.
  </p>

  <p>
    The baseline numbers strongly support the eye-test: Tottenham's attacking unit, and particularly the arrival of attacking midfielder Signe Gaupset (a.k.a. <strong>"Siggy"</strong>) in January, operates with exceptional positional fluidity.
    A glance at the goal distribution, penalty-box touches from midfielders, and spatial heatmaps demonstrates an attack that deliberately resists fixed, rigid roles.
  </p>

  <!-- Part 1: Attack & Positionless -->
  <div class="rounded-xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/50 dark:bg-[#121215] p-5 sm:p-6 space-y-4">
    <h2 class="text-xl font-bold text-neutral-900 dark:text-white flex items-center gap-2">
      <span>1. Positionless Attack: Decentralized Scoring & Box Occupancy</span>
    </h2>

    <p class="text-sm sm:text-base text-neutral-700 dark:text-neutral-300">
      Unlike most sides in the division that rely heavily on a single focal point (e.g. Manchester City, where <strong>Bunny Shaw</strong> was personally responsible for 34% of team goals), Spurs scored <strong>35 league goals spread across 11 different players</strong>. Not a single player accounted for more than 23% of the team's total:
    </p>

    <!-- Goal Distribution Table -->
    <div class="overflow-x-auto">
      <table class="w-full text-sm text-left border-collapse">
        <thead>
          <tr class="border-b border-neutral-200 dark:border-neutral-700 text-neutral-500 dark:text-neutral-400 font-mono">
            <th class="py-2 pl-2">Player</th>
            <th class="py-2">Designated Role</th>
            <th class="py-2 text-center">Goals</th>
            <th class="py-2 text-center">Assists</th>
            <th class="py-2 text-right pr-2">Share of Team Goals</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-neutral-100 dark:divide-neutral-800 font-mono text-xs sm:text-sm">
          <tr>
            <td class="py-2.5 pl-2 font-sans font-semibold text-neutral-900 dark:text-white">Olga Ahtinen / Olivia Holdt (Olive)</td>
            <td class="py-2.5 font-sans text-neutral-500">Midfielder / Free 8-10</td>
            <td class="py-2.5 text-center font-bold text-neutral-900 dark:text-white">8</td>
            <td class="py-2.5 text-center">3</td>
            <td class="py-2.5 text-right pr-2">22.9%</td>
          </tr>
          <tr>
            <td class="py-2.5 pl-2 font-sans">Beth England</td>
            <td class="py-2.5 font-sans text-neutral-500">Striker / Captain</td>
            <td class="py-2.5 text-center font-bold">7</td>
            <td class="py-2.5 text-center">1</td>
            <td class="py-2.5 text-right pr-2">20.0%</td>
          </tr>
          <tr>
            <td class="py-2.5 pl-2 font-sans">Cathinka Tandberg</td>
            <td class="py-2.5 font-sans text-neutral-500">Target Forward</td>
            <td class="py-2.5 text-center font-bold">6</td>
            <td class="py-2.5 text-center">1</td>
            <td class="py-2.5 text-right pr-2">17.1%</td>
          </tr>
          <tr>
            <td class="py-2.5 pl-2 font-sans">Signe Gaupset (Siggy)</td>
            <td class="py-2.5 font-sans text-neutral-500">Central Midfielder (From Jan)</td>
            <td class="py-2.5 text-center font-bold">3</td>
            <td class="py-2.5 text-center">1</td>
            <td class="py-2.5 text-right pr-2">8.6%</td>
          </tr>
          <tr>
            <td class="py-2.5 pl-2 font-sans text-neutral-600 dark:text-neutral-400">Summanen (2), Koga (2), Blakstad, Hamano, Vinberg, Thomas, Ahtinen (1 each)</td>
            <td class="py-2.5 font-sans text-neutral-500">Midfield & Defense</td>
            <td class="py-2.5 text-center font-bold">11</td>
            <td class="py-2.5 text-center">16</td>
            <td class="py-2.5 text-right pr-2">31.4%</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Heatmap Image Visual Overlay -->
    <div class="my-4">
      <h3 class="text-base font-bold text-neutral-900 dark:text-white mb-2">
        Spatial Heatmap: Overlapping Zones & Left Half-Space Overload
      </h3>
      <div class="rounded-xl overflow-hidden border border-neutral-200 dark:border-neutral-800 bg-[#06090E] p-2">
        <img src="{{ '/assets/images/evaluations/tottenham_positionless_heatmap.png' | relative_url }}" alt="Tottenham Positionless Attack Heatmap Overlay" class="w-full h-auto rounded-lg shadow-lg">
      </div>
      <p class="text-xs sm:text-sm text-neutral-500 dark:text-neutral-400 mt-2 italic text-center">
        Overlapping spatial zones: 74.2% spatial overlap between attacking midfielders and forwards, with 58.6% of box touches coming from non-traditional number nines.
      </p>
    </div>

    <!-- Spatial Table -->
    <div class="overflow-x-auto">
      <table class="w-full text-xs sm:text-sm text-left border-collapse">
        <thead>
          <tr class="border-b border-neutral-200 dark:border-neutral-700 text-neutral-500 dark:text-neutral-400 font-mono">
            <th class="py-2 pl-2">Player</th>
            <th class="py-2 text-center">Left Half-Space</th>
            <th class="py-2 text-center">Central Box</th>
            <th class="py-2 text-center">Right Half-Space</th>
            <th class="py-2 text-center">Box Touches / 90</th>
            <th class="py-2 text-right pr-2">Fluidity Score</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-neutral-100 dark:divide-neutral-800 font-mono">
          <tr>
            <td class="py-2 pl-2 font-sans font-semibold">Olivia Holdt</td>
            <td class="py-2 text-center">26.2%</td>
            <td class="py-2 text-center">22.4%</td>
            <td class="py-2 text-center">21.1%</td>
            <td class="py-2 text-center">3.82</td>
            <td class="py-2 text-right pr-2 font-bold text-emerald-600 dark:text-emerald-400">92.4 (Free Role)</td>
          </tr>
          <tr>
            <td class="py-2 pl-2 font-sans font-semibold">Signe Gaupset (Siggy)</td>
            <td class="py-2 text-center">31.8%</td>
            <td class="py-2 text-center">28.6%</td>
            <td class="py-2 text-center">17.5%</td>
            <td class="py-2 text-center font-bold text-neutral-900 dark:text-white">5.34 (92nd %ile)</td>
            <td class="py-2 text-right pr-2 font-bold text-emerald-600 dark:text-emerald-400">94.1 (Depth Attacker)</td>
          </tr>
          <tr>
            <td class="py-2 pl-2 font-sans font-semibold">Julie Blakstad</td>
            <td class="py-2 text-center">28.3%</td>
            <td class="py-2 text-center">14.2%</td>
            <td class="py-2 text-center">8.1%</td>
            <td class="py-2 text-center">2.45</td>
            <td class="py-2 text-right pr-2">81.0 (Inside Runner)</td>
          </tr>
          <tr>
            <td class="py-2 pl-2 font-sans font-semibold text-neutral-500">Cathinka Tandberg</td>
            <td class="py-2 text-center text-neutral-500">12.4%</td>
            <td class="py-2 text-center font-bold">65.8%</td>
            <td class="py-2 text-center text-neutral-500">11.2%</td>
            <td class="py-2 text-center">6.84</td>
            <td class="py-2 text-right pr-2 text-neutral-500">44.0 (Box Anchor)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- Part 2: Defense & Toko Koga -->
  <div class="rounded-xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/50 dark:bg-[#121215] p-5 sm:p-6 space-y-4">
    <h2 class="text-xl font-bold text-neutral-900 dark:text-white flex items-center gap-2">
      <span>2. The Defensive Unit: The Transformative Impact of Toko Koga</span>
    </h2>

    <p>
      Beyond the attack, we must address the back line. Last season, the arrival of <strong>Toko Koga</strong> transformed this defense. Completely.
    </p>

    <p>
      It is hard to overstate her impact: 1,705 league minutes, 2 goals, and an assist, while being Spurs' most composed operator on the ball and in 1v1 duels. By any measure, she was our best performer.
    </p>

    <p>
      Her absence during the Women's Asian Cup was glaring: without Koga anchoring the backline, old vulnerabilities resurfaced. The on/off splits illustrate the team's absolute structural dependence on her:
    </p>

    <!-- Toko Koga Impact Table -->
    <div class="overflow-x-auto">
      <table class="w-full text-xs sm:text-sm text-left border-collapse">
        <thead>
          <tr class="border-b border-neutral-200 dark:border-neutral-700 text-neutral-500 font-mono">
            <th class="py-2 pl-2">Defensive Performance Metric</th>
            <th class="py-2 text-center">With Toko Koga (19 Matches)</th>
            <th class="py-2 text-center">Without Koga / Asian Cup (3 Matches)</th>
            <th class="py-2 text-right pr-2">Tactical Takeaway</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-neutral-100 dark:divide-neutral-800 font-mono">
          <tr>
            <td class="py-2.5 pl-2 font-sans font-semibold">Goals Conceded per Match</td>
            <td class="py-2.5 text-center font-bold text-emerald-600 dark:text-emerald-400">1.47</td>
            <td class="py-2.5 text-center font-bold text-red-600 dark:text-red-400">3.33 (10 goals in 3 games)</td>
            <td class="py-2.5 text-right pr-2 font-sans text-neutral-500">More than double concession rate</td>
          </tr>
          <tr>
            <td class="py-2.5 pl-2 font-sans font-semibold">Clean Sheets</td>
            <td class="py-2.5 text-center font-bold">6 matches (100% of team total)</td>
            <td class="py-2.5 text-center font-bold text-red-500">0</td>
            <td class="py-2.5 text-right pr-2 font-sans text-neutral-500">Zero clean sheets without Koga</td>
          </tr>
          <tr>
            <td class="py-2.5 pl-2 font-sans font-semibold">Opposition Shots Faced per Match</td>
            <td class="py-2.5 text-center">11.8</td>
            <td class="py-2.5 text-center font-bold text-red-500">18.3</td>
            <td class="py-2.5 text-right pr-2 font-sans text-neutral-500">+55% surge in defensive exposure</td>
          </tr>
          <tr>
            <td class="py-2.5 pl-2 font-sans font-semibold">Win Rate</td>
            <td class="py-2.5 text-center font-bold text-emerald-600">52.6% (10 wins)</td>
            <td class="py-2.5 text-center font-bold text-red-500">0.0% (0 wins)</td>
            <td class="py-2.5 text-right pr-2 font-sans text-neutral-500">Complete collapse in results</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p class="text-sm sm:text-base text-neutral-700 dark:text-neutral-300">
      The partnership of <strong>Koga and Clare Hunt</strong> in central defense (Hunt played 1,440 minutes) gave Spurs an identity. With Charlotte Grant and Molly Bartrip departing, finding the right complementary partner alongside Koga is the single most critical defensive task for 2026/27.
    </p>
  </div>

  <!-- Part 3: Goalkeeper Side Note - Lize Kop -->
  <div class="rounded-xl border border-amber-200 dark:border-amber-900/40 bg-amber-50/40 dark:bg-[#181510] p-5 sm:p-6 space-y-3">
    <div class="flex items-center gap-2 text-amber-700 dark:text-amber-400 font-bold text-base">
      <span>⚠️ Goalkeeping Note: The Question Mark Around Lize Kop</span>
    </div>
    
    <p class="text-sm sm:text-base text-neutral-700 dark:text-neutral-300">
      I remain unconvinced that <strong>Lize Kop</strong> should hold the starting goalkeeper shirt uncontested throughout the campaign. Her underlying numbers place her near the bottom tier of the league:
    </p>

    <!-- Goalkeeping Comparison Table -->
    <div class="overflow-x-auto pt-1">
      <table class="w-full text-xs sm:text-sm text-left border-collapse">
        <thead>
          <tr class="border-b border-amber-200 dark:border-amber-800/60 text-neutral-500 font-mono">
            <th class="py-1.5 pl-2">Club / Goalkeeper</th>
            <th class="py-1.5 text-center">Matches</th>
            <th class="py-1.5 text-center">GA per 90</th>
            <th class="py-1.5 text-center">Save %</th>
            <th class="py-1.5 text-right pr-2">WSL Rank</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-amber-100 dark:divide-amber-900/30 font-mono">
          <tr>
            <td class="py-2 pl-2 font-sans font-semibold text-neutral-900 dark:text-white">Tottenham (Lize Kop)</td>
            <td class="py-2 text-center">22</td>
            <td class="py-2 text-center font-bold text-red-600 dark:text-red-400">1.73 (38 Total)</td>
            <td class="py-2 text-center font-bold text-red-600 dark:text-red-400">62.4%</td>
            <td class="py-2 text-right pr-2 text-neutral-500">10th of 12</td>
          </tr>
          <tr class="text-neutral-500 dark:text-neutral-400">
            <td class="py-2 pl-2 font-sans">Chelsea (Benchmark)</td>
            <td class="py-2 text-center">22</td>
            <td class="py-2 text-center">0.91 (20 Total)</td>
            <td class="py-2 text-center">74.4%</td>
            <td class="py-2 text-right pr-2">1st</td>
          </tr>
          <tr class="text-neutral-500 dark:text-neutral-400">
            <td class="py-2 pl-2 font-sans">Arsenal & Man City (Benchmark)</td>
            <td class="py-2 text-center">22</td>
            <td class="py-2 text-center">0.64–0.86</td>
            <td class="py-2 text-center">73.6%</td>
            <td class="py-2 text-right pr-2">Top 3</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-400">
      With a 62.4% save rate, the arrival of 23-year-old Norwegian international goalkeeper <strong>Selma Panengstuen</strong> should spark an open, healthy battle for the number one spot.
    </p>
  </div>

  <!-- Outro & Forward Links -->
  <div class="pt-4 flex items-center justify-between border-t border-neutral-200 dark:border-neutral-800 text-sm font-mono">
    <a href="{{ '/en/teams/tottenham/' | relative_url }}" class="text-neutral-600 dark:text-neutral-400 hover:text-neutral-900 dark:hover:text-white">
      ← Part I: Identity & Leadership
    </a>
    <a href="{{ '/en/teams/tottenham/defense/' | relative_url }}" class="text-neutral-900 dark:text-white font-bold hover:underline">
      Part III: Defensive Deep Dive →
    </a>
  </div>

  <!-- Standardized Post Pagination -->
  {% include post_pagination.html %}

</div>
