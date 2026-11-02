import sys
sys.stdout.reconfigure(encoding='utf-8')
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    b = p.chromium.launch(channel='chrome', headless=True)
    for vp in [1280, 1920]:
        ctx = b.new_context(viewport={'width': vp, 'height': 800})
        pg = ctx.new_page()
        pg.goto('http://127.0.0.1:4321/ru/', wait_until='networkidle')
        pg.evaluate('''() => {
            const style = document.createElement('style');
            style.textContent = `
                .site-footer { padding: 24px var(--gutter) 18px !important; }
                .footer-inner { gap: 16px !important; }
                .footer-grid { align-items: start !important; }
                .footer-nav-list {
                    display: grid !important;
                    grid-template-columns: repeat(2, max-content) !important;
                    gap: 5px 24px !important;
                }
                .footer-bottom { padding-top: 14px !important; }
                .to-top { width: 40px !important; height: 40px !important; }
            `;
            document.head.appendChild(style);
        }''')
        h = pg.evaluate("() => document.querySelector('.site-footer').offsetHeight")
        print(f'Footer height on {vp}px: {h}')
        ctx.close()
    b.close()
