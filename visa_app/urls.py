from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleList.as_view(), name='home'), # Home page URL
    path('<slug:slug>/', views.article_detail, name='article_detail'), # URL to opening article 
    path('search/', views.search_view, name='search'),  # New URL pattern for search
]