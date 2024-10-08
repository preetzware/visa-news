from django.urls import path
from . import views
from .views import ArticleList, article_detail, like_article, index_view, search_view


urlpatterns = [
    path('', views.index_view, name='home'),  # Index page URL
    path('search/', search_view, name='search'),
    path('', views.ArticleList.as_view(), name='home'), # Home page URL
    path('articles/<slug:slug>/', views.article_detail, name='article_detail'), # URL to opening article 
    path('like_article/<int:article_id>/', views.like_article, name='like_article'),  # Like article URL
    path('articles/<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('articles/<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
]