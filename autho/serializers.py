from rest_framework import serializers
from autho.models import User


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password')

    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError('Пользователь с такой почтой уже существует')
        return attrs


class SignInSerializer(serializers.Serializer):
    email = serializers.CharField(
        required=True,
        max_length=50
    )
    password = serializers.CharField(
        required=True,
        min_length=8,
        max_length=128
    )

    def validate(self, attrs):
        user = User.objects.filter(email=attrs['email']).first()
        if not user:
            raise serializers.ValidationError('User not found')
        return attrs


class UserResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', )


class UserSerializer(serializers.Serializer):
    user = UserResponseSerializer()
    token = serializers.CharField()
