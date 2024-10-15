from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, EmailField
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserUpdateSerializer(ModelSerializer):
    confirm_password = CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'confirm_password', 'first_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        # Password va confirm_password ni tekshirish
        if data['password'] != data['confirm_password']:
            raise ValidationError("Passwords do not match.")
        return data

    def update(self, instance, validated_data):
        # Parolni yangilash
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
            validated_data.pop('confirm_password', None)

        # Boshqa ma'lumotlarni yangilash
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.save()
        return instance


class UserWishlist(ModelSerializer):
    class Meta:
        model = User
        fields = 'wishlist',


class RegisterUserModelSerializer(ModelSerializer):
    confirm_password = CharField(write_only=True)

    class Meta:
        model = User
        fields = 'id', 'email', 'password', 'confirm_password', 'first_name',

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        confirm_password = attrs.pop('confirm_password')
        if confirm_password != attrs.get('password'):
            raise ValidationError('Passwords did not match!')
        attrs['password'] = make_password(confirm_password)
        return attrs


class LoginUserModelSerializer(Serializer):
    email = EmailField()
    password = CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(username=email, password=password)
        if user is None:
            raise ValidationError("Invalid email or password")
        attrs['user'] = user
        return attrs


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token
