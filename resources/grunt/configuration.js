var
	jsGruntfile = 'Gruntfile',
	jsGrunttasks = 'resources/grunt/**/*.js',
	jsSource = 'static/js/src/',
	jsSources = jsSource + '**/*.js',
	jsTemplates = 'static/js/src/**/*.html',
	jsBuild = 'static/js/build/',
	jsRequireConfig = 'static/js/src/_configuration.js',

	sassSources = 'static/scss/**/*.scss',

	djangoTemplates = 'templates/**/*.html'
;

module.exports = {
	js: {
		gruntfile: jsGruntfile,
		grunttasks: jsGrunttasks,
		sourceDir: jsSource,
		sources: jsSources,
		buildDir: jsBuild,
		templates: jsTemplates,
		requirejsConfig: jsRequireConfig
	},

	sass: {
		sources: sassSources
	},

	django: {
		templates: djangoTemplates
	}
};
