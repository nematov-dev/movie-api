# urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenBlacklistView, TokenRefreshView

from .views import RegisterAPIView, VerifyOTPAPIView, ProfileAPIView, PhoneAPIView,LoginAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/',LoginAPIView.as_view(), name='login'),
    path('logout/', TokenBlacklistView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('send-otp/', PhoneAPIView.as_view(), name='send-otp'),
    path('verify-otp/', VerifyOTPAPIView.as_view(), name='verify-otp'),
    path('me/', ProfileAPIView.as_view(), name='user_profile'),
]