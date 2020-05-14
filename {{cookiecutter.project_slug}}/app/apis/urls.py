from django.conf.urls import include
from django.urls import path


urlpatterns = [
    path('auth/', include('app.authentication.urls')),
    path('users/', include('app.users.urls')),
]
