from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='home'),  # Index page URL
    path('', views.ArticleList.as_view(), name='home'), # Home page URL
    path('articles/<slug:slug>/', views.article_detail, name='article_detail'), # URL to opening article 
    path('search/', views.search_view, name='search'),  # New URL pattern for search
]