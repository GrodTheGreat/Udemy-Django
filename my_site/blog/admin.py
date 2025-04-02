from django.contrib import admin

from .models import Author, Post, Tag


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


# Register your models here.
admin.site.register(model_or_iterable=Author)
admin.site.register(model_or_iterable=Post, admin_class=PostAdmin)
admin.site.register(model_or_iterable=Tag)
