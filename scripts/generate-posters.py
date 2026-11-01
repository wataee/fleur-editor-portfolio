import os
import json
import urllib.request
import io
from PIL import Image

projects_path = r'C:\Users\timur\Desktop\fleur-editor-portfolio\src\data\projects.json'
posters_dir = r'C:\Users\timur\Desktop\fleur-editor-portfolio\public\posters'
local_fallback_dir = r'C:\Users\timur\Desktop\fleur-editor-portfolio\public\videos\posters'
work_dir = r'C:\Users\timur\Desktop\fleur-editor-portfolio\work'

os.makedirs(posters_dir, exist_ok=True)

with open(projects_path, 'r', encoding='utf-8') as f:
    projects = json.load(f)

# Map slug to local high-res poster fallback if available
FALLBACK_MAP = {
    'ai-niche-editing': os.path.join(local_fallback_dir, 'ai-edit.jpg'),
    'crypto-market-deepdive': os.path.join(local_fallback_dir, 'crypto-edit.jpg'),
    'podcast-minimalism': os.path.join(local_fallback_dir, 'podcast-edit.jpg'),
    'rental-income-reels': os.path.join(local_fallback_dir, 'rental-income-reel.jpg'),
    'gaming-montage-highlights': os.path.join(work_dir, 'gaming-sample.jpg') if os.path.exists(os.path.join(work_dir, 'gaming-sample.jpg')) else os.path.join(local_fallback_dir, 'gaming-edit.jpg'),
    'auto-vroomclub-promo': os.path.join(local_fallback_dir, 'vroomclub-reel.jpg'),
    'lifestyle-aesthetic-reel': os.path.join(local_fallback_dir, 'aesthetic-reel.jpg'),
    'creator-aesthetic-cut': os.path.join(local_fallback_dir, 'car-rental-reel.jpg'),
    'dynamic-speedramp-promo': os.path.join(local_fallback_dir, 'dynamic-reel.jpg'),
}

def crop_center_9_16(img):
    """Crop 9:16 aspect ratio from center of image, removing horizontal black bars."""
    w, h = img.size
    target_ratio = 9.0 / 16.0
    current_ratio = w / h
    
    if current_ratio > target_ratio:
        # Too wide (e.g. 16:9 or 4:3 with vertical video in center)
        new_w = int(h * target_ratio)
        offset = (w - new_w) // 2
        return img.crop((offset, 0, offset + new_w, h))
    elif current_ratio < target_ratio:
        new_h = int(w / target_ratio)
        offset = (h - new_h) // 2
        return img.crop((0, offset, w, offset + new_h))
    return img

def crop_center_16_9(img):
    """Crop 16:9 aspect ratio from center."""
    w, h = img.size
    target_ratio = 16.0 / 9.0
    current_ratio = w / h
    
    if current_ratio > target_ratio:
        new_w = int(h * target_ratio)
        offset = (w - new_w) // 2
        return img.crop((offset, 0, offset + new_w, h))
    elif current_ratio < target_ratio:
        new_h = int(w / target_ratio)
        offset = (h - new_h) // 2
        return img.crop((0, offset, w, offset + new_h))
    return img

for p in projects:
    vid = p['youtube_id']
    slug = p['slug']
    orient = p.get('orientation', 'horizontal')
    
    img = None
    fallback_file = FALLBACK_MAP.get(slug)
    
    # Check if local fallback file exists
    if fallback_file and os.path.exists(fallback_file):
        try:
            img = Image.open(fallback_file).convert('RGB')
            print(f'[{vid}] Loaded from local fallback: {os.path.basename(fallback_file)}')
        except Exception as e:
            print(f'[{vid}] Could not open local fallback: {e}')
    
    # If no local fallback, fetch best from YouTube
    if img is None:
        for qual in ['maxresdefault', 'sddefault', 'hqdefault']:
            url = f'https://i.ytimg.com/vi/{vid}/{qual}.jpg'
            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=5) as resp:
                    if resp.status == 200:
                        raw = resp.read()
                        if len(raw) > 3000:
                            test_img = Image.open(io.BytesIO(raw)).convert('RGB')
                            if test_img.size[0] >= 320:
                                img = test_img
                                print(f'[{vid}] Fetched {qual} from YouTube ({len(raw)} bytes)')
                                break
            except Exception:
                continue
                
    if img is None:
        print(f'ERROR: Could not get image for {vid}')
        continue
        
    # Crop to exact aspect ratio
    if orient == 'vertical':
        img = crop_center_9_16(img)
        target_960 = (960, 1706)
        target_480 = (480, 853)
    else:
        img = crop_center_16_9(img)
        target_960 = (960, 540)
        target_480 = (480, 270)
        
    # Generate 960px WebP
    img_960 = img.resize(target_960, Image.Resampling.LANCZOS)
    out_960 = os.path.join(posters_dir, f'{vid}.webp')
    img_960.save(out_960, 'WEBP', quality=88, method=6)
    
    # Generate 480px WebP
    img_480 = img.resize(target_480, Image.Resampling.LANCZOS)
    out_480 = os.path.join(posters_dir, f'{vid}-480.webp')
    img_480.save(out_480, 'WEBP', quality=85, method=6)
    
    p['thumbnail'] = f'/posters/{vid}.webp'
    print(f'[{vid}] Saved {out_960} ({os.path.getsize(out_960)/1024:.1f} KB) & 480.webp ({os.path.getsize(out_480)/1024:.1f} KB)')

with open(projects_path, 'w', encoding='utf-8') as f:
    json.dump(projects, f, ensure_ascii=False, indent=2)

print('Updated projects.json with local WebP poster paths!')
