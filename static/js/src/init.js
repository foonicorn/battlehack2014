(function() {

	$('.stats').each(function() {
		new window.chacha.StatsView({
			el: $(this)
		});
	});

	$('input[type=radio]').uniform({
		radioClass: "radio"
	});

})();
