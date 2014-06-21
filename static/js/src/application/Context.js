define(function(require) {
	var
		Geppetto = require('geppetto')
	;

	return Geppetto.Context.extend({
		initialize: function () {
			// wire initializes commands:
			window.alert('init');
		}
	});
});
