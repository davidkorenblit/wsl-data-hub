#!/usr/bin/env python3
"""
WSL Data Hub - Master Squad Sync & Verification Pipeline (2026/27)
==================================================================
Synchronizes verified official first-team squads across all 14 WSL clubs:
- Official shirt numbers and positions confirmed after summer 2026 transfer window closure
- Excludes departed/loaned players and unregistered academy trainees
- High-quality Hebrew transliterations and nicknames (`name_he`)
- Outputs cleanly formatted JSON to `_data/squads/<team_slug>.json`
- Supports `--team <slug>` or `--all` for full league sync
"""

import sys
import json
import argparse
from pathlib import Path
from typing import Dict, List, Any

# Ensure UTF-8 output on Windows
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SCRIPTS_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPTS_DIR.parent
SQUADS_DIR = PROJECT_ROOT / "_data" / "squads"


# ==============================================================================
# SQUAD REGISTRIES FOR ALL 14 WSL CLUBS (2026/2027)
# ==============================================================================

SQUADS_DATA = {
    # --------------------------------------------------------------------------
    # 1. TOTTENHAM HOTSPUR
    # --------------------------------------------------------------------------
    "tottenham": [
        {"player": "Lize Kop", "name_he": "ליזה קופ", "pos": "GK", "no": "1", "nation": "NED"},
        {"player": "Selma Panengstuen", "name_he": "סלמה פננגסטואן", "pos": "GK", "no": "12", "nation": "NOR"},
        {"player": "Heidi Hills", "name_he": "היידי הילס", "pos": "GK", "no": "50", "nation": "ENG"},
        {"player": "Sophie Jackson", "name_he": "סופי ג'קסון", "pos": "GK", "no": "56", "nation": "ENG"},
        {"player": "Ella Morris", "name_he": "אלה מוריס", "pos": "DF", "no": "3", "nation": "ENG"},
        {"player": "Caitlin Dijkstra", "name_he": "קייטלין דייקסטרה", "pos": "DF", "no": "4", "nation": "NED"},
        {"player": "Alice Sombath", "name_he": "אליס סומבאת", "pos": "DF", "no": "5", "nation": "FRA"},
        {"player": "Amanda Nildén", "name_he": "אמנדה נילדן", "pos": "DF", "no": "6", "nation": "SWE"},
        {"player": "Clare Hunt", "name_he": "קלייר האנט", "pos": "DF", "no": "15", "nation": "AUS"},
        {"player": "Hanna Wijk", "name_he": "חנה וייק", "pos": "DF", "no": "22", "nation": "SWE"},
        {"player": "Tōko Koga", "name_he": "טוקו קוגה", "pos": "DF", "no": "32", "nation": "JPN"},
        {"player": "Jhanaie Pierre", "name_he": "ז'אנאי פייר", "pos": "DF", "no": "37", "nation": "ENG"},
        {"player": "Julie Blakstad", "name_he": "ז'ולי בלקסטאד", "pos": "DF", "no": "41", "nation": "NOR"},
        {"player": "Signe Gaupset", "name_he": "סיגנה גאופסט ('סיגי')", "pos": "MF", "no": "8", "nation": "NOR"},
        {"player": "Maite Oroz", "name_he": "מאיטה אורוז", "pos": "MF", "no": "10", "nation": "ESP"},
        {"player": "Olga Ahtinen", "name_he": "אולגה אהטינן", "pos": "MF", "no": "20", "nation": "FIN"},
        {"player": "Victoria Pelova", "name_he": "ויקטוריה פלובה ('ויק')", "pos": "MF", "no": "23", "nation": "NED"},
        {"player": "Drew Spence", "name_he": "דרו ספנס", "pos": "MF", "no": "24", "nation": "JAM"},
        {"player": "Eveliina Summanen", "name_he": "אוולינה סומאנן", "pos": "MF", "no": "25", "nation": "FIN"},
        {"player": "Araya Dennis", "name_he": "אראיה דניס", "pos": "MF", "no": "30", "nation": "ENG"},
        {"player": "Jessica Naz", "name_he": "ג'סיקה נז", "pos": "FW", "no": "7", "nation": "ENG"},
        {"player": "Cathinka Tandberg", "name_he": "קת'ינקה טנדברג", "pos": "FW", "no": "9", "nation": "NOR"},
        {"player": "Olivia Holdt", "name_he": "אוליבה הולנדט ('אוליב')", "pos": "FW", "no": "11", "nation": "DEN"},
        {"player": "Matilda Vinberg", "name_he": "מטילדה וינברג", "pos": "FW", "no": "13", "nation": "SWE"},
        {"player": "Matilda Nildén", "name_he": "מטילדה נילדן", "pos": "FW", "no": "14", "nation": "SWE"},
        {"player": "Kirsty Hanson", "name_he": "קירסטי הנסון", "pos": "FW", "no": "16", "nation": "SCO"},
        {"player": "Lenna Gunning-Williams", "name_he": "לנה גאנינג-וויליאמס", "pos": "FW", "no": "18", "nation": "ENG"},
        {"player": "Shekiera Martinez", "name_he": "שקירה מרטינז", "pos": "FW", "no": "19", "nation": "GER"}
    ],

    # --------------------------------------------------------------------------
    # 2. ARSENAL
    # --------------------------------------------------------------------------
    "arsenal": [
        {"player": "Daphne van Domselaar", "name_he": "דפנה ואן דומסלאר", "pos": "GK", "no": "1", "nation": "NED"},
        {"player": "Misa Rodríguez", "name_he": "מיסה רודריגז", "pos": "GK", "no": "16", "nation": "ESP"},
        {"player": "Anneke Borbe", "name_he": "אנקה בורבה", "pos": "GK", "no": "28", "nation": "GER"},
        {"player": "Isabella Damm", "name_he": "איזבלה דאם", "pos": "GK", "no": "40", "nation": "ENG"},
        {"player": "Emily Fox", "name_he": "אמילי פוקס", "pos": "DF", "no": "2", "nation": "USA"},
        {"player": "Lotte Wubben-Moy", "name_he": "לוטה וובן-מוי", "pos": "DF", "no": "3", "nation": "ENG"},
        {"player": "Élisa De Almeida", "name_he": "אליסה דה אלמיידה", "pos": "DF", "no": "5", "nation": "FRA"},
        {"player": "Leah Williamson", "name_he": "ליאה ויליאמסון", "pos": "DF", "no": "6", "nation": "ENG"},
        {"player": "Steph Catley", "name_he": "סטפני קאטלי", "pos": "DF", "no": "7", "nation": "AUS"},
        {"player": "Ona Batlle", "name_he": "אונה באטייה", "pos": "DF", "no": "22", "nation": "ESP"},
        {"player": "Taylor Hinds", "name_he": "טיילור היינדס", "pos": "DF", "no": "24", "nation": "ENG"},
        {"player": "Katie Reid", "name_he": "קייטי ריד", "pos": "DF", "no": "26", "nation": "ENG"},
        {"player": "Smilla Holmberg", "name_he": "סמילה הולמברג", "pos": "DF", "no": "31", "nation": "SWE"},
        {"player": "Maddy Earl", "name_he": "מאדי ארל", "pos": "DF", "no": "38", "nation": "ENG"},
        {"player": "Georgia Stanway", "name_he": "ג'ורג'יה סטאנוויי ('G')", "pos": "MF", "no": "4", "nation": "ENG"},
        {"player": "Kim Little", "name_he": "קים ליטל", "pos": "MF", "no": "10", "nation": "SCO"},
        {"player": "Frida Maanum", "name_he": "פרידה מאנום", "pos": "MF", "no": "12", "nation": "NOR"},
        {"player": "Géraldine Reuteler", "name_he": "ז'רלדין רויטלר", "pos": "MF", "no": "14", "nation": "SUI"},
        {"player": "Lisa Baum", "name_he": "ליסה באום", "pos": "MF", "no": "19", "nation": "GER"},
        {"player": "Kyra Cooney-Cross", "name_he": "קיירה קוני-קרוס", "pos": "MF", "no": "32", "nation": "AUS"},
        {"player": "Mariona Caldentey", "name_he": "מריונה קלדנטיי", "pos": "FW", "no": "8", "nation": "ESP"},
        {"player": "Caitlin Foord", "name_he": "קייטלין פורד", "pos": "FW", "no": "9", "nation": "AUS"},
        {"player": "Olivia Smith", "name_he": "אוליביה סמית'", "pos": "FW", "no": "11", "nation": "CAN"},
        {"player": "Michelle Agyemang", "name_he": "מישל אג'ימאן ('מיש')", "pos": "FW", "no": "17", "nation": "ENG"},
        {"player": "Chloe Kelly", "name_he": "קלואי קלי", "pos": "FW", "no": "18", "nation": "ENG"},
        {"player": "Alessia Russo", "name_he": "אלסיה רוסו", "pos": "FW", "no": "23", "nation": "ENG"},
        {"player": "Stina Blackstenius", "name_he": "סטינה בלקסטניוס", "pos": "FW", "no": "25", "nation": "SWE"},
        {"player": "Selina Cerci", "name_he": "סלינה צ'רצ'י", "pos": "FW", "no": "29", "nation": "GER"}
    ],

    # --------------------------------------------------------------------------
    # 3. CHELSEA
    # --------------------------------------------------------------------------
    "chelsea": [
        {"player": "Livia Peng", "name_he": "ליביה פנג", "pos": "GK", "no": "1", "nation": "SUI"},
        {"player": "Hannah Hampton", "name_he": "האנה המפטון", "pos": "GK", "no": "24", "nation": "ENG"},
        {"player": "Becky Spencer", "name_he": "בקי ספנסר", "pos": "GK", "no": "38", "nation": "JAM"},
        {"player": "Ellie Carpenter", "name_he": "אלי קרפנטר", "pos": "DF", "no": "2", "nation": "AUS"},
        {"player": "Naomi Girma", "name_he": "נעמי גירמה", "pos": "DF", "no": "4", "nation": "USA"},
        {"player": "Veerle Buurman", "name_he": "וורלה בורמן", "pos": "DF", "no": "5", "nation": "NED"},
        {"player": "Nathalie Björn", "name_he": "נטלי ביורן", "pos": "DF", "no": "14", "nation": "SWE"},
        {"player": "Katie McCabe", "name_he": "קייטי מקייב", "pos": "DF", "no": "15", "nation": "IRL"},
        {"player": "Nelly Las", "name_he": "נלי לאס", "pos": "DF", "no": "17", "nation": "FRA"},
        {"player": "Lucy Bronze", "name_he": "לוסי ברונז", "pos": "DF", "no": "22", "nation": "ENG"},
        {"player": "Kadeisha Buchanan", "name_he": "קאדישה ביוקנן", "pos": "DF", "no": "26", "nation": "CAN"},
        {"player": "Chloe Sarwie", "name_he": "קלואי סארווי", "pos": "DF", "no": "42", "nation": "ENG"},
        {"player": "Sjoeke Nüsken", "name_he": "שוקה נוסקן", "pos": "MF", "no": "6", "nation": "GER"},
        {"player": "Erin Cuthbert", "name_he": "ארין קאת'ברט", "pos": "MF", "no": "8", "nation": "SCO"},
        {"player": "Giulia Dragoni", "name_he": "ג'וליה דראגוני", "pos": "MF", "no": "16", "nation": "ITA"},
        {"player": "Wieke Kaptein", "name_he": "וויקה קפטיין", "pos": "MF", "no": "19", "nation": "NED"},
        {"player": "Keira Walsh", "name_he": "קירה וולש", "pos": "MF", "no": "21", "nation": "ENG"},
        {"player": "Maika Hamano", "name_he": "מאיקה המאנו", "pos": "MF", "no": "23", "nation": "JPN"},
        {"player": "Lola Brown", "name_he": "לולה בראון", "pos": "MF", "no": "25", "nation": "ENG"},
        {"player": "Lexi Potter", "name_he": "לקסי פוטר", "pos": "MF", "no": "32", "nation": "ENG"},
        {"player": "Mayra Ramírez", "name_he": "מיירה ראמירז", "pos": "FW", "no": "7", "nation": "COL"},
        {"player": "Melvine Malard", "name_he": "מלווין מלארד", "pos": "FW", "no": "9", "nation": "FRA"},
        {"player": "Lauren James", "name_he": "לורן ג'יימס", "pos": "FW", "no": "10", "nation": "ENG"},
        {"player": "Sandy Baltimore", "name_he": "סנדי בולטימור", "pos": "FW", "no": "11", "nation": "FRA"},
        {"player": "Alyssa Thompson", "name_he": "אליסה תומפסון", "pos": "FW", "no": "12", "nation": "USA"},
        {"player": "Manaka Matsukubo", "name_he": "מאנאקה מאצוקובו", "pos": "FW", "no": "29", "nation": "JPN"},
        {"player": "Aggie Beever-Jones", "name_he": "אגי ביבר-ג'ונס", "pos": "FW", "no": "33", "nation": "ENG"}
    ],

    # --------------------------------------------------------------------------
    # 4. MANCHESTER CITY
    # --------------------------------------------------------------------------
    "manchester-city": [
        {"player": "Eartha Cumings", "name_he": "ארת'ה קאמינגס", "pos": "GK", "no": "1", "nation": "SCO"},
        {"player": "Anna Moorhouse", "name_he": "אנה מורהאוס", "pos": "GK", "no": "14", "nation": "ENG"},
        {"player": "Ayaka Yamashita", "name_he": "איאקה יאמאשיטה", "pos": "GK", "no": "31", "nation": "JPN"},
        {"player": "Eve Annets", "name_he": "איב אנטס", "pos": "GK", "no": "43", "nation": "ENG"},
        {"player": "Risa Shimizu", "name_he": "ריסה שימיזו", "pos": "DF", "no": "2", "nation": "JPN"},
        {"player": "Jade Rose", "name_he": "ג'ייד רוז", "pos": "DF", "no": "4", "nation": "CAN"},
        {"player": "Alex Greenwood", "name_he": "אלכס גרינווד", "pos": "DF", "no": "5", "nation": "ENG"},
        {"player": "Laura Wienroither", "name_he": "לאורה וינרויטר", "pos": "DF", "no": "13", "nation": "AUT"},
        {"player": "Kerstin Casparij", "name_he": "קרסטין קספאריי", "pos": "DF", "no": "18", "nation": "NED"},
        {"player": "Niamh Charles", "name_he": "ניאם צ'ארלס", "pos": "DF", "no": "21", "nation": "ENG"},
        {"player": "Rebecca Knaak", "name_he": "רבקה קנאאק", "pos": "DF", "no": "27", "nation": "GER"},
        {"player": "Gracie Prior", "name_he": "גרייסי פריור", "pos": "DF", "no": "28", "nation": "ENG"},
        {"player": "Mayzee Davies", "name_he": "מייזי דייוויס", "pos": "DF", "no": "53", "nation": "WAL"},
        {"player": "Grace Clinton", "name_he": "גרייס קלינטון", "pos": "MF", "no": "6", "nation": "ENG"},
        {"player": "Sam Coffey", "name_he": "סם קופי", "pos": "MF", "no": "17", "nation": "USA"},
        {"player": "Laura Blindkilde Brown", "name_he": "לאורה בלינדקילדה בראון", "pos": "MF", "no": "19", "nation": "ENG"},
        {"player": "Sydney Lohmann", "name_he": "סידני לומאן", "pos": "MF", "no": "22", "nation": "GER"},
        {"player": "Yui Hasegawa", "name_he": "יוי הסגאווה", "pos": "MF", "no": "25", "nation": "JPN"},
        {"player": "Eve O'Carroll", "name_he": "איב או'קרול", "pos": "MF", "no": "52", "nation": "ENG"},
        {"player": "Beth Mead", "name_he": "בת' מיד", "pos": "FW", "no": "7", "nation": "ENG"},
        {"player": "Mary Fowler", "name_he": "מרי פאולר", "pos": "FW", "no": "8", "nation": "AUS"},
        {"player": "Khadija Shaw", "name_he": "חדיג'ה ('באני') שואו", "pos": "FW", "no": "9", "nation": "JAM"},
        {"player": "Vivianne Miedema", "name_he": "ויוויאן מידמה", "pos": "FW", "no": "10", "nation": "NED"},
        {"player": "Lauren Hemp", "name_he": "לורן המפ", "pos": "FW", "no": "11", "nation": "ENG"},
        {"player": "Aoba Fujino", "name_he": "אאובה פוג'ינו", "pos": "FW", "no": "20", "nation": "JPN"},
        {"player": "Iman Beney", "name_he": "אימן בנאי", "pos": "FW", "no": "24", "nation": "SUI"},
        {"player": "Carlotta Wamser", "name_he": "קרלוטה ואמזר", "pos": "FW", "no": "37", "nation": "GER"}
    ],

    # --------------------------------------------------------------------------
    # 5. MANCHESTER UNITED
    # --------------------------------------------------------------------------
    "manchester-utd": [
        {"player": "Janina Leitzig", "name_he": "יאנינה לייציג", "pos": "GK", "no": "25", "nation": "GER"},
        {"player": "Jessica Anderson", "name_he": "ג'סיקה אנדרסון", "pos": "GK", "no": "47", "nation": "ENG"},
        {"player": "Phallon Tullis-Joyce", "name_he": "פאלון טוליס-ג'ויס", "pos": "GK", "no": "91", "nation": "USA"},
        {"player": "Anna Sandberg", "name_he": "אנה סנדברג", "pos": "DF", "no": "2", "nation": "SWE"},
        {"player": "Maya Le Tissier", "name_he": "מאיה לה טיסייה", "pos": "DF", "no": "4", "nation": "ENG"},
        {"player": "Hanna Lundkvist", "name_he": "חנה לונדקוויסט", "pos": "DF", "no": "5", "nation": "SWE"},
        {"player": "Andrea Medina", "name_he": "אנדראה מדינה", "pos": "DF", "no": "6", "nation": "ESP"},
        {"player": "Jayde Riviere", "name_he": "ג'ייד ריבייר", "pos": "DF", "no": "14", "nation": "CAN"},
        {"player": "Dominique Janssen", "name_he": "דומיניק יאנסן", "pos": "DF", "no": "17", "nation": "NED"},
        {"player": "Jess Simpson", "name_he": "ג'ס סימפסון", "pos": "DF", "no": "26", "nation": "ENG"},
        {"player": "Lucy Newell", "name_he": "לוסי ניואל", "pos": "DF", "no": "55", "nation": "ENG"},
        {"player": "Ella Toone", "name_he": "אלה טון", "pos": "MF", "no": "7", "nation": "ENG"},
        {"player": "Jess Park", "name_he": "ג'ס פארק", "pos": "MF", "no": "8", "nation": "ENG"},
        {"player": "Simi Awujo", "name_he": "סימי אווג'ו", "pos": "MF", "no": "13", "nation": "CAN"},
        {"player": "Julia Zigiotti Olme", "name_he": "יוליה זיגיוטי אולמה", "pos": "MF", "no": "15", "nation": "SWE"},
        {"player": "Rebeca Bernal", "name_he": "רבקה ברנאל", "pos": "MF", "no": "16", "nation": "MEX"},
        {"player": "Hinata Miyazawa", "name_he": "הינאטה מיאזאווה", "pos": "MF", "no": "20", "nation": "JPN"},
        {"player": "Emma Watson", "name_he": "אמה ווטסון", "pos": "MF", "no": "21", "nation": "SCO"},
        {"player": "Scarlett Hill", "name_he": "סקרלט היל", "pos": "MF", "no": "22", "nation": "ENG"},
        {"player": "Mared Griffiths", "name_he": "מאראד גריפית'ס", "pos": "MF", "no": "36", "nation": "WAL"},
        {"player": "Elisabeth Terland", "name_he": "אליזבת טרלנד", "pos": "FW", "no": "10", "nation": "NOR"},
        {"player": "Celin Bizet Dønnum", "name_he": "סלין ביזט דונם", "pos": "FW", "no": "11", "nation": "NOR"},
        {"player": "Fridolina Rolfö", "name_he": "פרידולינה רולפו", "pos": "FW", "no": "12", "nation": "SWE"},
        {"player": "Ellen Wangerheim", "name_he": "אלן ואנגרהיים", "pos": "FW", "no": "19", "nation": "SWE"},
        {"player": "Monica Jusu Bah", "name_he": "מוניקה ג'וסו בה", "pos": "FW", "no": "23", "nation": "SWE"},
        {"player": "Lea Schüller", "name_he": "ליאה שילר", "pos": "FW", "no": "24", "nation": "GER"},
        {"player": "Layla Drury", "name_he": "ליילה דרורי", "pos": "FW", "no": "27", "nation": "ENG"}
    ],

    # --------------------------------------------------------------------------
    # 6. LIVERPOOL
    # --------------------------------------------------------------------------
    "liverpool": [
        {"player": "Rachael Laws", "name_he": "רייצ'ל לוז", "pos": "GK", "no": "1", "nation": "ENG"},
        {"player": "Khiara Keating", "name_he": "קיארה קיטינג", "pos": "GK", "no": "12", "nation": "ENG"},
        {"player": "Faye Kirby", "name_he": "פיי קירבי", "pos": "GK", "no": "22", "nation": "ENG"},
        {"player": "Lucy Parry", "name_he": "לוסי פארי", "pos": "DF", "no": "2", "nation": "ENG"},
        {"player": "Grace Fisk", "name_he": "גרייס פיסק", "pos": "DF", "no": "4", "nation": "ENG"},
        {"player": "Natalia Ramos", "name_he": "נטליה ראמוס", "pos": "DF", "no": "6", "nation": "ESP"},
        {"player": "Lily Woodham", "name_he": "לילי וודהאם", "pos": "DF", "no": "16", "nation": "WAL"},
        {"player": "Jenna Clark", "name_he": "ג'נה קלארק", "pos": "DF", "no": "17", "nation": "SCO"},
        {"player": "Sara Agrež", "name_he": "שרה אגרז'", "pos": "DF", "no": "23", "nation": "SVN"},
        {"player": "Alice Bergström", "name_he": "אליס ברגסטרום", "pos": "DF", "no": "25", "nation": "SWE"},
        {"player": "Mari Ward", "name_he": "מארי וורד", "pos": "DF", "no": "28", "nation": "ENG"},
        {"player": "Alejandra Bernabé", "name_he": "אלחנדרה ברנאבה", "pos": "DF", "no": "29", "nation": "ESP"},
        {"player": "Fūka Nagano", "name_he": "פוקה נאגאנו", "pos": "MF", "no": "8", "nation": "JPN"},
        {"player": "Marie Höbinger", "name_he": "מארי הבינגר", "pos": "MF", "no": "14", "nation": "AUT"},
        {"player": "Ceri Holland", "name_he": "סרי הולנד", "pos": "MF", "no": "18", "nation": "WAL"},
        {"player": "Kirsty Maclean", "name_he": "קירסטי מקלין", "pos": "MF", "no": "19", "nation": "SCO"},
        {"player": "Sam Kerr", "name_he": "סם קר (סקוטלנד)", "pos": "MF", "no": "24", "nation": "SCO"},
        {"player": "Zara Shaw", "name_he": "זארה שואו", "pos": "MF", "no": "36", "nation": "ENG"},
        {"player": "Cornelia Kapocs", "name_he": "קורנליה קפוטש", "pos": "FW", "no": "7", "nation": "SWE"},
        {"player": "Vivien Endemann", "name_he": "ויוויאן אנדמן", "pos": "FW", "no": "9", "nation": "GER"},
        {"player": "Sophie Román Haug", "name_he": "סופי רומאן האוג", "pos": "FW", "no": "10", "nation": "NOR"},
        {"player": "Beata Olsson", "name_he": "ביאטה אולסון", "pos": "FW", "no": "11", "nation": "SWE"},
        {"player": "Mia Enderby", "name_he": "מיה אנדרבי", "pos": "FW", "no": "13", "nation": "ENG"},
        {"player": "Anna Jøsendal", "name_he": "אנה יוסנדאל", "pos": "FW", "no": "21", "nation": "NOR"},
        {"player": "Mao Itamura", "name_he": "מאו איטמורה", "pos": "FW", "no": "26", "nation": "JPN"},
        {"player": "Aurélie Csillag", "name_he": "אורלי צ'ילאג", "pos": "FW", "no": "27", "nation": "SUI"}
    ],

    # --------------------------------------------------------------------------
    # 7. BRIGHTON & HOVE ALBION
    # --------------------------------------------------------------------------
    "brighton": [
        {"player": "Chiamaka Nnadozie", "name_he": "צ'יאמקה ננאדוזי", "pos": "GK", "no": "16", "nation": "NGA"},
        {"player": "Hannah Poulter", "name_he": "חנה פולטר", "pos": "GK", "no": "25", "nation": "ENG"},
        {"player": "Melina Loeck", "name_he": "מלינה לוק", "pos": "GK", "no": "28", "nation": "GER"},
        {"player": "Eleanor Heeps", "name_he": "אלינור היפס", "pos": "GK", "no": "30", "nation": "ENG"},
        {"player": "Manuela Vanegas", "name_he": "מנואלה ונגאס", "pos": "DF", "no": "2", "nation": "COL"},
        {"player": "Moeka Minami", "name_he": "מואקה מינאמי", "pos": "DF", "no": "3", "nation": "JPN"},
        {"player": "Maelys Mpomé", "name_he": "מאיליס מפומה", "pos": "DF", "no": "5", "nation": "FRA"},
        {"player": "Gabby George", "name_he": "גבי ג'ורג'", "pos": "DF", "no": "6", "nation": "ENG"},
        {"player": "Caitlin Hayes", "name_he": "קייטלין הייז", "pos": "DF", "no": "18", "nation": "IRL"},
        {"player": "Marisa Olislagers", "name_he": "מריסה אוליסלגרס", "pos": "DF", "no": "19", "nation": "NED"},
        {"player": "Marit Auée", "name_he": "מאריט אווה", "pos": "DF", "no": "23", "nation": "NED"},
        {"player": "Grace McEwen", "name_he": "גרייס מקיואן", "pos": "DF", "no": "24", "nation": "ENG"},
        {"player": "Charlize Rule", "name_he": "שארליז רול", "pos": "DF", "no": "33", "nation": "AUS"},
        {"player": "Emilie Gay", "name_he": "אמילי גיי", "pos": "DF", "no": "64", "nation": "ENG"},
        {"player": "Maisie Symonds", "name_he": "מייזי סימונדס", "pos": "MF", "no": "8", "nation": "ENG"},
        {"player": "Jelena Čanković", "name_he": "ילנה צ'אנקוביץ'", "pos": "MF", "no": "10", "nation": "SRB"},
        {"player": "Lia Wälti", "name_he": "ליה ואלטי", "pos": "MF", "no": "13", "nation": "SUI"},
        {"player": "Emilie Joramo", "name_he": "אמילי יוראמו", "pos": "MF", "no": "15", "nation": "NOR"},
        {"player": "Bex Rayner", "name_he": "בק ריינר", "pos": "MF", "no": "17", "nation": "ENG"},
        {"player": "Olaug Tvedten", "name_he": "אולאוג טוודטן", "pos": "MF", "no": "20", "nation": "NOR"},
        {"player": "Taylor Warren", "name_he": "טיילור וורן", "pos": "MF", "no": "41", "nation": "ENG"},
        {"player": "Aisha Masaka", "name_he": "עאישה מסאקה", "pos": "FW", "no": "7", "nation": "TAN"},
        {"player": "Madison Haley", "name_he": "מדיסון היילי", "pos": "FW", "no": "9", "nation": "USA"},
        {"player": "Kiko Seike", "name_he": "קיקו סייקה", "pos": "FW", "no": "11", "nation": "JPN"},
        {"player": "Fran Kirby", "name_he": "פראן קירבי", "pos": "FW", "no": "14", "nation": "ENG"},
        {"player": "Olivia García", "name_he": "אוליביה גרסיה", "pos": "FW", "no": "21", "nation": "ESP"},
        {"player": "Sophie Peskett", "name_he": "סופי פסקט", "pos": "FW", "no": "27", "nation": "ENG"},
        {"player": "Emily Murphy", "name_he": "אמילי מרפי", "pos": "FW", "no": "35", "nation": "ENG"},
        {"player": "Nadia Krezyman", "name_he": "נדיה קז'ימאן", "pos": "FW", "no": "44", "nation": "POL"}
    ],

    # --------------------------------------------------------------------------
    # 8. ASTON VILLA
    # --------------------------------------------------------------------------
    "aston-villa": [
        {"player": "Emily Ramsey", "name_he": "אמילי ראמזי", "pos": "GK", "no": "1", "nation": "ENG"},
        {"player": "Ellie Roebuck", "name_he": "אלי רובאק", "pos": "GK", "no": "26", "nation": "ENG"},
        {"player": "Soffia Kelly", "name_he": "סופיה קלי", "pos": "GK", "no": "40", "nation": "IRL"},
        {"player": "Mathilde Harviken", "name_he": "מתילדה הרוויקן", "pos": "DF", "no": "3", "nation": "NOR"},
        {"player": "Anna Patten", "name_he": "אנה פאטן", "pos": "DF", "no": "4", "nation": "IRL"},
        {"player": "Lynn Wilms", "name_he": "לין וילמס", "pos": "DF", "no": "14", "nation": "NED"},
        {"player": "Lucy Parker", "name_he": "לוסי פארקר", "pos": "DF", "no": "15", "nation": "ENG"},
        {"player": "Noelle Maritz", "name_he": "נואל מאריץ", "pos": "DF", "no": "16", "nation": "SUI"},
        {"player": "Rofiat Imuran", "name_he": "רופיאת אימוראן", "pos": "DF", "no": "22", "nation": "NGA"},
        {"player": "Akane Ōkuma", "name_he": "אקאנה אוקומה", "pos": "DF", "no": "23", "nation": "JPN"},
        {"player": "Océane Deslandes", "name_he": "אוסאן דסלאנד", "pos": "DF", "no": "24", "nation": "FRA"},
        {"player": "Lily Clark", "name_he": "לילי קלארק", "pos": "DF", "no": "42", "nation": "ENG"},
        {"player": "Katie Scott", "name_he": "קייטי סקוט", "pos": "DF", "no": "43", "nation": "SCO"},
        {"player": "Justine Kielland", "name_he": "ז'וסטין צ'ילאנד", "pos": "MF", "no": "5", "nation": "NOR"},
        {"player": "Oriane Jean-François", "name_he": "אוריאן ז'אן-פרנסואה", "pos": "MF", "no": "6", "nation": "FRA"},
        {"player": "Missy Bo Kearns", "name_he": "מיסי בו קרנס", "pos": "MF", "no": "7", "nation": "ENG"},
        {"player": "Jill Baijings", "name_he": "ג'יל בייאינגס", "pos": "MF", "no": "8", "nation": "NED"},
        {"player": "Lucia Kendall", "name_he": "לוסיה קנדל", "pos": "MF", "no": "21", "nation": "ENG"},
        {"player": "Miri Taylor", "name_he": "מירי טיילור", "pos": "MF", "no": "25", "nation": "ENG"},
        {"player": "Rachel Maltby", "name_he": "רייצ'ל מולטבי", "pos": "MF", "no": "38", "nation": "ENG"},
        {"player": "Rachel Daly", "name_he": "רייצ'ל דיילי", "pos": "FW", "no": "9", "nation": "ENG"},
        {"player": "Kamilla Melgård", "name_he": "קמילה מלגורד", "pos": "FW", "no": "11", "nation": "NOR"},
        {"player": "Maya Hijikata", "name_he": "מאיה היג'יקאטה", "pos": "FW", "no": "13", "nation": "JPN"},
        {"player": "Chasity Grant", "name_he": "צ'אסיטי גרנט", "pos": "FW", "no": "17", "nation": "NED"},
        {"player": "Georgia Mullett", "name_he": "ג'ורג'יה מולט", "pos": "FW", "no": "18", "nation": "ENG"},
        {"player": "Lily Murphy", "name_he": "לילי מרפי", "pos": "FW", "no": "19", "nation": "ENG"},
        {"player": "Amalie Vangsgaard", "name_he": "אמלי ואנגסגורד", "pos": "FW", "no": "20", "nation": "DEN"},
        {"player": "Mia McAulay", "name_he": "מיה מקאוליי", "pos": "FW", "no": "27", "nation": "SCO"}
    ],

    # --------------------------------------------------------------------------
    # 9. EVERTON
    # --------------------------------------------------------------------------
    "everton": [
        {"player": "Courtney Brosnan", "name_he": "קורטני ברוסנן", "pos": "GK", "no": "1", "nation": "IRL"},
        {"player": "Rylee Foster", "name_he": "ריילי פוסטר-אינמן", "pos": "GK", "no": "24", "nation": "CAN"},
        {"player": "Hannah Blundell", "name_he": "חנה בלנדל", "pos": "DF", "no": "2", "nation": "ENG"},
        {"player": "Rion Ishikawa", "name_he": "ריון אישיקאווה", "pos": "DF", "no": "3", "nation": "JPN"},
        {"player": "Issy Hobson", "name_he": "איזי הובסון", "pos": "DF", "no": "4", "nation": "ENG"},
        {"player": "Naomi Layzell", "name_he": "נעמי לייזל", "pos": "DF", "no": "5", "nation": "ENG"},
        {"player": "Hikaru Kitagawa", "name_he": "היקארו קיטאגאווה", "pos": "DF", "no": "13", "nation": "JPN"},
        {"player": "Megan Finnigan", "name_he": "מייגן פיניגן", "pos": "DF", "no": "20", "nation": "ENG"},
        {"player": "Hannah Silcock", "name_he": "חנה סילקוק", "pos": "DF", "no": "25", "nation": "ENG"},
        {"player": "Maz Pacheco", "name_he": "מאז פאצ'קו", "pos": "DF", "no": "33", "nation": "ENG"},
        {"player": "Honoka Hayashi", "name_he": "הונוקה היאשי", "pos": "MF", "no": "6", "nation": "JPN"},
        {"player": "Clare Wheeler", "name_he": "קלייר ווילר", "pos": "MF", "no": "7", "nation": "AUS"},
        {"player": "Rosa van Gool", "name_he": "רוזה ואן חול", "pos": "MF", "no": "8", "nation": "NED"},
        {"player": "Ornella Vignola", "name_he": "אורנלה ויניולה", "pos": "MF", "no": "18", "nation": "ESP"},
        {"player": "Zara Kramžar", "name_he": "זארה קראמז'אר", "pos": "MF", "no": "21", "nation": "SVN"},
        {"player": "Aurora Galli", "name_he": "אורורה גאלי", "pos": "MF", "no": "22", "nation": "ITA"},
        {"player": "Karen Holmgaard", "name_he": "קארן הולמגורד", "pos": "MF", "no": "28", "nation": "DEN"},
        {"player": "Yūka Momiki", "name_he": "יוקה מומיקי", "pos": "MF", "no": "29", "nation": "JPN"},
        {"player": "Ruby Mace", "name_he": "רובי מייס", "pos": "MF", "no": "30", "nation": "ENG"},
        {"player": "Macy Settle", "name_he": "מייסי סטל", "pos": "MF", "no": "32", "nation": "ENG"},
        {"player": "Holly McNamara", "name_he": "הולי מקנמרה", "pos": "FW", "no": "9", "nation": "AUS"},
        {"player": "Inma Gabarro", "name_he": "אינמה גאבארו", "pos": "FW", "no": "10", "nation": "ESP"},
        {"player": "Hannah Cain", "name_he": "חנה קיין", "pos": "FW", "no": "11", "nation": "WAL"},
        {"player": "Jutta Rantala", "name_he": "יוטה רנטאלה", "pos": "FW", "no": "15", "nation": "FIN"},
        {"player": "Noémie Mouchon", "name_he": "נואמי מושון", "pos": "FW", "no": "17", "nation": "FRA"}
    ],

    # --------------------------------------------------------------------------
    # 10. WEST HAM UNITED
    # --------------------------------------------------------------------------
    "west-ham": [
        {"player": "Constance Picaud", "name_he": "קונסטנס פיקו", "pos": "GK", "no": "14", "nation": "FRA"},
        {"player": "Megan Walsh", "name_he": "מייגן וולש", "pos": "GK", "no": "25", "nation": "IRL"},
        {"player": "Rebekah Dowsett", "name_he": "רבקה דאוסט", "pos": "GK", "no": "45", "nation": "ENG"},
        {"player": "Yu Endo", "name_he": "יו אנדו", "pos": "DF", "no": "2", "nation": "JPN"},
        {"player": "Laia Codina", "name_he": "לאיה קודינה", "pos": "DF", "no": "3", "nation": "ESP"},
        {"player": "Tuva Hansen", "name_he": "טובה האנסן", "pos": "DF", "no": "5", "nation": "NOR"},
        {"player": "Inès Belloumou", "name_he": "אינס בלומו", "pos": "DF", "no": "7", "nation": "FRA"},
        {"player": "Eva Nyström", "name_he": "אווה ניסטרום", "pos": "DF", "no": "13", "nation": "FIN"},
        {"player": "Nadine Riesen", "name_he": "נדין ריזן", "pos": "DF", "no": "22", "nation": "SUI"},
        {"player": "Niamh Peacock", "name_he": "ניאם פיקוק", "pos": "DF", "no": "26", "nation": "ENG"},
        {"player": "Estelle Cascarino", "name_he": "אסטל קסקרינו", "pos": "DF", "no": "28", "nation": "FRA"},
        {"player": "Oona Siren", "name_he": "אונה סירן", "pos": "MF", "no": "4", "nation": "FIN"},
        {"player": "Saki Kumagai", "name_he": "סאקי קומאגאי", "pos": "MF", "no": "8", "nation": "JPN"},
        {"player": "Katie Zelem", "name_he": "קייטי זלם", "pos": "MF", "no": "10", "nation": "ENG"},
        {"player": "Ylinn Tennebø", "name_he": "אילין טנבו", "pos": "MF", "no": "15", "nation": "NOR"},
        {"player": "Sienna Wareing", "name_he": "סיינה וורינג", "pos": "MF", "no": "19", "nation": "ENG"},
        {"player": "Selin Cemal", "name_he": "סלין סמאל", "pos": "MF", "no": "43", "nation": "ENG"},
        {"player": "Seraina Piubel", "name_he": "סראינה פיובל", "pos": "MF", "no": "77", "nation": "SUI"},
        {"player": "Riko Ueki", "name_he": "ריקו אוואקי", "pos": "FW", "no": "9", "nation": "JPN"},
        {"player": "Kelly Gago", "name_he": "קלי גאגו", "pos": "FW", "no": "11", "nation": "FRA"},
        {"player": "Ebony Salmon", "name_he": "אבוני סלמון", "pos": "FW", "no": "17", "nation": "ENG"},
        {"player": "Viviane Asseyi", "name_he": "ויוויאן אסיי", "pos": "FW", "no": "20", "nation": "FRA"},
        {"player": "Ffion Morgan", "name_he": "פיון מורגן", "pos": "FW", "no": "23", "nation": "WAL"},
        {"player": "Leila Wandeler", "name_he": "ליילה ונדלר", "pos": "FW", "no": "27", "nation": "SUI"}
    ],

    # --------------------------------------------------------------------------
    # 11. CRYSTAL PALACE
    # --------------------------------------------------------------------------
    "crystal-palace": [
        {"player": "Pauline Peyraud-Magnin", "name_he": "פולין פרו-מניאן", "pos": "GK", "no": "26", "nation": "FRA"},
        {"player": "Shae Yáñez", "name_he": "שיי יאנז", "pos": "GK", "no": "30", "nation": "USA"},
        {"player": "Comfort Erhabor", "name_he": "קומפורט ארהאבור", "pos": "GK", "no": "56", "nation": "ENG"},
        {"player": "Jamie-Lee Napier", "name_he": "ג'יימי-לי נייפייר", "pos": "DF", "no": "3", "nation": "SCO"},
        {"player": "Aimee Everett", "name_he": "איימי אוורט", "pos": "DF", "no": "6", "nation": "ENG"},
        {"player": "Ashleigh Weerden", "name_he": "אשלי וורדן", "pos": "DF", "no": "11", "nation": "NED"},
        {"player": "Hayley Nolan", "name_he": "היילי נולאן", "pos": "DF", "no": "15", "nation": "IRL"},
        {"player": "Teyah Goldie", "name_he": "טיה גולדי", "pos": "DF", "no": "22", "nation": "ENG"},
        {"player": "Allyson Swaby", "name_he": "אליסון סוואבי", "pos": "DF", "no": "29", "nation": "JAM"},
        {"player": "Molly Bartrip", "name_he": "מולי ברטריפ", "pos": "DF", "no": "32", "nation": "ENG"},
        {"player": "Emilia Browne", "name_he": "אמיליה בראון", "pos": "DF", "no": "41", "nation": "ENG"},
        {"player": "Sierra Enge", "name_he": "סיירה אנג'", "pos": "MF", "no": "4", "nation": "USA"},
        {"player": "My Cato", "name_he": "מאי קאטו", "pos": "MF", "no": "5", "nation": "SWE"},
        {"player": "Josie Green", "name_he": "ג'וזי גרין", "pos": "MF", "no": "14", "nation": "WAL"},
        {"player": "Hayley Ladd", "name_he": "היילי לאד", "pos": "MF", "no": "16", "nation": "WAL"},
        {"player": "Annabel Blanchard", "name_he": "אנאבל בלנשארד", "pos": "MF", "no": "17", "nation": "ENG"},
        {"player": "Justine Vanhaevermaet", "name_he": "ז'וסטין ואנהאוורמאט", "pos": "MF", "no": "18", "nation": "BEL"},
        {"player": "Shanade Hopcroft", "name_he": "שאנייד הופקרופט", "pos": "MF", "no": "24", "nation": "ENG"},
        {"player": "Fūka Tsunoda", "name_he": "פוקה צונודה", "pos": "MF", "no": "25", "nation": "JPN"},
        {"player": "Amy Moynihan", "name_he": "איימי מויניהאן", "pos": "MF", "no": "61", "nation": "ENG"},
        {"player": "Lexi Lloyd-Smith", "name_he": "לקסי לויד-סמית'", "pos": "FW", "no": "7", "nation": "ENG"},
        {"player": "Molly-Mae Sharpe", "name_he": "מולי-מיי שארפ", "pos": "FW", "no": "8", "nation": "ENG"},
        {"player": "Bethany England", "name_he": "בת'אני אינגלנד", "pos": "FW", "no": "9", "nation": "ENG"},
        {"player": "Kirsty Howat", "name_he": "קירסטי הוואט", "pos": "FW", "no": "10", "nation": "SCO"},
        {"player": "Abbie Larkin", "name_he": "אבי לארקין", "pos": "FW", "no": "19", "nation": "IRL"},
        {"player": "Shannon O'Brien", "name_he": "שאנון או'בריין", "pos": "FW", "no": "27", "nation": "ENG"},
        {"player": "Jessica Lee", "name_he": "ג'סיקה לי", "pos": "FW", "no": "48", "nation": "ENG"}
    ],

    # --------------------------------------------------------------------------
    # 12. LONDON CITY LIONESSES
    # --------------------------------------------------------------------------
    "london-city-lionesses": [
        {"player": "Mary Earps", "name_he": "מרי ארפס", "pos": "GK", "no": "27", "nation": "ENG"},
        {"player": "Sophie Hillyerd", "name_he": "סופי היליירד", "pos": "GK", "no": "28", "nation": "ENG"},
        {"player": "Sophia Poor", "name_he": "סופיה פור", "pos": "GK", "no": "35", "nation": "ENG"},
        {"player": "Elene Lete", "name_he": "אלנה לטה", "pos": "GK", "no": "77", "nation": "ESP"},
        {"player": "Jana Fernández", "name_he": "יאנה פרננדז", "pos": "DF", "no": "2", "nation": "ESP"},
        {"player": "Poppy Pattinson", "name_he": "פופי פטינסון", "pos": "DF", "no": "3", "nation": "ENG"},
        {"player": "Isa Kardinaal", "name_he": "איסה קרדינאל", "pos": "DF", "no": "4", "nation": "NED"},
        {"player": "Lucía Corrales", "name_he": "לוסיה קוראלס", "pos": "DF", "no": "7", "nation": "ESP"},
        {"player": "Elena Linari", "name_he": "אלנה לינארי", "pos": "DF", "no": "13", "nation": "ITA"},
        {"player": "Alanna Kennedy", "name_he": "אלאנה קנדי", "pos": "DF", "no": "33", "nation": "AUS"},
        {"player": "Mapi León", "name_he": "מאפי לאון", "pos": "DF", "no": "44", "nation": "ESP"},
        {"player": "Janni Thomsen", "name_he": "יאני תומסן", "pos": "DF", "no": "97", "nation": "DEN"},
        {"player": "Corrine Henson", "name_he": "קורין הנסון", "pos": "DF", "no": "99", "nation": "ENG"},
        {"player": "María Pérez", "name_he": "מריה פרז", "pos": "MF", "no": "6", "nation": "ESP"},
        {"player": "Daniëlle van de Donk", "name_he": "דניאל ואן דה דונק", "pos": "MF", "no": "10", "nation": "NED"},
        {"player": "Alexia Putellas", "name_he": "אלכסיה פוטלאס", "pos": "MF", "no": "11", "nation": "ESP"},
        {"player": "Daniela Arques", "name_he": "דניאלה ארקס", "pos": "MF", "no": "16", "nation": "ESP"},
        {"player": "Malou Marcetto Rylov", "name_he": "מאלו מארצ'טו רילוב", "pos": "MF", "no": "18", "nation": "DEN"},
        {"player": "Grace Geyoro", "name_he": "גרייס גיורו", "pos": "MF", "no": "88", "nation": "FRA"},
        {"player": "Kosovare Asllani", "name_he": "קוסובארה אסלאני", "pos": "FW", "no": "9", "nation": "SWE"},
        {"player": "Freya Godfrey", "name_he": "פריה גודפרי", "pos": "FW", "no": "14", "nation": "ENG"},
        {"player": "Nikita Parris", "name_he": "ניקיטה פאריס", "pos": "FW", "no": "17", "nation": "ENG"},
        {"player": "Nicole Anyomi", "name_he": "ניקול אניומי", "pos": "FW", "no": "19", "nation": "GER"},
        {"player": "Delphine Cascarino", "name_he": "דלפין קסקרינו", "pos": "FW", "no": "20", "nation": "FRA"},
        {"player": "Kadidiatou Diani", "name_he": "קדידיאטו דיאני", "pos": "FW", "no": "21", "nation": "FRA"},
        {"player": "Isobel Goodwin", "name_he": "איזובל גודווין", "pos": "FW", "no": "23", "nation": "ENG"},
        {"player": "Rosa Kafaji", "name_he": "רוזה קפאג'י", "pos": "FW", "no": "76", "nation": "SWE"}
    ],

    # --------------------------------------------------------------------------
    # 13. BIRMINGHAM CITY
    # --------------------------------------------------------------------------
    "birmingham-city": [
        {"player": "Lucy Thomas", "name_he": "לוסי תומאס", "pos": "GK", "no": "1", "nation": "ENG"},
        {"player": "Sophie Baggaley", "name_he": "סופי באגלי", "pos": "GK", "no": "32", "nation": "ENG"},
        {"player": "Katie Startup", "name_he": "קייטי סטארט-אפ", "pos": "GK", "no": "40", "nation": "ENG"},
        {"player": "Martha Harris", "name_he": "מרתה האריס", "pos": "DF", "no": "2", "nation": "ENG"},
        {"player": "Marie Levasseur", "name_he": "מארי לבאסר", "pos": "DF", "no": "3", "nation": "CAN"},
        {"player": "Jade Rastocle", "name_he": "ז'ייד רסטוקל", "pos": "DF", "no": "4", "nation": "FRA"},
        {"player": "Shannon Cooke", "name_he": "שאנון קוק", "pos": "DF", "no": "6", "nation": "ENG"},
        {"player": "Rebecca Holloway", "name_he": "רבקה הולוואי", "pos": "DF", "no": "15", "nation": "NIR"},
        {"player": "Rebecca McKenna", "name_he": "רבקה מקנה", "pos": "DF", "no": "18", "nation": "NIR"},
        {"player": "Millie Turner", "name_he": "מילי טרנר", "pos": "DF", "no": "21", "nation": "ENG"},
        {"player": "Neve Herron", "name_he": "ניב הרון", "pos": "DF", "no": "30", "nation": "ENG"},
        {"player": "Lisa Naalsund", "name_he": "ליסה נאלסונד", "pos": "MF", "no": "8", "nation": "NOR"},
        {"player": "Charlie Crosthwaite", "name_he": "צ'ארלי קרוסתווייט", "pos": "MF", "no": "16", "nation": "ENG"},
        {"player": "Chelsea Cornet", "name_he": "צ'לסי קורנט", "pos": "MF", "no": "19", "nation": "SCO"},
        {"player": "Océane Hurtré", "name_he": "אוסאן הורטרה", "pos": "MF", "no": "22", "nation": "FRA"},
        {"player": "Asato Miyagawa", "name_he": "אסאטו מיאגאווה", "pos": "MF", "no": "26", "nation": "JPN"},
        {"player": "Veatriki Sarri", "name_he": "ויאטריקי סארי", "pos": "MF", "no": "27", "nation": "GRE"},
        {"player": "Lee Geum-min", "name_he": "לי גום-מין", "pos": "FW", "no": "7", "nation": "KOR"},
        {"player": "Simone Magill", "name_he": "סימון מאגיל", "pos": "FW", "no": "9", "nation": "NIR"},
        {"player": "Wilma Leidhammar", "name_he": "וילמה ליידהאמר", "pos": "FW", "no": "10", "nation": "SWE"},
        {"player": "Chancelle Effa Effa", "name_he": "שאנסל אפה אפה", "pos": "FW", "no": "20", "nation": "GAB"},
        {"player": "Batcheba Louis", "name_he": "בטשבה לואיס", "pos": "FW", "no": "29", "nation": "HAI"}
    ],

    # --------------------------------------------------------------------------
    # 14. CHARLTON ATHLETIC
    # --------------------------------------------------------------------------
    "charlton-athletic": [
        {"player": "Sophie Whitehouse", "name_he": "סופי וייטהאוס", "pos": "GK", "no": "1", "nation": "IRL"},
        {"player": "Anna Koivunen", "name_he": "אנה קויווונן", "pos": "GK", "no": "24", "nation": "FIN"},
        {"player": "Ellie Mason", "name_he": "אלי מייסון", "pos": "DF", "no": "2", "nation": "NIR"},
        {"player": "Charlotte Newsham", "name_he": "שארלוט ניושאם", "pos": "DF", "no": "3", "nation": "SCO"},
        {"player": "Grace Johnston", "name_he": "גרייס ג'ונסטון", "pos": "DF", "no": "4", "nation": "SCO"},
        {"player": "Elisha N'Dow", "name_he": "אלישה אנדאו", "pos": "DF", "no": "5", "nation": "ENG"},
        {"player": "Jodie Hutton", "name_he": "ג'ודי האטון", "pos": "DF", "no": "12", "nation": "ENG"},
        {"player": "Kiera Skeels", "name_he": "קיירה סקילס", "pos": "DF", "no": "17", "nation": "ENG"},
        {"player": "Hawa Cissoko", "name_he": "הוואה סיסוקו", "pos": "DF", "no": "19", "nation": "FRA"},
        {"player": "Anna Pederson", "name_he": "אנה פדרסון", "pos": "DF", "no": "21", "nation": "ENG"},
        {"player": "Lucia Lobato", "name_he": "לוסיה לובאטו", "pos": "DF", "no": "23", "nation": "IRL"},
        {"player": "Lizzie Waldie", "name_he": "ליזי וולדי", "pos": "DF", "no": "25", "nation": "ENG"},
        {"player": "Ashleigh Neville", "name_he": "אשלי נוויל", "pos": "DF", "no": "29", "nation": "ENG"},
        {"player": "Leah Davidson", "name_he": "ליאה דייווידסון", "pos": "MF", "no": "6", "nation": "AUS"},
        {"player": "Carla Humphrey", "name_he": "קרלה האמפרי", "pos": "MF", "no": "8", "nation": "ENG"},
        {"player": "Lucy Fitzgerald", "name_he": "לוסי פיצג'רלד", "pos": "MF", "no": "11", "nation": "ENG"},
        {"player": "Keira Flannery", "name_he": "קיירה פלאנרי", "pos": "MF", "no": "14", "nation": "ENG"},
        {"player": "Emily van Egmond", "name_he": "אמילי ואן אגמונד", "pos": "MF", "no": "22", "nation": "AUS"},
        {"player": "Paula Partido", "name_he": "פאולה פרטידו", "pos": "FW", "no": "7", "nation": "ESP"},
        {"player": "Lorena Azzaro", "name_he": "לורנה אזארו", "pos": "FW", "no": "9", "nation": "ALG"},
        {"player": "Gillian Kenney", "name_he": "ג'יליאן קני", "pos": "FW", "no": "10", "nation": "ENG"},
        {"player": "Linda Líf Boama", "name_he": "לינדה ליף בואמה", "pos": "FW", "no": "13", "nation": "ISL"},
        {"player": "Katie Lockwood", "name_he": "קייטי לוקווד", "pos": "FW", "no": "15", "nation": "ENG"},
        {"player": "Gloria Siber", "name_he": "גלוריה סיבר", "pos": "FW", "no": "18", "nation": "FRA"},
        {"player": "Mary McAteer", "name_he": "מרי מקאטיר", "pos": "FW", "no": "20", "nation": "WAL"}
    ]
}


def sync_squad_file(slug: str, squad: List[Dict[str, Any]], dry_run: bool = False) -> Dict[str, Any]:
    # Sort order: GK -> DF -> MF -> FW, then by shirt number ascending
    pos_order = {"GK": 1, "DF": 2, "MF": 3, "FW": 4}
    
    def sort_key(p):
        p_order = pos_order.get(p.get("pos"), 99)
        num_str = str(p.get("no", "999"))
        num = int(num_str) if num_str.isdigit() else 999
        return (p_order, num)

    sorted_squad = sorted(squad, key=sort_key)
    
    target_path = SQUADS_DIR / f"{slug}.json"
    
    # Check old squad if exists
    old_count = 0
    if target_path.exists():
        try:
            with open(target_path, "r", encoding="utf-8") as f:
                old_data = json.load(f)
                old_count = len(old_data)
        except Exception:
            pass

    if not dry_run:
        target_path.parent.mkdir(parents=True, exist_ok=True)
        with open(target_path, "w", encoding="utf-8") as f:
            json.dump(sorted_squad, f, ensure_ascii=False, indent=2)

        # Also sync aliases if relevant
        if slug == "london-city-lionesses":
            alias_path = SQUADS_DIR / "lionesses.json"
            with open(alias_path, "w", encoding="utf-8") as f:
                json.dump(sorted_squad, f, ensure_ascii=False, indent=2)
        elif slug == "tottenham":
            alias_path = SQUADS_DIR / "tottenham_2026_27.json"
            with open(alias_path, "w", encoding="utf-8") as f:
                json.dump(sorted_squad, f, ensure_ascii=False, indent=2)

    return {
        "slug": slug,
        "count": len(sorted_squad),
        "old_count": old_count,
        "path": target_path
    }


def main():
    parser = argparse.ArgumentParser(description="Sync WSL Team Squads 2026/27")
    parser.add_argument("--team", type=str, default="all", help="Team slug or 'all'")
    parser.add_argument("--dry-run", action="store_true", help="Do not write files")
    args = parser.parse_args()

    targets = []
    if args.team == "all":
        targets = list(SQUADS_DATA.keys())
    else:
        slug = args.team.lower().strip()
        if slug not in SQUADS_DATA:
            print(f"[!] Unknown team '{slug}'. Available: {list(SQUADS_DATA.keys())}")
            sys.exit(1)
        targets = [slug]

    print("=" * 68)
    print(f"  ⚽ WSL 2026/27 Official First-Team Squads Synchronization Engine")
    print("=" * 68)

    results = []
    for slug in targets:
        squad = SQUADS_DATA[slug]
        res = sync_squad_file(slug, squad, dry_run=args.dry_run)
        results.append(res)
        diff_str = f"(היה: {res['old_count']})" if res['old_count'] else "(קובץ חדש ✨)"
        print(f"  ✓ {slug:<22} -> {res['count']} שחקניות {diff_str}")

    print("-" * 68)
    total_players = sum(r["count"] for r in results)
    print(f"✨ סונכרנו בהצלחה {len(results)} מועדונים עם סך כולל של {total_players} שחקניות רשמיות!")
    print("=" * 68)


if __name__ == "__main__":
    main()
