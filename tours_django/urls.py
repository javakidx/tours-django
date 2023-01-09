"""tours_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from tours_app import views
from django.urls import include

urlpatterns = [
    path(r'', views.index, name='index'),
    path('tours_app/', include('tours_app.urls')),
    path('app-two', views.app_two),
    path('admin/', admin.site.urls),
    path('help', views.help),
    path('users', views.user_page),
    path('formpage', views.form_name_view, name='form_name')
]
