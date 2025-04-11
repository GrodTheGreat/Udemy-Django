from django.contrib import admin

from . import models


class MeetupAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "location")
    list_filter = ("location", "date")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(model_or_iterable=models.Meetup, admin_class=MeetupAdmin)
admin.site.register(model_or_iterable=models.Location)
admin.site.register(model_or_iterable=models.Participant)
