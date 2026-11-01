with open('src/components/BeforeAfter.astro', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace(
    '<span>DA VINCI RESOLVE STUDIO</span>',
    '<span class="hidden sm:inline">DA VINCI RESOLVE STUDIO</span>'
)
c = c.replace(
    '<span class="text-text-mute">·</span>',
    '<span class="text-text-mute hidden sm:inline">·</span>'
)
c = c.replace(
    '<span>3840×2160 UHD</span>',
    '<span class="hidden xs:inline">3840×2160 UHD</span>'
)

with open('src/components/BeforeAfter.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated BeforeAfter.astro HUD strip successfully')
