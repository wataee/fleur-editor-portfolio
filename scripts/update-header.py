with open('src/components/Header.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Update NavData interface to include difference
c = c.replace(
    'interface NavData {\n  work: string;\n  process: string;',
    'interface NavData {\n  work: string;\n  difference?: string;\n  process: string;'
)

# Desktop nav links
old_desktop = '''    <!-- Desktop Navigation -->
    <nav class="site-nav" aria-label="Main Navigation">
      <a class="nav-link" href="#work">{nav.work}</a>
      <a class="nav-link" href="#process">{nav.process}</a>
      <a class="nav-link" href="#about">{nav.about}</a>
      <a class="nav-link" href="#pricing">{nav.pricing || (lang === 'kz' ? 'Бағалар' : lang === 'en' ? 'Pricing' : 'Цены')}</a>
      <a class="nav-link" href="#faq">FAQ</a>
      <a class="nav-link" href="#contact">{nav.contact}</a>
    </nav>'''

new_desktop = '''    <!-- Desktop Navigation (<= 6 items matching page flow) -->
    <nav class="site-nav" aria-label="Main Navigation">
      <a class="nav-link" href="#work">{nav.work}</a>
      <a class="nav-link" href="#pricing">{nav.pricing || (lang === 'kz' ? 'Бағалар' : lang === 'en' ? 'Pricing' : 'Цены')}</a>
      <a class="nav-link" href="#process">{nav.process}</a>
      <a class="nav-link" href="#difference">{nav.difference || (lang === 'kz' ? 'Түс' : lang === 'en' ? 'Color' : 'Цвет')}</a>
      <a class="nav-link" href="#about">{nav.about}</a>
      <a class="nav-link" href="#contact">{nav.contact}</a>
    </nav>'''

c = c.replace(old_desktop, new_desktop)

# Mobile panel links
old_mobile = '''        <nav class="nav-panel-links">
          <a class="nav-panel-link" href="#work">{nav.work}</a>
          <a class="nav-panel-link" href="#process">{nav.process}</a>
          <a class="nav-panel-link" href="#about">{nav.about}</a>
          <a class="nav-panel-link" href="#pricing">{nav.pricing || (lang === 'kz' ? 'Бағалар' : lang === 'en' ? 'Pricing' : 'Цены')}</a>
          <a class="nav-panel-link" href="#faq">FAQ</a>
          <a class="nav-panel-link" href="#contact">{nav.contact}</a>
        </nav>'''

new_mobile = '''        <nav class="nav-panel-links">
          <a class="nav-panel-link" href="#work">{nav.work}</a>
          <a class="nav-panel-link" href="#pricing">{nav.pricing || (lang === 'kz' ? 'Бағалар' : lang === 'en' ? 'Pricing' : 'Цены')}</a>
          <a class="nav-panel-link" href="#process">{nav.process}</a>
          <a class="nav-panel-link" href="#difference">{nav.difference || (lang === 'kz' ? 'Түс' : lang === 'en' ? 'Color' : 'Цвет')}</a>
          <a class="nav-panel-link" href="#about">{nav.about}</a>
          <a class="nav-panel-link" href="#contact">{nav.contact}</a>
        </nav>'''

c = c.replace(old_mobile, new_mobile)

with open('src/components/Header.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print('Header.astro navigation updated successfully')
