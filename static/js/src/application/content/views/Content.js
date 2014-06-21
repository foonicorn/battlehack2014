define(function(require) {

	var
		_ = require('underscore'),
		Backbone = require('backbone'),
		View = require('core/View'),
		Template = require('text!application/content/views/Content.html')
	;

	return View.extend({

		_template: _.template(Template),

		_init: function(options) {
			this._views = [];
		},

		render: function() {
			this._content = $(this._template()).appendTo(this.$el);
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
