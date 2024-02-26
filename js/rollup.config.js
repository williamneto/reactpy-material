import nodeResolve from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';
import babel from '@rollup/plugin-babel';
import replace from '@rollup/plugin-replace';

export default {
  input: "src/index.js",
  output: {
    file: "../reactpy_material/bundle.js",
    format: "esm",
  },
  plugins: [
    nodeResolve({
      extensions: ['.js', '.jsx']
   }),
   babel({
      babelHelpers: 'bundled',
      presets: ['@babel/preset-react'],
      extensions: ['.js', '.jsx']
   }),
   commonjs(),
   replace({
      preventAssignment: false,
      'process.env.NODE_ENV': '"development"'
   })
  ],
  onwarn: function (warning) {
    if (warning.code === "THIS_IS_UNDEFINED") {
      // skip warning where `this` is undefined at the top level of a module
      return;
    }
    else if (warning.code === "MODULE_LEVEL_DIRECTIVE") {
      return;
    }
    console.warn(warning.message);
  },
};
