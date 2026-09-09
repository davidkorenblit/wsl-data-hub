---
layout: default
title: "Metrics Reference & Dictionary | WSL Data Hub"
permalink: /en/metrics/
prev_url: /en/methodology/
prev_title: "Methodology & Framework"
lang: en
alt_url: /metrics/
---

<div class="space-y-6">

  <!-- Header -->
  <div class="border-b border-neutral-200 dark:border-neutral-800 pb-4">
    <div class="text-xs font-mono uppercase text-neutral-500 dark:text-neutral-400 font-bold tracking-wider mb-1">
      DATA DICTIONARY & METRICS
    </div>
    <h1 class="text-2xl md:text-3xl font-bold tracking-tight text-neutral-900 dark:text-white mb-2">
      Metrics Reference & Technical Definitions
    </h1>
    <p class="text-sm sm:text-base text-neutral-600 dark:text-neutral-300 leading-relaxed font-sans">
      A comprehensive guide to all core metrics, calculation formulas, and analytical rationales used across our club evaluations.
    </p>
  </div>

  <!-- Main Content Card -->
  <div class="rounded-md border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-[#121215] p-6 space-y-8 text-neutral-800 dark:text-neutral-200 leading-relaxed font-sans">

    <!-- Overview Note -->
    <div class="p-3.5 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 text-xs sm:text-sm text-neutral-600 dark:text-neutral-300">
      <strong class="text-neutral-900 dark:text-white font-mono uppercase text-[11px]">Data Source:</strong> Powered by FBref and Opta/FotMob event logs across the WSL and major domestic competitions. All volume metrics are normalized per 90 minutes (Per 90) for accurate comparative analysis.
    </div>

    <!-- 1. Attack & Finishing -->
    <section class="space-y-3 pt-2">
      <div class="text-xs font-mono uppercase text-neutral-500 dark:text-neutral-400 font-bold tracking-wider mb-1">
        CATEGORY 01
      </div>
      <h2 class="text-xl font-bold text-neutral-900 dark:text-white">
        1. Attack, Shot Generation & Finishing Efficiency
      </h2>
      <div class="space-y-2.5">
        <div class="p-3 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900 dark:text-white">GF / GF per 90 (Goals For)</span>
            <span class="text-[10px] font-mono border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-neutral-900 px-1.5 py-0.5 rounded text-neutral-600 dark:text-neutral-300">Actual Goals</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300">Total goals scored by the team and the average per 90 minutes.</p>
        </div>

        <div class="p-3 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900 dark:text-white">Sh/90 (Shots per 90)</span>
            <span class="text-[10px] font-mono border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-neutral-900 px-1.5 py-0.5 rounded text-neutral-600 dark:text-neutral-300">Shot Volume</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300">Average number of shots produced per 90 minutes.</p>
        </div>

        <div class="p-3 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900 dark:text-white">SoT% (Shots on Target Percentage)</span>
            <span class="text-[10px] font-mono border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-neutral-900 px-1.5 py-0.5 rounded text-neutral-600 dark:text-neutral-300">Target Accuracy</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300">Percentage of total shots that hit the target.</p>
        </div>

        <div class="p-3 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900 dark:text-white">G/Sh (Goals per Shot)</span>
            <span class="text-[10px] font-mono border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-neutral-900 px-1.5 py-0.5 rounded text-neutral-600 dark:text-neutral-300">Conversion Rate</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300">Conversion efficiency measuring how many goals are scored per shot taken.</p>
        </div>
      </div>
    </section>

    <!-- 2. Creation & Passing -->
    <section class="space-y-3 pt-4 border-t border-neutral-200 dark:border-neutral-800">
      <div class="text-xs font-mono uppercase text-neutral-500 dark:text-neutral-400 font-bold tracking-wider mb-1">
        CATEGORY 02
      </div>
      <h2 class="text-xl font-bold text-neutral-900 dark:text-white">
        2. Creativity, Playmaking & Chance Creation
      </h2>
      <div class="space-y-2.5">
        <div class="p-3 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900 dark:text-white">Ast / Ast per 90 (Assists)</span>
            <span class="text-[10px] font-mono border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-neutral-900 px-1.5 py-0.5 rounded text-neutral-600 dark:text-neutral-300">Direct Assists</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300">Final passes leading directly to a goal, normalized per 90 minutes.</p>
        </div>

        <div class="p-3 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900 dark:text-white">Poss% (Possession Percentage)</span>
            <span class="text-[10px] font-mono border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-neutral-900 px-1.5 py-0.5 rounded text-neutral-600 dark:text-neutral-300">Ball Control</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300">Share of total completed passes / match time controlled by the team.</p>
        </div>
      </div>
    </section>

    <!-- 3. Defense & Goalkeeping -->
    <section class="space-y-3 pt-4 border-t border-neutral-200 dark:border-neutral-800">
      <div class="text-xs font-mono uppercase text-neutral-500 dark:text-neutral-400 font-bold tracking-wider mb-1">
        CATEGORY 03
      </div>
      <h2 class="text-xl font-bold text-neutral-900 dark:text-white">
        3. Defensive Solidity, Prevention & Goalkeeping
      </h2>
      <div class="space-y-2.5">
        <div class="p-3 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900 dark:text-white">GA / GA per 90 (Goals Against)</span>
            <span class="text-[10px] font-mono border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-neutral-900 px-1.5 py-0.5 rounded text-neutral-600 dark:text-neutral-300">Goals Conceded</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300">Total goals conceded by the team and average conceded per 90 minutes.</p>
        </div>

        <div class="p-3 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900 dark:text-white">Save% (Save Percentage)</span>
            <span class="text-[10px] font-mono border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-neutral-900 px-1.5 py-0.5 rounded text-neutral-600 dark:text-neutral-300">Save Rate</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300">Proportion of on-target shots faced that were saved by the goalkeeper.</p>
        </div>

        <div class="p-3 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900 dark:text-white">PSxG +/- (Post-Shot xG Difference)</span>
            <span class="text-[10px] font-mono border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-neutral-900 px-1.5 py-0.5 rounded text-neutral-600 dark:text-neutral-300">Shot Stopping Quality</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300">Advanced metric calculating goals prevented relative to the post-shot trajectory quality of attempts on target. Positive values denote exceptional shot-stopping.</p>
        </div>
      </div>
    </section>

    <!-- 4. Macro & Benchmarks -->
    <section class="space-y-3 pt-4 border-t border-neutral-200 dark:border-neutral-800">
      <div class="text-xs font-mono uppercase text-neutral-500 dark:text-neutral-400 font-bold tracking-wider mb-1">
        CATEGORY 04
      </div>
      <h2 class="text-xl font-bold text-neutral-900 dark:text-white">
        4. Expectation Modeling & Projections (Baseline Benchmarks)
      </h2>
      <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300">
        Benchmark models calculating expected team production relative to league averages:
      </p>

      <div class="space-y-2.5">
        <div class="p-3.5 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="font-mono text-xs font-bold text-neutral-900 dark:text-white">1. Expected Goals Conceded (xGA)</div>
          <p class="text-xs text-neutral-700 dark:text-neutral-300">
            <strong>Formula:</strong> <code class="font-mono text-xs text-neutral-900 dark:text-white bg-white dark:bg-neutral-900 px-1 py-0.5 rounded border border-neutral-200 dark:border-neutral-700">xGA = SoTA × (1 - League Average Save%)</code>
          </p>
        </div>

        <div class="p-3.5 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="font-mono text-xs font-bold text-neutral-900 dark:text-white">2. Expected Goals Scored (xGF)</div>
          <p class="text-xs text-neutral-700 dark:text-neutral-300">
            <strong>Formula:</strong> <code class="font-mono text-xs text-neutral-900 dark:text-white bg-white dark:bg-neutral-900 px-1 py-0.5 rounded border border-neutral-200 dark:border-neutral-700">xGF = SoT × League Goals per Shot on Target</code>
          </p>
        </div>

        <div class="p-3.5 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="font-mono text-xs font-bold text-neutral-900 dark:text-white">3. Expected Assists (xAst)</div>
          <p class="text-xs text-neutral-700 dark:text-neutral-300">
            <strong>Formula:</strong> <code class="font-mono text-xs text-neutral-900 dark:text-white bg-white dark:bg-neutral-900 px-1 py-0.5 rounded border border-neutral-200 dark:border-neutral-700">xAst = GF × League Assists to Goals Ratio</code>
          </p>
        </div>

        <div class="p-3.5 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="font-mono text-xs font-bold text-neutral-900 dark:text-white">4. Expected Points (xPTS) from Goal Difference Regression</div>
          <p class="text-xs text-neutral-700 dark:text-neutral-300">
            <strong>22-Match Season Formula:</strong> <code class="font-mono text-xs text-neutral-900 dark:text-white bg-white dark:bg-neutral-900 px-1 py-0.5 rounded border border-neutral-200 dark:border-neutral-700">xPTS = 0.576 × GD + 31.0</code>
          </p>
          <p class="text-xs text-neutral-700 dark:text-neutral-300 mt-1">
            <strong>Expanded 26-Match Season Formula (14 clubs):</strong> <code class="font-mono text-xs text-neutral-900 dark:text-white bg-white dark:bg-neutral-900 px-1 py-0.5 rounded border border-neutral-200 dark:border-neutral-700">xPTS_26 = 0.576 × GD + 36.6</code>
          </p>
        </div>
      </div>
    </section>

    <!-- 5. Advanced Creation & Quality Metrics (Opta / FotMob) -->
    <section class="space-y-3 pt-4 border-t border-neutral-200 dark:border-neutral-800">
      <div class="text-xs font-mono uppercase text-neutral-500 dark:text-neutral-400 font-bold tracking-wider mb-1">
        CATEGORY 05
      </div>
      <h2 class="text-xl font-bold text-neutral-900 dark:text-white">
        5. Advanced Creation, Territory & Pressure Metrics (Opta / FotMob)
      </h2>
      <div class="space-y-2.5">
        <div class="p-3 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900 dark:text-white">Chances Created / Big Chances</span>
            <span class="text-[10px] font-mono border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-neutral-900 px-1.5 py-0.5 rounded text-neutral-600 dark:text-neutral-300">Key Passes</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300">Key passes leading to an attempt (Chances Created) and clear-cut 1v1 situations (Big Chances Created).</p>
        </div>

        <div class="p-3 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900 dark:text-white">Touches in Opposition Box</span>
            <span class="text-[10px] font-mono border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-neutral-900 px-1.5 py-0.5 rounded text-neutral-600 dark:text-neutral-300">Box Presence</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300">Ball touches and actions inside the opponent's 18-yard penalty area — a vital proxy for attacking territory and direct goal threat.</p>
        </div>

        <div class="p-3 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900 dark:text-white">Possession Won Final 3rd</span>
            <span class="text-[10px] font-mono border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-neutral-900 px-1.5 py-0.5 rounded text-neutral-600 dark:text-neutral-300">High Regains</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300">Ball recoveries and tackles won inside the attacking third — measuring counter-pressing intensity and high-turnover generation.</p>
        </div>

        <div class="p-3 bg-neutral-50 dark:bg-[#18181b] rounded border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-neutral-900 dark:text-white">Positional Percentiles</span>
            <span class="text-[10px] font-mono border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-neutral-900 px-1.5 py-0.5 rounded text-neutral-600 dark:text-neutral-300">Percentile Ranks</span>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-300">Player statistical rankings compared directly against peers in the same position across the Top 5 European leagues and the UEFA Women's Champions League (UWCL).</p>
        </div>
      </div>
    </section>

  </div>

  <!-- Standardized Post Pagination -->
  {% include post_pagination.html %}

</div>
