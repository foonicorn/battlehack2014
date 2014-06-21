var
	merge = require('merge'),
	configuration = require('../configuration')
;

module.exports = function(grunt) {
	grunt.config('requirejs', {
		build: {
			options: merge(
				{
					baseUrl: '.',
					appDir: configuration.js.sourceDir, /* source dir */
					dir: configuration.js.buildDir, /* output dir */
					modules: [{name: 'application'}],
					almond: true, /* simple AMD loader for build files */
					findNestedDependencies: true, /* allows nested require()-calls which is needed to build with shared requirejs config */
					wrap: true, /* to use with the almond option */
					preserveLicenseComments: false,
					logLevel: 1,
					optimize: 'none'
				},
				require('../../../' + configuration.js.requirejsConfig) /* require the basic configuration */
			)
		}
	});

	grunt.loadNpmTasks('grunt-requirejs');
};
