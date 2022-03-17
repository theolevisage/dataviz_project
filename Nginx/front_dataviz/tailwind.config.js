const colors = require('tailwindcss/colors')

module.exports = {
  purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    screens: {
      'sm': '640px',
      // => @media (min-width: 640px) { ... }

      'md': '768px',
      // => @media (min-width: 768px) { ... }

      'lg': '1024px',
      // => @media (min-width: 1024px) { ... }

      'xl': '1280px',
      // => @media (min-width: 1280px) { ... }

      '2xl': '1536px',
      // => @media (min-width: 1536px) { ... }
    },
    height: {
      10: '10%',
      20: '20%',
      30: '30%',
      40: '40%',
      50: '50%',
      60: '60%',
      70: '70%',
      80: '80%',
      90: '90%',
      'full': '100%'
    },
    extend: {
      width: {
        '1/20': '5%',
        '1/10': '10%',
        '3/20': '15%',
        '2/10': '20%',
        '5/20': '25%',
        '3/10': '30%',
        '7/20': '35%',
        '4/10': '40%',
        '9/20': '45%',
        '5/10': '50%',
        '11/20': '55%',
        '6/10': '60%',
        '13/20': '65%',
        '7/10': '70%',
        '15/20': '75%',
        '8/10': '80%',
        '17/20': '85%',
        '9/10': '90%',
        '19/20': '95%'
      }
    },
    colors: {
      white: colors.white,
      black: colors.black,
      gray: colors.blueGray,
      blue: colors.blue,
      teal: colors.teal,
      yellow: colors.yellow,
      red: colors.red,
      pink: colors.pink
    },
    opacity: {
      '0': '0',
      '10': '.1',
      '20': '.2',
      '30': '.3',
      '40': '.4',
      '50': '.5',
      '60': '.6',
      '70': '.7',
      '80': '.8',
      '90': '.9',
      '100': '1',
    }
  },
  variants: {
    extend: {},
  },
  plugins: [],
}