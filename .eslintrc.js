module.exports = {
  "parser": "babel-eslint",
  "env": {
    "browser": true,
    "node": true
  },
  "extends": [
    "airbnb",
    'plugin:react/all',
  ],
  "rules": {
    "react/require-optimization": [0],
    "react/prefer-stateless-function": [0],

    'import/no-extraneous-dependencies': ['error', { devDependencies: true }],
    'react/jsx-filename-extension': [2, { extensions: ['.js'] }],
    'import/extensions': [
      'error',
      'always', {
        js: 'never',
        jsx: 'never',
        json: 'never',
        coffee: 'never',
      },
    ],
    'no-underscore-dangle': 0,
    "indent": ["error", 2],
    "linebreak-style": [
      "error",
      "unix"
    ],
    'react/jsx-max-depth': 0,
    'react/jsx-no-literals': 0,
    // this is annoying and broken
    'react/jsx-one-expression-per-line': 0,
    // this is annoying too
    'react/jsx-child-element-spacing': 0,
    // sort props in abc order
    'react/jsx-sort-props': [
      'error', {
        reservedFirst: false,
        ignoreCase: true,
      },
    ],

    'react/no-set-state': [0],
    "react/destructuring-assignment": [0, "always"],
  }
}
