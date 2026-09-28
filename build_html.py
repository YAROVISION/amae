import json
import os

classification_data = {
    "ACEDIA": ("1. Екзистенційні - Абстрактні", "Негативні", "Непереборна екзистенційна нудьга та апатія."),
    "DESPAIR": ("1. Екзистенційні - Абстрактні", "Негативні", "Повна втрата надії."),
    "LONELINESS": ("1. Екзистенційні - Абстрактні", "Негативні", "Глибоке відчуття самотності."),
    "MELANCHOLY": ("1. Екзистенційні - Абстрактні", "Негативні", "Світла або глибока туга, сум."),
    "TOSKA": ("1. Екзистенційні - Абстрактні", "Негативні", "Духовна туга без видимої причини (рос. тоска)."),
    "VIRAHA": ("1. Екзистенційні - Абстрактні", "Негативні", "Усвідомлення любові через розлуку (хінді)."),
    "AL": ("1. Екзистенційні - Абстрактні", "Негативні", "Польський Żal: сум через безповоротну втрату."),
    "VULNERABILITY": ("1. Екзистенційні - Абстрактні", "Негативні", "Відчуття власної вразливості."),
    "MONO NO AWARE": ("1. Екзистенційні - Абстрактні", "Змішані", "Японська емоція: сумна краса швидкоплинності речей."),
    "SAUDADE": ("1. Екзистенційні - Абстрактні", "Змішані", "Португальська: глибока ностальгійна туга за тим, чого немає."),
    "WONDER": ("1. Екзистенційні - Абстрактні", "Змішані", "Подив і трепет перед величчю світу."),
    "LOVE": ("1. Екзистенційні - Абстрактні", "Позитивні", "Глибока прихильність та любов."),
    "JOY": ("1. Екзистенційні - Абстрактні", "Позитивні", "Чиста радість."),
    "ECSTASY": ("1. Екзистенційні - Абстрактні", "Позитивні", "Екстаз, вихід за межі себе."),
    "EUPHORIA": ("1. Екзистенційні - Абстрактні", "Позитивні", "Стан надзвичайного піднесення."),
    "COMPASSION": ("1. Екзистенційні - Абстрактні", "Позитивні", "Співчуття і милосердя до інших."),
    
    "ANGER": ("2. Базові - Загальні", "Негативні", "Гнів."),
    "ANXIETY": ("2. Базові - Загальні", "Негативні", "Тривога."),
    "APATHY": ("2. Базові - Загальні", "Негативні", "Байдужість."),
    "BOREDOM": ("2. Базові - Загальні", "Негативні", "Нудьга."),
    "CONTEMPT": ("2. Базові - Загальні", "Негативні", "Презирство."),
    "DISAPPOINTMENT": ("2. Базові - Загальні", "Негативні", "Розчарування."),
    "DISGUST": ("2. Базові - Загальні", "Негативні", "Огида."),
    "DISMAY": ("2. Базові - Загальні", "Негативні", "Збентеження, переляк."),
    "DREAD": ("2. Базові - Загальні", "Негативні", "Страх перед майбутнім."),
    "ENVY": ("2. Базові - Загальні", "Негативні", "Заздрість."),
    "FEAR": ("2. Базові - Загальні", "Негативні", "Страх."),
    "FRUSTRATION": ("2. Базові - Загальні", "Негативні", "Фрустрація."),
    "GRIEF": ("2. Базові - Загальні", "Негативні", "Горе."),
    "GUILT": ("2. Базові - Загальні", "Негативні", "Провина."),
    "HATRED": ("2. Базові - Загальні", "Негативні", "Ненависть."),
    "IMPATIENCE": ("2. Базові - Загальні", "Негативні", "Нетерпіння."),
    "IRRITATION": ("2. Базові - Загальні", "Негативні", "Роздратування."),
    "JEALOUSY": ("2. Базові - Загальні", "Негативні", "Ревнощі."),
    "PANIC": ("2. Базові - Загальні", "Негативні", "Паніка."),
    "REGRET": ("2. Базові - Загальні", "Негативні", "Жаль за скоєним."),
    "REMORSE": ("2. Базові - Загальні", "Негативні", "Докори сумління."),
    "SADNESS": ("2. Базові - Загальні", "Негативні", "Смуток."),
    "SHAME": ("2. Базові - Загальні", "Негативні", "Сором."),
    "TERROR": ("2. Базові - Загальні", "Негативні", "Жах."),
    "WORRY": ("2. Базові - Загальні", "Негативні", "Занепокоєння."),
    "ANTICIPATION": ("2. Базові - Загальні", "Змішані", "Передчуття."),
    "CURIOSITY": ("2. Базові - Загальні", "Змішані", "Цікавість."),
    "EMPATHY": ("2. Базові - Загальні", "Змішані", "Емпатія."),
    "RELUCTANCE": ("2. Базові - Загальні", "Змішані", "Небажання."),
    "SHOCK": ("2. Базові - Загальні", "Змішані", "Шок."),
    "SURPRISE": ("2. Базові - Загальні", "Змішані", "Сюрприз."),
    "UNCERTAINTY": ("2. Базові - Загальні", "Змішані", "Невпевненіність."),
    "CALM": ("2. Базові - Загальні", "Позитивні", "Спокій."),
    "CAREFREE": ("2. Базові - Загальні", "Позитивні", "Безтурботність."),
    "CHEERFULNESS": ("2. Базові - Загальні", "Позитивні", "Життєрадісність."),
    "COMFORT": ("2. Базові - Загальні", "Позитивні", "Комфорт."),
    "CONFIDENCE": ("2. Базові - Загальні", "Позитивні", "Впевненість."),
    "CONTENTMENT": ("2. Базові - Загальні", "Позитивні", "Задоволеність."),
    "COURAGE": ("2. Базові - Загальні", "Позитивні", "Сміливість."),
    "DELIGHT": ("2. Базові - Загальні", "Позитивні", "Захоплення."),
    "DESIRE": ("2. Базові - Загальні", "Позитивні", "Бажання."),
    "EXCITEMENT": ("2. Базові - Загальні", "Позитивні", "Збудження."),
    "FEELING GOOD (About Yourself)": ("2. Базові - Загальні", "Позитивні", "Відчуття власної гідності."),
    "GLADSOMENESS": ("2. Базові - Загальні", "Позитивні", "Втіха."),
    "GLEE": ("2. Базові - Загальні", "Позитивні", "Зловтіха або бурхлива радість."),
    "GRATITUDE": ("2. Базові - Загальні", "Позитивні", "Вдячність."),
    "HAPPINESS": ("2. Базові - Загальні", "Позитивні", "Щастя."),
    "HOPEFULNESS": ("2. Базові - Загальні", "Позитивні", "Надія."),
    "PRIDE": ("2. Базові - Загальні", "Позитивні", "Гордість."),
    "RELIEF": ("2. Базові - Загальні", "Позитивні", "Полегшення."),
    "SATISFACTION": ("2. Базові - Загальні", "Позитивні", "Задоволення."),
    "TRIUMPH": ("2. Базові - Загальні", "Позитивні", "Тріумф."),
    
    "ABHIMAN": ("3. Контекстуальні - Соціальні", "Негативні", "Гнів і біль через недбалість коханих (хінді)."),
    "CHEESED (Off)": ("3. Контекстуальні - Соціальні", "Негативні", "Роздратування, коли все дістало."),
    "DISGRUNTLEMENT": ("3. Контекстуальні - Соціальні", "Негативні", "Невдоволення."),
    "EMBARRASSMENT": ("3. Контекстуальні - Соціальні", "Негативні", "Зніяковіння."),
    "EXASPERATION": ("3. Контекстуальні - Соціальні", "Негативні", "Роздратування."),
    "FRAUD Feeling Like a": ("3. Контекстуальні - Соціальні", "Негативні", "Синдром самозванця."),
    "HAN": ("3. Контекстуальні - Соціальні", "Негативні", "Колективне почуття горя і несправедливості (Корея)."),
    "HOMESICKNESS": ("3. Контекстуальні - Соціальні", "Негативні", "Туга за домом."),
    "HUFF In a": ("3. Контекстуальні - Соціальні", "Негативні", "Образа."),
    "HUMILIATION": ("3. Контекстуальні - Соціальні", "Негативні", "Приниження."),
    "INDIGNATION": ("3. Контекстуальні - Соціальні", "Негативні", "Обурення."),
    "INSULTED Feeling": ("3. Контекстуальні - Соціальні", "Негативні", "Відчуття образи."),
    "LITOST": ("3. Контекстуальні - Соціальні", "Негативні", "Жаль і сором за власне убозтво (Чехія)."),
    "MALU": ("3. Контекстуальні - Соціальні", "Негативні", "Раптове зніяковіння перед статусними людьми (Індонезія)."),
    "OIME": ("3. Контекстуальні - Соціальні", "Негативні", "Дискомфорт від боргу перед кимось (Японія)."),
    "OVERWHELMED Feeling": ("3. Контекстуальні - Соціальні", "Негативні", "Перевантаження."),
    "PARANOIA": ("3. Контекстуальні - Соціальні", "Негативні", "Параноя."),
    "REPROACHFULNESS": ("3. Контекстуальні - Соціальні", "Негативні", "Докір."),
    "RESENTMENT": ("3. Контекстуальні - Соціальні", "Негативні", "Обурення, образа."),
    "SELF-PITY": ("3. Контекстуальні - Соціальні", "Негативні", "Жалість до себе."),
    "SONG": ("3. Контекстуальні - Соціальні", "Негативні", "Справедливе обурення через порушення правил (Мікронезія)."),
    "SUSPICION": ("3. Контекстуальні - Соціальні", "Негативні", "Підозра."),
    "VENGEFULNESS": ("3. Контекстуальні - Соціальні", "Негативні", "Мстивість."),
    "VERGENZA AJENA": ("3. Контекстуальні - Соціальні", "Негативні", "Іспанський сором (за когось іншого)."),
    "AMAE": ("3. Контекстуальні - Соціальні", "Змішані", "Бажання бути залежним і любимим (Японія)."),
    "BAFFLEMENT": ("3. Контекстуальні - Соціальні", "Змішані", "Збентеження."),
    "BEFUDDLEMENT": ("3. Контекстуальні - Соціальні", "Змішані", "Спантеличеність."),
    "BEWILDERMENT": ("3. Контекстуальні - Соціальні", "Змішані", "Здивування."),
    "BROODINESS": ("3. Контекстуальні - Соціальні", "Змішані", "Бажання мати дітей / заглибленість."),
    "DPAYSEMENT": ("3. Контекстуальні - Соціальні", "Змішані", "Дезорієнтація в чужій країні (Франція)."),
    "FAGO": ("3. Контекстуальні - Соціальні", "Змішані", "Суміш любові, смутку та співчуття (Мікронезія)."),
    "GRENG JAI": ("3. Контекстуальні - Соціальні", "Змішані", "Небажання завдавати клопоту іншим (Таїланд)."),
    "HIRAETH": ("3. Контекстуальні - Соціальні", "Змішані", "Валлійська туга за домом, якого ніколи не було."),
    "INHABITIVENESS": ("3. Контекстуальні - Соціальні", "Змішані", "Прихильність до певного місця."),
    "LIGET": ("3. Контекстуальні - Соціальні", "Змішані", "Гнівна енергія змагання (Філіппіни)."),
    "MAN": ("3. Контекстуальні - Соціальні", "Змішані", "Гордість і співчуття."),
    "PERVERSITY": ("3. Контекстуальні - Соціальні", "Змішані", "Схильність робити навпаки."),
    "PHILOPROGENITIVENESS": ("3. Контекстуальні - Соціальні", "Змішані", "Любов до нащадків."),
    "PITY": ("3. Контекстуальні - Соціальні", "Змішані", "Жалість."),
    "RIVALRY": ("3. Контекстуальні - Соціальні", "Змішані", "Суперництво."),
    "SCHADENFREUDE": ("3. Контекстуальні - Соціальні", "Змішані", "Радість від чужого горя."),
    "SMUGNESS": ("3. Контекстуальні - Соціальні", "Змішані", "Самозадоволення."),
    "WANDERLUST": ("3. Контекстуальні - Соціальні", "Змішані", "Жага до подорожей."),
    "COMPERSION": ("3. Контекстуальні - Соціальні", "Позитивні", "Радість за радість іншого."),
    "GEZELLIGHEID": ("3. Контекстуальні - Соціальні", "Позитивні", "Затишок у колі близьких (Нідерланди)."),
    "HOMEFULNESS": ("3. Контекстуальні - Соціальні", "Позитивні", "Відчуття дому."),
    "HUMBLE Feeling": ("3. Контекстуальні - Соціальні", "Позитивні", "Смиренність."),
    "HWYL": ("3. Контекстуальні - Соціальні", "Позитивні", "Емоційне піднесення та натхнення (Уельс)."),
    "IJIRASHII": ("3. Контекстуальні - Соціальні", "Позитивні", "Розчулення перед тим, хто старається попри перешкоди (Японія)."),
    "MUDITA": ("3. Контекстуальні - Соціальні", "Позитивні", "Безкорислива радість успіхам інших (Буддизм)."),
    "NAKHES": ("3. Контекстуальні - Соціальні", "Позитивні", "Гордість за досягнення дітей (Їдиш)."),
    "PRONOIA": ("3. Контекстуальні - Соціальні", "Позитивні", "Віра, що світ змовився, щоб допомогти тобі."),
    "WARM GLOW": ("3. Контекстуальні - Соціальні", "Позитивні", "Тепле відчуття після доброї справи."),

    "AMBIGUPHOBIA": ("4. Високоспецифічні - Фізичні", "Негативні", "Страх неоднозначності."),
    "AWUMBUK": ("4. Високоспецифічні - Фізичні", "Негативні", "Порожнеча після від'їзду гостей (Папуа Нова Гвінея)."),
    "CLAUSTROPHOBIA": ("4. Високоспецифічні - Фізичні", "Негативні", "Клаустрофобія."),
    "COLLYWOBBLES The": ("4. Високоспецифічні - Фізичні", "Негативні", "Бурчання в животі через нерви."),
    "CYBERCHONDRIA": ("4. Високоспецифічні - Фізичні", "Негативні", "Пошук хвороб в інтернеті."),
    "DISAPPEAR The Desire to": ("4. Високоспецифічні - Фізичні", "Негативні", "Бажання зникнути."),
    "HEEBIE-JEEBIES The": ("4. Високоспецифічні - Фізичні", "Негативні", "Мурашки по шкірі від чогось моторошного."),
    "MATUTOLYPEA": ("4. Високоспецифічні - Фізичні", "Негативні", "Ранкова депресія."),
    "MIFFED A Bit": ("4. Високоспецифічні - Фізичні", "Негативні", "Злегка роздратований."),
    "NGINYIWARRARRINGU": ("4. Високоспецифічні - Фізичні", "Негативні", "Раптовий страх, що штовхає на втечу (Австралія)."),
    "PEUR DES ESPACES": ("4. Високоспецифічні - Фізичні", "Негативні", "Страх відкритих просторів."),
    "PI YE A Fit of Q": ("4. Високоспецифічні - Фізичні", "Негативні", "Раптовий приступ образи (Pique)."),
    "POSTAL Going": ("4. Високоспецифічні - Фізичні", "Негативні", "Раптовий і неконтрольований гнів на роботі."),
    "RINGXIETY": ("4. Високоспецифічні - Фізичні", "Негативні", "Ілюзія телефонного дзвінка."),
    "ROAD RAGE": ("4. Високоспецифічні - Фізичні", "Негативні", "Дорожній гнів."),
    "TECHNOSTRESS": ("4. Високоспецифічні - Фізичні", "Негативні", "Стрес від технологій."),
    "TORSCHLUSSPANIK": ("4. Високоспецифічні - Фізичні", "Негативні", "Паніка перед зачиненими дверима (втрачені можливості)."),
    "UMPTY": ("4. Високоспецифічні - Фізичні", "Негативні", "Стан, коли все йде не так."),
    "BRABANT": ("4. Високоспецифічні - Фізичні", "Змішані", "Схильність дражнити когось заради розваги."),
    "FORMAL FEELING A": ("4. Високоспецифічні - Фізичні", "Змішані", "Холодне оніміння після шоку."),
    "Hoard The Urge to": ("4. Високоспецифічні - Фізичні", "Змішані", "Бажання накопичувати речі."),
    "HUNGER": ("4. Високоспецифічні - Фізичні", "Змішані", "Голод (у тому числі емоційний)."),
    "IKTSUARPOK": ("4. Високоспецифічні - Фізичні", "Змішані", "Нетерпляче очікування гостя (Інуїти)."),
    "ILINX": ("4. Високоспецифічні - Фізичні", "Змішані", "Радість від руйнування або запаморочення."),
    "KAUKOKAIPUU": ("4. Високоспецифічні - Фізичні", "Змішані", "Туга за місцем, де ніколи не був (Фінляндія)."),
    "LAPPEL DU VIDE": ("4. Високоспецифічні - Фізичні", "Змішані", "Потяг до безодні."),
    "MEHAMEHA": ("4. Високоспецифічні - Фізичні", "Змішані", "Страх перед надприродним (Гаваї)."),
    "MORBID CURIOSITY": ("4. Високоспецифічні - Фізичні", "Змішані", "Хвороблива цікавість."),
    "NOSTALGIA": ("4. Високоспецифічні - Фізичні", "Змішані", "Ностальгія."),
    "RUINENLUST": ("4. Високоспецифічні - Фізичні", "Змішані", "Тяга до руїн."),
    "BASOREXIA": ("4. Високоспецифічні - Фізичні", "Позитивні", "Раптове бажання когось поцілувати."),
    "DOLCE FAR NIENTE": ("4. Високоспецифічні - Фізичні", "Позитивні", "Солодке байдикування (Італія).")
}

def generate_html():
    html_template = """<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Human Emotions Database</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=DM+Mono:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet">
    <style>
        :root {
            --paper: #f0eddf;
            --ink: #292b23;
            --muted: #636456;
            --line: #c3c2af;
            --orange: #bc4129;
            --green: #42623e;
            --dark-blue: #486789;
            --hover-field: #dedcc9;
            --receipt-bg: #e6e2cf;
        }
        
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            background-color: var(--paper);
            color: var(--ink);
            font-family: "DM Mono", monospace;
            font-size: 13px;
            line-height: 1.5;
            padding: 0 5vw;
        }

        .container {
            max-width: 1440px;
            margin: 0 auto;
            border-left: 2px solid var(--ink);
            border-right: 2px solid var(--ink);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }

        .masthead {
            border-bottom: 5px solid var(--ink);
            border-top: 1px solid var(--ink);
            padding: 8px 16px;
            display: flex;
            justify-content: space-between;
            font-size: 10px;
            font-weight: 500;
            letter-spacing: 0.09em;
            text-transform: uppercase;
            margin-top: 20px;
        }

        .hero {
            padding: 40px 16px;
            border-bottom: 2px solid var(--ink);
            text-align: center;
        }

        h1 {
            font-family: "Barlow Condensed", sans-serif;
            font-weight: 800;
            font-size: clamp(64px, 8.5vw, 150px);
            line-height: 0.81;
            letter-spacing: -0.045em;
            text-transform: uppercase;
            margin-bottom: 20px;
        }
        
        .hero-meta {
            font-size: 11px;
            color: var(--muted);
            text-transform: uppercase;
            letter-spacing: 0.06em;
        }

        .grid-container {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            flex-grow: 1;
        }

        .column {
            border-right: 1px solid var(--line);
            display: flex;
            flex-direction: column;
        }
        
        .column:last-child {
            border-right: none;
        }

        .column-header {
            font-family: "Barlow Condensed", sans-serif;
            font-weight: 700;
            font-size: 27px;
            line-height: 1;
            text-transform: uppercase;
            padding: 16px;
            border-bottom: 2px solid var(--ink);
            background-color: var(--receipt-bg);
            text-align: center;
        }

        .valence-section {
            border-bottom: 1px solid var(--line);
        }

        .valence-header {
            font-family: "Barlow Condensed", sans-serif;
            font-weight: 600;
            font-size: 20px;
            text-transform: uppercase;
            padding: 12px 16px;
            border-bottom: 1px solid var(--line);
            background-color: var(--paper);
            color: var(--muted);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .valence-header.negative { color: var(--orange); border-bottom: 2px dashed var(--ink); }
        .valence-header.positive { color: var(--green); border-bottom: 2px dashed var(--ink); }
        .valence-header.mixed { color: var(--dark-blue); border-bottom: 2px dashed var(--ink); }

        .quest {
            padding: 16px;
            border-bottom: 1px solid var(--line);
            transition: background-color 0.2s ease;
            cursor: pointer;
            position: relative;
        }

        .quest:last-child {
            border-bottom: none;
        }

        .quest:hover {
            background-color: var(--hover-field);
        }

        .quest-title {
            font-family: "Barlow Condensed", sans-serif;
            font-weight: 700;
            font-size: 25px;
            line-height: 1;
            margin-bottom: 8px;
            text-transform: uppercase;
        }

        .quest-desc {
            font-size: 11px;
            color: var(--muted);
        }
        
        .quest-meta {
            font-size: 9px;
            font-weight: 500;
            letter-spacing: 0.1em;
            color: var(--orange);
            margin-bottom: 4px;
        }

        .stamp {
            display: inline-block;
            border: 2px solid var(--orange);
            color: var(--orange);
            font-family: "Barlow Condensed", sans-serif;
            font-weight: 700;
            font-size: 14px;
            text-transform: uppercase;
            padding: 2px 6px;
            transform: rotate(-5deg);
            margin-top: 10px;
        }
        
        .receipt-footer {
            background-color: var(--receipt-bg);
            border-top: 2px dashed var(--ink);
            padding: 24px;
            text-align: center;
            font-size: 11px;
            color: var(--muted);
        }

        @media (max-width: 950px) {
            .grid-container {
                grid-template-columns: repeat(2, 1fr);
            }
            .column:nth-child(2) { border-right: none; }
            .column:nth-child(3) { border-top: 2px solid var(--ink); }
            .column:nth-child(4) { border-top: 2px solid var(--ink); }
        }

        @media (max-width: 650px) {
            .grid-container {
                grid-template-columns: 1fr;
            }
            .column {
                border-right: none;
                border-bottom: 2px solid var(--ink);
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="masthead">
            <span>Encyclopedia of Emotions</span>
            <span>Ref: segments/</span>
            <span>Iss. 1 / Vol. 2026</span>
        </div>
        
        <div class="hero">
            <h1>HUMAN EMOTIONS DATABASE</h1>
            <div class="hero-meta">Total Records: 154 | Classification Method: Karpathy LLM Wiki | Display: Retro-Brutalism</div>
        </div>

        <div class="grid-container">
"""

    levels = [
        "1. Екзистенційні - Абстрактні",
        "2. Базові - Загальні",
        "3. Контекстуальні - Соціальні",
        "4. Високоспецифічні - Фізичні"
    ]
    
    valences = [
        ("Позитивні", "positive", "POS"),
        ("Змішані", "mixed", "MIX"),
        ("Негативні", "negative", "NEG")
    ]

    for level in levels:
        html_template += f'''
            <div class="column">
                <div class="column-header">{level.split(". ")[1]}</div>
'''
        for val_name, val_class, val_code in valences:
            emotions_in_section = [(k, v) for k, v in classification_data.items() if v[0] == level and v[1] == val_name]
            if emotions_in_section:
                html_template += f'''
                <div class="valence-section">
                    <div class="valence-header {val_class}">
                        <span>{val_name}</span>
                        <span>[{val_code}]</span>
                    </div>
'''
                for emo, desc in sorted(emotions_in_section):
                    html_template += f'''
                    <div class="quest" onclick="window.location.href='segments/{emo}.md'">
                        <div class="quest-meta">ID: {emo[:3].upper()}-{len(emo):02d}</div>
                        <div class="quest-title">{emo}</div>
                        <div class="quest-desc">{desc[2]}</div>
                    </div>
'''
                html_template += '''
                </div>
'''
        html_template += '''
            </div>
'''

    html_template += """
        </div>
        
        <div class="receipt-footer">
            <div style="font-size: 16px; margin-bottom: 10px; font-weight: bold; color: var(--ink);">END OF REPORT</div>
            <div>Generated by Antigravity IDE • 154 Items Processed</div>
            <div class="stamp">CLASSIFIED</div>
        </div>
    </div>
</body>
</html>
"""

    with open("/Users/kostantinkrivula/Desktop/amae/index.html", "w", encoding="utf-8") as f:
        f.write(html_template)
    print("HTML generated.")

if __name__ == "__main__":
    generate_html()
