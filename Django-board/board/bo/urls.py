from django.urls import path, include
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
app_name = 'bo'


# board_list = BoardViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# board_detail = BoardViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partail_update',
#     'delete': 'destory'
# })


urlpatterns = format_suffix_patterns([
    # path('', IndexView.as_view(), name='index'),
    # path('<int:pk>/', DetailView.as_view(), name='detail'),
    # path('create/', BoardCreateView.as_view(), name='board_create'),
    # path('<int:pk>/edit', BoardUpdateView.as_view(), name='board_edit'),
    # path('<int:pk>/delete', BoardDeleteView.as_view(), name='board_delete')
    # path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('boards/', BoardList.as_view(), name='board_list'),
    path('boards/<int:pk>/', BoardDetail.as_view(), name='board_detail'),
])
