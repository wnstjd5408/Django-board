from django.views.generic import *
from .models import Place, Location
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import LocationSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# DRF API view => 두 종류의 wrapper 선택가능
# 1. 함숭형 : @api_view 데코레이터 사용
# 2. 클래스형 : APIView 클래스 상속
class LocationListView(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

# class LocationListView(ListView):
#     template_name = 'place/locationlist.html'
#     context_object_name = 'locationlist'
#     model = Location

#     def get_queryset(self):
#         return Location.objects.order_by('id')


class PlaceListView(DetailView):
    template_name = 'place/placelist.html'
    context_object_name = 'placelist'
    model = Place
    # paginate_by = 10  # 10개씩 리스트에 표시

    def get_queryset(self):
        return Place.objects.order_by('id')

    def get_context_data(self, **kwargs):
        context = super(PlaceListView, self).get_context_data(**kwargs)
        context['list'] = Place.objects.filter(location=self.kwargs['pk'])
        return context


class PlaceDetailView(DetailView):
    model = Place
    template_name = 'place/placedetail.html'
    context_objcet_name = 'place'
