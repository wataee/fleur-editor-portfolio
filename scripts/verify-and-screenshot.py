import os
import sys
from playwright.sync_api import sync_playwright

os.makedirs('screenshots', exist_ok=True)

viewports = [
    ('mobile-360', 360, 740),
    ('mobile-390', 390, 844),
    ('tablet-768', 768, 1024),
    ('desktop-1280', 1280, 800),
    ('desktop-1920', 1920, 1080),
]

urls = [
    ('ru', 'http://127.0.0.1:4321/ru/'),
    ('en', 'http://127.0.0.1:4321/'),
    ('kz', 'http://127.0.0.1:4321/kz/'),
]

errors = []

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    
    for lang, url in urls:
        print(f"\n=== Testing Language: {lang.upper()} ({url}) ===")
        context = browser.new_context(viewport={'width': 1280, 'height': 800})
        page = context.new_page()
        
        # Track 404s
        failed_requests = []
        page.on('response', lambda res: failed_requests.append(res.url) if res.status >= 400 else None)
        
        page.goto(url, wait_until='networkidle')
        
        # Check for DRAFT or [TODO]
        body_text = page.inner_text('body')
        if 'DRAFT' in body_text:
            msg = f"[{lang}] DRAFT found in rendered text!"
            print(f"ERROR: {msg}")
            errors.append(msg)
        else:
            print(f"[{lang}] OK: No DRAFT found.")
            
        if '[TODO]' in body_text:
            msg = f"[{lang}] [TODO] found in rendered text!"
            print(f"ERROR: {msg}")
            errors.append(msg)
        else:
            print(f"[{lang}] OK: No [TODO] found.")

        # Check for Reviews section presence
        reviews_sec = page.query_selector('#reviews')
        if reviews_sec and reviews_sec.is_visible():
            msg = f"[{lang}] Reviews section is visible despite 0 non-draft reviews!"
            print(f"ERROR: {msg}")
            errors.append(msg)
        else:
            print(f"[{lang}] OK: Reviews section is cleanly hidden.")
            
        # Check failed image/asset requests
        img_failures = [u for u in failed_requests if any(ext in u for ext in ['.webp', '.jpg', '.png', '.svg'])]
        if img_failures:
            msg = f"[{lang}] Failed images: {img_failures}"
            print(f"ERROR: {msg}")
            errors.append(msg)
        else:
            print(f"[{lang}] OK: All images loaded successfully.")
            
        context.close()
        
        # Viewport tests & screenshots
        for vp_name, width, height in viewports:
            ctx = browser.new_context(viewport={'width': width, 'height': height})
            pg = ctx.new_page()
            pg.goto(url, wait_until='networkidle')
            
            # Check horizontal scroll overflow
            scroll_width = pg.evaluate("document.documentElement.scrollWidth")
            inner_width = pg.evaluate("window.innerWidth")
            diff = scroll_width - inner_width
            if diff > 1: # Allow 1px subpixel rounding
                msg = f"[{lang} @ {vp_name}] Horizontal overflow detected! scrollWidth: {scroll_width}, innerWidth: {inner_width} (diff: {diff}px)"
                print(f"ERROR: {msg}")
                errors.append(msg)
            else:
                print(f"[{lang} @ {vp_name}] OK: No horizontal scroll (scrollWidth: {scroll_width}, innerWidth: {inner_width}).")

            # Check hero showreel visibility on mobile (360/390px)
            if width <= 390:
                showreel = pg.query_selector('.hero-showreel-col')
                if showreel:
                    box = showreel.bounding_box()
                    print(f"[{lang} @ {vp_name}] Showreel monitor Y offset: {box['y']}px (viewport height: {height}px)")

            # Save screenshot
            shot_path = f"screenshots/{lang}-{vp_name}.png"
            pg.screenshot(path=shot_path, full_page=(vp_name in ['mobile-360', 'desktop-1280']))
            print(f"Saved screenshot: {shot_path}")
            
            # Modal interaction test on desktop-1280
            if vp_name == 'desktop-1280' and lang == 'ru':
                first_play = pg.query_selector('.showreel-screen')
                if first_play:
                    first_play.click()
                    pg.wait_for_timeout(500)
                    modal = pg.query_selector('#video-modal')
                    if modal and modal.is_visible():
                        print("OK: Video modal opened on showreel click.")
                        pg.screenshot(path="screenshots/video-modal-open.png")
                        # Close modal
                        pg.keyboard.press('Escape')
                        pg.wait_for_timeout(300)
                    else:
                        errors.append("Video modal did not open on showreel click!")

            ctx.close()

    browser.close()

print("\n================ VERIFICATION SUMMARY ================")
if errors:
    print(f"FAILED with {len(errors)} error(s):")
    for e in errors:
        print(f" - {e}")
    sys.exit(1)
else:
    print("ALL TESTS PASSED WITH 0 ERRORS!")
    print("Zero DRAFT pills, zero [TODO]s, zero broken images, zero horizontal overflow at 360px.")
