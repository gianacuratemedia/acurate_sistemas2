from .views import RegisterView, LoginAPIView, VerifyEmail, LogoutAPIView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
]
