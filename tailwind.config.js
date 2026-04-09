import defaultTheme from 'tailwindcss/defaultTheme';
import forms from '@tailwindcss/forms';

/** @type {import('tailwindcss').Config} */
export default {
    content: [
        './vendor/laravel/framework/src/Illuminate/Pagination/resources/views/*.blade.php',
        './storage/framework/views/*.php',
        './resources/views/**/*.blade.php',
    ],

    theme: {
        extend: {
            fontFamily: {
                sans: ['Jost', ...defaultTheme.fontFamily.sans],
                serif: ['Bodoni Moda', ...defaultTheme.fontFamily.serif],
            },
            colors: {
                'havva-pink': {
                    50: '#F7EFF2',   /* Pearly Pink Header/Footer */
                    100: '#FDEEF4',
                    500: '#D3A2BE',  /* Orchid Pink CTA */
                    600: '#E11D74',  /* Bright Pink Hero Button */
                },
                'havva-gold': {
                    50: '#FEFCE8',
                    100: '#FEF9C3',
                    200: '#FEF08A',
                    300: '#FDE047',
                    400: '#FACC15',
                    500: '#EAB308',
                    600: '#CA8A04', /* Primary CTA */
                    700: '#A16207',
                    800: '#854D0E',
                    900: '#713F12',
                },
                'havva-stone': {
                    50: '#FAFAF9',
                    100: '#F5F5F4',
                    200: '#E7E5E4',
                    300: '#D6D3D1',
                    400: '#A8A29E',
                    500: '#78716C',
                    600: '#57534E',
                    700: '#44403C',
                    800: '#292524',
                    900: '#1C1917',
                },
            }
        },
    },

    plugins: [forms],
};
