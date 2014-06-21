define(function(require) {

	var
		// $ = require('jquery'),
		// _ = require('underscore'),
		Backbone = require('backbone')
	;

	return Backbone.View.extend({

		initialize: function(options) {
			if (!options.context) {
				throw new Error('Missing context in view options');
			}

			this._context = options.context;
			this._options = options;
			this._init.apply(this, arguments);
		},

		_init: function() {},

		render: function() {
			return this;
		}

	});

});
