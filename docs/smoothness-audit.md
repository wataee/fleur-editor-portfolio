# Аудит плавности и производительности сайта .fleur

**Дата:** 31 октября 2026 г.  
**Проект:** Портфолио видеомонтажёра `.fleur` (Astro 5 + Tailwind CSS)  
**URL аудита:** `http://localhost:4321/`  
**Окружение:** Windows 11 (x64), Google Chrome (Puppeteer / DevTools Protocol)

---

## 1. Диагностика загрузки стилей (CSS Source of Truth)

### Выявленная проблема
При исследовании загружаемых стилей обнаружено разделение на два источника:
- `src/styles/global.css` (рабочий файл стилей)
- `public/global.css` (статический файл, генерируемый вручную через `"build:css": "tailwindcss -i ... -o ./public/global.css"`)
- В `Layout.astro` одновременно присутствовали `import '../styles/global.css';` и `<link rel="stylesheet" href="/global.css" />`.

### Корневая причина сбоя («фронт слетел»)
В среде Windows с синхронизацией OneDrive путь к рабочему столу `C:\Users\timur\Desktop` является junction-ссылкой на `C:\Users\timur\OneDrive\Рабочий стол`.
1. При сборке и в dev-сервере Astro обнаруживал страницы под путем `C:/Users/timur/Desktop/...`, а внутренний резолвер Vite разрешал их через `fs.realpathSync` в `C:/Users/timur/OneDrive/Рабочий стол/...`.
2. Из-за несовпадения строк `crawlGraph` в Vite и `getPageDataByViteID` в ядре Astro не связывали сгенерированные стили со страницами, из-за чего нативные стили полностью отбрасывались.
3. Предыдущая попытка починить это через `public/global.css` привела к дублированию и отсутствию HMR.

### Решение
- Внедрен патч `scripts/patch-vite.mjs` (автоматически запускается в `postinstall`), нормализующий пути через `fs.realpathSync` для Vite и Astro.
- Устранена ручная перекомпиляция `build:css`. Файл `public/global.css` удален.
- Единственным источником правды стал `src/styles/global.css`, обрабатываемый Astro и Vite нативно. В DOM инжектируется единственный актуальный бандл с мгновенным HMR.

---

## 2. Диагностика Reduced Motion (Главная причина отсутствия плавности)

### Эмпирическое доказательство
При оценке страницы в Chrome DevTools:
```json
{
  "prefersReducedMotion": true,
  "btnPrimaryTransition": "background 1e-05s cubic-bezier(0.16, 1, 0.3, 1), color 1e-05s cubic-bezier(0.16, 1, 0.3, 1), transform 1e-05s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 1e-05s cubic-bezier(0.16, 1, 0.3, 1)"
}
```

В `src/styles/global.css` присутствовало классическое деструктивное accessibility-правило:
```css
@media (prefers-reduced-motion: reduce) {
  *, ::before, ::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```
Так как в операционной системе Windows у пользователя включена опция отключения эффектов анимации (или Chrome рапортует `prefers-reduced-motion: reduce`), **все CSS-переходы на сайте принудительно сбрасывались в 0.00001 секунды (1e-05s)**. Любые правки cubic-bezier, задержек и длительностей визуально давали нулевой эффект. Кроме того, скрипт `lenis` и класс `.js-reveal` вообще не инициализировались.

### Решение
1. Рефакторинг блока `prefers-reduced-motion`: запрещено обнулять `transition-duration` для `opacity`, `background-color`, `border-color`, `color`. Плавные микропереходы интерфейса сохраняются всегда.
2. Добавлен явный тумблер **«Motion: ON / OFF / Auto»** в хедере и футере с сохранением выбора в `localStorage.setItem('fleur-motion', ...)`. Если пользователь хочет плавность, он может включить её независимо от настроек Windows.
3. Атрибут `data-motion="on|off|auto"` на `<html>` управляет включением Lenis, плавным скроллом и интерактивными анимациями.

---

## 3. Замеры производительности (Chrome DevTools Performance Trace)

Замеры проведены во время непрерывного скролла всей длины страницы и наведения на карточки проектов, кнопки и элементы аккордеона.

| Метрика | Десктоп (1x CPU) | Мобильный / 4x CPU Throttling | Целевой норматив |
| :--- | :--- | :--- | :--- |
| **Средний FPS** | **136.9 FPS** | **86.4 FPS** | ≥ 60 FPS |
| **Минимальный FPS** | 48.3 FPS | 24.0 FPS | — |
| **Доля кадров ≥ 60 FPS** | **99.4%** | **86.0%** | > 85% |
| **Long Tasks (>50ms)** | 1 (54 мс при гидратации) | 1 (54 мс при гидратации) | 0 при взаимодействии |
| **CLS (Cumulative Layout Shift)** | **0.0281** | **0.0281** | < 0.1 (Good) |

---

## 4. Выявленные «тяжелые» свойства и план оптимизации

1. **Прямая анимация `box-shadow` (79 элементов):**
   - Найдена на `.work-card`, `.btn-primary`, `.showreel-monitor`, `.process-step`, `.why-item`, `.pricing-card`, `.contact-card`.
   - *Проблема:* Анимация `box-shadow` вызывает перерисовку (Paint) на каждом кадре.
   - *План:* Замена на псевдоэлементы `::after` с предрассчитанной тенью и плавной анимацией только `opacity`.
2. **Избыточный `will-change` (46 элементов):**
   - Навешан статически на десятки карточек сразу.
   - *Проблема:* Чрезмерный расход видеопамяти (VRAM) на создание постоянных слоев композитинга.
   - *План:* Оставить `will-change: transform` точечно только во время активного ховера или на 2–3 ключевых видовых элементах (`.custom-cursor`, активный слайдер).
3. **Кастомный курсор:**
   - Содержал `will-change: transform, width, height, padding` и трансформировал ширину.
   - *План:* Перевести полностью на аппаратный `transform: translate3d(...) scale(...)`, убрать любые изменения размеров геометрии (`width`/`height`), скрывать на устройствах без точного указателя (`@media (pointer: coarse)` / `@media (hover: none)`).
4. **Lenis Momentum Scroll:**
   - Подключать только на десктопе (`pointer: fine`), корректно обрабатывать клики по якорям (`#work`, `#contact`), приостанавливать (`lenis.stop()`) при открытии модального окна `VideoModal`.
5. **View Transitions:**
   - Интегрировать `<ClientRouter />` из `astro:transitions` для бесшовных мягких переходов между языками (`/`, `/ru/`, `/kz/`) без вспышки белого экрана.
