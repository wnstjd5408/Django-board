from django.contrib import admin

# Register your models here.
from .models import Place


class PlaceAdmin(admin.ModelAdmin):
    search_fields = ['place_name']


admin.site.register(Place, PlaceAdmin)
