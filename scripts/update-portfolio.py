import re

with open('src/components/Portfolio.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Add tags to interface
if 'tags_ru?:' not in c:
    c = c.replace(
        '  body_ru: string; body_en: string; body_kz?: string;',
        '  body_ru: string; body_en: string; body_kz?: string;\n  tags_ru?: string[];\n  tags_en?: string[];\n  tags_kz?: string[];'
    )

# 2. Add getTags helper
helper = '''const getTags = (project: Project): string[] => {
  const suffix = lang === 'kz' ? 'kz' : lang === 'en' ? 'en' : 'ru';
  const val = project[`tags_${suffix}` as keyof Project];
  if (Array.isArray(val) && val.length > 0) return val as string[];
  return project.tags_ru || [];
};'''

if 'const getTags' not in c:
    c = c.replace('const verticalProjects =', helper + '\n\nconst verticalProjects =')

# 3. Horizontal img srcset
old_h_img = '''                  <img
                    class="work-thumb"
                    src={project.thumbnail}
                    alt=""
                    loading="lazy"
                    decoding="async"
                    width="1280"
                    height="720"
                  />'''

new_h_img = '''                  <img
                    class="work-thumb"
                    src={project.thumbnail}
                    srcset={`/posters/${project.youtube_id}-480.webp 480w, /posters/${project.youtube_id}.webp 960w`}
                    sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 600px"
                    alt=""
                    loading="lazy"
                    decoding="async"
                    width="960"
                    height="540"
                  />'''

c = c.replace(old_h_img, new_h_img)

# 4. Vertical img srcset
old_v_img = '''                  <img
                    class="work-thumb work-thumb--portrait"
                    src={project.thumbnail}
                    alt=""
                    loading="lazy"
                    decoding="async"
                    width="720"
                    height="1280"
                  />'''

new_v_img = '''                  <img
                    class="work-thumb work-thumb--portrait"
                    src={project.thumbnail}
                    srcset={`/posters/${project.youtube_id}-480.webp 480w, /posters/${project.youtube_id}.webp 960w`}
                    sizes="(max-width: 640px) 50vw, 360px"
                    alt=""
                    loading="lazy"
                    decoding="async"
                    width="540"
                    height="960"
                  />'''

c = c.replace(old_v_img, new_v_img)

# 5. Tag strip in horizontal cards
old_h_body = '<p class="work-body">{body}</p>'
new_h_body = '''<p class="work-body">{body}</p>

                  {getTags(project).length > 0 && (
                    <div class="work-tags-strip">
                      <span class="work-tags-label">{lang === 'kz' ? 'Жасалған:' : lang === 'en' ? 'Done:' : 'Сделано:'}</span>
                      <ul class="work-tags-list">
                        {getTags(project).map((t) => (
                          <li class="work-tag">{t}</li>
                        ))}
                      </ul>
                    </div>
                  )}'''

c = c.replace(old_h_body, new_h_body, 1)

# 6. Tag strip in vertical cards
old_v_body = '<p class="work-body work-body--clamp">{body}</p>'
new_v_body = '''<p class="work-body work-body--clamp">{body}</p>

                  {getTags(project).length > 0 && (
                    <div class="work-tags-strip">
                      <span class="work-tags-label">{lang === 'kz' ? 'Жасалған:' : lang === 'en' ? 'Done:' : 'Сделано:'}</span>
                      <ul class="work-tags-list">
                        {getTags(project).map((t) => (
                          <li class="work-tag">{t}</li>
                        ))}
                      </ul>
                    </div>
                  )}'''

c = c.replace(old_v_body, new_v_body, 1)

with open('src/components/Portfolio.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print('Portfolio.astro updated successfully')
