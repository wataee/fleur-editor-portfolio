import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
import urllib.parse
from playwright.sync_api import sync_playwright

os.makedirs('screenshots/footer-after', exist_ok=True)

viewports = [
    ('360', 360, 740),
    ('768', 768, 1024),
    ('1280', 1280, 800),
    ('1920', 1920, 1080),
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
        print(f"\n==========================================")
        print(f"VERIFYING FOOTER: {lang.upper()} ({url})")
        print(f"==========================================")

        for vp_name, width, height in viewports:
            for theme in ['dark', 'light']:
                ctx = browser.new_context(viewport={'width': width, 'height': height})
                page = ctx.new_page()
                page.goto(url, wait_until='networkidle')

                if theme == 'light':
                    page.evaluate("""() => {
                        document.documentElement.classList.add('light');
                        document.documentElement.setAttribute('data-theme', 'light');
                    }""")

                # Scroll to footer
                page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
                page.wait_for_timeout(250)

                # Check horizontal scroll
                scroll_w = page.evaluate("document.documentElement.scrollWidth")
                inner_w = page.evaluate("window.innerWidth")
                if scroll_w - inner_w > 1:
                    msg = f"[{lang} @ {vp_name}-{theme}] Horizontal overflow! scrollWidth={scroll_w}, innerWidth={inner_w}"
                    print(f"ERROR: {msg}")
                    errors.append(msg)

                footer = page.query_selector('footer.site-footer')
                if not footer:
                    msg = f"[{lang} @ {vp_name}-{theme}] footer.site-footer not found!"
                    print(f"ERROR: {msg}")
                    errors.append(msg)
                    ctx.close()
                    continue

                footer_box = footer.bounding_box()
                footer_h = footer_box['height']
                print(f"[{lang} @ {vp_name}-{theme}] Footer height: {footer_h:.1f}px")

                # Check desktop height (~220 px)
                if width >= 1280:
                    if footer_h > 230:
                        msg = f"[{lang} @ {vp_name}-{theme}] Desktop footer height {footer_h:.1f}px exceeds ~220px limit (max 230px)!"
                        print(f"ERROR: {msg}")
                        errors.append(msg)
                    else:
                        print(f"[{lang} @ {vp_name}-{theme}] OK: Desktop height {footer_h:.1f}px <= 230px.")

                # Check footer text does not contain ".fleur"
                footer_text = footer.inner_text()
                if '.fleur' in footer_text:
                    msg = f"[{lang} @ {vp_name}-{theme}] Found forbidden '.fleur' in footer text!"
                    print(f"ERROR: {msg}")
                    errors.append(msg)
                else:
                    print(f"[{lang} @ {vp_name}-{theme}] OK: No '.fleur' in footer text.")

                # Check footer does not contain FX
                if 'FX:' in footer_text or 'FX: ON' in footer_text:
                    msg = f"[{lang} @ {vp_name}-{theme}] Found FX in footer!"
                    print(f"ERROR: {msg}")
                    errors.append(msg)

                # Check .to-top button
                to_top = page.query_selector('.site-footer .to-top')
                if not to_top:
                    msg = f"[{lang} @ {vp_name}-{theme}] .to-top button not found in footer!"
                    print(f"ERROR: {msg}")
                    errors.append(msg)
                else:
                    # check position is not fixed
                    position = page.evaluate("el => window.getComputedStyle(el).position", to_top)
                    if position == 'fixed':
                        msg = f"[{lang} @ {vp_name}-{theme}] .to-top button still has position: fixed!"
                        print(f"ERROR: {msg}")
                        errors.append(msg)
                    else:
                        print(f"[{lang} @ {vp_name}-{theme}] OK: .to-top position is '{position}' (not fixed).")

                    # check dimensions are circular
                    btn_box = to_top.bounding_box()
                    bw, bh = btn_box['width'], btn_box['height']
                    print(f"[{lang} @ {vp_name}-{theme}] .to-top button size: {bw:.1f}px x {bh:.1f}px")
                    if abs(bw - bh) > 1.5:
                        msg = f"[{lang} @ {vp_name}-{theme}] .to-top button not circular! w={bw}, h={bh}"
                        print(f"ERROR: {msg}")
                        errors.append(msg)
                    if not (38 <= bw <= 46):
                        msg = f"[{lang} @ {vp_name}-{theme}] .to-top button size {bw}px out of 40-44px range!"
                        print(f"ERROR: {msg}")
                        errors.append(msg)

                    # check aria-label
                    aria_lbl = to_top.get_attribute('aria-label')
                    if not aria_lbl:
                        msg = f"[{lang} @ {vp_name}-{theme}] .to-top button missing aria-label!"
                        print(f"ERROR: {msg}")
                        errors.append(msg)
                    else:
                        print(f"[{lang} @ {vp_name}-{theme}] OK: .to-top aria-label='{aria_lbl}'")

                # Check navigation anchors exist
                for anchor_name in ['#work', '#process', '#pricing', '#faq', '#contact']:
                    nav_link = page.query_selector(f'.site-footer a[href="{anchor_name}"]')
                    if not nav_link:
                        msg = f"[{lang} @ {vp_name}-{theme}] Footer missing nav link with href='{anchor_name}'!"
                        print(f"ERROR: {msg}")
                        errors.append(msg)

                # Check contacts (telegram, email, x)
                contacts_links = page.query_selector_all('.site-footer .footer-contacts-list a')
                if len(contacts_links) < 3:
                    msg = f"[{lang} @ {vp_name}-{theme}] Expected 3 contact links, found {len(contacts_links)}!"
                    print(f"ERROR: {msg}")
                    errors.append(msg)
                else:
                    for cl in contacts_links:
                        href = cl.get_attribute('href')
                        if href.startswith('mailto:'):
                            parsed = urllib.parse.urlparse(href)
                            qs = urllib.parse.parse_qs(parsed.query)
                            subj = qs.get('subject', [''])[0]
                            # check no raw '/' in subject
                            if '/' in subj:
                                msg = f"[{lang} @ {vp_name}-{theme}] Raw '/' found in mailto subject: {subj}"
                                print(f"ERROR: {msg}")
                                errors.append(msg)
                            else:
                                print(f"[{lang} @ {vp_name}-{theme}] OK: Mailto subject is valid: '{subj}'")

                # Check mobile tap target height (>= 44px)
                if width <= 768:
                    links = page.query_selector_all('.site-footer .footer-link')
                    for idx, lk in enumerate(links[:3]):
                        lbox = lk.bounding_box()
                        if lbox and lbox['height'] < 43:
                            msg = f"[{lang} @ {vp_name}-{theme}] Mobile tap target height {lbox['height']:.1f}px < 44px for link {idx}!"
                            print(f"ERROR: {msg}")
                            errors.append(msg)
                            break
                    else:
                        print(f"[{lang} @ {vp_name}-{theme}] OK: Mobile tap targets are >= 44px.")

                # Save screenshot of footer
                shot_path = f"screenshots/footer-after/{lang}-{vp_name}-{theme}.png"
                footer.screenshot(path=shot_path)
                print(f"Saved screenshot: {shot_path}")

                ctx.close()

    browser.close()

print("\n================ VERIFICATION SUMMARY ================")
if errors:
    print(f"FAILED with {len(errors)} error(s):")
    for e in errors:
        print(f" - {e}")
    sys.exit(1)
else:
    print("ALL FOOTER TESTS PASSED WITH 0 ERRORS!")
