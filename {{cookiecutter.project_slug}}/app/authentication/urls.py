from django.urls import path

from app.authentication.views import (
    LoginApi,
    RegistrationApi,
)

urlpatterns = [
    path('login/', LoginApi.as_view()),
    path('register/', RegistrationApi.as_view()),
]
