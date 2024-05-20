"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin


from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)