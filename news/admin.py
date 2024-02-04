from django.contrib import admin

from news.models import News, Categories


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'image', 'category')
