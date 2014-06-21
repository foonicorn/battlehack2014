define(function(require) {

	var
		_ = require('underscore'),
		Backbone = require('backbone'),
		View = require('core/View')
	;

	return View.extend({

		_init: function(options) {
			this._views = [];
		},

		render: function() {
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
				view.destroy();
			});
		}
	});
});
