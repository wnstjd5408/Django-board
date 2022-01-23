from django import views
from django.urls import path
from .views import *


app_name = 'place'

urlpatterns = [
    path('', PlaceListView.as_view(), name='index'),



]
