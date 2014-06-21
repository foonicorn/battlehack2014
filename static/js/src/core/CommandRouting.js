define(function(require) {

	var
		$ = require('jquery'),
		BaseCommand = require('core/Command')
	;

	function Command() {}

	$.extend(Command.prototype, new BaseCommand(), {

		execute: function() {
			// Call super:
			BaseCommand.prototype.execute.apply(this, arguments);

			// Cleanup old views from content region:
			var contentView = this.context.getObject('views:content');
			contentView.clean();
		}

	});

	return Command;

});
