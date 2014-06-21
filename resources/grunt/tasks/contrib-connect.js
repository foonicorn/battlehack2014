var
	configuration = require('../configuration')
;

module.exports = function(grunt) {

	grunt.config('connect', {
		all: {
			options: {
				port: 9000,
				keepalive: true
			}
		}
	});

	grunt.loadNpmTasks('grunt-contrib-connect');
};
