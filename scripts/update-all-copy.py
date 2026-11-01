import json

ru_path = r'C:\Users\timur\Desktop\fleur-editor-portfolio\src\data\ru.json'
en_path = r'C:\Users\timur\Desktop\fleur-editor-portfolio\src\data\en.json'
kz_path = r'C:\Users\timur\Desktop\fleur-editor-portfolio\src\data\kz.json'

with open(ru_path, 'r', encoding='utf-8') as f:
    ru = json.load(f)
with open(en_path, 'r', encoding='utf-8') as f:
    en = json.load(f)
with open(kz_path, 'r', encoding='utf-8') as f:
    kz = json.load(f)

# === RU UPDATES ===
ru['hero']['status'] = 'Открыт для проектов'
ru['hero']['aiBadge'] = 'Ручной монтаж'
ru['hero']['title'] = 'Монтаж видео для YouTube и соцсетей, который удерживает внимание и растит аудиторию'
ru['hero']['sub'] = 'Я — .fleur, видеомонтажёр. Монтирую длинные выпуски, студийные подкасты и динамичные Reels: вычищаю паузы, собираю моушн-графику, крашу видео и свожу чистый студийный звук. Первый драфт — через 48–72 часа.'
ru['hero']['cta'] = 'Смотреть работы'
ru['hero']['ctaTg'] = 'Написать в Telegram'
ru['hero']['colorCta'] = 'До и после цветокоррекции'
ru['hero']['industriesNote'] = 'Форматы: YouTube-эссе, разговорные подкасты, авто и недвижимость, экспертные Reels.'
ru['hero']['servicesTitle'] = 'Что я делаю'
ru['hero']['proofStats'] = [
    {'value': '01', 'title': 'Динамичный монтаж', 'desc': 'Сборка хука с первых 3 секунд, чистка пауз и удержание зрителя'},
    {'value': '02', 'title': 'Моушн-графика', 'desc': 'Визуализация тезисов, анимированные схемы, титры и плашки'},
    {'value': '03', 'title': 'Цветокоррекция', 'desc': 'Кинематографичный вид, естественные оттенки кожи и чистый контраст'},
    {'value': '04', 'title': 'Звуковой дизайн', 'desc': 'Чистый голос без шума, сведение музыки и звуковых акцентов'}
]

ru['process'] = {
    'eyebrow': 'Рабочий процесс',
    'title': '3 понятных этапа без бесконечных созвонов',
    'steps': [
        {
            'num': '01',
            'title': 'Бриф и передача файлов',
            'period': '1–2 день (48–72 часа)',
            'desc': 'Вы присылаете исходники через облако и референсы. Через 48–72 часа получаете первый черновой драфт с выстроенным темпом.'
        },
        {
            'num': '02',
            'title': 'Графика, цвет и звук',
            'period': '3–4 день',
            'desc': 'Добавляем моушн-титры, инфографику, выравниваем цвет в DaVinci и сводим многоканальный звук.'
        },
        {
            'num': '03',
            'title': 'Правки и финальный мастер',
            'period': '4–5 день',
            'desc': 'Вносим правки по таймкодам. Сдача готового чистого мастера в 4K за 3–5 рабочих дней.'
        }
    ]
}

ru['pricing'] = {
    'eyebrow': 'Стоимость',
    'title': 'Прозрачные тарифы и понятные сроки',
    'cta': 'Обсудить проект',
    'plans': [
        {
            'id': 'plan-reels',
            'name': 'Reels / Shorts',
            'price': 'от $[TODO]',
            'price_hint': 'Короткие вертикальные ролики',
            'badge': None,
            'published': False,
            'description': 'Динамичные вертикальные ролики 9:16 с субтитрами, зум-акцентами и плотным звуком.',
            'features': [
                'Готовый ролик за 24–48 часов',
                'Динамичные субтитры с акцентами',
                'Звуковые эффекты и моушн-переходы',
                '2 раунда правок включены'
            ]
        },
        {
            'id': 'plan-youtube',
            'name': 'Длинный выпуск',
            'price': 'от $200',
            'price_hint': 'YouTube-видео и подкасты от 10 мин',
            'badge': 'Основной формат',
            'published': True,
            'description': 'Полный цикл для YouTube-каналов и подкастов: сборка темпа, моушн-графика, цвет и сведение звука.',
            'features': [
                'Первый драфт: 48–72 часа',
                'Чистка пауз, оговорок и эха',
                'Моушн-графика и оформление титров',
                '2 раунда правок включены',
                'Финальная сдача: 3–5 рабочих дней'
            ]
        },
        {
            'id': 'plan-motion',
            'name': 'Моушн и графика',
            'price': 'Расчёт по брифу',
            'price_hint': 'Зависит от объёма графики',
            'badge': None,
            'published': True,
            'description': 'Инфографика, анимированные схемы, заставки, плашки и визуальное оформление шоу.',
            'features': [
                'Разработка стиля титров и плашек',
                'Анимация схем, скриншотов и карт',
                'Промежуточные превью каждого элемента',
                'Для расчёта: пришлите сценарий и референс'
            ]
        },
        {
            'id': 'plan-retainer',
            'name': 'Постоянный ретейнер',
            'price': 'Пакетная скидка',
            'price_hint': 'Фиксированная ставка в месяц',
            'badge': 'Выгодно',
            'published': True,
            'description': 'Системный монтаж роликов для вашего канала по стабильному еженедельному расписанию.',
            'features': [
                'Бронирование слотов в календаре',
                'Единый узнаваемый почерк выпусков',
                'Приоритетная сдача драфтов (48 часов)',
                'Для расчёта: ссылка на канал и частота выхода'
            ]
        }
    ]
}

ru['whyMe'] = {
    'eyebrow': 'Принципы',
    'title': 'Почему авторы работают со мной вдолгую',
    'items': [
        {
            'id': 'about',
            'title': 'Ручной авторский монтаж',
            'desc': 'Без генеративного ИИ и шаблонных нейро-эффектов. Каждая склейка, титр и звуковой переход делаются вручную с пониманием драматургии.'
        },
        {
            'id': 'async',
            'title': 'Асинхронная связь без лишних созвонов',
            'desc': 'Вам не нужно тратить часы на созвоны. Чёткие апдейты в Telegram, комментарии по таймкодам и отчёты экономят ваше время.'
        },
        {
            'id': 'longterm',
            'title': 'Погружение в стилистику канала',
            'desc': 'Изучаю подачу спикера и вкусы зрителей. Со второго ролика процесс ускоряется: я уже знаю ваши предпочтения.'
        },
        {
            'id': 'sound',
            'title': 'Внимание к звуку и деталям',
            'desc': 'Плотный саунд-дизайн, чистый голос без эха и естественная динамика пауз, чтобы видео смотрелось на одном дыхании.'
        }
    ]
}

ru['faq'] = {
    'eyebrow': 'FAQ',
    'title': 'Часто задаваемые вопросы',
    'items': [
        {
            'q': 'Сколько стоит монтаж одного видео?',
            'a': 'Базовый монтаж длинного YouTube-выпуска начинается от $200. Итоговая цена зависит от хронометража, объёма исходников и плотности графики. Точный расчёт даю в течение 1–2 часов после взгляда на исходники и бриф.'
        },
        {
            'q': 'Какие точные сроки сдачи проекта?',
            'a': 'Первый черновой драфт готов через 48–72 часа после получения исходников. Финальный выпуск со звуком, графикой и цветокоррекцией сдаётся за 3–5 рабочих дней.'
        },
        {
            'q': 'Как передавать исходники и материалы?',
            'a': 'Через любое удобное облако: Google Drive, Яндекс Диск, Dropbox или Telegram. Для больших архивов использую прямые протоколы без урезания скорости.'
        },
        {
            'q': 'Сколько раундов правок входит в стоимость?',
            'a': 'В каждый проект включены 2 полноценных раунда правок по таймкодам. Этого абсолютно достаточно, так как темп и структура согласуются на этапе первого драфта.'
        },
        {
            'q': 'Как устроена работа над правками?',
            'a': 'Вы смотрите драфт по закрытой ссылке и присылаете список правок по таймкодам (в Telegram или документом). Я вношу их в течение 24 часов.'
        },
        {
            'q': 'Работаете ли вы с международными клиентами?',
            'a': 'Да, работаю с клиентами по всему миру (США, Европа, СНГ). Принимаю оплату в удобном формате (USDT, криптовалюта, международные переводы).'
        }
    ]
}

ru['contact']['briefHelper'] = 'Что прислать для расчёта: ссылка на канал, пример/референс ролика, хронометраж исходников и желаемый дедлайн.'
ru['theDifference']['eyebrow'] = 'Цветокоррекция'
ru['theDifference']['title'] = 'Sony S-Log3 ➔ Кинематографичный Rec.709'
ru['theDifference']['description'] = 'Интерактивное сравнение кадров: слева — плоский сырой лог с камеры, справа — точная эмуляция плёнки с глубоким контрастом и естественным скинтоном.'


# === EN UPDATES ===
en['hero']['status'] = 'Available for Select Projects'
en['hero']['aiBadge'] = 'Craft-First Editing'
en['hero']['title'] = 'High-retention video editing for YouTube & brands that scales your audience'
en['hero']['sub'] = 'I am .fleur, video editor & colorist. Crafting narrative YouTube essays, studio podcasts, and kinetic Reels: seamless pacing, custom motion graphics, broadcast audio mastering, and color grading. First cut in 48–72 hours.'
en['hero']['cta'] = 'Explore Work'
en['hero']['ctaTg'] = 'Message on Telegram'
en['hero']['colorCta'] = 'Color grading: before & after'
en['hero']['industriesNote'] = 'Formats: YouTube essays, studio podcasts, automotive, and creator Reels.'
en['hero']['servicesTitle'] = 'What I Do'
en['hero']['proofStats'] = [
    {'value': '01', 'title': 'Dynamic Editing', 'desc': 'Hook construction in first 3 seconds, natural dead-air trimming, and audience retention'},
    {'value': '02', 'title': 'Motion Graphics', 'desc': 'Concept visualization, animated data charts, lower thirds, and kinetic type'},
    {'value': '03', 'title': 'Color Grading', 'desc': 'Cinematic film tone, multicam color matching, and natural skin tones'},
    {'value': '04', 'title': 'Sound Design', 'desc': 'Vocal clarity without room hiss, impact foley, and balanced musical score'}
]

en['process'] = {
    'eyebrow': 'Workflow',
    'title': '3 clear stages without endless calls',
    'steps': [
        {
            'num': '01',
            'title': 'Brief & Raw Footage Transfer',
            'period': 'Days 1–2 (48–72 hrs)',
            'desc': 'Share raw files via cloud and reference videos. Receive your first structured pacing cut in 48–72 hours.'
        },
        {
            'num': '02',
            'title': 'Motion Graphics & Color & Sound',
            'period': 'Days 3–4',
            'desc': 'We add kinetic typography, data charts, color grade in DaVinci Resolve, and master studio vocal audio.'
        },
        {
            'num': '03',
            'title': 'Revisions & Final 4K Master',
            'period': 'Days 4–5',
            'desc': 'Timecode-based revisions. Final 4K pristine master delivered in 3–5 business days.'
        }
    ]
}

en['pricing'] = {
    'eyebrow': 'Pricing',
    'title': 'Clear rates and dependable timelines',
    'cta': 'Start a Project',
    'plans': [
        {
            'id': 'plan-reels',
            'name': 'Reels / Shorts',
            'price': 'from $[TODO]',
            'price_hint': 'Short-form vertical video',
            'badge': None,
            'published': False,
            'description': 'High-velocity 9:16 cuts featuring word-by-word animated captions, zooms, and punchy sound design.',
            'features': [
                'First cut ready in 24–48 hours',
                'Kinetic captions & keypoint highlights',
                'Impact sound cues and match transitions',
                '2 rounds of revisions included'
            ]
        },
        {
            'id': 'plan-youtube',
            'name': 'Long-Form Release',
            'price': 'from $200',
            'price_hint': 'YouTube essays & podcasts from 10m',
            'badge': 'Flagship Format',
            'published': True,
            'description': 'Full-cycle editing for YouTube channels and studio podcasts: narrative rhythm, motion graphics, color, and audio mastering.',
            'features': [
                'First pacing cut: 48–72 hours',
                'Pause trimming, breath cleanup & audio leveling',
                'Custom motion graphics & lower thirds',
                '2 revision rounds included',
                'Final delivery: 3–5 business days'
            ]
        },
        {
            'id': 'plan-motion',
            'name': 'Motion & Graphics',
            'price': 'Custom Quote',
            'price_hint': 'Depends on graphics volume',
            'badge': None,
            'published': True,
            'description': 'Infographics, animated schematics, recurring show packaging, kinetic typography, and visual assets.',
            'features': [
                'Bespoke title and lower-third style design',
                'Schematic, document & chart animations',
                'Milestone previews for each graphic block',
                'To estimate: send brief and reference links'
            ]
        },
        {
            'id': 'plan-retainer',
            'name': 'Monthly Retainer',
            'price': 'Package Discount',
            'price_hint': 'Fixed monthly fee for steady output',
            'badge': 'Best Value',
            'published': True,
            'description': 'Systematic editing for your channel on an agreed weekly publishing calendar.',
            'features': [
                'Guaranteed calendar slots reserved',
                'Consistent, recognizable visual identity & pacing',
                'Priority draft turnaround (48 hours)',
                'To estimate: share channel link and release cadence'
            ]
        }
    ]
}

en['whyMe'] = {
    'eyebrow': 'Principles',
    'title': 'Why creators choose long-term collaboration',
    'items': [
        {
            'id': 'about',
            'title': 'Artisan Handcrafted Editing',
            'desc': 'Zero generative AI slop or generic templates. Every cut, title card, and audio hit is curated intentionally with narrative discipline.'
        },
        {
            'id': 'async',
            'title': 'Async Speed Without Endless Meetings',
            'desc': 'No hour-long discovery calls required. Clear Telegram updates, timestamped reviews, and structural deliverables protect your focus.'
        },
        {
            'id': 'longterm',
            'title': 'Channel Stylistic Immersion',
            'desc': 'I study your delivery and audience taste. From project two onward, turnarounds accelerate as preferred rhythms are already locked in.'
        },
        {
            'id': 'sound',
            'title': 'Obsessive Audio & Detail Discipline',
            'desc': 'Tactile foley, room hiss removal, and natural vocal cadence so viewers stay hooked from the first hook to the outro.'
        }
    ]
}

en['faq'] = {
    'eyebrow': 'FAQ',
    'title': 'Frequently Asked Questions',
    'items': [
        {
            'q': 'How much does editing cost per video?',
            'a': 'Full editing for a long-form YouTube release starts at $200. Final investment depends on raw footage volume, graphics density, and pacing. An exact quote is provided within 1–2 hours after reviewing raw material and your brief.'
        },
        {
            'q': 'What are your exact turnaround times?',
            'a': 'The first structured draft cut is delivered within 48–72 hours after receiving raw footage. The final release with motion graphics, color grading, and mastered audio is delivered in 3–5 business days.'
        },
        {
            'q': 'How do we transfer raw video files?',
            'a': 'Via Google Drive, Dropbox, OneDrive, or Telegram. For large camera cards, direct high-speed links ensure rapid transfer without compression.'
        },
        {
            'q': 'How many revision rounds are included?',
            'a': 'Every project includes 2 comprehensive timecode-based revision passes. This is consistently sufficient because core pacing is locked in the initial draft.'
        },
        {
            'q': 'How do we handle feedback and notes?',
            'a': 'You review the private preview link and send timecode notes in Telegram or a shared document. Notes are implemented within 24 hours.'
        },
        {
            'q': 'Do you work with international clients?',
            'a': 'Yes, I work with creators and brands worldwide (US, Europe, Central Asia). Payments are handled via USDT, cryptocurrency, or wire transfer.'
        }
    ]
}

en['contact']['briefHelper'] = 'What to send for a quick estimate: channel link, reference video, raw footage duration, and your target deadline.'
en['theDifference']['eyebrow'] = 'Color Grading'
en['theDifference']['title'] = 'Sony S-Log3 ➔ Cinematic Rec.709'
en['theDifference']['description'] = 'Interactive frame comparison: on the left is flat raw sensor data straight from camera, on the right is an authentic film-emulation grade with rich contrast and natural skin tones.'


# === KZ UPDATES ===
kz['hero']['status'] = 'Жобалар үшін ашық'
kz['hero']['aiBadge'] = 'Қолдан жасалған монтаж'
kz['hero']['title'] = 'Көрерменнің назарын ұстап, аудиторияны өсіретін YouTube пен әлеуметтік желілерге арналған бейнемонтаж'
kz['hero']['sub'] = 'Мен — .fleur, бейнемонтажермін. Ұзақ шығарылымдарды, подкасттар мен серпінді Reels-терді жинаймын: кідірістерді тазалау, моушн-графика, түс түзету және таза студиялық дыбыс. Алғашқы нұсқа — 48–72 сағат ішінде.'
kz['hero']['cta'] = 'Жұмыстарды көру'
kz['hero']['ctaTg'] = 'Telegram-да жазу'
kz['hero']['colorCta'] = 'Түс түзету: дейін және кейін'
kz['hero']['industriesNote'] = 'Форматтар: YouTube-эсселер, подкасттар, авто және жылжымайтын мүлік, авторлық Reels.'
kz['hero']['servicesTitle'] = 'Мен не істеймін'
kz['hero']['proofStats'] = [
    {'value': '01', 'title': 'Серпінді монтаж', 'desc': 'Алғашқы 3 секундта қызықтыру, кідірістерді тазалау және көрермен назарын сақтау'},
    {'value': '02', 'title': 'Моушн-графика', 'desc': 'Мағынаны визуалдау, анимациялық сызбалар, титрлер мен плашкалар'},
    {'value': '03', 'title': 'Түс түзету', 'desc': 'Кинематографиялық көрініс, камераларды сәйкестендіру және табиғи реңк'},
    {'value': '04', 'title': 'Дыбыс дизайны', 'desc': 'Артық шусыз таза дауыс, музыка үйлесімі және дыбыстық екпіндер'}
]

kz['process'] = {
    'eyebrow': 'Жұмыс барысы',
    'title': 'Шексіз қоңырауларсыз 3 анық кезең',
    'steps': [
        {
            'num': '01',
            'title': 'Бриф және файлдарды қабылдау',
            'period': '1–2 күн (48–72 сағат)',
            'desc': 'Шикі материалдар мен референстерді қабылдаймын. 48–72 сағат ішінде нақты ырғағы бар алғашқы нұсқа дайын болады.'
        },
        {
            'num': '02',
            'title': 'Графика, түс және дыбыс',
            'period': '3–4 күн',
            'desc': 'Моушн-титрлер қосу, DaVinci жүйесінде түс түзету және көпжолақты таза дыбыс жасау.'
        },
        {
            'num': '03',
            'title': 'Түзетулер және дайын бейне',
            'period': '4–5 күн',
            'desc': 'Таймкод бойынша түзетулер енгізу. Дайын таза 4K нұсқасын 3–5 жұмыс күні ішінде тапсыру.'
        }
    ]
}

kz['pricing'] = {
    'eyebrow': 'Бағалар',
    'title': 'Ашық тарифтер мен нақты мерзімдер',
    'cta': 'Жобаны талқылау',
    'plans': [
        {
            'id': 'plan-reels',
            'name': 'Reels / Shorts',
            'price': '$[TODO] бастап',
            'price_hint': 'Қысқа тік бейнелер',
            'badge': None,
            'published': False,
            'description': 'Субтитрлері, зум-екпіндері және сапалы дыбысы бар серпінді 9:16 форматындағы роликтер.',
            'features': [
                'Дайын бейне 24–48 сағат ішінде',
                'Екпінді анимациялық субтитрлер',
                'Дыбыстық әсерлер мен моушн-ауысулар',
                '2 түзету кезеңі қамтылған'
            ]
        },
        {
            'id': 'plan-youtube',
            'name': 'Ұзақ шығарылым',
            'price': '$200 бастап',
            'price_hint': '10 минуттан басталатын YouTube-роликтер',
            'badge': 'Негізгі формат',
            'published': True,
            'description': 'YouTube-арналар мен подкасттарға арналған толық цикл: монтаж, моушн-графика, түс түзету және дыбыс.',
            'features': [
                'Алғашқы нұсқа: 48–72 сағат',
                'Кідірістер мен артық шуды тазалау',
                'Моушн-графика және титрлер',
                '2 түзету кезеңі қамтылған',
                'Соңғы тапсыру: 3–5 жұмыс күні'
            ]
        },
        {
            'id': 'plan-motion',
            'name': 'Моушн және графика',
            'price': 'Бриф бойынша',
            'price_hint': 'Графика көлеміне байланысты',
            'badge': None,
            'published': True,
            'description': 'Инфографика, сызбалар анимациясы, кіріспелер және бағдарламаның визуалды стилі.',
            'features': [
                'Титрлер мен плашкалардың жеке стилі',
                'Сызбалар мен құжаттарды анимациялау',
                'Әр элементтің аралық нұсқаларын көрсету',
                'Есептеу үшін: сценарий мен референс жіберіңіз'
            ]
        },
        {
            'id': 'plan-retainer',
            'name': 'Тұрақты ретейнер',
            'price': 'Пакеттік жеңілдік',
            'price_hint': 'Айлық бекітілген төлем',
            'badge': 'Тиімді',
            'published': True,
            'description': 'Арнаңыз үшін тұрақты кесте бойынша бейнелерді жүйелі монтаждау.',
            'features': [
                'Күнтізбеден тұрақты уақытты брондау',
                'Шығарылымдардың бірыңғай танымал стилі',
                'Басымдықты тапсыру (48 сағат)',
                'Есептеу үшін: арнаға сілтеме мен шығу жиілігі'
            ]
        }
    ]
}

kz['whyMe'] = {
    'eyebrow': 'Ұстанымдар',
    'title': 'Авторлар неге менімен ұзақ жұмыс істейді',
    'items': [
        {
            'id': 'about',
            'title': 'Таза авторлық монтаж',
            'desc': 'Генеративті AI қоқысынсыз және дайын шаблондарсыз. Әрбір ауысу, титр мен дыбыс мағынаны түсініп қолмен жасалады.'
        },
        {
            'id': 'async',
            'title': 'Уақытты үнемдейтін байланыс',
            'desc': 'Сағаттап созылатын қоңыраулардың қажеті жоқ. Telegram-дағы нақты есептер мен таймкодтар уақытыңызды үнемдейді.'
        },
        {
            'id': 'longterm',
            'title': 'Арна стилін терең түсіну',
            'desc': 'Спикердің сөйлеу мәнері мен аудитория талғамын зерттеймін. Екінші роликте жұмыс жылдамдай түседі.'
        },
        {
            'id': 'sound',
            'title': 'Дыбыс пен бөлшектерге көңіл бөлу',
            'desc': 'Таза дауыс, тыңғылықты саунд-дизайн және табиғи ырғақ — бейнені бір демде көру үшін.'
        }
    ]
}

kz['faq'] = {
    'eyebrow': 'FAQ',
    'title': 'Жиі қойылатын сұрақтар',
    'items': [
        {
            'q': 'Бір бейнені монтаждау қанша тұрады?',
            'a': 'Ұзақ YouTube-шығарылымының негізгі монтажы $200 басталады. Қорытынды баға материал көлеміне, графика тығыздығына байланысты. Нақты соманы шикі түсірілім мен брифті көрген соң 1–2 сағат ішінде айтамын.'
        },
        {
            'q': 'Жобаны тапсырудың нақты мерзімі қандай?',
            'a': 'Алғашқы нобайлық нұсқа шикіжазбаны алған соң 48–72 сағат ішінде дайын болады. Графикасы, дыбысы және түсі реттелген соңғы бейне 3–5 жұмыс күнінде тапсырылады.'
        },
        {
            'q': 'Материалдарды қалай жіберуге болады?',
            'a': 'Кез келген ыңғайлы бұлттық қойма арқылы: Google Drive, Dropbox, Яндекс Диск немесе Telegram. Үлкен көлемдер үшін жылдамдықты шектемейтін тікелей байланыс қолданылады.'
        },
        {
            'q': 'Бағаға қанша түзету кезеңі кіреді?',
            'a': 'Әр жобаға таймкодтар бойынша 2 толық түзету раунды кіреді. Бұл толықтай жеткілікті, өйткені негізгі құрылым алғашқы нобайда келісіледі.'
        },
        {
            'q': 'Түзетулер қалай енгізіледі?',
            'a': 'Сіз жабық сілтеме арқылы нобайды қарап, таймкод бойынша ескертулер тізімін жібересіз (Telegram немесе құжатта). Мен оларды 24 сағат ішінде енгіземін.'
        },
        {
            'q': 'Шетелдік клиенттермен жұмыс істейсіз бе?',
            'a': 'Иә, әлем бойынша авторлармен және брендтермен жұмыс істеймін (АҚШ, Еуропа, ТМД). Төлем кез келген ыңғайлы тәсілмен қабылданады (USDT, криптовалюта, халықаралық аударымдар).'
        }
    ]
}

kz['contact']['briefHelper'] = 'Бағасын есептеу үшін: арнаға сілтеме, референс, шикі материал ұзақтығы және дедлайн.'
kz['theDifference']['eyebrow'] = 'Түс түзету'
kz['theDifference']['title'] = 'Sony S-Log3 ➔ Кинематографиялық Rec.709'
kz['theDifference']['description'] = 'Интерактивті салыстыру: сол жақта — шикі лог кадры, оң жақта — байсалды контраст және табиғи реңкі бар түс түзету.'

with open(ru_path, 'w', encoding='utf-8') as f:
    json.dump(ru, f, ensure_ascii=False, indent=2)
with open(en_path, 'w', encoding='utf-8') as f:
    json.dump(en, f, ensure_ascii=False, indent=2)
with open(kz_path, 'w', encoding='utf-8') as f:
    json.dump(kz, f, ensure_ascii=False, indent=2)

print('Updated ru.json, en.json, kz.json successfully!')
