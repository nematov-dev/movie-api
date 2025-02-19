from random import randint
from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","is_user","is_admin","full_name","phone","password")

    def create(self, validated_data):
        """ Yangi foydalanuvchini yaratish """
        otp_code = str(randint(1000, 9999))
        user = User.objects.create(
            phone=validated_data['phone'],
            full_name=validated_data.get('full_name',),
            otp=otp_code,
            is_active=False
        )
        user.set_password(validated_data['password'])
        user.save()
        print(f"OTP: {otp_code}")
        return user


class VerifyOTPSerializer(serializers.Serializer):
        phone = serializers.CharField()
        otp = serializers.CharField()

        def validate(self, data):
            try:
                user = User.objects.get(phone=data['phone'])
            except User.DoesNotExist:
                raise serializers.ValidationError("Foydalanuvchi topilmadi.")

            if user.otp != data['otp']:
                raise serializers.ValidationError("Noto‘g‘ri OTP kiritildi.")

            user.is_active = True
            user.otp = None
            user.save()
            return data
