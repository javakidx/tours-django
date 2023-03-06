from django.urls import path
from tours_app import views

urlpatterns = [
    path('', views.tours, name='tours'),
    path('<int:pk>', views.tours_with_id, name='tours-with-id')
]
