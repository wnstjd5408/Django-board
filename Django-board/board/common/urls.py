

from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'common'


user_list = UserViewSet.as_view({
    'get': 'list'
})


user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    # path('join/', views.UserCreateView.as_view(), name='join'),
    # path('login/', auth_views.LoginView.as_view(template_name='common/login1.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('<int:pk>/', views.UserDetailView.as_view(), name='info'),
    # path('<int:pk>/update', views.UserUpdateView.as_view(), name='update'),
    # path('<int:pk>/delete', views.UserDeleteView.as_view(), name='delete'),
    # path('<int:pk>/change-password/',
    #      views.UserPasswordChangeview.as_view(), name="change-password"),
    path('users/', user_list, name='userlist'),
    path('users/<int:pk>', user_detail, name="userdetail")
]
urlpatterns = format_suffix_patterns(urlpatterns)
