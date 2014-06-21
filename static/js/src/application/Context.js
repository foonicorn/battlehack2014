define(function(require) {
	var
		Backbone = require('backbone'),
		Geppetto = require('geppetto'),
		Router = require('application/Router'),
		ContentView = require('application/content/views/Content')

		// InitChallengeCommand = require('application/challenge/commands/InitCommand')
	;

	return Geppetto.Context.extend({
		initialize: function () {
			var
				router = new Router(),
				contentView = new ContentView({
					el: $('body'),
					context: this
				}).render();
			;

			// Base setup:
			// this.wireCommands({'application:start': [
			// 	InitChallengeCommand
			// ]});

			// Setup routes:
			this._setupIndex(router, this);
			this._setupChallenge(router, this);

			// Start:
			this.wireValue('router', router);
			this.vent.trigger('application:init');
			Backbone.history.start();
		},

		_setupIndex: function(router, context) {
			// Wire commands:
			this.wireCommands({'index:init': []});

			// Setup route:
			router.route('*index', 'index', function() {
				context.vent.trigger('index:init');
			});
		},

		_setupChallenge: function(router, context) {
			// Wire commands:
			this.wireCommands({'challenge:init': []});

			// Setup route:
			router.route('challenge/:id', 'challenge', function(id) {
				context.vent.trigger('challenge:start', {id: id});
			});
		}
	});
});
