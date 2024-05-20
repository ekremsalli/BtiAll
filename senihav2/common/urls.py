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
   permission_classes=[permissions.AllowAny],
)

from app.views import dispatch, order


urlpatterns = [
    path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('dispatch', dispatch.Dispatch.as_view()),
    path('idea/order', order.IdeaOrder.as_view()),
    path('idea/cargo', order.IdeaCargo.as_view()),
    path('idea/stock', order.IdeaStock.as_view()),
    path('trendyol/picking', order.TrendyolPickingStatus.as_view()),
    path('trendyol/invoiced', order.TrendyolInvoicedStatus.as_view()),
    path('trendyol/unsupplied', order.TrendyolUnsuppliedStatus.as_view()),
    path('trendyol/cargo', order.TrendyolCargo.as_view()),

    path('', include('portal.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
