var
	configuration = require('../configuration')
;

module.exports = function(grunt) {
	grunt.config('scsslint', {
		all: {
			src: configuration.sass.sources,
			options: {
				config: '.scss-lint.yml'
			}
		}
	});

	grunt.loadNpmTasks('grunt-scss-lint');
};
