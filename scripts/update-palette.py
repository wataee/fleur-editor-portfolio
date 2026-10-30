import re

css_path = r'C:\Users\timur\Desktop\fleur-editor-portfolio\src\styles\global.css'

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Dark Theme Palette
css = re.sub(
    r'/\* Matte Graphite & Tungsten Amber Palette \(Cinematic NLE Dark Theme\) \*/\s*--bg: #0D0E12;[\s\S]*?--shadow-glow-hover: 0 16px 40px -10px rgba\(226, 133, 34, 0\.35\);',
    '''/* Matte Graphite & Dark Velvet Rose Palette (Cinematic NLE Dark Theme) */
  --bg: #0D0E12;
  --surface: #131419;
  --surface-raised: #1A1C23;
  --surface-overlay: rgba(19, 20, 25, 0.88);
  --line: #22242D;
  --hairline: #181920;
  --text: #F0F0F3;
  --text-dim: #9A9EAB;
  --text-muted: #5E6270;
  --accent: #9E2A38; /* Dark Velvet Rose (exact match to .fleur avatar) */
  --accent-hover: #BD4353; /* Petal Highlight Rose */
  --accent-warm: #BD4353;
  --accent-glow: #7A202A;
  --accent-soft: rgba(158, 42, 56, 0.16);
  --accent-line: rgba(184, 58, 73, 0.42);
  --live-rec: #EF4444;
  --live-halo: rgba(239, 68, 68, 0.35);
  --live-halo-0: rgba(239, 68, 68, 0);
  --shadow-card: 0 20px 40px -15px rgba(0, 0, 0, 0.8);
  --shadow-header: 0 12px 32px -8px rgba(0, 0, 0, 0.7);
  --shadow-glow: 0 8px 30px -8px rgba(158, 42, 56, 0.28);
  --shadow-glow-hover: 0 16px 40px -10px rgba(189, 67, 83, 0.4);''',
    css
)

# 2. Light Theme Palette
css = re.sub(
    r'--accent: #B85C0A; /\* Warm Amber - WCAG AA > 4\.8:1 \*/[\s\S]*?--shadow-glow-hover: 0 16px 36px -10px rgba\(184, 92, 10, 0\.28\);',
    '''--accent: #8E202E; /* Rich Wine Rose - WCAG AA > 6:1 on light */
  --accent-hover: #A62838;
  --accent-warm: #A62838;
  --accent-soft: rgba(142, 32, 46, 0.1);
  --accent-line: rgba(142, 32, 46, 0.35);
  --live-rec: #DC2626;
  --live-halo: rgba(220, 38, 38, 0.25);
  --live-halo-0: rgba(220, 38, 38, 0);
  --shadow-card: 0 12px 30px -10px rgba(0, 0, 0, 0.08);
  --shadow-header: 0 8px 24px -6px rgba(0, 0, 0, 0.06);
  --shadow-glow: 0 8px 24px -8px rgba(142, 32, 46, 0.2);
  --shadow-glow-hover: 0 16px 36px -10px rgba(142, 32, 46, 0.28);''',
    css
)

# 3. Cursor pill
css = re.sub(
    r'(\.cursor-pill\s*\{[^}]*?background:\s*var\(--accent\);\s*)color:\s*#000;',
    r'\1color: #FFF;',
    css
)

# 4. btn-primary
css = re.sub(
    r'(\.btn-primary\s*\{[^}]*?)color:\s*#000;',
    r'\1color: #FFF;',
    css
)
css = re.sub(
    r'(\.btn-primary:hover\s*\{[\s\S]*?background:)\s*#FFF;([\s\S]*?color:)\s*#000;([\s\S]*?box-shadow:)\s*0 4px 16px rgba\([^)]+\);',
    r'\1 var(--accent-hover);\2 #FFF;\3 0 4px 16px rgba(189, 67, 83, 0.4);',
    css
)

# 5. hero-play-btn
css = re.sub(
    r'(\.hero-play-btn\s*\{[^}]*?)color:\s*#000;',
    r'\1color: #FFF;',
    css
)
css = re.sub(
    r'(\.hero-play-btn:hover\s*\{[\s\S]*?background:)\s*#FFF;',
    r'\1 var(--accent-hover);',
    css
)

# 6. work-tab active
css = re.sub(
    r'(\.work-tab\.active,\s*\.work-tab\[aria-selected="true"\]\s*\{[^}]*?)color:\s*#000;',
    r'\1color: #FFF;',
    css
)

# 7. work-play-badge
css = re.sub(
    r'(\.work-play-badge\s*\{[^}]*?)color:\s*#000;',
    r'\1color: #FFF;',
    css
)
css = re.sub(
    r'(\.work-facade:hover\s+\.work-play-badge\s*\{[\s\S]*?background:)\s*#FFF;([\s\S]*?color:)\s*#000;',
    r'\1 var(--accent-hover);\2 #FFF;',
    css
)

# 8. work-cta-watch
css = re.sub(
    r'(\.work-cta-watch\s*\{[^}]*?)color:\s*#000;',
    r'\1color: #FFF;',
    css
)
css = re.sub(
    r'(\.work-cta-watch:hover\s*\{[\s\S]*?background:)\s*#FFF;([\s\S]*?color:)\s*#000;',
    r'\1 var(--accent-hover);\2 #FFF;',
    css
)

# 9. pricing-card-badge
css = re.sub(
    r'(\.pricing-card-badge\s*\{[^}]*?)color:\s*#000;',
    r'\1color: #FFF;',
    css
)

# 10. Replace all remaining rgba(226, 133, 34, <alpha>) with rgba(189, 67, 83, <alpha>)
css = re.sub(r'rgba\(226,\s*133,\s*34,\s*([\d\.]+)\)', r'rgba(189, 67, 83, \1)', css)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print('Updated global.css successfully')
