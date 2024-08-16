from django.contrib import admin

from app.models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", 'category', 'published_at')
    search_fields = 'title',
    list_filter = 'title',


class CategoryAdmin(admin.ModelAdmin):
    list_display = "name",
    search_fields = 'name',
    list_filter = 'name',


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
