import re

# 1. Update Header.astro
with open('src/components/Header.astro', 'r', encoding='utf-8') as f:
    header = f.read()

# Remove desktop motion toggle
header = re.sub(
    r'\s*<!-- Motion Toggle \(Animations ON / OFF\) -->\s*<button[^>]*id="motion-toggle"[^>]*>.*?</button>',
    '',
    header,
    flags=re.DOTALL
)

# Remove mobile motion toggle
header = re.sub(
    r'\s*<!-- Mobile Motion Toggle -->\s*<button[^>]*id="motion-toggle-mobile"[^>]*>.*?</button>',
    '',
    header,
    flags=re.DOTALL
)

# Rename default fallback for pricing
header = header.replace(
    "nav.pricing || (lang === 'kz' ? 'Бағалар' : lang === 'en' ? 'Pricing' : 'Цены')",
    "nav.pricing || (lang === 'kz' ? 'Құны' : lang === 'en' ? 'Pricing' : 'Стоимость')"
)

with open('src/components/Header.astro', 'w', encoding='utf-8') as f:
    f.write(header)

print("Updated Header.astro: FX toggles removed")

# 2. Update Footer.astro
with open('src/components/Footer.astro', 'r', encoding='utf-8') as f:
    footer = f.read()

footer = re.sub(
    r'\s*<div class="footer-motion-wrap">.*?</div>\s*',
    '\n\n',
    footer,
    flags=re.DOTALL
)

with open('src/components/Footer.astro', 'w', encoding='utf-8') as f:
    f.write(footer)

print("Updated Footer.astro: FX footer button removed")
