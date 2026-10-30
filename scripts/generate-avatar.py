import os
import base64
from io import BytesIO
from PIL import Image, ImageDraw

src = r'C:\Users\timur\Downloads\Gemini_Generated_Image_aqj7f3aqj7f3aqj7.jpg'
if not os.path.exists(src):
    print('Source not found:', src)
    exit(1)

img = Image.open(src).convert('RGBA')

# 1. High-resolution anti-aliased circular crop
size = (512, 512)
scale = 4
large_size = (size[0] * scale, size[1] * scale)

# Crop image to square centered
w, h = img.size
min_dim = min(w, h)
left = (w - min_dim) // 2
top = (h - min_dim) // 2
img_square = img.crop((left, top, left + min_dim, top + min_dim))
img_large = img_square.resize(large_size, Image.Resampling.LANCZOS)

mask_large = Image.new('L', large_size, 0)
draw = ImageDraw.Draw(mask_large)
draw.ellipse((0, 0, large_size[0], large_size[1]), fill=255)
mask = mask_large.resize(size, Image.Resampling.LANCZOS)

circle_img = Image.new('RGBA', size, (0, 0, 0, 0))
circle_img.paste(img_square.resize(size, Image.Resampling.LANCZOS), (0, 0), mask=mask)

os.makedirs('public', exist_ok=True)
circle_img.save('public/avatar.png', 'PNG', optimize=True)
circle_img.save('public/avatar.webp', 'WEBP', quality=95)
print('Saved public/avatar.png and public/avatar.webp')

# 2. JPG version for OG tags / backward compatibility (on dark #0D0E12 background)
jpg_bg = Image.new('RGB', size, (13, 14, 18))
jpg_bg.paste(circle_img, (0, 0), mask=circle_img.split()[3])
jpg_bg.save('public/avatar.jpg', 'JPEG', quality=95)
jpg_bg.save('public/logo.jpg', 'JPEG', quality=95)
print('Saved public/avatar.jpg and public/logo.jpg')

# 3. Favicon PNG
fav_size = (64, 64)
fav_mask_large = Image.new('L', (fav_size[0] * scale, fav_size[1] * scale), 0)
draw_fav = ImageDraw.Draw(fav_mask_large)
draw_fav.ellipse((0, 0, fav_size[0] * scale, fav_size[1] * scale), fill=255)
fav_mask = fav_mask_large.resize(fav_size, Image.Resampling.LANCZOS)

fav_img = img_square.resize(fav_size, Image.Resampling.LANCZOS)
fav_circle = Image.new('RGBA', fav_size, (0, 0, 0, 0))
fav_circle.paste(fav_img, (0, 0), mask=fav_mask)
fav_circle.save('public/favicon.png', 'PNG')
print('Saved public/favicon.png')

# 4. SVG Favicon
buf = BytesIO()
circle_img.resize((128, 128), Image.Resampling.LANCZOS).save(buf, format='PNG')
b64_png = base64.b64encode(buf.getvalue()).decode('utf-8')

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <defs>
    <clipPath id="circle-clip">
      <circle cx="32" cy="32" r="32"/>
    </clipPath>
  </defs>
  <image href="data:image/png;base64,{b64_png}" width="64" height="64" clip-path="url(#circle-clip)" preserveAspectRatio="xMidYMid slice"/>
</svg>'''

with open('public/favicon.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)
print('Saved public/favicon.svg')
