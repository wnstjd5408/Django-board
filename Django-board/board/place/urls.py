from django import views
from django.urls import path
from .views import *


app_name = 'location'

urlpatterns = [
    path('location/<int:pk>', PlaceListView.as_view(), name='index'),
    # path('', PlaceDetailView.as_view(), name='detail'),
    path('location/', LocationListView.as_view(), name='idx')

]
