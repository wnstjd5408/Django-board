from django.shortcuts import render
from django.views.generic import *
from .models import Place, Location
# Create your views here.


class LocationListView(ListView):
    template_name = 'place/locationlist.html'
    context_object_name = 'locationlist'
    model = Location

    def get_queryset(self):
        return Location.objects.order_by('id')


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
