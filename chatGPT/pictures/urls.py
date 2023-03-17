from django.urls import path, include
from .views import picture_view, picture_view_list

app_name = 'pictures'

urlpatterns = [
    path('', view=picture_view, name='index'),
    path('list/', view=picture_view_list, name='list'),
]
