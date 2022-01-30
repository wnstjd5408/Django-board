from django import views
from django.urls import path
from .views import *


app_name = 'location'

urlpatterns = [
    path('<int:pk>', LocationDetailView.as_view(), name='index'),
    # path('', PlaceDetailView.as_view(), name='detail'),
    path('', LocationListView.as_view(), name='idx')

]
