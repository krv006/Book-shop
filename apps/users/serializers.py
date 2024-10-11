from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, Serializer
from users.models import User
from django.contrib.auth.hashers import make_password


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UpdateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class RegisterUserModelSerializer(serializers.ModelSerializer):
    confirm_password = CharField(write_only=True)

    class Meta:
        model = User
        fields = 'id', 'first_name', 'last_name', 'username', 'password', 'confirm_password'

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        confirm_password = attrs.pop('confirm_password')
        if confirm_password != attrs.get('password'):
            raise serializers.ValidationError('Passwords did not match!')
        attrs['password'] = make_password(confirm_password)
        return attrs


class LoginUserModelSerializer(Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid username or password")
        attrs['user'] = user
        return attrs
