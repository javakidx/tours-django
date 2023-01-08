from django.urls import path
from tours_app import views

urlpatterns = [
    path('', views.include_index, name='index'),
    # path('help', views.help, name='help')
]
