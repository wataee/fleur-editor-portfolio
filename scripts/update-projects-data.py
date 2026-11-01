import json

projects_path = r'C:\Users\timur\Desktop\fleur-editor-portfolio\src\data\projects.json'

with open(projects_path, 'r', encoding='utf-8') as f:
    projects = json.load(f)

DATA = {
    'cZZgi5xn930': {
        'client_ru': 'YouTube-канал об ИИ',
        'client_en': 'AI Explainer Channel',
        'client_kz': 'AI туралы YouTube-арна',
        'title_ru': 'Разбор архитектуры нейросетей',
        'title_en': 'Neural Network Architecture Deep-Dive',
        'title_kz': 'Нейрожелілер архитектурасына шолу',
        'body_ru': 'Длинный выпуск: вычистил паузы спикера, анимировал схемы нейросетей, собрал динамичный интро-хук и свёл звук голоса без шума.',
        'body_en': 'Long-form essay: trimmed dead air, built motion graphics for network models, created an engaging hook, and cleaned dialogue.',
        'body_kz': 'Ұзақ шығарылым: кідірістерді тазалау, схемалар анимациясы, тартымды кіріспе және таза дыбыс.',
        'tags_ru': ['Сборка и темп', 'Моушн-графика', 'Цветокоррекция', 'Сведение звука'],
        'tags_en': ['Pacing & Cut', 'Motion Graphics', 'Color Grading', 'Sound Mastering'],
        'tags_kz': ['Монтаж және ырғақ', 'Моушн-графика', 'Түс түзету', 'Дыбысты өңдеу']
    },
    'JpYdNQUO9gA': {
        'client_ru': 'Канал о крипторынке',
        'client_en': 'Crypto Market Channel',
        'client_kz': 'Крипто-талдау арнасы',
        'title_ru': 'Обзор рынка и графиков токеномики',
        'title_en': 'Market & Tokenomics Breakdown',
        'title_kz': 'Нарық пен токеномикаға шолу',
        'body_ru': 'Динамичный монтаж с акцентами: визуализировал графики биржи, добавил всплывающие цифры и убрал провисания в речи.',
        'body_en': 'Market breakdown: animated charts, on-screen data callouts, and eliminated conversational pauses.',
        'body_kz': 'Қарқынды монтаж: биржа графиктерін визуалдау, сандар анимациясы және кідіріссіз сөйлеу ырғағы.',
        'tags_ru': ['Монтаж', 'Инфографика', 'Цветокоррекция', 'Звуковые акценты'],
        'tags_en': ['Editing', 'Infographics', 'Color', 'Sound FX'],
        'tags_kz': ['Монтаж', 'Инфографика', 'Түс', 'Дыбыстық екпіндер']
    },
    'W80pFjEQAbk': {
        'client_ru': 'Студийный подкаст',
        'client_en': 'Studio Podcast',
        'client_kz': 'Студиялық подкаст',
        'title_ru': 'Интервью с двумя спикерами',
        'title_en': 'Two-Speaker Studio Session',
        'title_kz': 'Екі қонақпен сұхбат',
        'body_ru': 'Мультикамерный подкаст: бесшовные переключения между спикерами, чистка оговорок, сведение микрофонов и выравнивание баланса.',
        'body_en': 'Multicam interview: natural angle cuts on speaking cue, breath cleanup, and balanced studio vocal mix.',
        'body_kz': 'Мультикамералық подкаст: сөйлеушілер арасындағы бірқалыпты ауысу, артық дыбыстарды тазалау және дыбыс теңгерімі.',
        'tags_ru': ['Мультикам', 'Чистка звука', 'Выравнивание громкости', 'Цвет'],
        'tags_en': ['Multicam', 'Audio Cleanup', 'Voice Leveling', 'Color'],
        'tags_kz': ['Мультикам', 'Дыбысты тазалау', 'Дыбыс деңгейі', 'Түс']
    },
    'B5Rn-nVXL8U': {
        'client_ru': 'Рилс для недвижимости',
        'client_en': 'Real Estate Reel',
        'client_kz': 'Жылжымайтын мүлік рилсі',
        'title_ru': 'Расчёт доходности апартаментов',
        'title_en': 'Rental Yield Breakdown',
        'title_kz': 'Пәтер табыстылығын есептеу',
        'body_ru': 'Короткий ролик для продаж: анимированные плашки с расчётом окупаемости, плавный трекинг текста к стенам и плотный звук.',
        'body_en': 'Sales vertical reel: animated ROI callouts, 3D room text tracking, and crisp sound design.',
        'body_kz': 'Қысқа сату рилсі: кірістілік плашкалары, қабырғаға мәтін трекингі және нақты дыбыс.',
        'tags_ru': ['Монтаж 9:16', 'Трекинг текста', 'Субтитры', 'Саунд-дизайн'],
        'tags_en': ['9:16 Edit', 'Text Tracking', 'Captions', 'Sound Design'],
        'tags_kz': ['9:16 монтаж', 'Мәтін трекингі', 'Субтитрлер', 'Саунд-дизайн']
    },
    '9pBFZDq8POA': {
        'client_ru': 'Игровой стрим',
        'client_en': 'Gaming Streamer',
        'client_kz': 'Ойын стримі',
        'title_ru': 'Нарезка лучших моментов',
        'title_en': 'Clutch Gameplay Highlight',
        'title_kz': 'Үздік ойын сәттері',
        'body_ru': 'Динамичный Short: ускорения и замедления под ритм выстрелов, плотный бас и зум-акценты на реакции игрока.',
        'body_en': 'Fast-paced Short: velocity speed ramps to impact, punchy bass hits, and punch-ins on facecam.',
        'body_kz': 'Қарқынды Short: әрекет ырғағына сәйкес үдету, салмақты бас және ойыншы реакциясына екпін.',
        'tags_ru': ['Спидрэмпы', 'Зум-акценты', 'Звуковые эффекты', 'Субтитры'],
        'tags_en': ['Speed Ramps', 'Punch-ins', 'Impact SFX', 'Subtitles'],
        'tags_kz': ['Спидрэмптер', 'Зум-екпіндер', 'Дыбыстық әсерлер', 'Субтитрлер']
    },
    'H2MjwWcbAJE': {
        'client_ru': 'Сервис проката авто',
        'client_en': 'Car Rental Service',
        'client_kz': 'Көлік жалдау сервисі',
        'title_ru': 'Динамичный обзор автопарка',
        'title_en': 'Fleet Promo Reel',
        'title_kz': 'Автопаркке динамикалық шолу',
        'body_ru': 'Коммерческий ролик: бесшовные переходы через маски кузова, ритмичный саунд-дизайн под мотор и контрастная цветокоррекция.',
        'body_en': 'Brand reel: match cuts across car panels, engine sound sync, and punchy commercial color grade.',
        'body_kz': 'Коммерциялық ролик: көлік шанағы арқылы бірқалыпты ауысу, қозғалтқыш дыбысына саунд-дизайн және контрастты түс.',
        'tags_ru': ['Монтаж под бит', 'Маски и переходы', 'Цветокоррекция', 'Звук мотора'],
        'tags_en': ['Beat Sync', 'Mask Transitions', 'Commercial Grade', 'Foley SFX'],
        'tags_kz': ['Ырғаққа монтаж', 'Маскалар мен ауысулар', 'Түс түзету', 'Дыбыс дизайны']
    },
    'cp-Fx5PuVco': {
        'client_ru': 'Лайфстайл-канал',
        'client_en': 'Lifestyle Channel',
        'client_kz': 'Лайфстайл-арна',
        'title_ru': 'Атмосферный ролик дня',
        'title_en': 'Atmospheric Lifestyle Reel',
        'title_kz': 'Күн атмосферасы туралы эстетикалық ролик',
        'body_ru': 'Мягкий визуальный ритм: плавная кинематографичная склейка кадров, выверенная палитра и атмосферный эмбиент.',
        'body_en': 'Aesthetic cut: measured pacing, coherent warm film tone, and ambient sound design.',
        'body_kz': 'Жайлы визуалды ырғақ: кадрлардың кинематографиялық үйлесімі, жылы реңктер және фондық дыбыс.',
        'tags_ru': ['Монтаж', 'Цвет под плёнку', 'Эмбиент-звук', 'Ритм'],
        'tags_en': ['Editing', 'Film Color Tone', 'Ambient Audio', 'Pacing'],
        'tags_kz': ['Монтаж', 'Пленкалық түс', 'Фондық дыбыс', 'Ырғақ']
    },
    'Cn7qbOIXKks': {
        'client_ru': 'Экспертный блог',
        'client_en': 'Creator Channel',
        'client_kz': 'Сарапшы блогы',
        'title_ru': 'Экспертный совет в Reels',
        'title_en': 'Expert Advice Reel',
        'title_kz': 'Reels-тегі сарапшылық кеңес',
        'body_ru': 'Удержание внимания: динамичные субтитры с выделением ключевых слов, перебивки по смыслу и чистый звук голоса.',
        'body_en': 'Talking head cut: kinetic word-by-word captions, relevant B-roll cutaways, and pristine vocal presence.',
        'body_kz': 'Көрермен назарын ұстау: сөздік субтитрлер, мағыналық B-roll кадрлар және таза дауыс.',
        'tags_ru': ['Субтитры', 'B-roll перебивки', 'Чистка пауз', 'Звук'],
        'tags_en': ['Captions', 'B-roll Cutaways', 'Pause Cleanup', 'Vocal Mix'],
        'tags_kz': ['Субтитрлер', 'B-roll кадрлар', 'Кідірісті тазалау', 'Дауыс']
    },
    '8YToswyXOLI': {
        'client_ru': 'Промо-тизер',
        'client_en': 'Promo Teaser',
        'client_kz': 'Промо-тизер',
        'title_ru': 'Динамичный тизер',
        'title_en': 'Fast-Paced Teaser',
        'title_kz': 'Қарқынды тизер',
        'body_ru': 'Тизер для соцсетей: ритмичные склейки под музыку, моушн-акценты и звуковые эффекты переходов.',
        'body_en': 'Short teaser: aggressive rhythm cuts to beat drops, punchy transitions, and custom impact sound.',
        'body_kz': 'Әлеуметтік желіге арналған тизер: музыка ырғағына агрессивті склейкалар, моушн-екпіндер және дыбыстық ауысулар.',
        'tags_ru': ['Монтаж под бит', 'Динамика', 'Звуковые эффекты', 'Графика'],
        'tags_en': ['Beat Sync', 'High Energy', 'Impact SFX', 'Motion'],
        'tags_kz': ['Ырғаққа монтаж', 'Динамика', 'Дыбыстық әсерлер', 'Графика']
    }
}

for p in projects:
    vid = p['youtube_id']
    if vid in DATA:
        p.update(DATA[vid])
    p['thumbnail'] = f'/posters/{vid}.webp'

with open(projects_path, 'w', encoding='utf-8') as f:
    json.dump(projects, f, ensure_ascii=False, indent=2)

print('Updated projects.json with honest descriptions, tags, and local posters')
