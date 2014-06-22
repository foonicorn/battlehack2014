from django.contrib import admin
from django.utils.html import format_html

from . import models


class PaymentAdmin(admin.ModelAdmin):
    readonly_fields = ('pid', 'create_link')
    list_display = ('attendee', 'status', 'pid')

    def create_link(self, obj):
        if obj.status == models.STATUS_INITIATED:
            return format_html(
                '<a href="{0}">create</a>',
                obj.get_create_url())
        return 'already created'
    create_link.short_description = 'create link'
    create_link.allow_tags = True

admin.site.register(models.Payment, PaymentAdmin)
