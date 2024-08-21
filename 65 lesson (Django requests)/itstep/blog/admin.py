from django.contrib import admin
from .models import Post, Category, Tag

admin.site.register(Category)
admin.site.register(Tag)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish']
    list_filter = ['status', 'created', 'publish', 'category']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['publish']
