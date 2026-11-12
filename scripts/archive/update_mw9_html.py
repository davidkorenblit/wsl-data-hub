import re

# Template for the updated Arsenal widget
updated_widget = """        <!-- ================= INTERACTIVE ARSENAL SIMULATION WIDGET ================= -->
        <div class="my-6 rounded-xl border border-neutral-200 dark:border-neutral-800 bg-neutral-900 text-white p-4 sm:p-6 shadow-md">
          <div class="flex items-center justify-between border-b border-neutral-800 pb-3 mb-4 flex-wrap gap-2">
            <div>
              <div class="text-xs font-mono uppercase text-red-400 font-bold tracking-wider">
                TACTICAL SIMULATION & TELESTRATOR · הדמיית שערים ומסך שידור
              </div>
              <h3 class="text-lg sm:text-xl font-bold text-white mt-0.5">
                שבלונת הספיגה של ארסנל במעברים: 5 משחקים שונים
              </h3>
            </div>
            
            <!-- View Mode Switcher -->
            <div class="flex items-center gap-1.5 p-1 bg-neutral-800 rounded-lg border border-neutral-700">
              <button id="view-mode-telestrator" type="button" onclick="setArsenalViewMode('telestrator')" class="px-3 py-1.5 rounded-md text-xs font-sans font-bold transition-all bg-primary-600 text-white shadow-xs flex items-center gap-1.5">
                <span>📺</span>
                <span>פריים שידור חי (Telestrator)</span>
              </button>
              <button id="view-mode-tactical" type="button" onclick="setArsenalViewMode('tactical')" class="px-3 py-1.5 rounded-md text-xs font-sans text-neutral-400 hover:text-white transition-all flex items-center gap-1.5">
                <span>📋</span>
                <span>לוח טקטי דו-ממדי</span>
              </button>
            </div>
          </div>

          <!-- Goal Selector Tabs (Switches both views) -->
          <div class="mb-4">
            <div class="text-xs font-sans text-neutral-400 mb-2 font-medium">בחר שער להדמיה (מעבר בין 5 המשחקים):</div>
            <div id="ars-sim-tabs" class="flex items-center gap-2 overflow-x-auto pb-2 scrollbar-thin">
              <!-- Rendered by JS -->
            </div>
          </div>

          <!-- 1. TELESTRATOR VIEW CONTAINER (Default) -->
          <div id="ars-telestrator-container" class="space-y-3">
            <div class="flex items-center justify-between flex-wrap gap-2 text-xs font-sans border-b border-neutral-800/80 pb-2">
              <div id="telestrator-step-controls" class="flex items-center gap-1.5">
                <span class="text-xs font-mono text-neutral-400">שלב מהלך:</span>
                <button id="tele-step-buildup" type="button" onclick="setTelestratorStep('buildup')" class="px-2.5 py-1 text-xs font-sans font-bold rounded bg-amber-500 text-black border border-amber-400 transition-colors">
                  1. שחרור המסירה (Buildup)
                </button>
                <button id="tele-step-sprint" type="button" onclick="setTelestratorStep('sprint')" class="px-2.5 py-1 text-xs font-sans rounded bg-neutral-800 text-neutral-300 hover:text-white border border-neutral-700 transition-colors">
                  2. הספרינט ל-1v1 (Sprint)
                </button>
                <button id="tele-autoplay-btn" type="button" onclick="toggleTelestratorAutoplay()" class="px-2.5 py-1 text-xs font-sans rounded bg-neutral-800 text-neutral-300 hover:text-white border border-neutral-700 transition-colors flex items-center gap-1">
                  <span>▶</span>
                  <span>נגן שלבים</span>
                </button>
              </div>
              <div id="tele-step-title" class="text-amber-400 font-bold font-sans text-xs">
                שלב 1: שחרור המסירה (קו הגנה גבוה)
              </div>
            </div>

            <!-- Telestrator Image + SVG Overlay -->
            <div class="relative w-full aspect-[16/9] max-w-4xl mx-auto rounded-lg overflow-hidden border border-neutral-700 bg-black shadow-inner select-none">
              <img id="tele-frame-img" src="{{ '/assets/images/arsenal_conceded/mw9_olsson_buildup.jpg' | relative_url }}" alt="Arsenal Conceded Goal Broadcast Frame" class="w-full h-full object-cover block">
              <svg id="tele-svg-overlay" viewBox="0 0 1920 1080" class="absolute inset-0 w-full h-full pointer-events-none">
                <!-- Rendered dynamically by mw9-widgets.js -->
              </svg>
            </div>

            <!-- Telestrator Dynamic Description -->
            <div id="tele-step-desc" class="p-3 bg-neutral-950/80 rounded-lg border border-neutral-800 text-xs sm:text-sm text-neutral-300 font-sans leading-relaxed">
              שחרור המסירה: קו ההגנה של ארסנל עומד סביב קו האמצע באנפילד. כדור ארוך מוקפץ מעל הראש של ליאה וויליאמסון לתוך 38 מטרים של דשא פנוי לחלוטין.
            </div>
          </div>

          <!-- 2. TACTICAL 2D PITCH CONTAINER (Secondary) -->
          <div id="ars-tactical-container" style="display:none;" class="space-y-3">
            <div class="flex items-center justify-end gap-2 text-xs font-mono">
              <span class="text-neutral-400">מהירות:</span>
              <button id="sim-speed-1x" type="button" onclick="setSimSpeed(1.0)" class="px-2 py-1 text-xs font-mono font-bold rounded bg-primary-600 text-white">1x</button>
              <button id="sim-speed-15x" type="button" onclick="setSimSpeed(1.5)" class="px-2 py-1 text-xs font-mono rounded bg-neutral-800 text-neutral-400 hover:text-white">1.5x</button>
            </div>

            <div class="relative w-full aspect-[800/520] max-w-3xl mx-auto rounded-lg overflow-hidden border border-neutral-700 bg-[#16351c] shadow-inner select-none">
              <svg id="ars-tactical-pitch" viewBox="0 0 800 520" class="w-full h-full block">
                <defs>
                  <pattern id="pitch-stripes" width="80" height="520" patternUnits="userSpaceOnUse">
                    <rect width="40" height="520" fill="#183b1f" />
                    <rect x="40" width="40" height="520" fill="#1a4223" />
                  </pattern>
                  <marker id="arrow-pass" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#FBBF24" />
                  </marker>
                  <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
                    <feGaussianBlur stdDeviation="3" result="blur" />
                    <feComposite in="SourceGraphic" in2="blur" operator="over" />
                  </filter>
                </defs>

                <rect width="800" height="520" fill="url(#pitch-stripes)" />

                <g stroke="rgba(255,255,255,0.4)" stroke-width="2" fill="none">
                  <rect x="20" y="20" width="760" height="480" />
                  <line x1="400" y1="20" x2="400" y2="500" />
                  <circle cx="400" cy="260" r="60" />
                  <circle cx="400" cy="260" r="3" fill="rgba(255,255,255,0.5)" />

                  <rect x="20" y="140" width="130" height="240" />
                  <rect x="20" y="195" width="45" height="130" />
                  <path d="M 150 215 A 60 60 0 0 1 150 305" />
                  <rect x="6" y="225" width="14" height="70" stroke="rgba(255,255,255,0.7)" fill="rgba(255,255,255,0.1)" />

                  <rect x="650" y="140" width="130" height="240" />
                  <rect x="735" y="195" width="45" height="130" />
                  <path d="M 650 215 A 60 60 0 0 0 650 305" />
                  <rect x="780" y="225" width="14" height="70" stroke="rgba(255,255,255,0.7)" fill="rgba(255,255,255,0.1)" />
                </g>

                <g id="sim-highline-group">
                  <line x1="330" y1="20" x2="330" y2="500" stroke="#EF4444" stroke-width="1.5" stroke-dasharray="6 4" opacity="0.65" />
                  <rect x="335" y="30" width="165" height="20" rx="4" fill="rgba(239, 68, 68, 0.85)" />
                  <text x="417" y="44" fill="#ffffff" font-size="10" font-family="sans-serif" font-weight="bold" text-anchor="middle">
                    קו הגנה גבוה (40 מ' מהשער)
                  </text>
                </g>

                <rect x="65" y="60" width="260" height="400" fill="rgba(239,68,68,0.06)" rx="8" />
                <text x="195" y="475" fill="rgba(255,255,255,0.3)" font-size="11" font-family="sans-serif" text-anchor="middle">
                  שטח מופקר לחלוטין (35–45 מטרים ללא חיפוי)
                </text>

                <path id="sim-elem-passline" d="" fill="none" stroke="#FBBF24" stroke-width="2.5" stroke-dasharray="5 3" marker-end="url(#arrow-pass)" />
                <circle id="sim-elem-turnover" cx="0" cy="0" r="10" fill="#EF4444" stroke="#FFFFFF" stroke-width="2" filter="url(#glow)" style="display:none;" />

                <g id="sim-elem-striker" transform="translate(0,0)">
                  <circle r="14" fill="#3B82F6" stroke="#FFFFFF" stroke-width="2" filter="url(#glow)" />
                  <text y="4" fill="#FFFFFF" font-size="11" font-family="sans-serif" font-weight="bold" text-anchor="middle">9</text>
                  <text y="25" fill="#FBBF24" font-size="10" font-family="sans-serif" font-weight="bold" text-anchor="middle">חלוצה</text>
                </g>

                <g id="sim-elem-defender" transform="translate(0,0)">
                  <circle r="14" fill="#DC2626" stroke="#FFFFFF" stroke-width="2" filter="url(#glow)" />
                  <text y="4" fill="#FFFFFF" font-size="10" font-family="sans-serif" font-weight="bold" text-anchor="middle">6</text>
                  <text y="25" fill="#FFFFFF" font-size="10" font-family="sans-serif" font-weight="bold" text-anchor="middle">וויליאמסון</text>
                </g>

                <g id="sim-elem-gk" transform="translate(0,0)">
                  <circle r="13" fill="#EAB308" stroke="#000000" stroke-width="1.5" />
                  <text y="4" fill="#000000" font-size="10" font-family="sans-serif" font-weight="bold" text-anchor="middle">GK</text>
                  <text y="24" fill="#EAB308" font-size="9" font-family="sans-serif" text-anchor="middle">מיסה</text>
                </g>

                <circle id="sim-elem-ball" cx="0" cy="0" r="6" fill="#FFFFFF" stroke="#000000" stroke-width="1.5" filter="url(#glow)" />

                <g id="sim-elem-goal-banner" style="display:none;">
                  <rect x="250" y="220" width="300" height="70" rx="10" fill="rgba(15,23,42,0.95)" stroke="#10B981" stroke-width="2" />
                  <text x="400" y="250" fill="#10B981" font-size="18" font-family="sans-serif" font-weight="bold" text-anchor="middle">
                    ⚽ שער ברשת!
                  </text>
                  <text x="400" y="274" fill="#FFFFFF" font-size="12" font-family="sans-serif" text-anchor="middle">
                    1 על 1 מושלם · אותה תבנית ספיגה
                  </text>
                </g>
              </svg>
            </div>

            <div class="mt-4 flex flex-col sm:flex-row sm:items-center justify-between gap-3 pt-3 border-t border-neutral-800">
              <div class="flex items-center gap-3">
                <button id="sim-play-btn" type="button" onclick="toggleSimPlay()" class="px-4 py-2 rounded-lg bg-primary-600 hover:bg-primary-500 text-white font-bold text-xs sm:text-sm font-sans flex items-center gap-2 transition-colors shadow-sm">
                  <span class="inline-block w-3 text-center">▶</span>
                  <span>נגן הדמיה</span>
                </button>
                <button type="button" onclick="replaySim()" class="px-3 py-2 rounded-lg bg-neutral-800 hover:bg-neutral-700 text-neutral-300 font-medium text-xs sm:text-sm font-sans flex items-center gap-1.5 transition-colors">
                  <span>🔄</span>
                  <span>התחל מחדש</span>
                </button>
              </div>

              <div class="flex-1 max-w-md flex items-center gap-2">
                <span class="text-[11px] font-mono text-neutral-400">שלב:</span>
                <input id="sim-scrubber" type="range" min="0" max="100" value="0" oninput="handleScrub(this.value)" class="w-full accent-primary-500 cursor-pointer h-1.5 bg-neutral-700 rounded-lg">
              </div>
            </div>

            <div id="sim-phase-label" class="mt-2 text-xs font-mono text-amber-300/90 text-center sm:text-right">
              שלב 1: קו הגנה גבוה של ארסנל (40 מ' מהשער) · איבוד כדור במעבר
            </div>
          </div>

          <!-- Goal Metadata Card (Shared across views) -->
          <div class="mt-4 p-3.5 rounded-lg bg-neutral-950/70 border border-neutral-800 text-xs font-sans space-y-2">
            <div class="flex items-center justify-between flex-wrap gap-2 border-b border-neutral-800/80 pb-2">
              <div class="font-bold text-white text-sm flex items-center gap-2">
                <span class="text-primary-400">📌</span>
                <span id="sim-detail-match">ליברפול 1 – 2 ארסנל (מחזור 9)</span>
              </div>
              <div class="flex items-center gap-2">
                <span class="px-2 py-0.5 rounded bg-red-950/80 text-red-300 font-mono font-bold border border-red-800/60" id="sim-detail-scorer">אוליביה אולסון (דקה 15')</span>
                <span class="px-2 py-0.5 rounded bg-neutral-800 text-neutral-300 font-mono" id="sim-detail-xg">0.48 xG</span>
              </div>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 text-neutral-300 pt-1 text-[11px]">
              <div><strong>מסירת המוצא:</strong> <span id="sim-detail-passer" class="text-neutral-400">ספירי קוברלי (כדור עומק ארוך)</span></div>
              <div><strong>הבלמית במרדף:</strong> <span id="sim-detail-defender" class="text-neutral-400">ליאה וויליאמסון</span></div>
              <div><strong>מרחק הספרינט:</strong> <span id="sim-detail-distance" class="text-neutral-400">38 מטרים בשטח פתוח</span></div>
            </div>

            <p id="sim-detail-desc" class="text-neutral-400 text-[11px] leading-relaxed pt-1 border-t border-neutral-800/50">
              ארסנל לוחצת גבוה באנפילד, קו ההגנה עומד 40 מטר מהשער שלה. איבוד כדור במעבר מוביל להקשת כדור ישירה מעל וויליאמסון. אולסון רצה קדימה כשוויליאמסון רצה לאחור ללא חיפוי, 1 על 1 נקי מול מיסה וסיומת מדויקת לרשת.
            </p>
          </div>
        </div>"""

def update_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern for the old widget block
    old_widget_pattern = r'<!-- ================= INTERACTIVE ARSENAL SIMULATION WIDGET ================= -->.*?<!-- ================= SECTION 3: CHELSEA vs EVERTON ================= -->'
    
    replacement = updated_widget + "\n\n        <p>\n          <strong>ההערה השנייה: התקפית.</strong>"
    
    # Let's check where the widget starts and ends
    start_str = "<!-- ================= INTERACTIVE ARSENAL SIMULATION WIDGET ================= -->"
    end_str = "<!-- Goal Metadata Card -->"
    
    # We want to replace from start_str through the closing </div> of the widget
    # Let's find the closing </div> right before "<strong>ההערה השנייה: התקפית.</strong>"
    idx_start = content.find(start_str)
    idx_end = content.find("<strong>ההערה השנייה: התקפית.</strong>")
    
    if idx_start == -1 or idx_end == -1:
        print(f"Error finding boundaries in {path}")
        return False

    # Find the last </div> before idx_end
    last_div = content.rfind("</div>", idx_start, idx_end) + len("</div>")
    
    new_content = content[:idx_start] + updated_widget + content[last_div:]
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {path} successfully!")
    return True

update_file('weekly/mw9.md')
update_file('weekly.md')
