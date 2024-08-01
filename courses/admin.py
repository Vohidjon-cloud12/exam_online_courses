from django.contrib import admin

from courses.models import Course, Category, Video


@admin.register(Category)
class CategoryAdminModel(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(Course)
class CourseAdminModel(admin.ModelAdmin):
    list_display = ('title', 'number_of_students', 'price')
    search_fields = ('title', 'courses')
    list_filter = ('price',)


@admin.register(Video)
class VideoAdminModel(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title']
