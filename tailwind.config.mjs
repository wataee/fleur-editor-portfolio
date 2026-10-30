/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  darkMode: ['class', '[data-theme="dark"]'],
  theme: {
    extend: {
      colors: {
        bg: 'var(--bg)',
        surface: 'var(--surface)',
        'surface-raised': 'var(--surface-raised)',
        line: 'var(--line)',
        hairline: 'var(--hairline)',
        text: 'var(--text)',
        'text-dim': 'var(--text-dim)',
        'text-mute': 'var(--text-mute)',
        accent: 'var(--accent)',
        'accent-warm': 'var(--accent-warm)',
        live: 'var(--live)',
        danger: 'var(--danger)',
      },
      fontFamily: {
        display: ['"Unbounded"', 'Onest', 'system-ui', 'sans-serif'],
        body: ['Onest', 'system-ui', 'sans-serif'],
        mono: ['"JetBrains Mono"', 'ui-monospace', 'monospace'],
      },
      borderRadius: {
        sm: '8px',
        md: '12px',
        pill: '999px',
      },
      boxShadow: {
        header: 'var(--shadow-header)',
        glow: 'var(--shadow-glow)',
        'glow-hover': 'var(--shadow-glow-hover)',
      },
      maxWidth: {
        container: '1200px',
      }
    },
  },
  plugins: [],
};