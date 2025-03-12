from django.contrib import admin

from article.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'author'
    ]
    list_filter = [
        'title',
        'author'
    ]
    list_per_page = 10

