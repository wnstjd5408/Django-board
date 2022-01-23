from django.shortcuts import render
from django.views.generic import *
from .models import Place
# Create your views here.


class PlaceListView(ListView):
    template_name = 'place/placelist.html'
    context_object_name = 'placelist'
    model = Place
    paginate_by = 10  # 10개씩 리스트에 표시

    def get_queryset(self):
        return Place.objects.order_by('-id')
