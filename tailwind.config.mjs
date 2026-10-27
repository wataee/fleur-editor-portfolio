/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        bg: '#FBFCFD',
        surface: '#F2F5F8',
        'surface-raised': '#E9EEF4',
        line: '#7E8C9E',
        hairline: '#E3E9F0',
        text: '#0E1319',
        'text-dim': '#4A5566',
        'text-mute': '#5C6878',
        accent: '#0B62D6',
        'accent-warm': '#9A6212',
        live: '#1B7A4F',
        danger: '#B3261E',
      },
      fontFamily: {
        display: ['Onest', 'system-ui', 'sans-serif'],
        body: ['Onest', 'system-ui', 'sans-serif'],
        mono: ['"JetBrains Mono"', 'ui-monospace', 'monospace'],
      },
      borderRadius: {
        sm: '8px',
        md: '12px',
        pill: '999px',
      },
      boxShadow: {
        header: '0 1px 2px rgba(14,19,25,.06), 0 10px 28px -6px rgba(14,19,25,.1)',
        glow: '0 8px 20px -8px rgba(11,98,214,.22)',
        'glow-hover': '0 16px 32px -10px rgba(11,98,214,.22)',
      },
      maxWidth: {
        container: '1200px',
      }
    },
  },
  plugins: [],
};
