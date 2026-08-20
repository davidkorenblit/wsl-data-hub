# ניתוח כל הטבלאות – WSL Data Hub

## מבנה הנתונים

יש לנו **שתי רמות נתונים** לכל קטגוריה סטטיסטית:
- **WSL-level**: כל 12 הקבוצות בליגה
- **LCL-level**: רק London City Lionesses (squad=1 row, player=כל השחקניות)

ויש **שלוש נקודות מבט** לכל קטגוריה:
- `_squad` – סיכום ברמת קבוצה
- `_player` – פירוט ברמת שחקנית
- `_opponent` – מה שהיריב עשה נגד הקבוצה (רק ב-WSL level)

---

## טבלאות WSL (ליגתיות)

### 1. `wsl_squad` / `wsl_player`
**תפקיד**: טבלת הסיכום הכללית – "סקירת כל" (standard stats).  
**מכילה**: Goals, Assists, G+A, Penalty, Cards, דקות, 90s.  
**שימוש**: **BASE TABLE** – נקודת ייחוס להשוואת קבוצות. מה הייצור ההתקפי הכולל של כל קבוצה? LCL עם 44 G+A היא מאיפה בליגה?  
**ציון חשיבות**: ⭐⭐⭐⭐⭐

### 2. `wsl_standard_squad` / `wsl_standard_player` / `wsl_standard_opponent`
**תפקיד**: גרסה מורחבת של הסטנדרט – עם נתוני xG, xA, npxG.  
**מכילה**: כל מה שב-`wsl_squad` + expected goals (xG, xAG, npxG).  
**שימוש**: **קריטי** לניתוח "האם הקבוצה מבצעת מעל/מתחת לציפייה?" – xG vs Actual Goals.  
**ציון חשיבות**: ⭐⭐⭐⭐⭐

### 3. `wsl_shooting_squad` / `wsl_shooting_player` / `wsl_shooting_opponent`
**תפקיד**: ניתוח איכות הבעיטות.  
**מכילה**: Sh, SoT, SoT%, Sh/90, G/Sh, Dist, FK, xG, npxG, G-xG.  
**שימוש**: **G-xG** – האם LCL מנצלת הזדמנויות? האם שחקנית מסוימת overperfoms/underperforms? חיוני לניתוח קרייאר שחקניות למעבר.  
**ציון חשיבות**: ⭐⭐⭐⭐⭐

### 4. `wsl_passing_squad` / `wsl_passing_player` / `wsl_passing_opponent`
**תפקיד**: ניתוח מעמיק של הפסים – כמות, דיוק, סוג.  
**מכילה**: Att, Cmp, Cmp%, TotDist, Short/Medium/Long pass breakdown, Ast, xAG, KP (Key Passes), 1/3 (passes into final third), PPA, CrsPA.  
**שימוש**: האם LCL משחקת direct או build-up? KP ו-1/3 מגלים מי מייצר. קריטי לזיהוי שחקניות שפועלות כ-"playmaker".  
**ציון חשיבות**: ⭐⭐⭐⭐⭐

### 5. `wsl_goal_and_shot_creation_squad` / `_player` / `_opponent`
**תפקיד**: ניתוח שרשרת הפעולות שמובילות לגול/בעיטה (GCA, SCA).  
**מכילה**: SCA (Shot-Creating Actions), GCA (Goal-Creating Actions), פירוט לפי סוג פעולה (Passlive, Drib, Sh, Fld, Def).  
**שימוש**: **מי מייצר** את ההזדמנויות? לא רק מי מסיים. מדד אובייקטיבי לתרומה יצירתית. מצוין לניתוח MF ו-FW.  
**ציון חשיבות**: ⭐⭐⭐⭐⭐

### 6. `wsl_possession_squad`
**תפקיד**: מדדי השתלטות על כדור – carries, take-ons, touches.  
**מכילה**: Poss%, Touches (by zone), Take-ons att/succ, Carries (distance, progressive), Rec.  
**⚠️ שים לב**: רוב העמודות `nan` – נראה שהנתון אינו זמין ב-FBref לעונה זו. רק `poss` עובד.  
**שימוש**: מוגבל כרגע. אם ייתוקן – יכול לגלות האם LCL שולטת בכדור vs סגנון קאונטר.  
**ציון חשיבות**: ⭐⭐ (כרגע, עקב nan)

### 7. `wsl_playing_time_squad` / `wsl_playing_time_player`
**תפקיד**: **מפתח מנהלי** – מי משחקת, כמה, ומתי (starts vs subs).  
**מכילה**: MP, Min, Starts, Subs, team_success (PPM, onG, onGA), team_success +/-.  
**שימוש**: **קריטי לניתוח Squad Depth**. מי שחקנית מרכזית vs שוליים? team_success +/- מגלה האם LCL מנצחת כשהשחקנית על המגרש.  
**ציון חשיבות**: ⭐⭐⭐⭐⭐

### 8. `wsl_pass_types_squad` / `_player` / `_opponent`
**תפקיד**: סוג הפסים – live, dead, FK, corners, switches.  
**מכילה**: att, live, dead, FK, TB, Sw, CRS, TI, CK, corner outcomes, blocks.  
**⚠️ שים לב**: רוב נתוני ה-pass breakdown הם `nan`. רק `pass_types_crs` (כורנרים) עובד.  
**שימוש**: מוגבל. יכול לגלות מי מכה כורנרים ו-FK, אבל הנתון חסר.  
**ציון חשיבות**: ⭐⭐ (כרגע)

### 9. `wsl_defensive_squad`
**תפקיד**: מדדי הגנה ברמת קבוצה.  
**מכילה**: Tackles (TklW), Challenges, Blocks, Int, Clr, Err.  
**⚠️ שים לב**: רוב הנתונים `nan` מלבד TklW ו-Int. הטבלה חלקית.  
**שימוש**: Int (ניצולים) ו-TklW כמדד יחסי בין הקבוצות. מוגבל.  
**ציון חשיבות**: ⭐⭐⭐

### 10. `wsl_goalkeeping_squad`
**תפקיד**: ביצועי שוערות.  
**מכילה**: GA, GA90, SoTA, Saves, Save%, W/D/L (as GK), CS%, penalty save%.  
**שימוש**: לא ישיר לאנליזת LCL (שוערת vs מגרש), אבל שימושי להשוואת חוסן הגנתי בין קבוצות.  
**ציון חשיבות**: ⭐⭐⭐

### 11. `wsl_advanced_goalkeeping_squad` / `_player` / `_opponent`
**תפקיד**: xG-based goalkeeping – PSxG, launched passes.  
**מכילה**: PSxG (post-shot expected goals), PSxG/SoT, PSxG+/-, launched pass %, average pass length, crosses/sweeper metrics.  
**⚠️ שים לב**: רוב הנתונים `nan` – זמינות נמוכה לעונה זו.  
**שימוש**: PSxG+/- הוא **המדד הטוב ביותר** לביצועי שוערת. אם יתמלא – gold.  
**ציון חשיבות**: ⭐⭐⭐⭐ (פוטנציאל גבוה)

### 12. `wsl_misc_squad`
**תפקיד**: מגוון מדדים "שאריות" שלא נכנסו לטבלאות אחרות.  
**מכילה**: CrdY, CrdR, 2CrdY, Fls (fouls), Fld (fouls drawn), Off (offsides), Crs (crosses), Int, TklW, PKwon, PKcon, OG (own goals).  
**שימוש**: Fls vs Fld – האם LCL מקבלת יותר עבירות משהיא עושה? Offsides – מדד לבניית הפקת לחץ. ציון אינדיקטיביות לסגנון משחק.  
**ציון חשיבות**: ⭐⭐⭐

---

## טבלאות LCL בלבד

### 13. `lcl_standard_squad` / `lcl_standard_player` / `lcl_standard_opponent`
**תפקיד**: ה-standard stats **בלעדית ל-LCL**.  
**מיוחד**: squad = שורה אחת (Lionesses). player = כל 26+ שחקניות.  
**שימוש**: **מיקרו ניתוח** – מה כל שחקנית ב-LCL תרמה? xG, G, Ast לכל אחת. בסיס לזיהוי top performers.  
**ציון חשיבות**: ⭐⭐⭐⭐⭐

### 14. `lcl_shooting_squad` / `lcl_shooting_player` / `lcl_shooting_opponent`
**תפקיד**: בעיטות LCL בלבד.  
**שימוש**: **G-xG per player** – מי underperforms? מי שחקנית "lucky"? חיוני לניתוח כוח הגמר.  
**ציון חשיבות**: ⭐⭐⭐⭐⭐

### 15. `lcl_passing_squad` / `lcl_passing_player` / `lcl_passing_opponent`
**תפקיד**: פסים LCL בלבד.  
**שימוש**: KP, xAG לכל שחקנית ב-LCL. מי היא ה-playmaker?  
**ציון חשיבות**: ⭐⭐⭐⭐

### 16. `lcl_goal_and_shot_creation_squad` / `_player` / `_opponent`
**תפקיד**: GCA/SCA ל-LCL.  
**שימוש**: מי מייצרת הכי הרבה הזדמנויות ב-LCL? אינדיקטור ל"מי חיוני" שלא נמדד בגולים.  
**ציון חשיבות**: ⭐⭐⭐⭐

### 17. `lcl_pass_types_squad` / `_player` / `_opponent`
**תפקיד**: סוגי פסים LCL.  
**שימוש**: מי בועטת קרנות ופריקיקים ב-LCL? תרומה ל-set pieces.  
**ציון חשיבות**: ⭐⭐⭐

### 18. `lcl_playing_time_squad` / `lcl_playing_time_player` / `lcl_playing_time_opponent`
**תפקיד**: זמן משחק ב-LCL.  
**שימוש**: **מי השחקנית המרכזית ב-LCL?** עומק הסגל. team_success +/- לכל שחקנית.  
**ציון חשיבות**: ⭐⭐⭐⭐⭐

### 19. `lcl_advanced_goalkeeping_squad` / `_player` / `_opponent`
**תפקיד**: advanced GK stats ל-LCL.  
**שימוש**: ביצועי השוערת של LCL – PSxG+/-. האם השוערת "saves above expected"?  
**ציון חשיבות**: ⭐⭐⭐⭐

---

## מפה לשאלות האנליטיות

| שאלה | טבלאות רלוונטיות |
|------|-----------------|
| **Squad Baseline** – איפה LCL בליגה? | `wsl_standard_squad`, `wsl_shooting_squad`, `wsl_playing_time_squad` |
| **Target Signings** – מי כדאי לגייס? | `wsl_standard_player`, `wsl_shooting_player`, `wsl_passing_player`, `wsl_playing_time_player` |
| **Net Replacement** – מה יחסרו אם שחקנית עוזבת? | `lcl_standard_player`, `lcl_shooting_player`, `lcl_goal_and_shot_creation_player`, `lcl_playing_time_player` |
| **Macro/xPTS** | `wsl_standard_squad`, `wsl_goalkeeping_squad`, `wsl_advanced_goalkeeping_squad` |

---

## תצפיות חשובות

1. **nan epidemic** – טבלאות `possession`, `pass_types`, `defensive` חסרות הרבה נתונים. זה לא באג בקוד – FBref פשוט לא מפרסם את הנתונים האלה ב-WSL לעונה 25/26.
2. **LCL squad = 1 שורה** – זה מובן. הפירוט האמיתי הוא ב-`_player` tables.
3. **Opponent tables** – מגלות מה היריבים עשו נגד LCL (כמה ירו, כמה הבקיעו etc). זה הצד ה"הגנתי".
4. **wsl_squad vs wsl_standard_squad** – נראה שאלה שתי גרסאות של אותם נתונים עם פורמט columns שונה (multi-level headers). כדאי לבדוק איחוד.
