from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="{{cookiecutter.project_name}}",
      default_version='v1',
      description="",
      contact=openapi.Contact(email="{{cookiecutter.email}}"),
      license=openapi.License(name="PRIVATE"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('v1/', include('app.apis.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
