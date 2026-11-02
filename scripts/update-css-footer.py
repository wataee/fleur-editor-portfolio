import re

css_path = r'C:\Users\timur\Desktop\fleur-editor-portfolio\src\styles\global.css'

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Replace Footer styles
old_footer_pattern = r'/\* Footer \*/[\s\S]*?\.footer-copy\s*\{[\s\S]*?\}'

new_footer_styles = """/* Footer */
.site-footer {
  border-top: 1px solid var(--hairline);
  padding: 28px var(--gutter) 20px;
  margin-top: var(--sp-9);
}
.footer-inner {
  max-width: var(--container);
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.footer-grid {
  display: grid;
  grid-template-columns: 1.35fr 1fr 1.25fr;
  gap: clamp(24px, 4vw, 48px);
  align-items: start;
}
.footer-brand-col {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.footer-tagline {
  font-size: 13px;
  color: var(--text-dim);
  line-height: 1.5;
  margin: 0;
  max-width: 32ch;
}
.footer-col {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.footer-col-title {
  font-family: var(--font-mono);
  font-size: 11px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--text-mute);
  font-weight: 500;
  margin: 0;
}
.footer-nav-list,
.footer-contacts-list {
  display: flex;
  flex-direction: column;
  gap: 5px;
}
.footer-link {
  font-size: 13px;
  color: var(--text-dim);
  text-decoration: none;
  display: inline-flex;
  align-items: baseline;
  gap: 6px;
  width: fit-content;
  transition: color 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}
.footer-link:hover {
  color: var(--accent);
}
.footer-link:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-radius: 4px;
}
.footer-contact-link {
  flex-wrap: wrap;
}
.footer-contact-name {
  font-weight: 400;
}
.footer-contact-handle {
  font-family: var(--font-mono);
  font-size: 12px;
  color: var(--text-mute);
  transition: color 0.2s ease;
}
.footer-contact-link:hover .footer-contact-handle {
  color: var(--text-dim);
}
.footer-bottom {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-top: 1px solid var(--hairline);
  padding-top: 16px;
  gap: 16px;
}
.footer-copy {
  font-size: 12px;
  color: var(--text-mute);
  font-weight: 400;
  line-height: 1.4;
  margin: 0;
}"""

css = re.sub(old_footer_pattern, new_footer_styles, css)

# 2. Replace .to-top styles
old_totop_pattern = r'/\* Scroll To Top \*/[\s\S]*?\.to-top svg\s*\{[\s\S]*?\}'

new_totop_styles = """/* Scroll To Top Button (Footer) */
.to-top {
  position: static;
  width: 42px;
  height: 42px;
  border-radius: 50%;
  aspect-ratio: 1 / 1;
  background: var(--surface);
  border: 1px solid var(--line);
  color: var(--text-dim);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  flex-shrink: 0;
  padding: 0;
  opacity: 1;
  transform: none;
  pointer-events: auto;
  transition: border-color 0.2s ease,
              color 0.2s ease,
              transform 0.2s ease,
              background-color 0.2s ease;
}
.to-top:hover {
  border-color: var(--accent);
  color: var(--accent);
  transform: translateY(-2px);
  background: var(--surface-hover, var(--surface));
}
.to-top:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}
.to-top svg {
  width: 18px;
  height: 18px;
  display: block;
}"""

css = re.sub(old_totop_pattern, new_totop_styles, css)

# 3. Clean up mobile .to-top positioning if any inside media queries
css = re.sub(r'\.to-top\s*\{\s*bottom:\s*76px;\s*right:\s*14px;\s*\}', '', css)

# 4. Add responsive footer styles
responsive_footer_css = """
@media (max-width: 768px) {
  .site-footer {
    padding: 32px var(--gutter) calc(var(--sp-6) + 72px);
  }
  .footer-inner {
    gap: 28px;
  }
  .footer-grid {
    grid-template-columns: 1fr;
    gap: 28px;
  }
  .footer-col-title {
    margin-bottom: 2px;
  }
  .footer-nav-list,
  .footer-contacts-list {
    gap: 2px;
  }
  .footer-link {
    min-height: 44px;
    display: inline-flex;
    align-items: center;
    font-size: 14px;
    width: 100%;
  }
  .footer-bottom {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-top: 20px;
    gap: 16px;
  }
  .to-top {
    width: 44px;
    height: 44px;
  }
}
"""

# Append responsive styles before reduced motion or at the end of breakpoints
if '.site-footer {' in css:
    css = css.replace('@media (prefers-reduced-motion: reduce)', responsive_footer_css + '\n@media (prefers-reduced-motion: reduce)')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print('Updated global.css successfully')
