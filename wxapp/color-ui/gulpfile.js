const gulp = require('gulp');
const del = require('del');
const jsonminify = require('gulp-jsonminify');
const path = require('path');

const distPath = path.resolve(__dirname, './dist');
const examplePath = path.resolve(__dirname, './examples/dist');
const srcPrefix = path.resolve(__dirname, './src');

const isProd = process.env.NODE_ENV === 'production' || false; // 'development'

// gulp.task('clean', () => {
//     return del([`${distPath}/**/*`])
// });

gulp.task('clean', () => {
    return del(['./dist/**/*'])
});

// gulp.task('json', () => {
//     return gulp.src(`${srcPrefix}/**/*.json`).pipe(isProd ? jsonminify() : through.obj()).pipe(gulp.dest(dist))
// });
//
// gulp.task('wxml', () => {
//     return gulp
//         .src(`${src}/**/*.wxml`)
//         .pipe(gulp.dest(dist))
// })
// gulp.task('wxs', () => {
//     return gulp.src(`${src}/**/*.wxs`).pipe(gulp.dest(dist))
// })
//
// gulp.task('wxss', () => {
//     const combined = combiner.obj([
//         gulp.src(`${src}/**/*.{wxss,scss}`),
//         sass().on('error', sass.logError),
//         postcss([pxtorpx(), base64()]),
//         isProd
//             ? cssnano({
//                 autoprefixer: false,
//                 discardComments: {removeAll: true}
//             })
//             : through.obj(),
//         rename((path) => (path.extname = '.wxss')),
//         gulp.dest(dist)
//     ])
//
//     combined.on('error', handleError)
// })
//
// gulp.task('images', () => {
//     return gulp.src(`${src}/images/**`).pipe(gulp.dest(`${dist}/images`))
// })
//
// gulp.task('js', () => {
//     const f = filter((file) => !/(mock)/.test(file.path))
//     gulp
//         .src(`${src}/**/*.js`)
//         .pipe(isProd ? f : through.obj())
//         .pipe(
//             isProd
//                 ? jdists({
//                     trigger: 'prod'
//                 })
//                 : jdists({
//                     trigger: 'dev'
//                 })
//         )
//         .pipe(isProd ? through.obj() : sourcemaps.init())
//         .pipe(
//             babel({
//                 presets: ['env']
//             })
//         )
//         .pipe(
//             isProd
//                 ? uglify({
//                     compress: true
//                 })
//                 : through.obj()
//         )
//         .pipe(isProd ? through.obj() : sourcemaps.write('./'))
//         .pipe(gulp.dest(dist))
// })
//
// gulp.task('watch', () => {
//     ;['wxml', 'wxss', 'js', 'json', 'wxs'].forEach((v) => {
//         gulp.watch(`${src}/**/*.${v}`, [v])
//     })
//     gulp.watch(`${src}/images/**`, ['images'])
//     gulp.watch(`${src}/**/*.scss`, ['wxss'])
// })
