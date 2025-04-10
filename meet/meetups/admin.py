from django.contrib import admin

from . import models


class MeetupAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    list_filter = ("title",)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(model_or_iterable=models.Meetup, admin_class=MeetupAdmin)
