define(function(require) {
	var
		$ = require('jquery'),
		OverviewView = require('application/overview/views/Overview'),
		Command = function() {}
	;

	$.extend(Command.prototype, {

		execute: function() {
			var
				collection = this.context.getObject('collections:challenges')
				view = new OverviewView({
					el: $('.content'),
					collection: collection,
					context: this.context
				})
			;

			console.log('init list');
			this.context.contentView.renderView(view);
		}

	});

	return Command;
});
