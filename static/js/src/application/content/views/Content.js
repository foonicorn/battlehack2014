define(function(require) {

	var
		$ = require('jquery'),
		_ = require('underscore'),
		View = require('core/View')
	;

	return View.extend({

		_init: function(options) {
			this._views = [];
		},

		render: function() {
			console.log('render content view');
			return this;
		},

		renderView: function(view) {
			if (!view || !(view instanceof Backbone.View)) {
				throw new Error('Missing view instance!');
			}

			view.render();
			this._views.push(view);
		},

		clean: function() {
			_.each(this._views, function(view) {

			});
		}

	});

});
