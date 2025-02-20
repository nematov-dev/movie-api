# urls.py
from django.urls import path
from .views import RegisterAPIView, VerifyOTPAPIView, ProfileAPIView, PhoneAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('send-otp/', PhoneAPIView.as_view(), name='send-otp'),
    path('verify-otp/', VerifyOTPAPIView.as_view(), name='verify-otp'),
    path('me/', ProfileAPIView.as_view(), name='user_profile'),
]
