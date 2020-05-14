from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Booking Service API",
      default_version='v1',
      description="",
      terms_of_service="https://dakzh.com/",
      contact=openapi.Contact(email="dakzholov@gmail.com"),
      license=openapi.License(name="PRIVATE"),
   ),
   url="https://api.dakzh.com",
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('v1/', include('app.apis.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
