// generated on 2016-07-12 using generator-chrome-extension 0.5.6
import gulp from 'gulp';
import gulpLoadPlugins from 'gulp-load-plugins';
import del from 'del';
import runSequence from 'run-sequence';
import {stream as wiredep} from 'wiredep';

const $ = gulpLoadPlugins();

gulp.task('extras', () => {
  return gulp.src([
    'app/*.*',
    'app/_locales/**',
    '!app/scripts.babel',
    '!app/*.json',
    '!app/*.html',
  ], {
    base: 'app',
    dot: true
  }).pipe(gulp.dest('dist'));
});

function lint(files, options) {
  return () => {
    return gulp.src(files)
      .pipe($.eslint(options))
      .pipe($.eslint.format());
  };
}

gulp.task('lint', lint('app/scripts.babel/**/*.js', {
  env: {
    es6: true
  }
}));

gulp.task('images', () => {
  return gulp.src('app/images/**/*')
    .pipe($.if($.if.isFile, $.cache($.imagemin({
      progressive: true,
      interlaced: true,
      svgoPlugins: [{cleanupIDs: false}]
    }))
    .on('error', function (err) {
      console.log(err);
      this.end();
    })))
    .pipe(gulp.dest('dist/images'));
});

gulp.task('sounds',  () => {
  return gulp.src('app/sounds/*.wav')
    .pipe(gulp.dest('dist'));
});

gulp.task('html', () => {
  return gulp.src('app/**/*.html')
    .pipe($.useref())
    .pipe($.if('*.js', $.uglify()))
    .pipe($.if('*.css', $.minifyCss()))
    .pipe(gulp.dest('dist'));
});

gulp.task('chromeManifest', () => {
  return gulp.src('app/manifest.json')
    .pipe($.chromeManifest({
      buildnumber: true,
      background: {
        target: 'assets/scripts/background.js',
        exclude: [
          'assets/scripts/chromereload.js'
        ]
      }
  }))
  .pipe($.if('*.css', $.cleanCss({compatibility: '*'})))
  .pipe($.if('*.js', $.sourcemaps.init()))
  .pipe($.if('*.js', $.uglify()))
  .pipe($.if('*.js', $.sourcemaps.write('.')))
  .pipe(gulp.dest('dist'));
});

gulp.task('styles', () => {
  return gulp.src('app/assets/styles/**/*.css')
  .pipe($.if('*.css', $.cleanCss({compatibility: '*'})))
  .pipe(gulp.dest('dist/assets/styles'));
});

gulp.task('scripts', () => {
  return gulp.src('app/assets/scripts/*.js')
  // .pipe($.if('*.js', $.uglify()))
  // .pipe($.if('*.js', $.sourcemaps.init()))
  // .pipe($.ignore.exclude('jquery.min.js'))
  // .pipe($.if('*.js', $.uglify()))
  // .pipe($.if('*.js', $.sourcemaps.write('.')))
  .pipe(gulp.dest('dist/assets/scripts'));
});

gulp.task('concats', () => {
  gulp.src([
      "app/assets/scripts/jquery.min.js",
      "app/assets/scripts/base.js",
      "app/assets/scripts/init.js",
      "app/assets/scripts/car.js",
      "app/assets/scripts/action.js",
      "app/assets/scripts/post.js"
    ])
    .pipe($.concat('contentscript.js'))
    .pipe(gulp.dest('dist/assets/scripts'));
});

gulp.task('babel', () => {
  return gulp.src('app/scripts.babel/**/*.js')
    .pipe($.babel({
      presets: ['es2015']
    }))
    .pipe(gulp.dest('app/assets/scripts'));
});

gulp.task('clean', del.bind(null, ['.tmp', 'dist']));
gulp.task('watch', ['lint', 'babel', 'html'], () => {
  $.livereload.listen();
  gulp.watch([
    'app/**/*.html',
    'app/assets/scripts/**/*.js',
    'app/assets/images/**/*',
    'app/assets/styles/**/*',
    'app/template/**/*',
    'app/_locales/**/*.json'
  ]).on('change', $.livereload.reload);

  gulp.watch('app/scripts.babel/**/*.js', ['lint', 'babel']);
  gulp.watch('bower.json', ['wiredep']);
});

gulp.task('size', () => {
  return gulp.src('dist/**/*').pipe($.size({title: 'build', gzip: true}));
});

gulp.task('wiredep', () => {
  gulp.src('app/*.html')
    .pipe(wiredep({
      ignorePath: /^(\.\.\/)*\.\./
    }))
    .pipe(gulp.dest('app'));
});

gulp.task('package', function () {
  var manifest = require('./dist/manifest.json');
  return gulp.src('dist/**')
    .pipe($.zip('caiji-' + manifest.version + '.zip'))
    .pipe(gulp.dest('package'));
});

gulp.task('build', (cb) => {
  runSequence(
    'lint', 'babel','chromeManifest',
    ['html', 'images', 'sounds', 'extras','styles','scripts'],
    'size', cb);
});

gulp.task('default', ['clean'], cb => {
  runSequence('build', cb);
});
