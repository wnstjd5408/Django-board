
from pyexpat.errors import messages
from django.http import Http404, request
from django.shortcuts import get_object_or_404
from .models import Board
# Create your views here.
from django.views import generic
from django.utils import timezone
from .forms import BoardForm
from django.urls import reverse_lazy
from hitcount.views import HitCountDetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .serializers import BoardSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics, permissions, viewsets
from rest_framework.pagination import PageNumberPagination
from common.permissions import IsUserOrReadOnly
# DRF mixins!
# APIView에서는 각 요청 method 맞게 serializer에서 직접 처리
# 그러나 자주 사용되는 기능이라 DRF에서 미리 구현 - >mixins!
# queryset과 serializer_class를 지정해주기만하면 나머지는 상속받은 Mixin과 연결해주기만 하면 됨


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 10


# class BoardViewSet(viewsets.ModelViewSet):
#     # ModelViewSet ? -> 자동적으로 list, create, 검색, update, destory를 수행

#     # 다른 기능 추가 원할 시 -> @action 데코레이터 사용

#     queryset = Board.objects.all()
#     serializer_class = BoardSerializer
#     permission_classes = [
#         permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]
#     pagination_class = StandardResultsSetPagination

#     def perform_create(self, serializer):
#         # Post 요청 - >perform_create() 오버라이딩
#         # instance save를 수정
#         serializer.save(author=self.request.user)

class BoardList(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, ]
    # 기존 permissions에 우리가 생성한 IsUserOrReadOnly도 추가

    # DRF -> 이용자 권한 설정 클래스 제공
    # 여기서는 IsAuthenticatedOrReadOnly -> authenticated는 R C 가능/ 아니면 R only
    def perform_create(self, serializer):
        # Post 요청 - >perform_create() 오버라이딩
        # instance save를 수정
        serializer.save(author=self.request.user)

# class BoardList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Board.objects.all()
#     serializer_class = BoardSerializer

#     # 요청 method 맞게 함수를 정의
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class BoardList(APIView):
#     def get(self, request, format=None):
#         board = Board.objects.all()
#         serializer = BoardSerializer(board, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = BoardSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['GET', 'POST'])
# def BoardList(request):
#     # Read
#     if request.method == 'GET':
#         board = Board.objects.all()
#         serializer = BoardSerializer(board.values(), many=True)
#         # many=True? Board.objects.all()로 검색한 객체는 list 형태!
#         # serializer는 한개의 객체만 이해할 수 있고, 리스트는 이해할 수 없다!
#         # 따라서 many=True를 추가해 중복 표현 값에 대한 list를 받게끔

#         return Response(serializer.data)
#         # Response의 정체는?
#         # -> TemplateResponse 객체의 일종으로 렌더링되지 않은 컨텐츠를 가져오고
#         # 클라이언트에게 반환할 올바른 컨텐츠 유형을 결정!
#     # create
#     elif request.method == 'POST':
#         serializer = BoardSerializer(data=request.data)
#         # request data의 정체는
#         # ->DRF가 제공! 기존의 HttpRequest를 request 객체로 확장하여, 더 유연한 요청 파싱을 제공한다고 함
#         # 즉, 핵심적인 기능을 form에서 섯던 request.POST와 유사하지만 웹 API에 더 유용한 속성입니다.

#         if serializer.is_valid():
#             # POST 요청 -> 유효성 검사는 필수다
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=404)
#         # status= 의 정체는 -> DRF가 제공하는 HTTP의 상태코드! 에러 종류에 따라 더욱 명식적인 식별자를 제공


class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]


# class BoardDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
#                   mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Board.objects.all()
#     serializer_class = BoardSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def get(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
# class BoardDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Board.objects.get(pk=pk)
#         except Board.DoesNotExist:
#             return Http404

#     def get(self, request, pk, format=None):
#         board = self.get_object(pk)
#         serializer = BoardSerializer(board)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         board = self.get_object(pk)
#         serializer = BoardSerializer(board, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         board = self.get_object(pk)
#         board.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'PUT', 'DELETE'])
# def BoardDetail(request, pk):
#     try:
#         board = Board.objects.get(pk=pk)
#     except Board.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     # 우선 pk에 해당하는 Board가 존재하는지! 없으면 404 에러를 띄워주도록

#     # Detail
#     if request.method == 'GET':
#         serializer = BoardSerializer(board)
#         return Response(serializer.data)

#     # Update
#     elif request.method == 'PUT':
#         serializer = BoardSerializer(board, data=request.data)
#         # request 요청이 들어온 그 board를 serializer 담아 가져옴

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # Delete
#     elif request.method == 'DELETE':
#         board.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
