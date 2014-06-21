define(function(require) {
	var
		$ = require('jquery'),
		Backbone = require('backbone'),
		Geppetto = require('geppetto'),
		Router = require('application/Router'),
		ContentView = require('application/content/views/Content'),

		InitChallengeCommand = require('application/challenge/commands/Init')
	;

	return Geppetto.Context.extend({
		initialize: function () {
			var
				router = new Router(),
				contentView
			;

			if (!window.battlehack ||
				!window.battlehack.settings ||
				!window.battlehack.settings.authenticated) {
				// Stop to init aplication cause somthing is not ready...
				return;
			}

			// Base setup:
			contentView = new ContentView({
				el: $('.content'),
				context: this
			}).render();

			this.wireCommands({'application:start': [
				InitChallengeCommand
			]});

			// Setup routes:
			this._setupIndex(router, this);
			this._setupChallenge(router, this);

			// Start:
			this.wireValue('views:content', contentView);
			this.wireValue('router', router);
			this.vent.trigger('application:start');
			Backbone.history.start();

			//@ToDo: Remove this:
			window.battlehack.context = this;
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
