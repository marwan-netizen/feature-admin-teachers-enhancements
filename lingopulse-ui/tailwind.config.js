/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        indigo: {
          950: '#0a0a2e',
          900: '#11114d',
        },
        cyan: {
          400: '#22d3ee',
          500: '#06b6d4',
        }
      },
    },
  },
  plugins: [],
}
