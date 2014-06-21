require(['_configuration'], function(configuration) {
	require.config(configuration);

	require([
		'core/Application',
		'application/Context',
		// Bootstrap-Stuff
		'bootstrapCollapse',
		'bootstrapModal'
	], function(Application, Context) {
		var app = new Application(Context);
		app.start();
	});
});
