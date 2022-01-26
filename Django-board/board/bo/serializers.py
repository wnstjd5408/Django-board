from rest_framework import serializers
from .models import *
from common.serializers import UserSerializer


class BoardSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Board
        fields = (
            'id',
            'author',
            'title',
            'ip',
            'creation_date',
            'modified_date',
            'comment',
            'hit_count_generic',
        )

        read_only_fields = ('creation_date', 'hit_count_generic',)
