"""
URL configuration for django_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
import django_sql_dashboard
from django.shortcuts import redirect


def redirect_to_admin(request):
    return redirect('/admin/')


urlpatterns = [
    path('', redirect_to_admin),  # Page d'accueil redirige vers admin
    path('admin/', admin.site.urls),
    path("dashboard/", include(django_sql_dashboard.urls)),
]
