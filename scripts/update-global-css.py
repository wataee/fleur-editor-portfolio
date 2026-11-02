import re

with open('src/styles/global.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Remove custom-cursor styles
css = re.sub(
    r'/\* Custom Editor Desktop Cursor \*/\s*\.custom-cursor\s*\{.*?\n\}\s*\.custom-cursor\.is-active\s*\{.*?\n\}\s*\.custom-cursor\.has-label\s*\{.*?\n\}\s*@media\s*\(hover:\s*none\)\s*or\s*\(pointer:\s*coarse\)\s*\{\s*\.custom-cursor\s*\{.*?\n\}\s*\}',
    '/* System cursor restored */',
    css,
    flags=re.DOTALL
)

# 2. Remove hero-studio-meta & hero-ai-badge
css = re.sub(
    r'\.hero-studio-meta\s*\{.*?\n\}\s*\.meta-separator\s*\{.*?\n\}\s*\.hero-ai-badge\s*\{.*?\n\}',
    '',
    css,
    flags=re.DOTALL
)

# 3. Update hero-title and hero-sub
old_hero_title = '''.hero-title {
  font-family: var(--font-display);
  font-weight: 800;
  font-size: var(--fs-hero);
  line-height: 1.05;
  letter-spacing: -0.035em;
  color: var(--text);
  margin: 0;
  max-width: 20ch;
  text-wrap: balance;
}'''

new_hero_title = '''.hero-title {
  font-family: var(--font-display);
  font-weight: 800;
  font-size: clamp(1.75rem, 1.2rem + 2.2vw, 3rem);
  line-height: 1.12;
  letter-spacing: -0.025em;
  color: var(--text);
  margin: 0;
  max-width: 28ch;
  text-wrap: balance;
}'''

css = css.replace(old_hero_title, new_hero_title)

# Also mobile hero-title override if present
css = css.replace(
    '.hero-title {\n    font-size: 1.85rem;\n  }',
    '/* mobile hero-title handled by clamp */'
)
css = re.sub(
    r'\.hero-title\s*\{\s*font-size:\s*clamp\(1\.85rem,\s*7vw,\s*2\.4rem\);\s*line-height:\s*1\.15;\s*\}',
    '',
    css
)

old_hero_sub = '''.hero-sub {
  font-size: var(--fs-lead);
  color: var(--text-dim);
  line-height: 1.6;
  margin: 0;
  max-width: 54ch;
}'''

new_hero_sub = '''.hero-sub {
  font-size: clamp(1rem, 0.95rem + 0.35vw, 1.125rem);
  color: var(--text-dim);
  line-height: 1.6;
  margin: 0;
  max-width: 60ch;
}'''

css = css.replace(old_hero_sub, new_hero_sub)

# 4. Remove hero-note & note-label
css = re.sub(
    r'\.hero-note\s*\{.*?\n\}\s*\.note-label\s*\{.*?\n\}',
    '',
    css,
    flags=re.DOTALL
)

# 5. Remove pillars section styles
css = re.sub(
    r'/\* Craft Pillars Section \*/\s*\.section--pillars\s*\{.*?\n\}\s*\.pillars-timeline-bar\s*\{.*?\n\}\s*\.timeline-rule\s*\{.*?\n\}\s*\.pillars-grid\s*\{.*?\n\}\s*\.pillar-card\s*\{.*?\n\}\s*\.pillar-card:hover\s*\{.*?\n\}\s*\.pillar-header\s*\{.*?\n\}\s*\.pillar-index\s*\{.*?\n\}\s*\.pillar-title\s*\{.*?\n\}',
    '',
    css,
    flags=re.DOTALL
)

# 6. Replace ba-handle and ba-handle-grip with true 1:1 circle
old_handle_block = re.search(
    r'\.ba-handle\s*\{.*?\.ba-handle:active \.ba-handle-grip\s*\{.*?\n\}',
    css,
    re.DOTALL
)

new_handle_block = '''.ba-handle {
  position: absolute;
  top: 0;
  bottom: 0;
  left: var(--ba-pos, 50%);
  width: 2px;
  transform: translateX(-50%);
  margin-left: 0;
  background: var(--accent);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: ew-resize;
  z-index: 4;
}
.ba-handle-line {
  position: absolute;
  inset: 0;
  background: var(--accent);
}
.ba-handle-grip {
  position: relative;
  width: 46px;
  height: 46px;
  min-width: 46px;
  min-height: 46px;
  aspect-ratio: 1 / 1;
  border-radius: 50%;
  flex-shrink: 0;
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  background: #131419;
  border: 2px solid var(--accent);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.6), 0 0 12px rgba(189, 67, 83, 0.4);
  z-index: 5;
  transition: transform 0.28s cubic-bezier(0.16, 1, 0.3, 1),
              border-color 0.28s ease,
              background-color 0.28s ease;
}
html.light .ba-handle-grip {
  background: #FFFFFF;
  border-color: var(--accent);
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.12), 0 0 10px rgba(142, 32, 46, 0.2);
}
.ba-handle:hover .ba-handle-grip {
  transform: scale(1.12);
  border-color: #FFFFFF;
  box-shadow: 0 0 20px rgba(189, 67, 83, 0.8);
}
.ba-handle:active .ba-handle-grip {
  transform: scale(1.18);
  box-shadow: 0 0 24px rgba(189, 67, 83, 1);
}
@media (max-width: 640px) {
  .ba-handle-grip {
    width: 42px;
    height: 42px;
    min-width: 42px;
    min-height: 42px;
  }
}'''

if old_handle_block:
    css = css.replace(old_handle_block.group(0), new_handle_block)
else:
    print("Warning: old_handle_block not found via regex")

# 7. Replace Process Section styles with timeline
old_process = re.search(
    r'/\* Process Section \*/\s*\.process-list\s*\{.*?\.step-progress\s*\{.*?\n\}',
    css,
    re.DOTALL
)

new_process = '''/* Process Timeline Section */
.section--process {
  position: relative;
}
.process-timeline-wrap {
  position: relative;
  margin-top: var(--sp-7);
}
.process-timeline {
  list-style: none;
  padding: 0;
  margin: 0;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: clamp(16px, 2.5vw, 36px);
  position: relative;
}
.process-timeline::before {
  content: '';
  position: absolute;
  top: 13px;
  left: 12.5%;
  right: 12.5%;
  height: 2px;
  background: var(--line);
  z-index: 1;
}
.timeline-step {
  position: relative;
  display: flex;
  flex-direction: column;
  z-index: 2;
}
.timeline-node {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: var(--surface);
  border: 2px solid var(--accent);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: var(--sp-4);
  box-shadow: 0 0 10px rgba(158, 42, 56, 0.35);
  flex-shrink: 0;
  align-self: flex-start;
}
.timeline-node-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--accent);
}
.timeline-content {
  display: flex;
  flex-direction: column;
}
.timeline-num {
  font-size: 13px;
  font-weight: 700;
  color: var(--accent);
  margin-bottom: 6px;
}
.timeline-title {
  font-family: var(--font-display);
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--text);
  margin: 0 0 8px 0;
  line-height: 1.35;
}
.timeline-desc {
  font-size: 0.875rem;
  color: var(--text-dim);
  line-height: 1.55;
  margin: 0;
}
.timeline-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 12px;
}
.timeline-tag {
  font-family: var(--font-mono);
  font-size: 11px;
  padding: 2px 8px;
  border-radius: var(--radius-pill);
  background: var(--surface-raised);
  border: 1px solid var(--line);
  color: var(--text-dim);
}
@media (max-width: 820px) {
  .process-timeline {
    display: flex;
    flex-direction: column;
    gap: 32px;
    padding-left: 38px;
  }
  .process-timeline::before {
    top: 14px;
    bottom: 14px;
    left: 13px;
    right: auto;
    width: 2px;
    height: auto;
  }
  .timeline-node {
    position: absolute;
    left: -38px;
    top: 0;
    margin-bottom: 0;
  }
}'''

if old_process:
    css = css.replace(old_process.group(0), new_process)
else:
    print("Warning: old_process not found via regex")

# 8. Replace WhyMe Section styles
old_why = re.search(
    r'/\* Why Me Section \*/\s*\.why-grid\s*\{.*?\.why-body\s*\{.*?\n\}',
    css,
    re.DOTALL
)

new_why = '''/* Why Me Section */
.why-grid {
  display: grid;
  gap: var(--sp-6);
  grid-template-columns: repeat(2, minmax(0, 1fr));
  margin-top: var(--sp-6);
}
.why-item {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: var(--sp-3);
  padding: clamp(20px, 2.5vw, 28px);
  background: var(--surface);
  border: 1px solid var(--hairline);
  border-radius: var(--radius-md);
  transition: border-color var(--dur-normal) ease;
}
.why-item:hover {
  border-color: var(--line);
}
.why-item-topline {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.why-index {
  font-family: var(--font-mono);
  font-size: 0.875rem;
  color: var(--accent);
  font-weight: 700;
  letter-spacing: var(--tracking-mono);
}
.why-title {
  font-family: var(--font-display);
  font-weight: 700;
  font-size: 1.1rem;
  margin: 0;
  line-height: 1.35;
}
.why-body {
  font-size: 0.875rem;
  color: var(--text-dim);
  margin: 0;
  line-height: 1.6;
}'''

if old_why:
    css = css.replace(old_why.group(0), new_why)
else:
    print("Warning: old_why not found via regex")

# 9. Replace Pricing Section styles
old_pricing = re.search(
    r'/\* Pricing Section \*/\s*\.pricing-grid\s*\{.*?\.pricing-desc\s*\{.*?\n\}',
    css,
    re.DOTALL
)

new_pricing = '''/* Compact Pricing Section */
.section--pricing {
  position: relative;
}
.pricing-compact-wrap {
  display: grid;
  grid-template-columns: 1.15fr 1.35fr 1.1fr;
  gap: clamp(24px, 3.5vw, 48px);
  align-items: start;
  margin-top: var(--sp-6);
  padding-top: var(--sp-6);
  border-top: 1px solid var(--line);
}
.pricing-col {
  display: flex;
  flex-direction: column;
}
.pricing-col-eyebrow {
  margin-bottom: 8px;
}
.pricing-ref-main {
  font-size: clamp(1.4rem, 2vw, 1.85rem);
  font-weight: 800;
  color: var(--accent);
  line-height: 1.25;
  margin: 4px 0 8px 0;
}
.pricing-ref-sub {
  font-size: 0.875rem;
  line-height: 1.5;
}
.pricing-factors-title {
  font-family: var(--font-display);
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--text);
  margin: 0 0 12px 0;
}
.pricing-factors-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.pricing-factor-item {
  display: flex;
  align-items: baseline;
  gap: 8px;
  font-size: 0.875rem;
  color: var(--text-dim);
  line-height: 1.5;
}
.factor-dash {
  font-weight: 700;
  user-select: none;
}
.pricing-cta-text {
  font-size: 0.875rem;
  line-height: 1.55;
  margin: 0 0 16px 0;
}
.pricing-cta-btn-wrap {
  display: flex;
  align-items: center;
}
@media (max-width: 860px) {
  .pricing-compact-wrap {
    grid-template-columns: 1fr;
    gap: 32px;
  }
}'''

if old_pricing:
    css = css.replace(old_pricing.group(0), new_pricing)
else:
    print("Warning: old_pricing not found via regex")

# Clean up remaining pricing styles
css = re.sub(r'\.pricing-badge\s*\{.*?\n\}', '', css, flags=re.DOTALL)
css = re.sub(r'\.pricing-features\s*\{.*?\n\}', '', css, flags=re.DOTALL)
css = re.sub(r'\.pricing-feature\s*\{.*?\n\}', '', css, flags=re.DOTALL)
css = re.sub(r'\.pricing-check\s*\{.*?\n\}', '', css, flags=re.DOTALL)
css = re.sub(r'\.pillar-desc\s*\{.*?\n\}', '', css, flags=re.DOTALL)

# 10. Clean up Motion System & Reduced Motion block
old_motion_block = re.search(
    r'/\* ==========================================================================\s*Motion System & Reduced Motion.*?@media \(prefers-reduced-motion: reduce\) \{.*?\}\s*\}',
    css,
    re.DOTALL
)

new_reduced_motion = '''/* ==========================================================================
   Prefers Reduced Motion (OS Setting)
   ========================================================================== */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
  [data-reveal] {
    opacity: 1 !important;
    transform: none !important;
  }
  .hero-lens-ring,
  .film-grain {
    animation: none !important;
  }
  .work-card,
  .work-card--horizontal,
  .timeline-step,
  .why-item,
  .contact-card,
  .btn-primary,
  .btn-secondary,
  .nav-link {
    transform: none !important;
    transition: background 0.15s ease, color 0.15s ease, border-color 0.15s ease !important;
  }
}'''

if old_motion_block:
    css = css.replace(old_motion_block.group(0), new_reduced_motion)
else:
    print("Warning: old_motion_block not found via regex")

# Clean up any remaining .process-list, .pricing-card references in media queries
css = css.replace('.process-list {\n    grid-template-columns: 1fr;\n  }', '')
css = re.sub(r'\.hero-studio-meta\s*\{.*?\}', '', css, flags=re.DOTALL)
css = re.sub(r'\.pillars-grid\s*\{.*?\}', '', css, flags=re.DOTALL)

with open('src/styles/global.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Updated src/styles/global.css successfully')
