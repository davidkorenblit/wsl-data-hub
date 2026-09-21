---
layout: default
title: "הפינה הטקטית · מחזור 3 | WSL Data Hub"
permalink: /weekly/tactics/
lang: he
alt_url: /en/weekly/
prev_url: /weekly/
prev_title: "חזרה לטור השבועי"
---

<div class="space-y-6">

  <!-- Page Header -->
  <div class="border-b border-neutral-200 dark:border-neutral-800 pb-4">
    <div class="text-xs font-mono uppercase text-neutral-500 dark:text-neutral-400 font-bold tracking-wider mb-1">
      TACTICAL CORNER · הפינה הטקטית
    </div>
    <h1 class="text-2xl md:text-3xl font-bold tracking-tight text-neutral-900 dark:text-white mb-2">
      הפינה הטקטית: מחזור 3
    </h1>
    <p class="text-sm sm:text-base text-neutral-600 dark:text-neutral-300 leading-relaxed font-sans">
      צלילה למספרים, תבניות הגנה ומגמות עומק מהמחזור האחרון ב-WSL.
    </p>
  </div>

  <!-- Featured Content Card -->
  <article class="rounded-xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-[#121215] p-6 sm:p-8 space-y-8 shadow-sm">

    <!-- Header Navigation -->
    <div class="flex items-center justify-between border-b border-neutral-100 dark:border-neutral-800 pb-3">
      <div class="flex items-center gap-2">
        <span class="text-xs font-mono font-bold px-2.5 py-0.5 rounded bg-primary-50 dark:bg-primary-950/40 text-primary-700 dark:text-primary-300 border border-primary-200 dark:border-primary-800">
          ניתוח נתונים
        </span>
        <span class="text-xs font-mono text-neutral-400 dark:text-neutral-500">
          עונת 2026/27
        </span>
      </div>

      <!-- Top Back Link -->
      <a href="{{ '/weekly/' | relative_url }}" class="text-xs font-mono text-neutral-600 dark:text-neutral-400 hover:text-neutral-950 dark:hover:text-white transition-colors flex items-center gap-1 font-medium">
        <span>→</span>
        <span>חזרה לטור הראשי</span>
      </a>
    </div>

    <div class="prose dark:prose-invert max-w-none text-neutral-800 dark:text-neutral-200 leading-relaxed space-y-8 font-sans text-base sm:text-lg">

      <!-- Section 1: Palace vs United Defense against Arsenal -->
      <section class="space-y-4">
        <h2 class="text-xl sm:text-2xl font-bold text-neutral-900 dark:text-white flex items-center gap-2">
          <span>🛡️</span>
          <span>פאלאס ויונייטד מול ארסנל: שתי דרכים לעצור את התותחניות</span>
        </h2>

        <p>
          שתי קבוצות שונות עצרו את ארסנל בשבועיים האחרונים בשתי תוצאות תיקו (0:0 מול פאלאס במחזור 2, 1:1 מול יונייטד במחזור 3). העין ראתה מאבק הרואי בשני המקרים, אבל מבט מעמיק בדאטה מגלה שני סגנונות הגנתיים שונים לחלוטין:
        </p>

        <!-- Comparative Data Table -->
        <div class="overflow-x-auto rounded-lg border border-neutral-200 dark:border-neutral-800 bg-neutral-50/40 dark:bg-[#16161a] p-1 my-4">
          <table class="w-full text-xs sm:text-sm text-right border-collapse font-mono">
            <thead>
              <tr class="border-b border-neutral-200 dark:border-neutral-700 text-neutral-500 dark:text-neutral-400">
                <th class="py-2.5 px-3 font-sans font-bold text-right">מדד טקטי</th>
                <th class="py-2.5 px-3 text-center">קריסטל פאלאס (מחזור 2)</th>
                <th class="py-2.5 px-3 text-center">מנצ'סטר יונייטד (מחזור 3)</th>
                <th class="py-2.5 px-3 font-sans font-medium text-left">המשמעות הטקטית</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-neutral-100 dark:divide-neutral-800">
              <tr>
                <td class="py-2.5 px-3 font-sans font-semibold text-neutral-800 dark:text-neutral-200">החזקת כדור</td>
                <td class="py-2.5 px-3 text-center font-bold">21% בלבד</td>
                <td class="py-2.5 px-3 text-center font-bold">41%</td>
                <td class="py-2.5 px-3 font-sans text-xs text-neutral-500">פאלאס ויתרה על הכדור לחלוטין; יונייטד לחצה וניהלה משחק</td>
              </tr>
              <tr>
                <td class="py-2.5 px-3 font-sans font-semibold text-neutral-800 dark:text-neutral-200">בעיטות שארסנל ביצעה</td>
                <td class="py-2.5 px-3 text-center text-red-600 dark:text-red-400 font-bold">30 בעיטות</td>
                <td class="py-2.5 px-3 text-center">17 בעיטות</td>
                <td class="py-2.5 px-3 font-sans text-xs text-neutral-500">מול פאלאס זה היה מטווח של ייאוש; יונייטד חסמה קווי מסירה</td>
              </tr>
              <tr>
                <td class="py-2.5 px-3 font-sans font-semibold text-neutral-800 dark:text-neutral-200">מדד xG של ארסנל</td>
                <td class="py-2.5 px-3 text-center">2.56 xG</td>
                <td class="py-2.5 px-3 text-center">1.96 xG</td>
                <td class="py-2.5 px-3 font-sans text-xs text-neutral-500">ארסנל הגיעה למצבים בשניהם, אבל בסוגים שונים</td>
              </tr>
              <tr>
                <td class="py-2.5 px-3 font-sans font-semibold text-neutral-800 dark:text-neutral-200">איכות ממוצעת לבעיטה (xG/Shot)</td>
                <td class="py-2.5 px-3 text-center font-bold text-amber-600 dark:text-amber-400">0.085 (נמוך מאוד)</td>
                <td class="py-2.5 px-3 text-center font-bold text-emerald-600 dark:text-emerald-400">0.115 (איכותי יותר)</td>
                <td class="py-2.5 px-3 font-sans text-xs text-neutral-500">פאלאס כפתה בעיטות מרחוק וצפופות תחת שמירה כפולה</td>
              </tr>
              <tr>
                <td class="py-2.5 px-3 font-sans font-semibold text-neutral-800 dark:text-neutral-200">הרחקות כדור של היריבה (Clearances)</td>
                <td class="py-2.5 px-3 text-center font-bold text-primary-600 dark:text-primary-400">73 הרחקות!</td>
                <td class="py-2.5 px-3 text-center">54 הרחקות</td>
                <td class="py-2.5 px-3 font-sans text-xs text-neutral-500">פאלאס שיחקה בהישרדות של להעיף כדורים לכל כיוון</td>
              </tr>
              <tr>
                <td class="py-2.5 px-3 font-sans font-semibold text-neutral-800 dark:text-neutral-200">חסימות בעיטה (Blocks)</td>
                <td class="py-2.5 px-3 text-center font-bold">10 חסימות</td>
                <td class="py-2.5 px-3 text-center">4 חסימות</td>
                <td class="py-2.5 px-3 font-sans text-xs text-neutral-500">בארטריפ וחברותיה נשכבו על הדשא מול כל כדור</td>
              </tr>
              <tr>
                <td class="py-2.5 px-3 font-sans font-semibold text-neutral-800 dark:text-neutral-200">מסירות בחצי של ארסנל</td>
                <td class="py-2.5 px-3 text-center text-neutral-400">23 בלבד בכל המשחק!</td>
                <td class="py-2.5 px-3 text-center">70 מסירות</td>
                <td class="py-2.5 px-3 font-sans text-xs text-neutral-500">פאלאס פשוט לא עברה את קו האמצע לאורך 90 דקות</td>
              </tr>
            </tbody>
          </table>
        </div>

        <p class="text-base sm:text-lg">
          <strong>ומה הדמיון המשותף?</strong> בשני המשחקים ארסנל הגיעה בדיוק ל-<strong>4 מצבי שער ודאיים (Big Chances)</strong>. מול פאלאס היא החמיצה 4 מ-4, ומול יונייטד החמיצה 3 מ-4 וסחטה שוויון מאוחר. בסך הכל: <strong>7 מתוך 8 מצבי שער בטוחים נזרקו לפח</strong> בשבועיים.
        </p>
      </section>

      <hr class="border-neutral-200 dark:border-neutral-800 my-6">

      <!-- Section 2: Kirsty Hanson Position -->
      <section class="space-y-4">
        <h2 class="text-xl sm:text-2xl font-bold text-neutral-900 dark:text-white flex items-center gap-2">
          <span>⚡</span>
          <span>הערה על העמדה של קריסטי הנסן: בימין זה עובד, אבל בשמאל היא בשיאה</span>
        </h2>

        <p>
          במהלך השנים ראינו מאמנים שמנסים לנייד את קריסטי הנסן לאורך כל חזית ההתקפה — באגף ימין, כחלוצה קדמית, ובאגף שמאל. הדאטה לאורך הקריירה מראה תבנית עקבית וברורה: <strong>הנסן בשיאה ההיסטורי תמיד כשהיא פועלת מצד שמאל</strong>.
        </p>

        <p>
          בעונת 2022/23 בווילה היא הייתה <strong>מלכת הבישולים של ה-WSL</strong> (9 בישולי ליגה, 10 בכל המסגרות) כששיחקה באגף שמאל קלאסי, עם מהירות על הקו וכדורי רוחב חדים לרייצ'ל דיילי. משמאל יש לה את זווית ההגבהה הטבעית ואת הפריצה בקו.
        </p>

        <p>
          אצל מרטין הו בספרס, היא מוצבת בפועל באגף ימין — בעיקר כי מתילדה וינברג ואוליביה הולדט נראות מצוין כשהן משחקות משמאל. נכון, הנסן דפקה צמד ענק מימין כבר במחזור הראשון מול ווסטהאם, אבל זה עדיין קצת מציק בעין: באגף ימין היא צריכה להמציא לעצמה זוויות, בעוד שמשמאל כל פעולה שלה זורמת בטבעיות מוחלטת.
        </p>
      </section>

      <hr class="border-neutral-200 dark:border-neutral-800 my-6">

      <!-- Section 3: Chelsea False 9 Concept -->
      <section class="space-y-4">
        <h2 class="text-xl sm:text-2xl font-bold text-neutral-900 dark:text-white flex items-center gap-2">
          <span>🔵</span>
          <span>רעיון שכדאי להרחיב עליו: צ'לסי של סוניה בומפסטור עם False 9</span>
        </h2>

        <p>
          מיירה רמירז וסאם קר לא עומדות כרגע לרשותה של צ'לסי בהרכב. במצב רגיל, כל קבוצה הייתה נכנסת למשבר עמוק בהיעדר חלוצת 9 דומיננטית. אבל בומפסטור לקחה את החיסרון הזה והפכה אותו לשיטה מבריקה: <strong>התקפה נטולת כתובת קבועה</strong>.
        </p>

        <p>
          לורן ג'יימס מתופקדת מעין חלוצה מדומה (False 9) שיורדת לעיגול האמצע כדי לקבל את הכדור, מושכת איתה את הבלמות ומפנה מסדרונות ריצה עצומים לשחקניות הגל השני.
        </p>

        <!-- Stats Grid for Chelsea -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 my-4">
          <div class="p-4 rounded-lg border border-neutral-200 dark:border-neutral-800 bg-neutral-50/50 dark:bg-[#16161a]">
            <div class="text-xs font-mono font-bold uppercase text-neutral-500 mb-1">פיזור השערים (3 מחזורים)</div>
            <div class="text-2xl font-bold font-mono text-neutral-900 dark:text-white">8 שערים · 7 כובשות שונות</div>
            <p class="text-xs text-neutral-600 dark:text-neutral-400 mt-2 font-sans">
              רק לורן ג'יימס כבשה 2. שאר 5 השערים נכבשו ע"י שחקניות הגנה וקישור (נוסקן, וולש, קרפנטר, ברונז, פוטר)!
            </p>
          </div>

          <div class="p-4 rounded-lg border border-neutral-200 dark:border-neutral-800 bg-neutral-50/50 dark:bg-[#16161a]">
            <div class="text-xs font-mono font-bold uppercase text-neutral-500 mb-1">האנומליה: אלי קרפנטר (מגנה ימנית!)</div>
            <div class="text-2xl font-bold font-mono text-primary-600 dark:text-primary-400">11 בעיטות · 33 נגיעות ברחבה</div>
            <p class="text-xs text-neutral-600 dark:text-neutral-400 mt-2 font-sans">
              עם 3.47 xG מצטבר ב-3 משחקים, קרפנטר מייצרת יותר נוכחות ברחבת היריבה מרוב חלוצות ה-9 בליגה.
            </p>
          </div>
        </div>

        <p>
          זהו כיוון טקטי מרתק שכדאי יהיה להמשיך לעקוב אחריו בשבועות הבאים — כי כרגע להגנות הליגה פשוט אין מושג את מי הן אמורות לסמן ברחבה.
        </p>
      </section>

      <hr class="border-neutral-200 dark:border-neutral-800 my-6">

      <!-- Section 4: Surprising Tidbits (Pikantria) -->
      <section class="space-y-4">
        <h2 class="text-xl sm:text-2xl font-bold text-neutral-900 dark:text-white flex items-center gap-2">
          <span>🍿</span>
          <span>פיקנטריה ונתונים מפתיעים מהמחזור</span>
        </h2>

        <div class="space-y-3">
          <div class="p-4 rounded-lg border border-neutral-200 dark:border-neutral-800 bg-neutral-50/50 dark:bg-[#16161a] space-y-1">
            <h3 class="font-bold text-base text-neutral-900 dark:text-white flex items-center gap-2">
              <span>⏱️</span>
              <span>הבונקר של פאלאס החזיק בדיוק 135 דקות רצופות</span>
            </h3>
            <p class="text-sm text-neutral-600 dark:text-neutral-300 font-sans">
              קריסטל פאלאס החזיקה ב-0:0 מול ארסנל 90 דקות שלמות במחזור 2. במחזור 3 מול ספרס, למרות שספגה כרטיס אדום ישיר בדקה ה-7, היא שוב שמרה על רשת נקייה עד המחצית (45 דקות). סך הכל: 135 דקות הירואיות ללא ספיגה... ואז קרסה וספגה 7 שערים ב-41 דקות בלבד!
            </p>
          </div>

          <div class="p-4 rounded-lg border border-neutral-200 dark:border-neutral-800 bg-neutral-50/50 dark:bg-[#16161a] space-y-1">
            <h3 class="font-bold text-base text-neutral-900 dark:text-white flex items-center gap-2">
              <span>🎯</span>
              <span>42 בעיטות במשחק אחד — שיא מועדון היסטורי</span>
            </h3>
            <p class="text-sm text-neutral-600 dark:text-neutral-300 font-sans">
              42 האיומים לשער של טוטנהאם על שערה של פאלאס ו-82 הנגיעות ברחבה הן המדדים הגבוהים ביותר שנמדדו למשחק בודד בתולדות טוטנהאם הוטספר מאז תחילת עידן הדאטה ב-WSL.
            </p>
          </div>

          <div class="p-4 rounded-lg border border-neutral-200 dark:border-neutral-800 bg-neutral-50/50 dark:bg-[#16161a] space-y-1">
            <h3 class="font-bold text-base text-neutral-900 dark:text-white flex items-center gap-2">
              <span>🌪️</span>
              <span>המחיר של לחץ גבוה: 4.27 xG לחובת ליברפול</span>
            </h3>
            <p class="text-sm text-neutral-600 dark:text-neutral-300 font-sans">
              ליברפול היא אחת מקבוצות הלחץ האגרסיביות בליגה (חילצה 45 כדורים מול צ'רלטון ו-53 מול ספרס). אבל כשמנצ'סטר סיטי עקפה את הגל הראשון, ליברפול ספגה 4.27 xG — שיא ה-xG השלילי שנרשם העונה ב-WSL לקבוצה במשחק בודד.
            </p>
          </div>
        </div>
      </section>
    </div>
  </article>

  <!-- Standardized Post Pagination -->
  {% include post_pagination.html %}
</div>
