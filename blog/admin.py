from django.contrib import admin

from blog.models import Blog, Author, BlogImage


# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('date_added', )
    date_hierarchy = 'date_added'
    search_fields = ('title',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name',)


@admin.register(BlogImage)
class BlogImageAdmin(admin.ModelAdmin):
    list_display = ('blog_id',)
