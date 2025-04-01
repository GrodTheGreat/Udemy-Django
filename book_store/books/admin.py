from django.contrib import admin

from .models import Book


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "author")
    list_filter = ("rating", "author")


admin.site.register(model_or_iterable=Book, admin_class=BookAdmin)
