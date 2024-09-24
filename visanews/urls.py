from django.urls import path
from . import views
from .views import VisanewsList, visanews_detail, like_article, comment_edit, comment_delete

urlpatterns = [
    path('visanews/', views.VisanewsList.as_view(), name='visanews_list'),
    path('<slug:slug>/', views.visanews_detail, name='visanews_detail'),
    path('visanews/search/', views.visanews_search_view, name='visanews_search'),  # New URL pattern for search in visanews
    path('like_article/<int:article_id>/', views.like_article, name='like_article'),  # Like article URL for visanews
    path('<slug:slug>/edit_comment/<int:comment_id>/', comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>/', comment_delete, name='comment_delete'),
]
