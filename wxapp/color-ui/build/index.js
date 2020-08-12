const {
    buildWxss,
    buildWxml,
    buildImage,
    buildJson,
    buildJs,
    copyStatic,
    clean,
    copy
} = require('./task');
const del = require('del');
const path = require('path');
const {
    series,
    parallel,
    watch
} = require('gulp');

// const distPath = path.resolve(__dirname, '../dist');
const distPath = '../dist';
// const examplePath = path.resolve(__dirname, '../examples/dist');
const examplePath = '../examples/dist';
// const srcPrefix = path.resolve(__dirname, '../src');
const srcPrefix = '../src';
const srcDevPath = `${srcPrefix}/**`;

module.exports = {
    build: series(
        clean(`${distPath}/**/*`),
        parallel(
            buildWxss(
                `${srcDevPath}/*.less`,
                distPath
            ),
            buildWxml(
                `${srcDevPath}/*.wxml`,
                distPath
            ),
            buildImage(
                `${srcDevPath}/*.png`,
                distPath
            ),
            buildJson(
                `${srcDevPath}/*.json`,
                distPath
            ),
            buildJs(
                `${srcDevPath}/*.js`,
                distPath
            ),
            copyStatic(
                srcDevPath,
                distPath
            )
        )
    ),
    dev: series(
        clean(`${examplePath}/**/*`),
        parallel(
            buildWxss(
                `${srcDevPath}/*.less`,
                examplePath
            ),
            copyStatic(
                srcDevPath,
                examplePath,
                'dev'
            )
        )
    ),
    watch: parallel(
        () => {
            watch('../src/**/*.less', buildWxss(`${srcDevPath}/*.less`, examplePath));
            watch('../src/**/*.wxml', copy(srcDevPath, examplePath, 'wxml'));
            watch('../src/**/*.wxs', copy(srcDevPath, examplePath, 'wxs'));
            watch('../src/**/*.json', copy(srcDevPath, examplePath, 'json'));
            watch('../src/**/*.js', copy(srcDevPath, examplePath, 'js'));
        }
    )
};