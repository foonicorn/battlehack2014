(function() {

	$('.stats').each(function() {
		new window.chacha.StatsView({
			el: $(this)
		});
	});

})();
