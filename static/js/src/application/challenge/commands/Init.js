define(function(require) {
	var
		$ = require('jquery'),
		ChallengeCollection = require('application/challenge/collections/Challenges'),
		Command = function() {}
	;

	$.extend(Command.prototype, {

		execute: function() {
			var collection = new ChallengeCollection({
				url: window.battlehack.settings.api.challenges
			});

			collection.fetch();

			this.context.wireValue('collections:challenges', collection);
		}

	});

	return Command;
});
