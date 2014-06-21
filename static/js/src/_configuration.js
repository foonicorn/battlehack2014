/* This is a requirejs configuration file which is loaded by requirejs in the
/* browser or by gruntjs to define the build & validation task.
/*
/* Defines a module that works in Node and AMD.
/* Taken from https://github.com/umdjs/umd/blob/master/nodeAdapter.js */

// Help Node out by setting up define:
if (typeof module === 'object' && typeof define !== 'function') {
	var define = function (factory) {
		module.exports = factory();
	};
}

define(function () {
	return {
		paths: {
			jquery: '../libs/jquery/jquery',
			underscore: '../libs/underscore/underscore',
			backbone: '../libs/backbone/backbone',
			marionette: '../libs/backbone/backbone.marionette',
			geppetto: '../libs/backbone/backbone.geppetto',
			text: '../libs/require/require.text',
			bootstrapCollapse: '../libs/bootstrap/collapse'
		},

		shim: {
			jquery: {
				deps: [],
				exports: '$'
			},
			underscore: {
				deps: [],
				exports: '_'
			},
			backbone: {
				deps: ['underscore', 'jquery'],
				exports: 'Backbone'
			},
			marionette: {
				deps: ['backbone'],
				exports: 'Backbone.Marionette'
			},
			geppetto: {
				deps: ['marionette'],
				exports: 'Backbone.Geppetto'
			},
			bootstrapCollapse: {
				deps: ['jquery']
			}
		}
	};
});
