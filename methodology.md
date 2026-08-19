---
layout: default
title: "מתודולוגיה | WSL Data Hub"
permalink: /methodology/
---

<div class="max-w-3xl mx-auto space-y-8">

  <!-- Header Card -->
  <div class="bg-surface-800 rounded-2xl border border-surface-700 p-8 sm:p-10 shadow-xl">
    <div class="flex items-center gap-2 mb-3">
      <span class="px-2.5 py-0.5 bg-brand-500/10 border border-brand-500/30 text-brand-400 text-xs font-semibold rounded-full">
        מתודולוגיה ושאלות מחקר
      </span>
      <span class="text-xs text-slate-500">WSL Data Hub</span>
    </div>
    <h1 class="text-3xl sm:text-4xl font-bold text-white mb-4">
      מתודולוגיה
    </h1>
    <p class="text-slate-300 text-lg leading-relaxed">
      אמרנו מדען נתונים, אז בואו נדבר קצת על הנתונים והמדדים.
    </p>
  </div>

  <!-- Main Content Card -->
  <div class="bg-surface-800 rounded-2xl border border-surface-700 p-8 sm:p-10 shadow-xl space-y-8 text-slate-300 leading-relaxed">

    <!-- Goal Section -->
    <section class="space-y-4">
      <h2 class="text-xl font-bold text-white flex items-center gap-2">
        <span>🎯</span>
        <span>המטרה שלנו</span>
      </h2>
      <p>
        אבל לפני זה, בואו נדבר שנייה על המטרה שלנו.
      </p>
      <p>
        במסגרת הפוסטים, אנתח את העונה הקודמת של כל קבוצה, ואנסה לענות האם הסגל החדש טוב יותר או שלם יותר.
      </p>
      <p>
        לטובת הניתוח אנסה לקבל תשובות ל-4 שאלות כלליות:
      </p>
    </section>

    <!-- 4 Questions Section -->
    <section class="space-y-4 pt-4 border-t border-surface-700">
      <h2 class="text-xl font-bold text-white flex items-center gap-2">
        <span>❓</span>
        <span>4 שאלות המחקר</span>
      </h2>
      
      <div class="space-y-3">
        <div class="p-4 bg-surface-700/40 rounded-xl border border-surface-600/50">
          <p class="font-bold text-brand-400 text-sm mb-1">שאלה 1: תמונת בסיס (Squad Baseline)</p>
          <p class="text-sm text-slate-200">איפה הקבוצה ממוקמת ביחס לשאר הליגה באיכות ההתקפה וההגנה (xG, xGA, יצירת מצבים ושליטה)?</p>
        </div>

        <div class="p-4 bg-surface-700/40 rounded-xl border border-surface-600/50">
          <p class="font-bold text-brand-400 text-sm mb-1">שאלה 2: רכש ויעדים (Target Signings)</p>
          <p class="text-sm text-slate-200">האם השחקניות שהצטרפו משדרגות את נקודות התורפה של הקבוצה ביחס לעונה הקודמת?</p>
        </div>

        <div class="p-4 bg-surface-700/40 rounded-xl border border-surface-600/50">
          <p class="font-bold text-brand-400 text-sm mb-1">שאלה 3: תחליפים ואיבודים (Net Replacement)</p>
          <p class="text-sm text-slate-200">מה הקבוצה מאבדת מעזיבת שחקניות מפתח והאם המחליפות מספקות תפוקה שקולה?</p>
        </div>

        <div class="p-4 bg-surface-700/40 rounded-xl border border-surface-600/50">
          <p class="font-bold text-brand-400 text-sm mb-1">שאלה 4: מאקרו ונקודות צפויות (Macro & xPTS)</p>
          <p class="text-sm text-slate-200">כמה נקודות הקבוצה הייתה "אמורה" לצבור לפי איכות הביצועים (xPTS), והאם המיקום בטבלה שיקף את היכולת האמיתית?</p>
        </div>
      </div>
    </section>

    <!-- Metrics Section -->
    <section class="space-y-6 pt-4 border-t border-surface-700">
      <div>
        <h2 class="text-xl font-bold text-white flex items-center gap-2 mb-2">
          <span>📊</span>
          <span>המדדים שבהם נשתמש</span>
        </h2>
        <p class="text-sm text-slate-400">
          על מנת לענות על השאלות האלה, נשתמש במדדים הבאים:
        </p>
      </div>

      <!-- Question 1 Metrics -->
      <div class="space-y-5">
        <h3 class="text-base font-bold text-brand-300 border-r-2 border-brand-500 pr-3">
          מדדים למענה על שאלה 1 (תמונת בסיס – Squad Baseline)
        </h3>

        <!-- Attacking -->
        <div class="bg-surface-700/30 p-4 rounded-xl space-y-2 border border-surface-700">
          <p class="font-semibold text-white text-sm">1. התקפה ואיכות איומים (Attacking & Shot Quality)</p>
          <ul class="list-disc list-inside text-xs text-slate-300 space-y-1.5 pr-2">
            <li><strong>xG לעומת G (והפרש G - xG):</strong> שערים צפויים מול שערים בפועל. מודד האם הקבוצה מייצרת מצבים איכותיים באופן עקבי או תלויה במזל וסיומת חריגה.</li>
            <li><strong>npxG/90:</strong> שערים צפויים ללא פנדלים ל-90 דקות – מדד הליבה לאיכות ייצור המצבים ממשחק פתוח.</li>
            <li><strong>Sh/90 ו-SoT%:</strong> כמות בעיטות ל-90 דקות ואחוז בעיטות למסגרת – מודד נפח איומים ויעילות הגעה למסגרת.</li>
          </ul>
        </div>

        <!-- Creation -->
        <div class="bg-surface-700/30 p-4 rounded-xl space-y-2 border border-surface-700">
          <p class="font-semibold text-white text-sm">2. יצירת מצבים (Chance Creation)</p>
          <ul class="list-disc list-inside text-xs text-slate-300 space-y-1.5 pr-2">
            <li><strong>SCA90 (Shot-Creating Actions):</strong> פעולות יוצרות בעיטה ל-90 דקות – המדד המרכזי לנפח היצירתיות של הקבוצה.</li>
            <li><strong>GCA90 (Goal-Creating Actions):</strong> פעולות יוצרות שער ל-90 דקות – בוחן את שרשרת המהלכים שמסתיימת ברשת.</li>
          </ul>
        </div>

        <!-- Defense -->
        <div class="bg-surface-700/30 p-4 rounded-xl space-y-2 border border-surface-700">
          <p class="font-semibold text-white text-sm">3. חוסן הגנתי וספיגה (Defensive Solidity)</p>
          <ul class="list-disc list-inside text-xs text-slate-300 space-y-1.5 pr-2">
            <li><strong>xGA לעומת GA:</strong> ספיגות צפויות מול שערים שנספגו בפועל מתוך טבלאות היריבות.</li>
            <li><strong>SoTA/90:</strong> בעיטות למסגרת שהיריבות מגיעות אליהן – מודד כמה ההגנה חשופה לאיומים ישירים.</li>
            <li><strong>TklW + Int:</strong> תאקלים מוצלחים וחטיפות – מדד הפעילות ההגנתית האקטיבית.</li>
          </ul>
        </div>

        <!-- Macro -->
        <div class="bg-surface-700/30 p-4 rounded-xl space-y-2 border border-surface-700">
          <p class="font-semibold text-white text-sm">4. מדד שליטה כולל (Macro Metric)</p>
          <ul class="list-disc list-inside text-xs text-slate-300 space-y-1.5 pr-2">
            <li><strong>xGD (הפרש שערים צפוי, xG - xGA):</strong> הפרש השערים הצפוי ל-90 דקות – המנבא הסטטיסטי המוביל למיקום אמיתי ולצבירת נקודות לאורך עונה.</li>
            <li><strong>Poss%:</strong> אחוז החזקה בכדור – מאפיין סגנון ושליטה בקצב המשחק.</li>
          </ul>
        </div>

      </div>

      <!-- Other Questions Placeholder -->
      <div class="p-6 bg-surface-700/20 rounded-xl border border-dashed border-surface-600 text-center space-y-2">
        <p class="text-2xl">🚧</p>
        <p class="font-bold text-white text-base">מדדים לשאלות 2, 3 ו-4</p>
        <p class="text-sm text-slate-400">כפרה עובדים</p>
      </div>

    </section>

    <!-- Scope & Notes Section -->
    <section class="space-y-4 pt-4 border-t border-surface-700">
      <div class="p-4 bg-amber-500/10 border border-amber-500/30 rounded-xl text-amber-200 text-sm">
        <strong>הערה חשובה:</strong> הליגה גדלה השנה בעוד שתי קבוצות, אשקלל גם את זה בתוך ניתוח הנתונים.
      </div>

      <p class="text-sm">
        בשלב הראשון נעשה על קבוצות מנצ'סטר ולונדון (סיטי האלופה, יונייטד שעוברת עליה הכנה מוזרה לעונה, צ'לסי האימתנית, ארסנל (שלא נדע), ספרס המתחדשת ולונדון סיטי הסופר מסקרנת), בהמשך בעזרת השם, נעשה זאת לכל קבוצות הליגה.
      </p>
    </section>

    <!-- Back link -->
    <div class="pt-6 border-t border-surface-700 flex justify-between items-center text-sm text-slate-400">
      <span>WSL Data Hub · 2025/26</span>
      <a href="{{ '/' | relative_url }}" class="text-brand-400 hover:text-brand-300 font-semibold flex items-center gap-1">
        לטבלת הליגה והקבוצות ←
      </a>
    </div>

  </div>

</div>
