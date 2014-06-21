define(function(require) {
	var
		// $ = require('jquery'),
		// _ = require('underscore'),
		Backbone = require('backbone')
	;

	return Backbone.Model.extend({
		defaults: {
			owner: -1,
			title: 'My challenge',
			description: 'In this challenge I bet...',
			charity: -1,
			amount: 1
		}
	});
});
