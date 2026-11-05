---
layout: default
title: "מפת התוהו ובוהו: סחרחרת ההרכבים של רנה סלגרס בארסנל (מחזורים 1–8) | WSL Data Hub"
permalink: /weekly/arsenal-rotations/
lang: he
alt_url: /en/weekly/
prev_url: /weekly/mw8/
prev_title: "חזרה לטור השבועי מחזור 8"
next_url: null
next_title: null
---

<div class="space-y-8 max-w-5xl mx-auto">

  <!-- Header & Breadcrumbs -->
  <div class="border-b border-neutral-200 dark:border-neutral-800 pb-5">
    <div class="flex items-center justify-between gap-3 flex-wrap mb-2">
      <div class="flex items-center gap-2">
        <span class="text-xs font-mono font-bold px-2.5 py-0.5 rounded bg-red-100 dark:bg-red-950/60 text-red-700 dark:text-red-300 border border-red-300 dark:border-red-800/80">
          לוח טקטי מורחב · עונת 2026/27
        </span>
        <span class="text-xs font-mono text-neutral-500 dark:text-neutral-400">
          Matchweeks 1–8
        </span>
      </div>

      <a href="{{ '/weekly/mw8/' | relative_url }}" class="text-xs font-mono text-neutral-600 dark:text-neutral-300 hover:text-red-600 dark:hover:text-red-400 transition-colors flex items-center gap-1.5 font-bold">
        <span>→</span>
        <span>חזרה לטור השבועי המלא (מחזור 8)</span>
      </a>
    </div>

    <h1 class="text-2xl sm:text-3xl lg:text-4xl font-extrabold text-neutral-900 dark:text-white tracking-tight mt-1">
      סחרחרת ההרכבים של רנה סלגרס: 8 מחזורים, 8 הרכבים שונים ו-0% המשכיות
    </h1>
    
    <p class="text-sm sm:text-base text-neutral-600 dark:text-neutral-300 leading-relaxed font-sans mt-2 max-w-3xl">
      ארסנל יצאה לפגרת הסתיו כשהיא עדיין מחפשת את הזהות היציבה שלה. ב-8 משחקי ליגה, סלגרס לא חזרה על אותו הרכב פותח אפילו פעם אחת. חקרו את הלוח הטקטי האינטראקטיבי: עקבו אחרי מפת הנדידה והפיצולים העונתיים, או בחרו בכל אחד מ-8 המחזורים לצפייה בהרכב ובמערך הנקודתי.
    </p>
  </div>

  <!-- ================= TACTICAL PITCH SCREEN (FULL WIDTH) ================= -->
  <div id="arsenal-tactical-screen" class="rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-[#0c1017] text-white shadow-xl overflow-hidden">
    
    <!-- Screen Header -->
    <div class="p-4 sm:p-5 bg-[#141923] border-b border-neutral-800 flex flex-col md:flex-row md:items-center justify-between gap-3">
      <div>
        <div class="text-xs font-mono font-bold text-red-400 uppercase tracking-wider flex items-center gap-2">
          <span class="w-2.5 h-2.5 rounded-full bg-red-500 animate-pulse"></span>
          <span>לוח טקטי אינטראקטיבי: מפת המגרש</span>
        </div>
        <div class="text-sm sm:text-base font-bold text-neutral-200 mt-1" id="ars-widget-subtitle">
          מפת התוהו ובוהו: רואים ממש על המגרש את השחקניות הנודדות והפיצולים
        </div>
      </div>

      <div class="text-xs font-mono text-neutral-400 bg-neutral-900/80 px-3 py-1.5 rounded-lg border border-neutral-800 self-start md:self-auto">
        עוגני 100%: <strong class="text-emerald-400">וויליאמסון (8/8)</strong> · <strong class="text-emerald-400">סטאנוויי (8/8)</strong>
      </div>
    </div>

    <!-- Pitch Stage -->
    <div class="p-4 sm:p-6 lg:p-8 bg-[#07170e] flex justify-center items-center relative overflow-hidden">
      
      <!-- Pitch Canvas Container -->
      <div class="relative w-full max-w-[720px] h-[580px] sm:h-[640px] rounded-xl border-2 border-emerald-500/50 shadow-2xl overflow-hidden" 
           style="background: radial-gradient(circle at center, #0f3d21 0%, #071a0e 100%);">
        
        <!-- Pitch Markings -->
        <div class="absolute inset-3 border-2 border-white/25 rounded pointer-events-none"></div>
        <div class="absolute top-1/2 left-0 right-0 h-0.5 bg-white/25 -translate-y-1/2 pointer-events-none"></div>
        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-32 h-32 border-2 border-white/25 rounded-full pointer-events-none"></div>
        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-2 h-2 bg-white/50 rounded-full pointer-events-none"></div>

        <!-- Opponent Penalty Box (Top) -->
        <div class="absolute top-3 left-1/2 -translate-x-1/2 w-64 h-24 border-2 border-white/25 border-t-0 pointer-events-none"></div>
        <div class="absolute top-3 left-1/2 -translate-x-1/2 w-32 h-10 border-2 border-white/25 border-t-0 pointer-events-none"></div>

        <!-- Arsenal Penalty Box (Bottom) -->
        <div class="absolute bottom-3 left-1/2 -translate-x-1/2 w-64 h-24 border-2 border-white/25 border-b-0 pointer-events-none"></div>
        <div class="absolute bottom-3 left-1/2 -translate-x-1/2 w-32 h-10 border-2 border-white/25 border-b-0 pointer-events-none"></div>

        <!-- Dynamic Player Nodes Layer (Populated by JS) -->
        <div id="ars-pitch-nodes" class="absolute inset-0">
          <!-- Injected dynamically by mw8-widgets.js -->
        </div>
      </div>
    </div>

    <!-- Navigation Bar: Tabs Directly Underneath the Pitch -->
    <div class="p-4 bg-[#121620] border-t border-neutral-800 flex flex-col sm:flex-row items-center justify-between gap-3">
      <div class="text-xs font-mono font-bold text-neutral-400">
        בחרו תצוגה:
      </div>
      <div class="flex items-center gap-2 flex-wrap font-mono text-xs justify-center" id="ars-tabs-container">
        <!-- Rendered dynamically by JS -->
      </div>
    </div>

    <!-- Dynamic Tactical Notes & Match Information (Underneath Tabs) -->
    <div class="p-5 sm:p-6 bg-[#0f131c] border-t border-neutral-800/80 space-y-4">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between border-b border-neutral-800 pb-3 gap-2">
        <div class="flex items-center gap-3">
          <span class="text-xs font-mono font-bold px-2 py-0.5 rounded bg-red-600/30 text-red-300 border border-red-500/40" id="ars-panel-round">
            עונת 2026/27
          </span>
          <span class="text-xs font-mono px-2 py-0.5 rounded bg-neutral-800 text-neutral-300" id="ars-panel-formation">
            מפת הפיצולים והנדידה
          </span>
        </div>
        <h3 class="text-base sm:text-lg font-bold text-white" id="ars-panel-match">
          סחרחרת ההרכבים: 0% המשכיות, 8 הרכבים שונים
        </h3>
      </div>

      <!-- Injected notes / 4-card overview -->
      <div id="ars-panel-notes" class="font-sans">
        <!-- Injected dynamically by JS -->
      </div>
    </div>

  </div>

  <!-- ================= IN-DEPTH TACTICAL BREAKDOWN ================= -->
  <div class="space-y-4 pt-4">
    <div class="flex items-center gap-2">
      <span class="text-lg">🔍</span>
      <h2 class="text-xl sm:text-2xl font-bold text-neutral-900 dark:text-white">
        ארבעת מוקדי הכאוס: ניתוח עומק של ההחלטות
      </h2>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 font-sans text-sm">
      
      <!-- Card 1: Russo Split -->
      <div class="p-5 rounded-xl border border-red-200 dark:border-red-900/60 bg-white dark:bg-[#161318] shadow-sm space-y-2">
        <div class="flex items-center gap-2 text-red-600 dark:text-red-400 font-bold font-mono text-xs uppercase">
          <span>⚡</span>
          <span>עמדה 9 מול עמדה 10: הפיצול של אלסיה רוסו</span>
        </div>
        <h3 class="text-base font-bold text-neutral-900 dark:text-white">
          4 פתיחות כחלוצת חוד (9) ⟷ 4 פתיחות כקשרית התקפית (10)
        </h3>
        <p class="text-neutral-700 dark:text-neutral-300 leading-relaxed text-xs sm:text-sm">
          רוסו מוצאת את עצמה נעה כמטוטלת בין תפקיד הסקוררית המסיימת (מחזורים 1, 2, 4 ו-5) לבין תפקיד הפליימייקרית המחברת (מחזורים 3, 6, 7 ו-8). כשהיא פותחת ב-10, ארסנל מרוויחה נוכחות פיזית בקישור, אך סובלת מנוכחות דלילה בתוך רחבת ה-16 כפי שראינו מול וילה.
        </p>
      </div>

      <!-- Card 2: Fullback Carousel -->
      <div class="p-5 rounded-xl border border-blue-200 dark:border-blue-900/60 bg-white dark:bg-[#121620] shadow-sm space-y-2">
        <div class="flex items-center gap-2 text-blue-600 dark:text-blue-400 font-bold font-mono text-xs uppercase">
          <span>🔄</span>
          <span>סחרחרת המגינות: אונה באטייה והרוטציה האינסופית</span>
        </div>
        <h3 class="text-base font-bold text-neutral-900 dark:text-white">
          6 פתיחות בשמאל, מעבר פתאומי לימין, ו-4 שחקניות שונות בעמדה
        </h3>
        <p class="text-neutral-700 dark:text-neutral-300 leading-relaxed text-xs sm:text-sm">
          באטייה פתחה 6 פעמים כמגן שמאלי, אך במחזור 8 מול וילה הוסטה במפתיע לימין. אמילי פוקס (שפתחה 6 פעמים) סופסלה, טיילור היינדס פתחה פעמיים בשמאל, וסמילה הולמברג קיבלה הופעה בודדת בימין. התנודות הבלתי פוסקות האלו מייצרות חוסר תיאום קריטי בהגנה על התקפות מעבר.
        </p>
      </div>

      <!-- Card 3: Olivia Smith -->
      <div class="p-5 rounded-xl border border-purple-200 dark:border-purple-900/60 bg-white dark:bg-[#18121f] shadow-sm space-y-2">
        <div class="flex items-center gap-2 text-purple-600 dark:text-purple-400 font-bold font-mono text-xs uppercase">
          <span>🔀</span>
          <span>אוליביה סמית' הנודדת: נכס ורסטילי או חוסר אונים טקטי?</span>
        </div>
        <h3 class="text-base font-bold text-neutral-900 dark:text-white">
          3 עמדות שונות ב-8 מחזורים: כנף שמאל, כנף ימין וחלוצה 9
        </h3>
        <p class="text-neutral-700 dark:text-neutral-300 leading-relaxed text-xs sm:text-sm">
          סמית' הגיעה כמטאור והוכיחה איכויות אישיות פנומנליות, אך סלגרס שיבצה אותה ב-3 תפקידים שונים: 3 פתיחות בכנף שמאל, פתיחה בכנף ימין, ובשני המחזורים האחרונים (מול טוטנהאם ואסטון וילה) כחלוצת שפיץ בודדת (9). הוורסטיליות שלה מרשימה, אך מונעת ממנה לבסס תבניות שיתוף פעולה קבועות.
        </p>
      </div>

      <!-- Card 4: Iron Anchors -->
      <div class="p-5 rounded-xl border border-emerald-200 dark:border-emerald-900/60 bg-white dark:bg-[#111a15] shadow-sm space-y-2">
        <div class="flex items-center gap-2 text-emerald-600 dark:text-emerald-400 font-bold font-mono text-xs uppercase">
          <span>🟢</span>
          <span>עוגני הברזל: שתי השחקניות היחידות שלא זזו מההרכב</span>
        </div>
        <h3 class="text-base font-bold text-neutral-900 dark:text-white">
          ליאה וויליאמסון וג'ורג'יה סטאנוויי (8 מתוך 8 פתיחות, 100%)
        </h3>
        <p class="text-neutral-700 dark:text-neutral-300 leading-relaxed text-xs sm:text-sm">
          בתוך ים השינויים, שתי שחקניות נותרו עמוד השדרה המוחלט של ארסנל: ליאה וויליאמסון במרכז ההגנה (105 נגיעות מול וילה ו-15 כדורים ארוכים מדויקים) וג'ורג'יה סטאנוויי במרכז המגרש. כל 9 העמדות האחרות עברו טלטלות שבועיות.
        </p>
      </div>

    </div>
  </div>

  <!-- ================= SUMMARY TABLE OF ALL 8 LINEUPS ================= -->
  <div class="space-y-4 pt-4 border-t border-neutral-200 dark:border-neutral-800">
    <div class="flex items-center justify-between">
      <div class="flex items-center gap-2">
        <span class="text-lg">📋</span>
        <h2 class="text-xl sm:text-2xl font-bold text-neutral-900 dark:text-white">
          טבלת כל 8 ההרכבים הפותחים מחזור-אחר-מחזור
        </h2>
      </div>
      <span class="text-xs font-mono text-neutral-500">עונת 2026/27</span>
    </div>

    <div class="overflow-x-auto rounded-xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-[#121215] shadow-sm">
      <table class="w-full text-right text-xs font-mono">
        <thead class="bg-neutral-100 dark:bg-[#181820] text-neutral-600 dark:text-neutral-400 text-[11px] border-b border-neutral-200 dark:border-neutral-800">
          <tr>
            <th class="p-3">מחזור</th>
            <th class="p-3">משחק ותוצאה</th>
            <th class="p-3 text-center">מערך</th>
            <th class="p-3">שוערת</th>
            <th class="p-3">רביעיית הגנה (LB, CB, CB, RB)</th>
            <th class="p-3">דאבל-פיווט (DM)</th>
            <th class="p-3">שלישייה התקפית (LW, AM, RW)</th>
            <th class="p-3 text-center font-bold text-red-500">חלוצה 9</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-neutral-200 dark:divide-neutral-800/80 text-[11px]">
          <tr class="hover:bg-neutral-50 dark:hover:bg-[#181822] transition-colors">
            <td class="p-3 font-bold text-neutral-900 dark:text-white">MW1</td>
            <td class="p-3">0:1 בחוץ מול ברייטון</td>
            <td class="p-3 text-center font-bold text-primary-600 dark:text-primary-400">4-2-3-1</td>
            <td class="p-3">מיסה</td>
            <td class="p-3">באטייה, קאטלי, וויליאמסון, פוקס</td>
            <td class="p-3">ליטל, סטאנוויי</td>
            <td class="p-3">סמית', קלדנטיי, באום</td>
            <td class="p-3 text-center font-bold text-red-400">רוסו</td>
          </tr>
          <tr class="hover:bg-neutral-50 dark:hover:bg-[#181822] transition-colors">
            <td class="p-3 font-bold text-neutral-900 dark:text-white">MW2</td>
            <td class="p-3">0:0 בבית מול פאלאס</td>
            <td class="p-3 text-center font-bold text-primary-600 dark:text-primary-400">4-2-3-1</td>
            <td class="p-3">מיסה</td>
            <td class="p-3">באטייה, וובן-מוי, וויליאמסון, פוקס</td>
            <td class="p-3">קוני-קרוס, סטאנוויי</td>
            <td class="p-3">קלי, קלדנטיי, באום</td>
            <td class="p-3 text-center font-bold text-red-400">רוסו</td>
          </tr>
          <tr class="hover:bg-neutral-50 dark:hover:bg-[#181822] transition-colors">
            <td class="p-3 font-bold text-neutral-900 dark:text-white">MW3</td>
            <td class="p-3">1:1 בבית מול יונייטד</td>
            <td class="p-3 text-center font-bold text-primary-600 dark:text-primary-400">4-2-3-1</td>
            <td class="p-3">מיסה</td>
            <td class="p-3">באטייה, קאטלי, וויליאמסון, פוקס</td>
            <td class="p-3">סטאנוויי, קלדנטיי</td>
            <td class="p-3">סמית', רוסו (10!), באום</td>
            <td class="p-3 text-center font-bold text-amber-400">בלקסטניוס</td>
          </tr>
          <tr class="hover:bg-neutral-50 dark:hover:bg-[#181822] transition-colors">
            <td class="p-3 font-bold text-neutral-900 dark:text-white">MW4</td>
            <td class="p-3">1:0 בחוץ לצ'לסי</td>
            <td class="p-3 text-center font-bold text-primary-600 dark:text-primary-400">4-2-3-1</td>
            <td class="p-3 text-red-400 font-bold">בורבה</td>
            <td class="p-3">באטייה, קאטלי, וויליאמסון, פוקס</td>
            <td class="p-3">קוני-קרוס, סטאנוויי</td>
            <td class="p-3">קלדנטיי, ליטל (10), באום</td>
            <td class="p-3 text-center font-bold text-red-400">רוסו</td>
          </tr>
          <tr class="hover:bg-neutral-50 dark:hover:bg-[#181822] transition-colors">
            <td class="p-3 font-bold text-neutral-900 dark:text-white">MW5</td>
            <td class="p-3">4:2 בחוץ לסיטי</td>
            <td class="p-3 text-center font-bold text-primary-600 dark:text-primary-400">4-2-3-1</td>
            <td class="p-3 text-red-400 font-bold">בורבה</td>
            <td class="p-3">באטייה, וובן-מוי, וויליאמסון, פוקס</td>
            <td class="p-3">קוני-קרוס, סטאנוויי</td>
            <td class="p-3">קלדנטיי, ליטל (10), באום</td>
            <td class="p-3 text-center font-bold text-red-400">רוסו</td>
          </tr>
          <tr class="hover:bg-neutral-50 dark:hover:bg-[#181822] transition-colors">
            <td class="p-3 font-bold text-neutral-900 dark:text-white">MW6</td>
            <td class="p-3">1:1 בבית מול ברמינגהאם</td>
            <td class="p-3 text-center font-bold text-primary-600 dark:text-primary-400">4-2-3-1</td>
            <td class="p-3">מיסה</td>
            <td class="p-3">באטייה, וובן-מוי, וויליאמסון, <strong class="text-blue-400">הולמברג</strong></td>
            <td class="p-3">קוני-קרוס, סטאנוויי</td>
            <td class="p-3">סמית', רוסו (10), באום</td>
            <td class="p-3 text-center font-bold text-amber-400">בלקסטניוס</td>
          </tr>
          <tr class="hover:bg-neutral-50 dark:hover:bg-[#181822] transition-colors">
            <td class="p-3 font-bold text-neutral-900 dark:text-white">MW7</td>
            <td class="p-3">1:2 בחוץ בדרבי מול ספרס</td>
            <td class="p-3 text-center font-bold text-primary-600 dark:text-primary-400">4-2-3-1</td>
            <td class="p-3">מיסה</td>
            <td class="p-3"><strong class="text-blue-400">היינדס</strong>, קאטלי, וויליאמסון, פוקס</td>
            <td class="p-3">קוני-קרוס, סטאנוויי</td>
            <td class="p-3">פורד, רוסו (10), באום</td>
            <td class="p-3 text-center font-bold text-purple-400">סמית'</td>
          </tr>
          <tr class="hover:bg-neutral-50 dark:hover:bg-[#181822] transition-colors">
            <td class="p-3 font-bold text-neutral-900 dark:text-white">MW8</td>
            <td class="p-3">1:1 בבית מול אסטון וילה</td>
            <td class="p-3 text-center font-bold text-primary-600 dark:text-primary-400">4-2-3-1</td>
            <td class="p-3">מיסה</td>
            <td class="p-3">היינדס, קאטלי, וויליאמסון, <strong class="text-blue-400">באטייה</strong></td>
            <td class="p-3">סטאנוויי, קוני-קרוס</td>
            <td class="p-3">פורד, רוסו (10), <strong class="text-neutral-300">רויטלר</strong></td>
            <td class="p-3 text-center font-bold text-purple-400">סמית'</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- Bottom Navigation Link -->
  <div class="border-t border-neutral-200 dark:border-neutral-800 pt-6 flex items-center justify-between font-mono text-xs">
    <a href="{{ '/weekly/mw8/' | relative_url }}" class="inline-flex items-center gap-1.5 px-4 py-2 rounded-lg bg-neutral-100 dark:bg-neutral-800 hover:bg-neutral-200 dark:hover:bg-neutral-700 text-neutral-800 dark:text-neutral-200 font-bold transition-colors">
      <span>→</span>
      <span>חזרה לטור השבועי המלא (מחזור 8)</span>
    </a>
    <a href="{{ '/weekly/' | relative_url }}" class="text-primary-600 dark:text-primary-400 font-bold hover:underline">
      אינדקס הטורים השבועיים
    </a>
  </div>

</div>

<!-- Load Widgets Script -->
<script src="{{ '/assets/js/mw8-widgets.js' | relative_url }}"></script>
