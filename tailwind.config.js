/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './templates/*.html', './main/templates/*.html'
  ],
  theme: {
    extend: {
      fontFamily: {
          Inter : ['Inter'],
          InterBold : ['InterBold']
      }
    },
  },
  plugins: [],
}

