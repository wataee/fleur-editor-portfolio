import os

pages = [
    r'C:\Users\timur\Desktop\fleur-editor-portfolio\src\pages\index.astro',
    r'C:\Users\timur\Desktop\fleur-editor-portfolio\src\pages\ru\index.astro',
    r'C:\Users\timur\Desktop\fleur-editor-portfolio\src\pages\kz\index.astro'
]

for p in pages:
    with open(p, 'r', encoding='utf-8') as f:
        text = f.read()
    text = text.replace(
        '<Footer data={enData.footer} contacts={contactsData} lang="en" />',
        '<Footer data={enData.footer} nav={enData.nav} contacts={contactsData} lang="en" />'
    )
    text = text.replace(
        '<Footer data={ruData.footer} contacts={contactsData} lang="ru" />',
        '<Footer data={ruData.footer} nav={ruData.nav} contacts={contactsData} lang="ru" />'
    )
    text = text.replace(
        '<Footer data={kzData.footer} contacts={contactsData} lang="kz" />',
        '<Footer data={kzData.footer} nav={kzData.nav} contacts={contactsData} lang="kz" />'
    )
    with open(p, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'Updated {p}')
