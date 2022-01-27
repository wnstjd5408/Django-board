from numpy import source
from rest_framework import serializers
from .models import *
from common.serializers import UserSerializer


class BoardSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Board
        # Board 작성 시 User와 연결되게끔 -> Board를 작성하는 BoardSerializer에 담아둘것
        # source를 통해 field에 채울 내용 정함
        author = serializers.ReadOnlyField(source='user.name')
        fields = (
            'id',
            'author',
            'title',
            'ip',
            'comment',
        )
