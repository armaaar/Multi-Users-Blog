module.exports = function(grunt) {

    // 1. All configuration goes here
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        sass: {
          options: {
              sourcemap: 'none',
              update : true,
          },
          dist: {
            files: [{
              expand: true,
              cwd: 'styles/src_sass',
              src: ['*.scss', '*.sass'],
              dest: 'styles/sass_to_css',
              ext: '.css'
            }]
          }
        },

        autoprefixer: {
            dist: {
                files: [{
                  expand: true,
                  cwd: 'styles/sass_to_css',
                  src: '*.css',
                  dest: 'styles/sass_to_css'
                },
                {
                  expand: true,
                  cwd: 'styles/src_css',
                  src: '*.css',
                  dest: 'styles/src_css'
                }]
            }
        },

        cssmin: {
            options: {
                keepSpecialComments: 0
            },
            combine : {
                files: {
                    'styles/global.min.css': ['styles/src_css/*.css', 'styles/sass_to_css/*.css']
                },
            },
        },

        // JS
        uglify: {
            options: {
              mangle: false
            },
            my_target: {
              files: {
                'scripts/global.min.js': ['scripts/src_js/*.js']
              }
            }
        },


        responsive_images: {
          dev: {
            options: {
              engine: 'gm',
              sizes: [
                {
                  width: 1300,
                  name: 'lg',
                  quality: 30
                },
                {
                  width: 800,
                  name: 'md',
                  quality: 30
                },
                {
                  width: 500,
                  name: 'sm',
                  quality: 30
                },
                {
                  width: 350,
                  name: 'xs',
                  quality: 30
                },
              ]
            },

            files: [{
              expand: true,
              src: ['*.{gif,jpg,png}'],
              cwd: 'imgs/imgs_src',
              dest: 'imgs/'
            }]
          }
        },

        watch: {
          styles: {
            files: ['styles/src_css/*.css', 'styles/src_sass/*.{sass,scss}'],
            tasks: ['sass', 'autoprefixer', 'cssmin'],
            options: {
              spawn: false,
            },
          },

          scripts: {
            files: ['scripts/src_js/*.js',],
            tasks: ['uglify'],
            options: {
              spawn: false,
            },
          },

          images: {
            files: ['imgs/imgs_src/*.{gif,jpg,jpeg,png}'],
            tasks: ['responsive_images'],
            options: {
              spawn: false,
            },
          }

        },

    });

    // 3. Where we tell Grunt we plan to use this plug-in.
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-autoprefixer');
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.loadNpmTasks('grunt-contrib-uglify');

    grunt.loadNpmTasks('grunt-responsive-images');

    grunt.loadNpmTasks('grunt-contrib-watch');

    // 4. Where we tell Grunt what to do when we type "grunt" into the terminal.
    grunt.registerTask('default', ['watch']);

};
