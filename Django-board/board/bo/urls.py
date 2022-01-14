from django.urls import path
from .views import *
from .import views


app_name = 'bo'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('create/', BoardCreateView.as_view(), name='board_create'),
    path('<int:pk>/edit', BoardUpdateView.as_view(), name='board_edit'),
    path('<int:pk>/delete', BoardDeleteView.as_view(), name='board_delete')
]
