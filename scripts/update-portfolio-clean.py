with open('src/components/Portfolio.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Remove eyebrow and tape-index before title
old_head = '''  <div class="section-head" data-reveal="true">
    <div class="inline-flex items-center gap-2">
      <span class="tape-index" aria-hidden="true">[REEL // 2026]</span>
      <span class="eyebrow">{data.eyebrow}</span>
    </div>
    <h2 class="section-title" id="work-title">{data.title}</h2>
  </div>'''

new_head = '''  <div class="section-head" data-reveal="true">
    <h2 class="section-title" id="work-title">{data.title}</h2>
  </div>'''

c = c.replace(old_head, new_head)

# 2. Remove YouTube links
import re

# Remove youtube link in horizontal cards
c = re.sub(
    r'<a\s+href=\{project\.youtube_url\}\s+target="_blank"\s+rel="noopener noreferrer"\s+class="work-yt-link"\s*>\s*\{data\.watch\}\s*</a>',
    '',
    c
)

# Remove youtube link in vertical cards
c = re.sub(
    r'<a\s+href=\{project\.youtube_url\}\s+target="_blank"\s+rel="noopener noreferrer"\s+class="work-yt-link text-xs"\s*>\s*YouTube ↗\s*</a>',
    '',
    c
)

with open('src/components/Portfolio.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated Portfolio.astro')
