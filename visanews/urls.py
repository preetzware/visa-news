from django.urls import path
from . import views

urlpatterns = [
    path('', views.VisanewsList.as_view(), name='visanews_list'),
    path('<slug:slug>/', views.visanews_detail, name='visanews_detail'),
]
