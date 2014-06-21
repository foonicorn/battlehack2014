from django.contrib import admin

from . import models


class PaymentAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Payment, PaymentAdmin)
