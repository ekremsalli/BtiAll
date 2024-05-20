from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from .views import MyObtainTokenPairView

schema_view = get_schema_view(
    openapi.Info(
        title="BTI",
        default_version='v0.0.1',
        description="BTI API Dökümantasyonu",
        terms_of_service="http://www.btidanismanlik.com/destek/",
        contact=openapi.Contact(email="yazilim@btidanismanlik.com"),
        license=openapi.License(name="Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır."),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [

                  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
                  path('api/', include('app.urls')),
                  path('token', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
                  path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
                  path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
                  path('admin/', admin.site.urls),
                #   re_path('.*', TemplateView.as_view(template_name='index.html')),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
