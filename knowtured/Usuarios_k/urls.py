
from .views import RegisterView, LoginAPIView, VerifyEmail, LogoutAPIView, RequestPasswordResetEmail, SetNewPasswordAPIView, PasswordTokenCheckAPI
from .views import MyProfile, MyProfileDetail, ProfesoresList, BusquedaProfesor
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.views import (
    TokenRefreshView,)
urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    #Only Get user profile 
    path('mi-perfil/', MyProfile.as_view(), name="my_profile"),
    #Only get and update user profile
    path('mi-perfil/update/<int:id>', MyProfileDetail.as_view(), name="edit_my_profile"),
    #Get lista de profesores que tengan el campo is_teacher=True
    path('profesores/', ProfesoresList.as_view(), name="profesores"),

#Busqueda profesor por username, nombre o apellidos 
    path('profesores/buscar/<str:busqueda>', BusquedaProfesor.as_view(), name="profesor_busqueda"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(),name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/',PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(),name='password-reset-complete')
]
