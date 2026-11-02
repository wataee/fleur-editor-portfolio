for path in ['src/pages/index.astro', 'src/pages/ru/index.astro', 'src/pages/kz/index.astro']:
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace(' tools={enData.tools}', '')
    c = c.replace(' tools={ruData.tools}', '')
    c = c.replace(' tools={kzData.tools}', '')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)

print('Updated pages to remove tools prop from WhyMe')
