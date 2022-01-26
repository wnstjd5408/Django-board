from rest_framework import serializers
from .models import *
from common.serializers import UserSerializer


class LocationSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)
    class Meta:
        model = Location
        fields = (
            'id',
            'location_name',
            'count',
        )
        # read_only_fields = ('count',)
