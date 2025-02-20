from random import randint
from rest_framework import serializers

from .models import User

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","is_user","is_admin","full_name","phone","password")

    def create(self, validated_data):
        """ Yangi foydalanuvchini yaratish """
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.is_active = True
        user.save()
        return user

class VerifyOTPSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15)
    verification_code = serializers.CharField(max_length=4)




