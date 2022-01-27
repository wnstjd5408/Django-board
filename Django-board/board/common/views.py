from django.views.generic import *
from .forms import *
from rest_framework import generics, viewsets
from .serializers import *


class UserViewSet(viewsets.ReadOnlyModelViewSet):

    # ReadOnlyModelViewSet - >자동적으로 ReadOnly를 수행

    # 해당 ViewSet은 자동적으로 list와 검색 기능을 수행

    queryset = User.objects.all()
    serializer_class = UserSerializer


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
