from django.urls import path
from . import views
from .views import VisanewsList, visanews_detail, like_article, comment_edit, comment_delete

urlpatterns = [
    path('visanews/', views.VisanewsList.as_view(), name='visanews_list'),
    path('visanews/articles/<slug:slug>/', views.visanews_detail, name='visanews_detail'),  # Adjusted to include 'articles/'
    path('visanews/search/', views.visanews_search_view, name='visanews_search'),
    path('visanews/like_article/<int:article_id>/', views.like_article, name='like_article'),
    path('visanews/<slug:slug>/edit_comment/<int:comment_id>/', comment_edit, name='comment_edit'),
    path('visanews/<slug:slug>/delete_comment/<int:comment_id>/', comment_delete, name='comment_delete'),
]
