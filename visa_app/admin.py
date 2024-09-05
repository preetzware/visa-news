from django.contrib import admin
from .models import Article, Comment, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.
admin.site.register(Category)
admin.site.register(Comment)

