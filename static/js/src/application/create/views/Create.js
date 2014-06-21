define(function(require) {

	var
		Backbone = require('backbone')
	;

	return Backbone.View.extend({

		render: function() {
			console.log('render create', this._options.model);
			return this;
		}

	});

});
