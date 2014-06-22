(function() {

	var
		SELECTOR_DATASET = 'dl',
		SELECTOR_DATALABEL = 'dt',
		SELECTOR_DATAVALUE = 'dd',
		defaults = {
			segmentShowStroke: false,
			animateScale: true,
			colors: [
				'#CAFF00',
				'#FFF'
			]
		}
	;

	function StatsView(options) {
		this._options = $.extend({}, defaults, options);
		this._el = this._options.el;

		this._parse();
		this._render();
	}

	$.extend(StatsView.prototype, {

		_parse: function() {
			var self = this;

			this._data = [];
			this._el
				.find(SELECTOR_DATASET)
				.each(function(index, set) {
					set = $(set);
					self._data.push({
						color: self._options.colors[index],
						value: parseInt(set.find(SELECTOR_DATAVALUE).text(), 10)
					});

					$('<span />')
						.css({background: self._options.colors[index]})
						.prependTo(set.find(SELECTOR_DATALABEL));
				});
		},

		_render: function() {
			this._canvas = $('<canvas width="300" height="200" />').appendTo(this._el);
			this._ctx = this._canvas.get(0).getContext('2d');
			this._chart = new window.Chart(this._ctx).Pie(this._data, this._options);
		}

	});

	window.chacha = window.chacha || {};
	window.chacha.StatsView = StatsView;

})();
