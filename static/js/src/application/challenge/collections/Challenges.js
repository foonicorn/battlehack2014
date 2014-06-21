define(function(require) {
	var
		// $ = require('jquery'),
		// _ = require('underscore'),
		Backbone = require('backbone'),
		ChallengeModel = require('application/challenge/models/Challenge')
	;

	return Backbone.Collection.extend({
		model: ChallengeModel,

		initialize: function(options) {
			this.url = options.url;
		}
	});
});
