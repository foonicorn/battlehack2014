var
	configuration = require('../configuration')
;

module.exports = function(grunt) {

	grunt.config('watch', {
		files: [
			configuration.js.sources,
			configuration.sass.sources
		],
		tasks: ['validate'],
	});

	grunt.loadNpmTasks('grunt-contrib-watch');
};
