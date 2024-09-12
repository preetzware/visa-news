from django.contrib import admin
from .models import VisanewsArticle, Category, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(VisanewsArticle)
class VisanewsArticleAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'user', 'body', 'created_on', 'approved', 'parent')
    list_filter = ('approved', 'created_on')
    search_fields = ('body', 'user__username', 'article__title')