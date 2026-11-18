import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  site: 'https://fleur-editor.netlify.app',
  devToolbar: {
    enabled: false
  },
  vite: {
    server: {
      fs: {
        strict: false
      }
    }
  },
  integrations: [tailwind({ applyBaseStyles: false })],
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'ru', 'kz'],
    routing: {
      prefixDefaultLocale: false
    }
  }
});
