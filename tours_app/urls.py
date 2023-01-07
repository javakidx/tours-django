from django.urls import path
from tours_app import views

urlpatterns = [
    path(r'', views.include_index, name='index')
]
