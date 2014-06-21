define(function(require) {
	var
		$ = require('jquery'),
		_ = require('underscore'),
		View = require('core/View'),
		Marionette = require('marionette'),
		ItemTemplate = require('text!application/overview/views/OverviewItem.html'),
		Template = require('text!application/overview/views/overview.html'),
		ItemView,
		CollectionView
	;

	ItemView = Marionette.ItemView.extend({
		template: _.template(ItemTemplate),
		tagName: 'li'
	});

	CollectionView = Marionette.CollectionView.extend({
		itemView: ItemView,
	});

	return View.extend({

		_template: _.template(Template),

		render: function() {
			this._content = $(this._template()).appendTo(this.$el);
			this._view = new CollectionView({
				el: this._content,
				collection: this._options.collection
			}).render();
		},

		destroy: function() {
			this._view.remove();
		}

	});
});
