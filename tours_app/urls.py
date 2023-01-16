from django.urls import path
from tours_app import views

#   TEMPLATE TAGGING
app_name = 'tours_app'

urlpatterns = [
    path('', views.include_index, name='index'),
    # path('help', views.help, name='help')
    path('relative', views.relative, name='relative'),
    path('other', views.other, name='other'),
    path('school_list', views.SchoolListView.as_view(), name='school_list'),
    path('school_detail/<pk>', views.SchoolDetailView.as_view(), name="school_detail"),
    path('school/create', views.SchoolCreateView.as_view(), name='school_create'),
    path('school/update/<pk>', views.SchoolUpdateView.as_view(), name='school_update'),
    path('school/delete/<pk>', views.SchoolDeleteView.as_view(), name='school_delete'),
]
