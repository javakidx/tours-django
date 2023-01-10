from django.urls import path
from tours_app import views

#   TEMPLATE TAGGING
app_name = 'tours_app'

urlpatterns = [
    path('', views.include_index, name='index'),
    # path('help', views.help, name='help')
    path('relative', views.relative, name='relative'),
    path('other', views.other, name='other')
]
