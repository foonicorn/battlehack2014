from django.contrib import admin

from . import models


class CharityAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Charity, CharityAdmin)


class ChallengeAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Challenge, ChallengeAdmin)
