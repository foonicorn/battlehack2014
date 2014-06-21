define(function(require) {
	var
		$ = require('jquery'),
		Model = require('application/challenge/models/Challenge'),
		View = require('application/create/views/Create')
		Command = function() {}
	;

	$.extend(Command.prototype, {

		execute: function() {
			var
				model = new Model(),
				view = new View({
					el: $('.content'),
					model: model
				});
			;

			this.context.contentView.renderView(view);
		}

	});

	return Command;
});
