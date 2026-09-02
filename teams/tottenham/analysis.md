---
layout: team
title: "Tottenham - חלק ב': ניתוח נתונים"
team_name: "Tottenham Hotspur"
team_slug: "tottenham"
team_meta: "WSL 2025/26 · חלק ב': ניתוח נתונים ותמונת בסיס"
permalink: /teams/tottenham/analysis/
prev_url: /teams/tottenham/
prev_title: "חלק א': מועדון, זהות ומנהיגות"
next_url: /teams/tottenham/defense/
next_title: "חלק ג': חוליית ההגנה והמשלימות לקוגה"
---

<div class="space-y-6 text-neutral-800 dark:text-neutral-200 leading-relaxed text-base sm:text-lg font-sans">

  <!-- Header -->
  <div class="border-b border-neutral-200 dark:border-neutral-800 pb-3">
    <div class="text-xs font-mono uppercase text-neutral-500 dark:text-neutral-400 font-bold tracking-wider mb-1">
      חלק ב': ניתוח נתונים ותמונת בסיס
    </div>
    <h1 class="text-2xl md:text-3xl font-bold tracking-tight text-neutral-900 dark:text-white">
      טוטנהאם: מערכים, פוזישנסלס ודאטה
    </h1>
  </div>

  <!-- Intro -->
  <p class="text-lg">
    המושג <strong>פוזישנסלס (Positionless)</strong> שייך לאחות מהכדורסל, אבל כמות הפעמים ששמעתי את המונח משחקניות ומאמן ספרס, מחייב אותי לאמת את זה מול הנתונים של העונה הקודמת.
  </p>

  <p>
    הנתונים היחסית הבסיסיים תומכים בכך ששחקניות ההתקפה, ומאז ינואר גם הקשרית ההתקפית המשמעותית, גאפסוט (להלן <strong>סיגי</strong>), מאוד פלואידיות במשחק שלהן. 
    מספיק להסתכל על התפלגות כיבוש השערים, על כמות הנגיעות ברחבה של שחקניות הקישור וההתקפה ועל מפות החום המרחביות כדי לראות שההתקפה של ספרס פעלה לחלוטין ללא עמדות קבועות.
  </p>

  <!-- Part 1: Attack & Positionless -->
  <div class="rounded-xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/50 dark:bg-[#121215] p-5 sm:p-6 space-y-4">
    <h2 class="text-xl font-bold text-neutral-900 dark:text-white flex items-center gap-2">
      <span>1. התקפת הפוזישנסלס: ביזור שערים והשתלטות על הרחבה</span>
    </h2>

    <p class="text-sm sm:text-base text-neutral-700 dark:text-neutral-300">
      בניגוד לרוב קבוצות הליגה שנשענות על סקוררית מרכזית (למשל מנצ'סטר סיטי, שבה <strong>באני שואו</strong> אחראית בלעדית על 34% משערי הקבוצה), בספרס נכבשו <strong>35 שערים שהתחלקו בין 11 שחקניות שונות</strong>. אף שחקנית לא חצתה את רף ה-23% מסך השערים:
    </p>

    <!-- Goal Distribution Table -->
    <div class="overflow-x-auto">
      <table class="w-full text-sm text-right border-collapse">
        <thead>
          <tr class="border-b border-neutral-200 dark:border-neutral-700 text-neutral-500 dark:text-neutral-400">
            <th class="py-2 pr-2">שחקנית</th>
            <th class="py-2">תפקיד מוצהר</th>
            <th class="py-2 text-center">שערים</th>
            <th class="py-2 text-center">בישולים</th>
            <th class="py-2 text-left pl-2">נתח משערי הקבוצה</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-neutral-100 dark:divide-neutral-800 font-mono text-xs sm:text-sm">
          <tr>
            <td class="py-2.5 pr-2 font-sans font-semibold text-neutral-900 dark:text-white">אוליבה הולנדט (אוליב)</td>
            <td class="py-2.5 font-sans text-neutral-500">קשרית / שחקנית חופשית</td>
            <td class="py-2.5 text-center font-bold text-primary-600 dark:text-primary-400">8</td>
            <td class="py-2.5 text-center">3</td>
            <td class="py-2.5 text-left pl-2">22.9%</td>
          </tr>
          <tr>
            <td class="py-2.5 pr-2 font-sans">בת' אנגלנד</td>
            <td class="py-2.5 font-sans text-neutral-500">חלוצה / קפטנית</td>
            <td class="py-2.5 text-center font-bold">7</td>
            <td class="py-2.5 text-center">1</td>
            <td class="py-2.5 text-left pl-2">20.0%</td>
          </tr>
          <tr>
            <td class="py-2.5 pr-2 font-sans">קת'ינקה טנדברג</td>
            <td class="py-2.5 font-sans text-neutral-500">חלוצת מטרה</td>
            <td class="py-2.5 text-center font-bold">6</td>
            <td class="py-2.5 text-center">1</td>
            <td class="py-2.5 text-left pl-2">17.1%</td>
          </tr>
          <tr>
            <td class="py-2.5 pr-2 font-sans">סיגנה גאופסט (סיגי)</td>
            <td class="py-2.5 font-sans text-neutral-500">קשרית מרכזית (מינואר)</td>
            <td class="py-2.5 text-center font-bold">3</td>
            <td class="py-2.5 text-center">1</td>
            <td class="py-2.5 text-left pl-2">8.6%</td>
          </tr>
          <tr>
            <td class="py-2.5 pr-2 font-sans text-neutral-600 dark:text-neutral-400">סומאנן (2), קוגה (2), בלקסטאד, המאנו, וינברג, תומאס, אהטינן (1 כ"א)</td>
            <td class="py-2.5 font-sans text-neutral-500">קישור והגנה</td>
            <td class="py-2.5 text-center font-bold">11</td>
            <td class="py-2.5 text-center">16</td>
            <td class="py-2.5 text-left pl-2">31.4%</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Heatmap Image Visual Overlay -->
    <div class="my-4">
      <h3 class="text-base font-bold text-neutral-900 dark:text-white mb-2">
        מפת חום מרחבית: חפיפה מוחלטת והעמסת חצי-המרחב השמאלי (Direct Overlay)
      </h3>
      <div class="rounded-xl overflow-hidden border border-neutral-200 dark:border-neutral-800 bg-[#06090E] p-2">
        <img src="/assets/images/tottenham_positionless_heatmap.png" alt="Tottenham Positionless Attack Heatmap Overlay" class="w-full h-auto rounded-lg shadow-lg">
      </div>
      <p class="text-xs sm:text-sm text-neutral-500 dark:text-neutral-400 mt-2 italic text-center">
        שכבות חום חופפות של אוליב (כחול), סיגי (כתום), בלקסטאד (ירוק) וטנדברג (אדום/צהוב) על מגרש יחיד: 74.2% חפיפה מרחבית ו-58.6% נגיעות ברחבה משחקניות שאינן חלוצות חוד.
      </p>
    </div>

    <!-- Spatial Table -->
    <div class="overflow-x-auto">
      <table class="w-full text-xs sm:text-sm text-right border-collapse">
        <thead>
          <tr class="border-b border-neutral-200 dark:border-neutral-700 text-neutral-500 dark:text-neutral-400 font-mono">
            <th class="py-2 pr-2">שחקנית</th>
            <th class="py-2 text-center">חצי-מרחב שמאל</th>
            <th class="py-2 text-center">רחבה מרכזית</th>
            <th class="py-2 text-center">חצי-מרחב ימין</th>
            <th class="py-2 text-center">נגיעות ברחבה / 90</th>
            <th class="py-2 text-left pl-2">מדד פלואידיות</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-neutral-100 dark:divide-neutral-800 font-mono">
          <tr>
            <td class="py-2 pr-2 font-sans font-semibold">אוליב הולנדט</td>
            <td class="py-2 text-center">26.2%</td>
            <td class="py-2 text-center">22.4%</td>
            <td class="py-2 text-center">21.1%</td>
            <td class="py-2 text-center">3.82</td>
            <td class="py-2 text-left pl-2 font-bold text-emerald-600 dark:text-emerald-400">92.4 (חופש מלא)</td>
          </tr>
          <tr>
            <td class="py-2 pr-2 font-sans font-semibold">סיגי (גאופסט)</td>
            <td class="py-2 text-center">31.8%</td>
            <td class="py-2 text-center">28.6%</td>
            <td class="py-2 text-center">17.5%</td>
            <td class="py-2 text-center font-bold text-primary-600 dark:text-primary-400">5.34 (אחוזון 92)</td>
            <td class="py-2 text-left pl-2 font-bold text-emerald-600 dark:text-emerald-400">94.1 (תקיפת עומק)</td>
          </tr>
          <tr>
            <td class="py-2 pr-2 font-sans font-semibold">ז'ולי בלקסטאד</td>
            <td class="py-2 text-center">28.3%</td>
            <td class="py-2 text-center">14.2%</td>
            <td class="py-2 text-center">8.1%</td>
            <td class="py-2 text-center">2.45</td>
            <td class="py-2 text-left pl-2">81.0 (כניסות פנימה)</td>
          </tr>
          <tr>
            <td class="py-2 pr-2 font-sans font-semibold text-neutral-500">קת'ינקה טנדברג</td>
            <td class="py-2 text-center text-neutral-500">12.4%</td>
            <td class="py-2 text-center font-bold">65.8%</td>
            <td class="py-2 text-center text-neutral-500">11.2%</td>
            <td class="py-2 text-center">6.84</td>
            <td class="py-2 text-left pl-2 text-neutral-500">44.0 (עוגן רחבה)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- Part 2: Defense & Toko Koga -->
  <div class="rounded-xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/50 dark:bg-[#121215] p-5 sm:p-6 space-y-4">
    <h2 class="text-xl font-bold text-neutral-900 dark:text-white flex items-center gap-2">
      <span>2. חוליית ההגנה: השדרוג העצום של טוקו קוגה והחיפוש אחר המשלימות</span>
    </h2>

    <p>
      מעבר להתקפה, מעניין אותי לדבר על ההגנה. בעונה שעברה, ההחתמה של <strong>טוקו קוגה</strong> שדרגה פלאים את ההגנה. פלאים.
    </p>

    <p>
      אני לא יודע אפילו אלו נתונים לחפש שידעו לכמת את השדרוג שלה להגנה, למשחק ההגנה ואפילו למשחק ההתקפה ברגעים מסוימים (1,705 דקות, 2 שערים ובישול), אבל היא הייתה הכי טובה ביי-פאר.
    </p>

    <p>
      החיסרון שלה הורגש בעיקר כשהתקיים גביע אסיה; בזמן שקוגה הייתה עם נבחרת יפן, ההגנה הזכירה נשכחות וחבל. הנתונים של ספרס עם קוגה לעומת המשחקים שנעדרה ממחישים את התלות המוחלטת בה:
    </p>

    <!-- Toko Koga Impact Table -->
    <div class="overflow-x-auto">
      <table class="w-full text-xs sm:text-sm text-right border-collapse">
        <thead>
          <tr class="border-b border-neutral-200 dark:border-neutral-700 text-neutral-500 font-mono">
            <th class="py-2 pr-2">מדד ביצוע הגנתי</th>
            <th class="py-2 text-center">עם טוקו קוגה (19 משחקים)</th>
            <th class="py-2 text-center">בלעדיה בגביע אסיה (3 משחקים)</th>
            <th class="py-2 text-left pl-2">משמעות טקטית</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-neutral-100 dark:divide-neutral-800 font-mono">
          <tr>
            <td class="py-2.5 pr-2 font-sans font-semibold">ספיגת שערים למשחק</td>
            <td class="py-2.5 text-center font-bold text-emerald-600 dark:text-emerald-400">1.47</td>
            <td class="py-2.5 text-center font-bold text-red-600 dark:text-red-400">3.33 (10 שערים ב-3 משחקים)</td>
            <td class="py-2.5 text-left pl-2 font-sans text-neutral-500">יותר מפי 2 ספיגות בהיעדרה</td>
          </tr>
          <tr>
            <td class="py-2.5 pr-2 font-sans font-semibold">רשתות נקיות (Clean Sheets)</td>
            <td class="py-2.5 text-center font-bold">6 משחקים (100% מהעונה)</td>
            <td class="py-2.5 text-center font-bold text-red-500">0</td>
            <td class="py-2.5 text-left pl-2 font-sans text-neutral-500">אפס יציבות ללא קוגה</td>
          </tr>
          <tr>
            <td class="py-2.5 pr-2 font-sans font-semibold">איומים לשער היריב למשחק</td>
            <td class="py-2.5 text-center">11.8</td>
            <td class="py-2.5 text-center font-bold text-red-500">18.3</td>
            <td class="py-2.5 text-left pl-2 font-sans text-neutral-500">זינוק של 55% בחשיפת ההגנה</td>
          </tr>
          <tr>
            <td class="py-2.5 pr-2 font-sans font-semibold">אחוזי ניצחון</td>
            <td class="py-2.5 text-center font-bold text-emerald-600">52.6% (10 נצחונות)</td>
            <td class="py-2.5 text-center font-bold text-red-500">0.0% (0 נצחונות)</td>
            <td class="py-2.5 text-left pl-2 font-sans text-neutral-500">קריסה טוטאלית בתוצאות</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p class="text-sm sm:text-base text-neutral-700 dark:text-neutral-300">
      הצימוד של <strong>קוגה ושרלוט גרנט</strong> היה מצוין. גרנט הלכה, ומעניין מי תשחק לצדה ומעניין עוד יותר מי תשחק בהגנה.
    </p>
  </div>

  <!-- Part 3: Goalkeeper Side Note - Lize Kop -->
  <div class="rounded-xl border border-amber-200 dark:border-amber-900/40 bg-amber-50/40 dark:bg-[#181510] p-5 sm:p-6 space-y-3">
    <div class="flex items-center gap-2 text-amber-700 dark:text-amber-400 font-bold text-base">
      <span>⚠️ הערת אגב קטנה: סימן השאלה סביב ליזה קופ</span>
    </div>
    
    <p class="text-sm sm:text-base text-neutral-700 dark:text-neutral-300">
      אני לא בטוח ש<strong>ליזה קופ</strong> היא זאת שתהיה השוערת הראשונה לאורך כל העונה. היא לא הכי טובה בליגה, רחוק מכך.
    </p>

    <!-- Goalkeeping Comparison Table -->
    <div class="overflow-x-auto pt-1">
      <table class="w-full text-xs sm:text-sm text-right border-collapse">
        <thead>
          <tr class="border-b border-amber-200 dark:border-amber-800/60 text-neutral-500 font-mono">
            <th class="py-1.5 pr-2">קבוצה / שוערת</th>
            <th class="py-1.5 text-center">משחקים</th>
            <th class="py-1.5 text-center">ספיגות ל-90</th>
            <th class="py-1.5 text-center">אחוז הצלות (Save %)</th>
            <th class="py-1.5 text-left pl-2">דירוג בליגה</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-amber-100 dark:divide-amber-900/30 font-mono">
          <tr>
            <td class="py-2 pr-2 font-sans font-semibold text-neutral-900 dark:text-white">טוטנהאם (ליזה קופ)</td>
            <td class="py-2 text-center">22</td>
            <td class="py-2 text-center font-bold text-red-600 dark:text-red-400">1.73 (38 סה״כ)</td>
            <td class="py-2 text-center font-bold text-red-600 dark:text-red-400">62.4%</td>
            <td class="py-2 text-left pl-2 text-neutral-500">מקום 10 מתוך 12</td>
          </tr>
          <tr class="text-neutral-500 dark:text-neutral-400">
            <td class="py-2 pr-2 font-sans">צ'לסי (בנצ'מרק)</td>
            <td class="py-2 text-center">22</td>
            <td class="py-2 text-center">0.91 (20 סה״כ)</td>
            <td class="py-2 text-center">74.4%</td>
            <td class="py-2 text-left pl-2">מקום 1</td>
          </tr>
          <tr class="text-neutral-500 dark:text-neutral-400">
            <td class="py-2 pr-2 font-sans">ארסנל וסיטי (בנצ'מרק)</td>
            <td class="py-2 text-center">22</td>
            <td class="py-2 text-center">0.64–0.86</td>
            <td class="py-2 text-center">73.6%</td>
            <td class="py-2 text-left pl-2">טופ 3</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-400">
      עם 62.4% הצלה בלבד, צירופה של השוערת הנורווגית הצעירה <strong>סלמה פננגסטואן</strong> (בת 23) עשוי להוביל לתחרות פתוחה לחלוטין על אפודת ההרכב.
    </p>
  </div>

  <!-- Outro & Forward Links -->
  <p class="pt-2">
    בעמוד הבא אנתח ואתמקד בעמדות ההגנה. אשווה בין השחקניות הקיימות והרכש החדש כדי להבין מה כל אחת מהן יכולה להביא, ונחפש את המשלימות המושלמות לקוגה בכל עמדה.
  </p>

  <!-- Standardized Post Pagination -->
  {% include post_pagination.html %}

</div>
