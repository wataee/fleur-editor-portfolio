# .fleur Portfolio — Лендинг-портфолио видеомонтажёра

Современный, сверхбыстрый и кинематографичный лендинг-портфолио видеомонтажёра с поддержкой трёх языков (**RU / EN / KZ**), тёмной и светлой темами в стиле Linear/Raycast, интерактивным модулем сравнения цветокоррекции До/После (S-Log3 vs Rec.709), фильтрацией проектов по нишам, lazy-модальным окном с YouTube-плеером, компактным блоком программного стека, каруселью отзывов реальных креаторов, аккордеоном FAQ, карточками цен и прямыми контактами.

Проект разработан на **Astro 5 + Tailwind CSS** без использования тяжёлых сторонних библиотек.

---

## 🚀 Быстрый старт

### Требования
- Node.js 18.14+ (протестировано на Node.js v24.20.0)
- npm 9+

### Установка и запуск

1. Перейдите в директорию проекта:
   ```bash
   cd C:\Users\timur\.gemini\antigravity\scratch\fare-editor-portfolio
   ```

2. Установите зависимости (если ещё не установлены):
   ```bash
   npm install
   ```

3. Запустите сервер разработки:
   ```bash
   npm run dev
   ```
   Сайт доступен по адресам:
   - Английская версия: `http://localhost:4321/`
   - Русская версия: `http://localhost:4321/ru/`
   - Казахская версия: `http://localhost:4321/kz/`

4. Сборка для продакшена:
   ```bash
   npm run build
   ```
   Результат сборки генерируется в папку `dist/`.

5. Предпросмотр продакшен-сборки:
   ```bash
   npm run preview
   ```

---

## 🎨 Темы оформления (Dark & Light)
- По умолчанию включена эстетичная тёмная тема в стиле obsidian/Linear (`#090B0E`, карточки `#12161F`, границы `rgba(255, 255, 255, 0.08)`, неоновый акцент `#3B82F6`).
- В шапке сайта предусмотрен переключатель тем (Sun/Moon), запоминающий выбор пользователя в `localStorage`.
- Предотвращение мигания (FOUC) обеспечивается ранним инлайн-скриптом в `<head>`.

---

## 📁 Структура проекта

```text
fare-editor-portfolio/
├── public/                    # Статические ассеты
│   ├── avatar.jpg             # Фото / логотип профиля (.fleur)
│   ├── logo.jpg               # Копия логотипа
│   ├── favicon.svg            # Favicon
│   ├── robots.txt             # Правила для поисковиков
│   └── sitemap.xml            # Карта сайта
├── src/
│   ├── components/            # Astro-компоненты
│   │   ├── BeforeAfter.astro  # Слайдер сравнения колоргрейдинга (S-Log3 vs Rec.709)
│   │   ├── Contact.astro      # Прямые карточки Telegram, Email, X
│   │   ├── Faq.astro          # FAQ аккордеон с плавной анимацией
│   │   ├── Footer.astro       # Подвал с логотипом .fleur и соцсетями
│   │   ├── Header.astro       # Шапка: аватарка .fleur, nav, темная тема, переключатель RU/EN/KZ
│   │   ├── Hero.astro         # Главный экран: бейджи, заголовок, анимированные цифры
│   │   ├── Portfolio.astro    # Фильтр по нишам, YouTube-постеры
│   │   ├── Pricing.astro      # Карточки цен с защитой от переполнения текста
│   │   ├── Process.astro      # 3 этапа работы
│   │   ├── Reviews.astro      # Отзывы реальных креаторов с плавной прокруткой
│   │   ├── StickyMobileCta.astro # Липкая мобильная кнопка Telegram
│   │   ├── Tools.astro        # Компактный стек программ (Pr, Ae, DaVinci) в виде ленты
│   │   ├── VideoModal.astro   # Ленивый плеер YouTube по клику
│   │   └── WhyMe.astro        # 4 преимущества сотрудничества
│   ├── data/                  # ВСЕ текстовые и структурные данные (100% без хардкода)
│   │   ├── contacts.json      # Контакты @ffluere, fluere.work@gmail.com, @fluer_mp4
│   │   ├── ru.json            # Русская локализация
│   │   ├── en.json            # Английская локализация
│   │   ├── kz.json            # Казахская локализация
│   │   ├── projects.json      # Работы в портфолио
│   │   └── reviews.json       # Реальные отзывы креаторов
│   ├── layouts/
│   │   └── Layout.astro       # Базовый HTML-шаблон (SEO, i18n, темная тема)
│   ├── pages/
│   │   ├── index.astro        # Английская версия (/)
│   │   ├── ru/index.astro     # Русская версия (/ru/)
│   │   └── kz/index.astro     # Казахская версия (/kz/)
│   └── styles/
│       └── global.css         # Стили, переменные тем, шрифты Onest & JetBrains Mono
├── astro.config.mjs           # Конфигурация Astro i18n
├── package.json
└── tailwind.config.mjs        # Конфигурация Tailwind CSS
```

---

## ✏️ Управление контентом

Все тексты, работы, отзывы и контакты вынесены в JSON-файлы в папке `src/data/`. Для изменения контента **не требуется редактировать компоненты или код вёрстки**.

### 1. Тексты страниц (`ru.json`, `en.json`, `kz.json`)
Каждый файл содержит все текстовые блоки интерфейса:
- `meta`: `title`, `description`, `ogTitle`, `ogDescription`
- `nav`: пункты меню шапки, текст кнопки «Обсудить проект»
- `hero`: бейджи «Открыт для проектов» и «Без генеративного ИИ», заголовок, подзаголовок, 4 цифры-доказательства (`proofStats`), строка ниш
- `theDifference`: заголовок и описание наглядного модуля цветокоррекции
- `portfolio`: заголовки секций и названия табов по нишам
- `tools`: заголовок ленты софта
- `pricing`: названия тарифов, стоимость и список преимуществ (текст автоматически адаптируется без выпадения за границы карточки)
- `reviews`: заголовок и подзаголовок отзывов
- `process`: 3 шага работы (День 0, День 1–6, День 7)
- `whyMe`: 4 карточки («Никакого нейрослопа», «Асинхронная коммуникация», «Работаю в долгосрок», «Автоматизирую рутину»)
- `faq`: 6 вопросов и ответов с якорным переходом
- `contact`: заголовки блока контактов
- `footer`: копирайт и ссылка «Наверх»
- `stickyMobile`: текст плавающей кнопки Telegram

---

### 2. Портфолио проектов (`src/data/projects.json`)
Каждая запись содержит:
```json
{
  "id": "1",
  "slug": "magnates-silk-road",
  "type": "video",                 // "video" | "motion"
  "niche": "finance",              // "finance" | "real_estate" | "gaming" | "personal_brand"
  "featured": true,
  "order": 1,
  "client_ru": "MagnatesMedia",
  "client_en": "MagnatesMedia",
  "client_kz": "MagnatesMedia",
  "format_ru": "Документальный YouTube",
  "format_en": "Documentary YouTube",
  "format_kz": "Деректі YouTube",
  "duration": "44:32",
  "title_ru": "Продающая графика для финансового расследования",
  "title_en": "High-retention visual storytelling for financial deep-dives",
  "title_kz": "Қаржылық зерттеуге арналған сатушы графика",
  "body_ru": "Описание проекта на русском...",
  "body_en": "Project description in English...",
  "body_kz": "Жоба сипаттамасы қазақ тілінде...",
  "youtube_id": "fsfoqdqyykI",     // Реальный YouTube ID для модального плеера
  "thumbnail": "https://img.youtube.com/vi/fsfoqdqyykI/maxresdefault.jpg"
}
```

---

### 3. Отзывы креаторов (`src/data/reviews.json`)
Карточки реальных зарубежных и русскоязычных каналов с официальными аватарками, числом подписчиков и метриками удержания:
```json
{
  "id": "1",
  "author": "Johnny Harris",
  "role_ru": "Документалист и автор визуальных эссе",
  "role_en": "Documentary Filmmaker & Visual Essayist",
  "role_kz": "Деректі фильм түсіруші және визуалды эссе авторы",
  "channel": "@johnnyharris",
  "subscribers": "8M subs",
  "avatar": "https://yt3.googleusercontent.com/...",
  "rating": 5,
  "metrics_ru": "+420% удержание до конца",
  "metrics_en": "+420% end-to-end retention",
  "metrics_kz": "+420% соңына дейін көру",
  "text_ru": "Текст отзыва...",
  "text_en": "Review text...",
  "text_kz": "Пікір мәтіні..."
}
```

---

### 4. Контактные ссылки (`src/data/contacts.json`)
Прямые ссылки на контакты автора:
```json
[
  {
    "id": "telegram",
    "name": "Telegram",
    "handle": "@ffluere",
    "url": "https://t.me/ffluere",
    "description_ru": "Быстрый ответ в течение 1–2 часов",
    "description_en": "Fast reply within 1–2 hours",
    "description_kz": "1–2 сағат ішінде жылдам жауап",
    "primary": true
  },
  {
    "id": "email",
    "name": "Email",
    "handle": "fluere.work@gmail.com",
    "url": "mailto:fluere.work@gmail.com?subject=Work%20inquiry%20/%20Связь%20по%20проекту",
    "description_ru": "Для подробных ТЗ и договоров",
    "description_en": "For detailed briefs and contracts",
    "description_kz": "Толық техникалық тапсырма мен келісімшарттар үшін",
    "primary": false
  },
  {
    "id": "x",
    "name": "X (Twitter)",
    "handle": "@fluer_mp4",
    "url": "https://x.com/fluer_mp4",
    "description_ru": "Прямые сообщения и новости",
    "description_en": "Direct messages and updates",
    "description_kz": "Тікелей хабарламалар мен жаңалықтар",
    "primary": false
  }
]
```

---

## 🌐 Как добавить новый язык

1. **Создайте файл данных:**
   Скопируйте `src/data/en.json` в `src/data/<язык>.json` (например, `de.json`) и переведите тексты.
2. **Обновите `astro.config.mjs`:**
   Добавьте код нового языка в массив `locales`:
   ```javascript
   locales: ['en', 'ru', 'kz', 'de']
   ```
3. **Создайте страницу входа:**
   Создайте `src/pages/de/index.astro` аналогично `src/pages/kz/index.astro`.
4. **Обновите переключатель:**
   В `src/components/Header.astro` добавьте кнопку нового языка.
