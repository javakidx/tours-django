from django.urls import path
from tours_app import views

urlpatterns = [
    path('', views.index, name='index')
]
