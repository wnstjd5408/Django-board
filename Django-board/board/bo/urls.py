from django.urls import path

from .import views


app_name = 'bo'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create/', views.BoardCreateView.as_view(), name='board_create'),
    path('<int:pk>/edit', views.BoardUpdateView.as_view(), name='board_edit'),
    path('<int:pk>/delete', views.BoardDeleteView.as_view(), name='board_delete')
]
