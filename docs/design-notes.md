# Результаты разведки дизайна fareeditor.com (RU / EN)

## 1. Дизайн-система и CSS-токены (Computed / CSS Variables)

### Цветовая палитра
- **Фон страницы (`--bg`):** `#FBFCFD` (чистый холодный светлый оттенок)
- **Поверхность карточек (`--surface`):** `#F2F5F8`
- **Приподнятая поверхность (`--surface-raised`):** `#E9EEF4`
- **Границы и разделители (`--hairline`):** `#E3E9F0` (тонкие линии 1px)
- **Контурные границы карточек (`--line`):** `#7E8C9E` (серый нейтральный)
- **Основной текст (`--text`):** `#0E1319` (почти черный глубокий)
- **Приглушенный текст (`--text-dim`):** `#4A5566`
- **Вторичный / служебный текст (`--text-mute`):** `#5C6878`
- **Основной акцент (`--accent`):** `#0B62D6` (яркий синий кобальт)
- **Акцентная граница (`--accent-line`):** `rgba(11, 98, 214, 0.34)`
- **Мягкий акцент (`--accent-soft`):** `rgba(11, 98, 214, 0.1)`
- **Теплый акцент (`--accent-warm`):** `#9A6212` (янтарный для активного FAQ и акцентов)
- **Индикатор статуса онлайн (`--live`):** `#1B7A4F` (изумрудный зеленый)
- **Ореол индикатора (`--live-halo`):** `rgba(27, 122, 79, 0.38)`
- **Ошибка / предупреждение (`--danger`):** `#B3261E`
- **Полупрозрачный фон с блюром (`--bg-blur`):** `rgba(251, 252, 253, 0.78)`

### Тени
- **Шапка (`--shadow-header`):** `0 1px 2px rgba(14,19,25,.06), 0 10px 28px -6px rgba(14,19,25,.1)`
- **Интерактивные карточки (`--shadow-glow`):** `0 8px 20px -8px rgba(11,98,214,.22)`
- **Ховер карточек (`--shadow-glow-hover`):** `0 16px 32px -10px rgba(11,98,214,.22)`

### Типографика
- **Display & Body Font:** `"Onest", system-ui, sans-serif`
- **Monospace Font:** `"JetBrains Mono", ui-monospace, monospace`
- **Веса шрифта:** Light (300), Regular (400), Medium (500), Semibold (600), Bold (700), Black (800)
- **Шкала размеров:**
  - Hero заголовок (`--fs-hero`): `clamp(2.25rem, 5.6vw, 4.5rem)` (~36px до 72px, line-height 1.02, letter-spacing -0.03em)
  - H2 заголовки секций (`--fs-h2`): `clamp(1.6875rem, 3.4vw, 2.625rem)` (letter-spacing -0.02em)
  - H3 заголовки карточек (`--fs-h3`): `clamp(1.0625rem, 1.5vw, 1.3125rem)`
  - Карточки портфолио (`--fs-work`): `clamp(1.25rem, 2.2vw, 1.75rem)`
  - Цифры статистики (`--fs-stat`): `clamp(2.25rem, 5.2vw, 3.75rem)` (font-weight 800)
  - Подзаголовок Hero (`--fs-lead`): `clamp(1.0313rem, 1.4vw, 1.1875rem)` (font-weight 300)
  - Основной текст (`--fs-body`): `1rem` (16px, line-height 1.6)
  - Мелкий текст (`--fs-sm`): `0.9375rem` (15px)
  - Моноширинный текст (`--fs-mono`): `0.6875rem` (11px, letter-spacing 0.16em, uppercase)
  - Моноширинный крупный (`--fs-mono-lg`): `0.8125rem` (13px)

### Радиусы скругления
- Малый (`--radius-sm`): `8px` (кнопки, инпуты)
- Средний (`--radius-md`): `12px` (карточки, слайдер До/После)
- Pill (`--radius-pill`): `999px` (шапка, бейджи, теги)

### Сетка и отступы
- Максимальная ширина контейнера: `1200px` (`--container: 1200px`)
- Боковые поля контейнера (`--gutter`): `clamp(20px, 5vw, 40px)`
- Вертикальные отступы секций (`--section-y`): `clamp(72px, 9vw, 132px)`
- Шаг отступов: `--sp-1: 4px`, `--sp-2: 8px`, `--sp-3: 12px`, `--sp-4: 16px`, `--sp-5: 24px`, `--sp-6: 32px`, `--sp-7: 48px`, `--sp-8: 64px`, `--sp-9: 96px`, `--sp-10: 128px`

---

## 2. Анимации и интерактивные состояния

### Появление контента при скролле (Scroll Reveal)
- Прогрессивное улучшение: без JS контент виден сразу (`[data-reveal] { opacity: 1; transform: none; }`).
- Скрипт вешает класс `js-reveal` на `<html>`:
  - Базовые элементы получают: `transform: translateY(24px); opacity: 0; transition: opacity .62s cubic-bezier(.22,.61,.36,1), transform .62s ...`
  - Карточки получают: `translate: 0 clamp(28px, 18%, 72px); opacity: 0;`
  - При пересечении зоны видимости (IntersectionObserver / scroll calculation) выставляется `data-revealed="1"`.
  - Специфические задержки для Hero: `--hero-delay-1: 0ms`, `--hero-delay-2: 80ms`, `--hero-delay-3: 160ms`.

### Пульсация индикатора доступности («Открыт для проектов»)
- `@keyframes fare-pulse`:
  - `0%, 100% { box-shadow: 0 0 0 0 rgba(27,122,79,.38); }`
  - `70% { box-shadow: 0 0 0 6px rgba(27,122,79,0); }` (период 2.4s)

### Счётчик цифр статистики
- Плавная интерполяция чисел от 0 до целевого значения за `--dur-count: 1.1s` с функцией easing: `1 - Math.pow(1 - t, 3)` (Ease-Out Cubic).

### Шапка сайта (Sticky Header)
- Позиционирование: `position: sticky; top: clamp(10px, 1.4vw, 18px); z-index: 90;`
- Сама секция `site-header` имеет `pointer-events: none`, чтобы не блокировать клики за пределами пилюли.
- Внутренний контейнер `.header-inner` имеет `pointer-events: auto`, `width: fit-content; margin: 0 auto; height: 68px; border-radius: 999px; background: var(--bg); border: 1px solid var(--hairline); box-shadow: var(--shadow-header);`
- При скролле: `backdrop-filter: blur(8px); background: var(--bg-blur)`.
- Активная ссылка навигации: подчеркивание `text-decoration: underline 2px var(--accent); text-underline-offset: 0.35em`.
- Мобильное меню: `<details class="nav-toggle">` с кнопкой-бургером `<summary>`, раскрывающей выпадающую панель с плавной анимацией пунктов через stagger delay.

### Аккордеон FAQ
- Техника CSS Grid анимации без фиксированной высоты:
  ```css
  .faq-panel {
    display: grid;
    grid-template-rows: 0fr;
    opacity: 0;
    transition: grid-template-rows 0.24s cubic-bezier(.22,.61,.36,1), opacity 0.24s ...;
  }
  .faq-panel-inner { overflow: hidden; min-height: 0; }
  .faq-item[data-open="true"] .faq-panel {
    grid-template-rows: 1fr;
    opacity: 1;
  }
  .faq-item[data-open="true"] .faq-icon {
    transform: rotate(45deg);
  }
  ```
- Рамка активного вопроса подсвечивается теплым янтарным контуром `--accent-warm` (`#9A6212`).

---

## 3. Слайдер «До/После» (The Difference)

### Разметка и синхронизация двух видео
1. Контейнер `.ba`: `position: relative; aspect-ratio: 16 / 9; overflow: hidden; border-radius: 12px; touch-action: none; cursor: ew-resize; user-select: none;`
2. Переменная положения: `--ba-pos: 50%` (от 0% до 100%).
3. Нижнее видео (После монтажа):
   `position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover;`
4. Верхний слой-маска `.ba-clip` (До монтажа):
   `position: absolute; inset: 0; clip-path: inset(0 calc(100% - var(--ba-pos)) 0 0);`
   Внутри лежит идентичное по размеру видео.
5. Разделитель и ручка `.ba-handle`:
   `position: absolute; top: 0; bottom: 0; left: var(--ba-pos); width: 2px; margin-left: -1px; background: var(--bg);`
   Ручка `.ba-handle-grip`: круглая кнопка 44x44px с `backdrop-filter: blur(6px)`.
6. События и доступность:
   - Мышь и тач: `PointerEvent` + `setPointerCapture(e.pointerId)` на контейнере. Вычисление процента: `Math.min(100, Math.max(0, ((e.clientX - rect.left) / rect.width) * 100))`.
   - Клавиатура: на ручке `role="slider"`, `tabindex="0"`, `aria-valuenow`, `aria-valuemin="0"`, `aria-valuemax="100"`. Стрелки влево/вправо с шагом 5%, клавиши Home (0%) и End (100%).
   - Синхронизация видео: видео А выступает мастером; при воспроизведении проверяется рассинхрон `Math.abs(videoA.currentTime - videoB.currentTime) > 0.15s`. Если превышает 150 мс, `videoB.currentTime = videoA.currentTime`. Проверка выполняется раз в 1 секунду.
   - Видимость: IntersectionObserver останавливает воспроизведение при уходе из вьюпорта и запускает при возвращении.

---

## 4. Сетка «Полнометражные видео» и отзывы

### Портфолио
- Табы категорий переключают видимую сетку без перезагрузки страницы.
- Карточки проектов:
  - Превью 16:9 (`.work-thumb`) с изображением-постером и плавающей кнопкой Play (круг 60px с иконкой).
  - При клике открывается модальное окно с ленивой загрузкой iframe плеера YouTube/Vimeo (улучшение).
  - Метаданные: клиент, площадка, хронометраж.
  - Заголовок и подробное описание решаемой задачи.
  - Внешняя ссылка «Смотреть на YouTube ↗».

### Отзывы (Карусель)
- Горизонтальный трек `.testimonial-track` со `scroll-snap-type: x mandatory` и скрытым скроллбаром.
- Кнопки навигации «Предыдущий» / «Следующий» скроллят трек на ширину карточки.
- Каждая карточка включает аватар 88x88px, имя, нишу/тематику канала, ключевую метрику (например «6 закрытых проектов»), цитату и список метрик (графика, сроки, процент сдачи).

---

## 5. Адаптивность по брейкпоинтам

1. **1440px (Desktop):**
   - Контейнер 1200px + padding 40px с каждой стороны.
   - Stats: 4 колонки в ряд (`grid-template-columns: repeat(4, 1fr)`).
   - Hero: заголовок и футер секции горизонтально, кнопка справа.
   - Сетка проектов: 2 колонки.
   - Шапка: горизонтальное меню со всеми ссылками.

2. **1024px (Small Desktop / Tablet Landscape):**
   - Контейнер сжимается по ширине.
   - Отступы секций плавно уменьшаются через `clamp()`.
   - Навигация и кнопки сохраняются.

3. **768px (Tablet Portrait):**
   - Навигация переключается на мобильную кнопку-бургер (`@media (max-width: 820px)`).
   - Stats перестраиваются в 2 колонки (`grid-template-columns: repeat(2, 1fr)`).
   - Hero футер перестраивается вертикально.
   - Сетка проектов: 1 или 2 колонки в зависимости от карточки.

4. **390px (Mobile Phone):**
   - Отступы по краям 20px.
   - Статистика: 2 колонки с уменьшенными паддингами.
   - Слайдер До/После: touch-перетаскивание на всю ширину.
   - Карточки отзывов занимают ~90-100% ширины экрана со snap-выравниванием.
   - Фиксированная кнопка «Написать в Telegram» внизу экрана (новое улучшение).
