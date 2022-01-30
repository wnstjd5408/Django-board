from django import views
from django.urls import path, include
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'location'


location_list = LocationListView.as_view({
    'post': 'create',
    'get': 'list',
})

location_detail = LocationListView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


urlpatterns = format_suffix_patterns([
    # path('location/<int:pk>', PlaceListView.as_view(), name='index'),
    # path('', PlaceDetailView.as_view(), name='detail'),
    path('locations/<int:pk>/', location_detail, name="location_detail"),
    path('locations/', location_list, name='idx')

])
