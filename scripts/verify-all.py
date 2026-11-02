import os
import sys
from playwright.sync_api import sync_playwright

os.makedirs('screenshots/after', exist_ok=True)

viewports = [
    ('360', 360, 740),
    ('390', 390, 844),
    ('768', 768, 1024),
    ('1280', 1280, 800),
]

urls = [
    ('ru', 'http://127.0.0.1:4321/ru/'),
    ('en', 'http://127.0.0.1:4321/'),
    ('kz', 'http://127.0.0.1:4321/kz/'),
]

errors = []

# Forbidden text fragments that must NOT appear anywhere on the pages
forbidden_texts = [
    'FX: ON',
    'FX: OFF',
    'Ручной монтаж',
    'Manual Edit',
    'Қолмен монтаждау',
    'REEL 2026',
    '[GENRE // EXPERTISE]',
    '[REEL // 2026]',
    'Смотреть на YouTube',
    'Watch on YouTube',
    'YouTube-та көру',
    'TODO',
    '[TODO]',
    '48–72',
    '48-72',
    'драфт',
    'draft',
]

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)

    for lang, url in urls:
        print(f"\n==========================================")
        print(f"Testing {lang.upper()} ({url})")
        print(f"==========================================")

        ctx = browser.new_context(viewport={'width': 1280, 'height': 800})
        page = ctx.new_page()
        page.goto(url, wait_until='networkidle')

        body_text = page.inner_text('body')

        # 1. Check forbidden strings
        for forbidden in forbidden_texts:
            if forbidden.lower() in body_text.lower():
                msg = f"[{lang}] Found forbidden text: '{forbidden}' in page text!"
                print(f"ERROR: {msg}")
                errors.append(msg)

        # 2. Check no FX button in header/footer
        if page.query_selector('#motion-toggle') or page.query_selector('#motion-toggle-mobile') or page.query_selector('#motion-toggle-footer'):
            msg = f"[{lang}] FX toggle element found in DOM!"
            print(f"ERROR: {msg}")
            errors.append(msg)
        else:
            print(f"[{lang}] OK: No FX toggle elements in DOM.")

        # 3. Check no custom cursor in DOM
        if page.query_selector('#custom-cursor') or page.query_selector('.custom-cursor'):
            msg = f"[{lang}] Custom cursor element found in DOM!"
            print(f"ERROR: {msg}")
            errors.append(msg)
        else:
            print(f"[{lang}] OK: No custom cursor element in DOM.")

        # 4. Check anchors #process and #pricing work
        for anchor in ['#work', '#pricing', '#process', '#difference', '#about', '#contact']:
            el = page.query_selector(anchor)
            if not el:
                msg = f"[{lang}] Anchor target {anchor} not found!"
                print(f"ERROR: {msg}")
                errors.append(msg)
            else:
                print(f"[{lang}] OK: Anchor {anchor} exists.")

        # 5. Check BeforeAfter handle circle
        handle_grip = page.query_selector('.ba-handle-grip')
        if handle_grip:
            box = handle_grip.bounding_box()
            w, h = box['width'], box['height']
            ratio = w / h if h > 0 else 0
            print(f"[{lang} @ 1280] Slider handle grip: {w:.1f}px x {h:.1f}px (ratio: {ratio:.3f})")
            if abs(w - h) > 1.5:
                msg = f"[{lang}] Slider handle is not circular! w={w}, h={h}"
                print(f"ERROR: {msg}")
                errors.append(msg)
            if not (44 <= w <= 50):
                msg = f"[{lang}] Slider handle diameter {w}px not in expected 44-48px range!"
                print(f"ERROR: {msg}")
                errors.append(msg)

        ctx.close()

        # Viewport specific checks
        for vp_name, width, height in viewports:
            v_ctx = browser.new_context(viewport={'width': width, 'height': height})
            v_page = v_ctx.new_page()
            v_page.goto(url, wait_until='networkidle')

            # Horizontal scroll check
            scroll_width = v_page.evaluate("document.documentElement.scrollWidth")
            inner_width = v_page.evaluate("window.innerWidth")
            diff = scroll_width - inner_width
            if diff > 1:
                msg = f"[{lang} @ {vp_name}] Horizontal overflow! scrollWidth={scroll_width}, innerWidth={inner_width} (diff: {diff}px)"
                print(f"ERROR: {msg}")
                errors.append(msg)
            else:
                print(f"[{lang} @ {vp_name}] OK: No horizontal scroll.")

            # Hero title line count check
            hero_title = v_page.query_selector('.hero-title')
            if hero_title:
                client_rects = v_page.evaluate("""(el) => {
                    const range = document.createRange();
                    range.selectNodeContents(el);
                    return range.getClientRects().length;
                }""", hero_title)
                print(f"[{lang} @ {vp_name}] Hero title line count: {client_rects}")
                if width == 1280 and client_rects > 3:
                    msg = f"[{lang} @ 1280] Hero title has {client_rects} lines (max allowed: 3)!"
                    print(f"ERROR: {msg}")
                    errors.append(msg)
                if width == 390 and client_rects > 4:
                    msg = f"[{lang} @ 390] Hero title has {client_rects} lines (max allowed: 4)!"
                    print(f"ERROR: {msg}")
                    errors.append(msg)

            # Mobile handle check
            if width <= 390:
                grip = v_page.query_selector('.ba-handle-grip')
                if grip:
                    box = grip.bounding_box()
                    w, h = box['width'], box['height']
                    print(f"[{lang} @ {vp_name}] Mobile slider grip: {w:.1f}px x {h:.1f}px")
                    if w < 40 or h < 40:
                        msg = f"[{lang} @ {vp_name}] Mobile slider grip < 40px! (w={w}, h={h})"
                        print(f"ERROR: {msg}")
                        errors.append(msg)

            # Screenshot
            shot_path = f"screenshots/after/{lang}-{vp_name}.png"
            v_page.screenshot(path=shot_path, full_page=True)
            print(f"Saved screenshot: {shot_path}")

            v_ctx.close()

    browser.close()

print("\n================ VERIFICATION SUMMARY ================")
if errors:
    print(f"FAILED with {len(errors)} error(s):")
    for e in errors:
        print(f" - {e}")
    sys.exit(1)
else:
    print("ALL TESTS PASSED WITH 0 ERRORS!")
