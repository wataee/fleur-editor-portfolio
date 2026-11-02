with open(r'C:\Users\timur\Desktop\fleur-editor-portfolio\src\styles\global.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update padding and gap in base footer styles
css = css.replace(
    'padding: 28px var(--gutter) 20px;',
    'padding: 24px var(--gutter) 18px;'
)
css = css.replace(
    '.footer-inner {\n  max-width: var(--container);\n  margin: 0 auto;\n  display: flex;\n  flex-direction: column;\n  gap: 20px;\n}',
    '.footer-inner {\n  max-width: var(--container);\n  margin: 0 auto;\n  display: flex;\n  flex-direction: column;\n  gap: 16px;\n}'
)
css = css.replace(
    '.footer-nav-list,\n.footer-contacts-list {\n  display: flex;\n  flex-direction: column;\n  gap: 5px;\n}',
    '.footer-nav-list {\n  display: grid;\n  grid-template-columns: repeat(2, max-content);\n  gap: 5px 24px;\n}\n.footer-contacts-list {\n  display: flex;\n  flex-direction: column;\n  gap: 5px;\n}'
)
css = css.replace(
    '.footer-bottom {\n  display: flex;\n  align-items: center;\n  justify-content: space-between;\n  border-top: 1px solid var(--hairline);\n  padding-top: 16px;\n  gap: 16px;\n}',
    '.footer-bottom {\n  display: flex;\n  align-items: center;\n  justify-content: space-between;\n  border-top: 1px solid var(--hairline);\n  padding-top: 14px;\n  gap: 16px;\n}'
)
css = css.replace(
    '/* Scroll To Top Button (Footer) */\n.to-top {\n  position: static;\n  width: 42px;\n  height: 42px;',
    '/* Scroll To Top Button (Footer) */\n.to-top {\n  position: static;\n  width: 40px;\n  height: 40px;'
)

# In mobile media query: ensure footer-nav-list is flex column
css = css.replace(
    '.footer-nav-list,\n  .footer-contacts-list {\n    gap: 2px;\n  }',
    '.footer-nav-list {\n    display: flex;\n    flex-direction: column;\n    gap: 2px;\n  }\n  .footer-contacts-list {\n    gap: 2px;\n  }'
)

with open(r'C:\Users\timur\Desktop\fleur-editor-portfolio\src\styles\global.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Updated global.css successfully')
