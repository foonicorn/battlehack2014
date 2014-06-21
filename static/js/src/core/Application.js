define(function(require) {

	var
		Marionette = require('marionette')
	;

	/* Marionette expects "template" to be the ID of a DOM element.
	 * But with RequireJS, template is actually the full text of the
	 * template. */
	Marionette.TemplateCache.prototype.loadTemplate = function(template) {

		// Make sure we have a template before trying to compile it:
		if (!template || template.length === 0){
			throw new Error('Could not find template: "' + template + '".');
		}

		return template;
	};

	return Marionette.Application.extend({
		constructor: function(Context) {
			Marionette.Application.prototype.constructor.apply(this, arguments);
			this.context = new Context(this);
		},

		start: function() {
			Marionette.Application.prototype.start.apply(this, arguments);
			this.context.dispatch('application:init');
		}
	});
});
