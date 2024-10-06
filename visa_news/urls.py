"""
URL configuration for visa_news project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import handler404 as custom_404, handler500 as custom_500, handler403 as custom_403
from .views import trigger_500_error, trigger_403_error

urlpatterns = [
    path('', include('visa_app.urls'), name="visa_app-urls"),
    path("accounts/", include("allauth.urls")), 
    path('visanews/', include('visanews.urls')),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    # URLs to trigger errors
    path('trigger-500/', trigger_500_error, name='trigger-500'),
    path('trigger-403/', trigger_403_error, name='trigger-403'),
]

# Point to the custom error handlers
handler403 = custom_403
handler404 = custom_404
handler500 = custom_500
