from django.urls import path
from . import views

urlpatterns = [
    path('', views.VisanewsList.as_view(), name='visanews_list'),
    path('<slug:slug>/', views.visanews_detail, name='visanews_detail'),
    path('visanews/search/', views.visanews_search_view, name='visanews_search'),  # New URL pattern for search in visanews
    path('visanews/like_article/<int:article_id>/', views.like_article, name='visanews_like_article'),  # Like article URL for visanews
    path('visanews/dislike_article/<int:article_id>/', views.dislike_article, name='visanews_dislike_article'),
    path('visanews/articles/<slug:slug>/edit_comment/<int:comment_id>/', views.comment_edit, name='visanews_comment_edit'),  # Edit comment in visanews
    path('visanews/articles/<slug:slug>/delete_comment/<int:comment_id>/', views.comment_delete, name='visanews_comment_delete'),  # Delete comment in visanews
]
