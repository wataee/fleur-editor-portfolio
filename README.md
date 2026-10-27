# FareEditor Portfolio — Лендинг видеомонтажёра

Современный, сверхбыстрый и адаптивный лендинг-портфолио видеомонтажёра с поддержкой двух языков (RU / EN), интерактивным слайдером «До/После» с синхронным воспроизведением видео, фильтрацией проектов по нишам, lazy-модальным окном с YouTube-плеером, аккордеоном FAQ, карточками цен и прямыми контактами без громоздких форм.

Проект разработан на **Astro 5 + Tailwind CSS** без использования тяжёлых UI-фреймворков.

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
   *(Рекомендуется открыть эту папку как активное рабочее пространство в вашей IDE)*

2. Установите зависимости (если ещё не установлены):
   ```bash
   npm install
   ```

3. Запустите сервер разработки:
   ```bash
   npm run dev
   ```
   Сайт будет доступен по адресам:
   - Английская версия: `http://localhost:4321/`
   - Русская версия: `http://localhost:4321/ru/`

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

## 📁 Структура проекта

```text
fare-editor-portfolio/
├── docs/                      # Дизайн-заметки и скриншоты оригинального сайта
│   ├── design-notes.md
│   └── screenshots/
├── public/                    # Статические ассеты (favicon, og-image, robots, sitemap)
│   ├── favicon.svg
│   ├── og-image.png
│   ├── robots.txt
│   └── sitemap.xml
├── src/
│   ├── components/            # Astro-компоненты секций
│   │   ├── BeforeAfter.astro  # Слайдер До/После с синхронным видео (PointerCapture + a11y)
│   │   ├── Contact.astro      # Прямые ссылки на контакты (без форм)
│   │   ├── Faq.astro          # FAQ аккордеон (ровно 1 открытый, smooth grid animation)
│   │   ├── Footer.astro       # Подвал сайта
│   │   ├── Header.astro       # Шапка, навигация, языковой переключатель, мобильное меню
│   │   ├── Hero.astro         # Главный экран: бейджи, заголовок, анимированные цифры
│   │   ├── Portfolio.astro    # Фильтр по нишам, сетка видео и моушн-графики
│   │   ├── Pricing.astro      # Блок цен и тарифов
│   │   ├── Process.astro      # 3 этапа работы
│   │   ├── Reviews.astro      # Карусель отзывов клиентов
│   │   ├── StickyMobileCta.astro # Липкая кнопка Telegram для мобильных
│   │   ├── Tools.astro        # Стек инструментов (Premiere, AE, DaVinci, Blender)
│   │   ├── VideoModal.astro   # Доступное модальное окно с ленивой подгрузкой YouTube
│   │   └── WhyMe.astro        # Преимущества и подход к работе
│   ├── data/                  # ВСЕ текстовые и структурные данные (100% без хардкода)
│   │   ├── contacts.json      # Ссылки на Telegram, Email, X
│   │   ├── en.json            # Английская локализация интерфейса
│   │   ├── projects.json      # Работы в портфолио
│   │   ├── reviews.json       # Отзывы клиентов
│   │   └── ru.json            # Русская локализация интерфейса
│   ├── layouts/
│   │   └── Layout.astro       # Базовый HTML-шаблон (SEO, OpenGraph, hreflang)
│   ├── pages/
│   │   ├── index.astro        # Английская главная страница (/)
│   │   └── ru/
│   │       └── index.astro    # Русская главная страница (/ru/)
│   └── styles/
│       └── global.css         # Стилизация, шрифты Onest & JetBrains Mono, токены
├── astro.config.mjs           # Конфигурация Astro и i18n
├── package.json
└── tailwind.config.mjs        # Конфигурация Tailwind CSS с точными дизайн-токенами
```

---

## ✏️ Управление контентом

Все тексты, работы, отзывы и контакты вынесены в JSON-файлы в папке `src/data/`. Для изменения контента **не требуется редактировать компоненты или код верстки**.

### 1. Тексты страниц (`src/data/ru.json` и `src/data/en.json`)
Содержат все текстовые блоки интерфейса:
- `meta`: заголовок `title`, описание `description`, `ogTitle`, `ogDescription`.
- `nav`: пункты меню шапки и мобильного меню, текст кнопки звонка/обсуждения.
- `hero`: бейдж статуса ("Открыт для проектов"), бейдж "Без генеративного ИИ", главный заголовок, подзаголовок, кнопка действия, строка ниш, строка моушна, а также **4 цифры-доказательства** (`stats`):
  ```json
  "stats": [
    { "value": "120M+", "number": 120, "suffix": "M+", "label": "Просмотров роликов" },
    { "value": "45+", "number": 45, "suffix": "+", "label": "Завершённых проектов" },
    { "value": "6+", "number": 6, "suffix": "+", "label": "Лет в видеомонтаже" },
    { "value": "100%", "number": 100, "suffix": "%", "label": "Клиентов довольны" }
  ]
  ```
- `difference`: заголовок, подзаголовок, подписи «До монтажа» и «После монтажа», ссылки на видео/постеры для слайдера.
- `portfolio`: заголовки секций длинных роликов и моушн-графики, названия фильтр-табов по нишам (`filters`).
- `tools`: заголовок и подзаголовок блока инструментов.
- `reviews`: заголовок и подзаголовок блока отзывов.
- `process`: заголовок, подзаголовок и 3 шага работы (`items`: `day`, `title`, `desc`).
- `whyMe`: 4 карточки преимуществ (`items`: `title`, `desc`). Первая карточка содержит `id: "about"` для якорной ссылки из FAQ.
- `pricing`: карточки цен с заголовком, ценой, периодом, фичами и CTA-кнопкой.
- `faq`: заголовок, подзаголовок и 6 вопросов с ответами. Вопрос про ИИ содержит якорную ссылку `anchorId: "about"` и `anchorText`.
- `contact`: заголовок, подзаголовок, призыв к действию и подписи под кнопками.
- `footer`: слоган, копирайт.

---

### 2. Портфолио проектов (`src/data/projects.json`)
Содержит список проектов. Каждая запись имеет следующую структуру:

```json
{
  "id": "project-slug",             // Уникальный строковый идентификатор
  "type": "video",                  // "video" (длинное видео) или "motion" (моушн-графика / 3D)
  "niche": "gaming",                // Ниша: "gaming" | "realestate" | "personal" | "finance"
  "title": {
    "ru": "Название на русском",
    "en": "Title in English"
  },
  "client": "Имя или канал клиента",
  "views": "2.4M",                  // Метрика просмотров для бейджа
  "duration": "14:20",              // Хронометраж ролика
  "year": "2024",
  "description": {
    "ru": "Краткое описание монтажа и задач ролика",
    "en": "Brief description of video editing and objectives"
  },
  "poster": "https://...",          // URL постера / обложки (WebP / JPG)
  "videoUrl": "https://www.youtube.com/watch?v=dQw4w9WgXcQ", // Ссылка на YouTube/Vimeo
  "youtubeId": "dQw4w9WgXcQ",       // ID ролика YouTube для ленивой вставки в модалку
  "aspectRatio": "16:9"             // Соотношение сторон
}
```

*При добавлении нового проекта просто добавьте объект в массив `projects.json`.*

---

### 3. Отзывы клиентов (`src/data/reviews.json`)
Содержит список отзывов с данными об авторе и статистике:

```json
{
  "id": "review-1",
  "author": "Алексей Смирнов",       // Имя клиента
  "role": {
    "ru": "YouTube-креатор",
    "en": "YouTube Creator"
  },
  "channel": "@tech_insider",       // Название канала / проекта
  "subscribers": "850K subs",       // Количество подписчиков
  "avatar": "https://...",          // URL аватарки автора
  "rating": 5,                      // Количество звёзд (1-5)
  "metrics": {
    "ru": "+340% удержание",
    "en": "+340% retention"
  },
  "text": {
    "ru": "Текст отзыва на русском языке...",
    "en": "Review text in English..."
  }
}
```

---

### 4. Контактные ссылки (`src/data/contacts.json`)
Ссылки на соцсети и мессенджеры:
```json
{
  "telegram": "https://t.me/fareeditor",
  "email": "work@fareeditor.com",
  "x": "https://x.com/fareeditor",
  "youtube": "https://youtube.com/@fareeditor"
}
```
*На сайте нет тяжёлых серверных форм — клик открывает диалог в Telegram или почтовый клиент.*

---

## 🌐 Как добавить новый язык

Благодаря встроенному роутингу Astro i18n добавить новый язык (например, испанский `es`) очень просто:

1. **Создайте файл данных:**
   Скопируйте `src/data/en.json` в `src/data/es.json` и переведите тексты.
2. **Обновите `astro.config.mjs`:**
   ```javascript
   i18n: {
     defaultLocale: 'en',
     locales: ['en', 'ru', 'es'],
     routing: {
       prefixDefaultLocale: false,
     },
   }
   ```
3. **Создайте страницу `src/pages/es/index.astro`:**
   Скопируйте `src/pages/ru/index.astro` и замените:
   - Импорт данных: `import esData from '../../data/es.json';`
   - Переменную `lang`: `const lang = 'es';`
   - Канонический URL: `canonicalUrl="https://fareeditor.com/es/"`
4. **Обновите ссылки в `src/components/Header.astro` и `src/layouts/Layout.astro`**, добавив новый язык в переключатель и мета-теги `hreflang`.

---

## ⚡ Оптимизации и качество (Lighthouse)

1. **Сверхбыстрая загрузка видео:**
   - Ролики в слайдере имеют `preload="none"`, `muted`, `playsinline`.
   - `IntersectionObserver` включает воспроизведение только тогда, когда слайдер виден на экране, и ставит на паузу при скролле.
2. **Ленивый плеер YouTube:**
   - Iframe YouTube **НЕ** грузится при открытии страницы.
   - Загрузка происходит строго в момент нажатия на карточку проекта.
   - Поддерживается доступность: открытие по Enter/Space, закрытие по `Escape` и клику на оверлей, фокус-трап.
3. **Слайдер До/После:**
   - Поддерживает перетаскивание курсором мыши, сенсорный ввод (`PointerCapture`) и стрелки клавиатуры (`ArrowLeft`, `ArrowRight`, `Home`, `End`) с ARIA-атрибутами.
4. **FAQ аккордеон:**
   - Плавная 60fps анимация на `grid-template-rows: 0fr -> 1fr`.
   - Не более одного открытого вопроса одновременно.
5. **SEO & Доступность:**
   - Валидные семантические теги (`header`, `main`, `section`, `article`, `footer`, `nav`).
   - `robots.txt`, `sitemap.xml`, `favicon.svg`, `og-image.png`, `theme-color`.
   - Поддержка режима пониженного движения (`prefers-reduced-motion`).
   - Контрастность текста по стандарту WCAG AA.
