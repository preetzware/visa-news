from django.urls import path
from . import views
from .views import VisanewsList, visanews_detail, like_article

urlpatterns = [
    path('visanews/', views.VisanewsList.as_view(), name='visanews_list'),
    path('articles/<slug:slug>/', views.visanews_detail, name='visanews_detail'),
    path('articles/search/', views.visanews_search_view, name='visanews_search'),
    path('like_article/<int:article_id>/', views.like_article, name='like_article'),
    path('articles/<slug:slug>/edit_comment/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('articles/<slug:slug>/delete_comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),
]
