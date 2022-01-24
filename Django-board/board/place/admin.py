from django.contrib import admin
from numpy import place

# Register your models here.
from .models import Place, Location
from django.utils.html import format_html


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    search_fields = ['place_name']
    list_display = ['id', 'place_name', 'image_tag']
    list_per_page = 30

    def image_tag(self, obj):
        return format_html('<img src="{}" width="50px;"/>'. format(obj.place_imageurl))
    image_tag.short_description = 'Image'


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):

    search_fiels = ['location_name']
