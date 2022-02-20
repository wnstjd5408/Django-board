from django.shortcuts import render
from django.views.generic import *
from .models import Place, Location
from django.db.models import Max
# Create your views here.
from django.views.generic.list import MultipleObjectMixin
import random


class LocationListView(ListView):
    template_name = 'place/locationlist.html'
    context_object_name = 'locationlist'
    model = Location

    def get_queryset(self):
        return Location.objects.order_by('id')

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        max_id = Place.objects.all().aggregate(max_id=Max('id'))['max_id']
        while True:
            pk = random.randint(1, max_id)
            place = Place.objects.filter(pk=pk).first()
            if place:
                context['random'] = place
                break
        return context


class LocationDetailView(MultipleObjectMixin, DetailView):
    template_name = 'place/placelist.html'
    context_object_name = 'placelist'

    model = Location
    paginate_by = 12  # 12개씩 리스트에 표시
    # def get_queryset(self):
    #     return Location.objects.order_by('id')

    def get_context_data(self,  ** kwargs):
        object_list = Place.objects.filter(location=self.get_object())

        context = super().get_context_data(object_list=object_list, ** kwargs)
        max_id = Place.objects.all().aggregate(max_id=Max('id'))['max_id']
        while True:
            pk = random.randint(1, max_id)
            place = Place.objects.filter(
                pk=pk, location=self.get_object()).first()
            if place:
                context['random'] = place
                break
        context['location'] = Location.objects.filter(
            id=self.kwargs['pk'])
        return context
        # context = super(LocationDetailView, self).get_context_data(**kwargs)
        # context['list'] = Place.objects.filter(location=self.kwargs['pk'])
        # return context


class PlaceDetailView(DetailView):
    model = Place
    template_name = 'place/placedetail.html'
    context_objcet_name = 'place'
