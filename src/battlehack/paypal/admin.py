from django.contrib import admin

from . import models


class PaymentAdmin(admin.ModelAdmin):
    readonly_fields = ('pid',)

admin.site.register(models.Payment, PaymentAdmin)
