from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_auth.registration.serializers import RegisterSerializer

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

User = get_user_model()


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", )
        password = data.get("password", None)
        user = authenticate(email=email, password=password)

        if user is None:
            return {
                'email': 'None'
            }
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'id': user.id,
            'token': jwt_token
        }

# 회원가입


class CustomRegisterSerializer(RegisterSerializer):
    username = None

    name = serializers.CharField(required=True, max_length=15)
    date_of_birth = serializers.DateField(required=True)
    gender = serializers.CharField(
        required=True, max_length=20)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['name'] = self.validated_data.get('name', '')
        data_dict['date_of_birth'] = self.validated_data.get(
            'date_of_birth', '')
        data_dict['gender'] = self.validated_data.get('gender', '')

        return data_dict


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', )
