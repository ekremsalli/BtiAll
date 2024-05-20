from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# rest
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
   openapi.Info(
      title="BTI",
      default_version='v0.0.1',
      description="BTI API Dökümantasyonu",
      terms_of_service="http://www.btidanismanlik.com/destek/",
      contact=openapi.Contact(email="yazilim@btidanismanlik.com"),
   ),
   public=True,
   #permission_classes=[permissions.AllowAny],
)

from app.views import ArpCard, SalesInvoice

urlpatterns = [
    path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('arpcard/arpcard/arpcard', ArpCard.as_view()),
    path('arpcard/arpcard/arpcard/id/<int:id>', ArpCard.as_view()),
    path('arpcard/arpcard/arpcard/delete/id/<int:id>', ArpCard.as_view()),
    path('salesInvoice/salesInvoice/salesInvoice', SalesInvoice.as_view()),
    path('salesInvoice/salesInvoice/delete/salesInvoice/id/<int:id>', SalesInvoice.as_view())
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
