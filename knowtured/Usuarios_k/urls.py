
from .views import RegisterView, LoginAPIView, VerifyEmail, LogoutAPIView, RequestPasswordResetEmail, SetNewPasswordAPIView, PasswordTokenCheckAPI
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.views import (
    TokenRefreshView,)
urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(),name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/',PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(),name='password-reset-complete')
]
