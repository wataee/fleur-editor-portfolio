import os
import re

p = r'C:\Users\timur\Desktop\fleur-editor-portfolio\src\layouts\Layout.astro'
with open(p, 'r', encoding='utf-8') as f:
    text = f.read()

# Remove the to-top button from Layout.astro
text = re.sub(r'\s*<!-- Scroll To Top Button -->\s*<button[\s\S]*?id="to-top"[\s\S]*?</button>', '', text)

# Remove data-visible toggle in handleScrollUpdate
text = re.sub(r'const toTopBtn = document\.getElementById\(\'to-top\'\);\s*', '', text, count=1)
text = re.sub(r'if \(toTopBtn\) \{\s*const isScrolled = window\.scrollY > window\.innerHeight \* 0\.35;\s*toTopBtn\.setAttribute\(\'data-visible\', isScrolled \? \'true\' : \'false\'\);\s*\}', '', text)

with open(p, 'w', encoding='utf-8') as f:
    f.write(text)

print('Layout.astro updated successfully')
