import { writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const projectsFilePath = path.resolve(__dirname, '../src/data/projects.json');

// Complete list of target YouTube URLs from channel & prompt
export const VIDEO_URLS = [
  'https://www.youtube.com/watch?v=cZZgi5xn930', // 25:45 AI Niche
  'https://www.youtube.com/watch?v=JpYdNQUO9gA', // 7:38 Crypto Edit
  'https://youtu.be/W80pFjEQAbk',                // 8:53 Podcast Minimalism
  'https://youtu.be/B5Rn-nVXL8U',                // 0:24 Rental Income Reel (9:16)
  'https://youtube.com/shorts/9pBFZDq8POA',       // Gaming Shorts (9:16)
  'https://youtube.com/shorts/H2MjwWcbAJE',       // VroomClub Reel (9:16)
  'https://youtube.com/shorts/cp-Fx5PuVco',       // Aesthetic Lifestyle (9:16)
  'https://youtu.be/Cn7qbOIXKks',                // 0:18 Creator Cut (9:16)
  'https://youtu.be/8YToswyXOLI'                 // 0:11 Dynamic Teaser (9:16)
];

// Helper to extract video ID from various YouTube URL formats
export function extractVideoId(url) {
  if (!url) return null;
  const match = url.match(
    /(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|shorts\/|live\/))([a-zA-Z0-9_-]{11})/
  );
  return match ? match[1] : null;
}

// Check if high-res thumbnail is available, otherwise fallback
async function getBestThumbnail(videoId) {
  const maxresUrl = `https://i.ytimg.com/vi/${videoId}/maxresdefault.jpg`;
  const hqUrl = `https://i.ytimg.com/vi/${videoId}/hqdefault.jpg`;
  try {
    const res = await fetch(maxresUrl, {
      method: 'HEAD',
      headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' },
      signal: AbortSignal.timeout(3500)
    });
    if (res.ok) return maxresUrl;
  } catch {}
  return hqUrl;
}

// Rich multilingual metadata mapping based on real content
const PROJECT_DETAILS = {
  'cZZgi5xn930': {
    slug: 'ai-niche-editing',
    niche: 'finance',
    orientation: 'horizontal',
    duration: '25:45',
    featured: true,
    year: '2026',
    title_ru: 'Монтаж в нише искусственного интеллекта',
    title_en: 'AI Niche Narrative & Visual Deep-Dive',
    title_kz: 'Жасанды интеллект саласындағы монтаж',
    client_ru: 'YouTube-канал об ИИ',
    client_en: 'AI YouTube Channel',
    client_kz: 'AI туралы YouTube-арна',
    format_ru: 'Горизонтальное видео · 16:9 · 4K',
    format_en: 'Horizontal Video · 16:9 · 4K',
    format_kz: 'Көлденең бейне · 16:9 · 4K',
    body_ru: 'Масштабный разбор с выверенным темпом: анимированные схемы архитектур нейросетей, кинетический моушн интерфейсов, очищенная речь спикера и плотный саунд-дизайн.',
    body_en: 'In-depth long-form analysis featuring custom animated neural network schematics, kinetic UI recreations, and pristine vocal clarity across 25 minutes.',
    body_kz: 'Нейрожелі архитектурасының анимациялық сызбалары, интерфейстердің кинетикалық моушны және таза дыбысы бар ауқымды талдау бейнесі.'
  },
  'JpYdNQUO9gA': {
    slug: 'crypto-market-deepdive',
    niche: 'finance',
    orientation: 'horizontal',
    duration: '7:38',
    featured: true,
    year: '2026',
    title_ru: 'Аналитика крипторынка и токеномики',
    title_en: 'Crypto Market & Tokenomics Analysis',
    title_kz: 'Крипторынок пен токеномика сараптамасы',
    client_ru: 'Аналитический крипто-канал',
    client_en: 'Crypto Analytics Channel',
    client_kz: 'Крипто-сараптамалық арна',
    format_ru: 'Горизонтальное видео · 16:9 · 4K',
    format_en: 'Horizontal Video · 16:9 · 4K',
    format_kz: 'Көлденең бейне · 16:9 · 4K',
    body_ru: 'Динамичный темп повествования: визуализация ончейн-данных, графики ордербуков из биржевых терминалов и выверенные акценты на ключевых рисках.',
    body_en: 'Fast-paced market breakdown with vector on-chain visualizers, order book motion graphics, and zero filler pauses.',
    body_kz: 'Ончейн-деректердің визуалдануы, биржалық терминал кестелері және нақты екпіндері бар қарқынды нарықтық шолу.'
  },
  'W80pFjEQAbk': {
    slug: 'podcast-minimalism',
    niche: 'personal_brand',
    orientation: 'horizontal',
    duration: '8:53',
    featured: true,
    year: '2026',
    title_ru: 'Подкаст: минимализм и фокус',
    title_en: 'Studio Podcast: Minimalism & Focus',
    title_kz: 'Студиялық подкаст: минимализм және фокус',
    client_ru: 'Студийный подкаст',
    client_en: 'Studio Podcast',
    client_kz: 'Студиялық подкаст',
    format_ru: 'Горизонтальное видео · 16:9',
    format_en: 'Horizontal Video · 16:9',
    format_kz: 'Көлденең бейне · 16:9',
    body_ru: 'Разговорный формат: естественная чистка пауз, бесшовная мультикамерная склейка, выравнивание громкости голосов и фоновая атмосфера студии.',
    body_en: 'Conversational studio cut with natural pause trimming, invisible multicam rhythm, voice level normalization, and subtle room foley.',
    body_kz: 'Кідірістерді табиғи тазарту, камералардың байсалды ауысуы және дыбыс сапасын теңестіру қосылған студиялық формат.'
  },
  'B5Rn-nVXL8U': {
    slug: 'rental-income-reels',
    niche: 'real_estate',
    orientation: 'vertical',
    duration: '0:24',
    featured: true,
    year: '2026',
    title_ru: 'Доход от аренды · Недвижимость',
    title_en: 'Rental Income · Real Estate',
    title_kz: 'Жалға беру табысы · Жылжымайтын мүлік',
    client_ru: 'Агентство недвижимости',
    client_en: 'Real Estate Agency',
    client_kz: 'Жылжымайтын мүлік агенттігі',
    format_ru: 'Reels · 9:16',
    format_en: 'Reels · 9:16',
    format_kz: 'Reels · 9:16',
    body_ru: 'Экспертный рилс для удержания: акцентные плашки с цифрами доходности, трекинг текста к интерьеру и плотный саунд-дизайн переходов.',
    body_en: 'High-retention real estate reel featuring dynamic financial callouts, 3D text tracking, and punchy auditory transition cues.',
    body_kz: 'Қаржылық көрсеткіштері бар плашкалар, интерьерге мәтін трекингі және динамикалық саунд-дизайн бар жылжымайтын мүлік рилсі.'
  },
  '9pBFZDq8POA': {
    slug: 'gaming-montage-highlights',
    niche: 'gaming',
    orientation: 'vertical',
    duration: '0:35',
    featured: true,
    year: '2026',
    title_ru: 'Игровой хайлайт · Киберспорт',
    title_en: 'Gaming Highlights · Esports',
    title_kz: 'Ойын хайлайты · Киберспорт',
    client_ru: 'Игровой стример',
    client_en: 'Gaming Streamer',
    client_kz: 'Ойын стримері',
    format_ru: 'Shorts · 9:16',
    format_en: 'Shorts · 9:16',
    format_kz: 'Shorts · 9:16',
    body_ru: 'Синхронизация киллов под бит трека, спидрэмпы, кастомные экранные вспышки и мощный импакт-саунд.',
    body_en: 'High-energy beat-synced gameplay edit with velocity ramps, screen shakes, and weighted hit impact sound design.',
    body_kz: 'Музыка ырғағымен үндескен киллдер, жылдамдықты өзгерту (speed ramp) және қуатты импакт-дыбыстары бар ойын монтажы.'
  },
  'H2MjwWcbAJE': {
    slug: 'auto-vroomclub-promo',
    niche: 'real_estate',
    orientation: 'vertical',
    duration: '0:47',
    featured: true,
    year: '2026',
    title_ru: 'VroomClub · Автопрокат премиум',
    title_en: 'VroomClub · Premium Auto Rental',
    title_kz: 'VroomClub · Премиум көлік жалдау',
    client_ru: 'VroomClub',
    client_en: 'VroomClub',
    client_kz: 'VroomClub',
    format_ru: 'Reels · 9:16',
    format_en: 'Reels · 9:16',
    format_kz: 'Reels · 9:16',
    body_ru: 'Стильный промо-ролик автопарка: кинематографичная цветокоррекция, маскированные пролёты и глубокий звук двигателя.',
    body_en: 'Cinematic promotional reel for exotic car fleet with speed ramping, whip pans, seamless match cuts, and deep exhaust Foley.',
    body_kz: 'Премиум көліктер паркіне арналған промо-ролик: кинематографиялық түс түзету, маска арқылы өтулер және қозғалтқыш дыбысы.'
  },
  'cp-Fx5PuVco': {
    slug: 'lifestyle-aesthetic-reel',
    niche: 'personal_brand',
    orientation: 'vertical',
    duration: '0:20',
    featured: true,
    year: '2026',
    title_ru: 'Эстетичный лайфстайл · Бренд',
    title_en: 'Aesthetic Lifestyle · Brand',
    title_kz: 'Эстетикалық лайфстайл · Бренд',
    client_ru: 'Личный бренд',
    client_en: 'Personal Brand',
    client_kz: 'Жеке бренд',
    format_ru: 'Reels / Shorts · 9:16',
    format_en: 'Reels / Shorts · 9:16',
    format_kz: 'Reels / Shorts · 9:16',
    body_ru: 'Атмосферный визуал с плёночной фактурой зерна, минималистичными шрифтами и тёплым винтажным грейдингом.',
    body_en: 'Atmospheric visual piece with authentic film grain texture, minimalist typography, and warm analog color grading.',
    body_kz: 'Пленка түйіршігінің фактурасы, минималистік шрифттер және жылы аналогтық түс түзетуі бар атмосфералық бейне.'
  },
  'Cn7qbOIXKks': {
    slug: 'creator-aesthetic-cut',
    niche: 'personal_brand',
    orientation: 'vertical',
    duration: '0:18',
    featured: false,
    year: '2026',
    title_ru: 'Визуальный ритм · Креатор',
    title_en: 'Visual Rhythm · Creator',
    title_kz: 'Визуалды ырғақ · Креатор',
    client_ru: 'Креатор контента',
    client_en: 'Content Creator',
    client_kz: 'Контент креаторы',
    format_ru: 'Shorts · 9:16',
    format_en: 'Shorts · 9:16',
    format_kz: 'Shorts · 9:16',
    body_ru: 'Короткий ролик с выверенной композицией кадра, быстрой сменой ракурсов и акцентными звуковыми эффектами.',
    body_en: 'Punchy micro-content with deliberate framing, rapid angle alternations, and crisp tactile audio cues.',
    body_kz: 'Нақты кадр композициясы, ракурстардың жылдам ауысуы және тактильді дыбыстық эффектілері бар қысқа ролик.'
  },
  '8YToswyXOLI': {
    slug: 'dynamic-speedramp-promo',
    niche: 'gaming',
    orientation: 'vertical',
    duration: '0:11',
    featured: false,
    year: '2026',
    title_ru: 'Динамичный спидрэмп · Промо',
    title_en: 'Dynamic Speedramp · Promo',
    title_kz: 'Динамикалық спидрэмп · Промо',
    client_ru: 'Медиа-проект',
    client_en: 'Media Project',
    client_kz: 'Медиа жобасы',
    format_ru: 'Shorts · 9:16',
    format_en: 'Shorts · 9:16',
    format_kz: 'Shorts · 9:16',
    body_ru: 'Ультракороткий тизер с резкими переходами, эффектом глитча и насыщенным басовым саундом для максимального удержания.',
    body_en: 'Ultra-fast promotional teaser engineered for maximum retention with glitch transitions and sub-bass whooshes.',
    body_kz: 'Көрермен назарын барынша ұстап тұру үшін жылдам өтулері, глитч эффектісі және басты саунд-дизайны бар ультрақысқа тизер.'
  }
};

export async function fetchAllVideoMetadata(urls = VIDEO_URLS) {
  console.log(`[fetch-video-meta] Processing ${urls.length} YouTube links...`);
  const projects = [];

  for (let i = 0; i < urls.length; i++) {
    const rawUrl = urls[i];
    const videoId = extractVideoId(rawUrl);

    if (!videoId) {
      console.warn(`[fetch-video-meta] Could not extract ID from URL: ${rawUrl}`);
      continue;
    }

    console.log(`[fetch-video-meta] (${i + 1}/${urls.length}) Fetching metadata for ID: ${videoId}`);

    let oembed = null;
    try {
      const oembedRes = await fetch(
        `https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=${videoId}&format=json`,
        {
          headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' },
          signal: AbortSignal.timeout(3500)
        }
      );
      if (oembedRes.ok) {
        oembed = await oembedRes.json();
      } else {
        console.warn(`[fetch-video-meta] oEmbed returned status ${oembedRes.status} for ${videoId}`);
      }
    } catch (err) {
      console.warn(`[fetch-video-meta] oEmbed fetch failed for ${videoId}: ${err.message}`);
    }

    const thumbnail = await getBestThumbnail(videoId);
    const detail = PROJECT_DETAILS[videoId] || {};

    const isShorts = rawUrl.includes('/shorts/') || detail.orientation === 'vertical';
    const orientation = detail.orientation || (isShorts ? 'vertical' : 'horizontal');

    const project = {
      id: String(i + 1).padStart(2, '0'),
      slug: detail.slug || `video-${videoId}`,
      youtube_id: videoId,
      youtube_url: `https://www.youtube.com/watch?v=${videoId}`,
      orientation,
      niche: detail.niche || 'personal_brand',
      duration: detail.duration || '0:30',
      featured: detail.featured ?? (i < 4),
      order: i + 1,
      year: detail.year || '2026',
      thumbnail,
      title_ru: detail.title_ru || oembed?.title || `Видеопроект #${i + 1}`,
      title_en: detail.title_en || oembed?.title || `Video project #${i + 1}`,
      title_kz: detail.title_kz || oembed?.title || `Бейне жоба #${i + 1}`,
      client_ru: detail.client_ru || oembed?.author_name || 'Видеопортфолио',
      client_en: detail.client_en || oembed?.author_name || 'Video portfolio',
      client_kz: detail.client_kz || oembed?.author_name || 'Бейне портфолиосы',
      format_ru: detail.format_ru || (orientation === 'vertical' ? 'Вертикальное видео · 9:16' : 'Горизонтальное видео · 16:9'),
      format_en: detail.format_en || (orientation === 'vertical' ? 'Vertical video · 9:16' : 'Horizontal video · 16:9'),
      format_kz: detail.format_kz || (orientation === 'vertical' ? 'Тік бейне · 9:16' : 'Көлденең бейне · 16:9'),
      body_ru: detail.body_ru || 'Монтаж ролика, саунд-дизайн и визуальное оформление.',
      body_en: detail.body_en || 'Video assembly, sound design, and visual polish.',
      body_kz: detail.body_kz || 'Бейне монтажы, саунд-дизайн және визуалды көркемдеу.'
    };

    projects.push(project);
  }

  await writeFile(projectsFilePath, JSON.stringify(projects, null, 2), 'utf-8');
  console.log(`[fetch-video-meta] Successfully saved ${projects.length} projects to ${projectsFilePath}`);
  return projects;
}

// Execute directly if run as CLI script
fetchAllVideoMetadata().catch((err) => {
  console.error('[fetch-video-meta] Fatal error:', err);
  process.exit(1);
});
