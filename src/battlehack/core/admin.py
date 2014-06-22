from django.contrib import admin

from . import models


class CharityAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Charity, CharityAdmin)


class AttendeeInline(admin.StackedInline):
    model = models.Attendee
    extra = 0
    readonly_fields = ('uuid', 'type', 'email', 'user', 'payment_status')

    def payment_status(self, obj):
        if obj.payment:
            return obj.payment.status
        return 'missing'
    payment_status.short_description = 'payment status'


class ChallengeAdmin(admin.ModelAdmin):
    inlines = (AttendeeInline,)
    list_display = ('title', 'charity', 'amount')

admin.site.register(models.Challenge, ChallengeAdmin)


class AttendeeAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid', 'type')
    list_display = ('__unicode__', 'type', 'user', 'email', 'status')

admin.site.register(models.Attendee, AttendeeAdmin)
