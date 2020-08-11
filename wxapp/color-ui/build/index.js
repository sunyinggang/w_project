const {
    // buildWxss,
    // buildWxml,
    // buildImage,
    // buildJson,
    // buildJs,
    // copyStatic,
    clean
    // copy
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
const examplePath = path.resolve(__dirname, '../examples/dist');
const srcPrefix = path.resolve(__dirname, '../src');

module.exports = {
    build: series(
        clean(`${distPath}/**/*`)
    )
};