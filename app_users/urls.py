# urls.py
from django.urls import path
from .views import RegisterAPIView, VerifyOTPAPIView, ProfileAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('verify/', VerifyOTPAPIView.as_view(), name='verify_otp'),
    path('me/', ProfileAPIView.as_view(), name='user_profile'),
]
