from django.contrib import admin
from .models import Post, Category, Rating

admin.site.register(Category)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish']
    list_filter = ['status', 'created', 'publish', 'category']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['publish']


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['post', 'user', 'rating', 'publish']
    list_filter = ['post', 'user', 'rating']