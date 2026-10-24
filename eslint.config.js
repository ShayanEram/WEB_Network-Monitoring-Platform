import globals from 'globals';

export default [
  {
    languageOptions: {
      ecmaVersion: 'latest',
      sourceType: 'module',
      globals: {
        ...globals.browser, // Allows window, document, fetch, etc.
        ...globals.jquery,  // Allows $ symbol if you use jQuery templates
      },
    },
    rules: {
      'no-unused-vars': 'warn',
      'no-undef': 'error',
      'no-console': 'off', // Keeps console.log available for easy UI debugging
    },
  },
];
