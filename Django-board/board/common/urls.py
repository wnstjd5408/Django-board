

from django.urls import path, reverse_lazy, include
from django.contrib.auth import views as auth_views
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns
from rest_auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from .views import *
app_name = 'common'


# user_list = UserViewSet.as_view({
#     'get': 'list'
# })


# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })

urlpatterns = [
    # path('join/', views.UserCreateView.as_view(), name='join'),
    # path('login/', auth_views.LoginView.as_view(template_name='common/login1.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('<int:pk>/', views.UserDetailView.as_view(), name='info'),
    # path('<int:pk>/update', views.UserUpdateView.as_view(), name='update'),
    # path('<int:pk>/delete', views.UserDeleteView.as_view(), name='delete'),
    # path('<int:pk>/change-password/',
    #      views.UserPasswordChangeview.as_view(), name="change-password"),
    # path('rest-auth/login/', LoginView.as_view(), name="userlogin"),
    path('login', Login.as_view()),
    path('signup/', UserCreate.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
