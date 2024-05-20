from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


from .views import user
from .views import integration

urlpatterns = [
    path('user/profile', user.Profile.as_view()),
    path('integration', integration.List.as_view()),
    path('product/search', integration.SearchProduct.as_view()),
    path('trendyol/init', integration.TrendyolInit.as_view()),
    path('trendyol/brand', integration.TrendyolBrandSearch.as_view()),
    path('trendyol/attrs', integration.TrendyolAttrs.as_view()),
    path('product/detail', integration.ProductDetail.as_view()),
    path('trendyol/product_match', integration.TrendyolProductMatch.as_view()),
    path('trendyol/product', integration.TrendyolProduct.as_view()),
    path('trendyol/mismatch', integration.TrendyolMismatch.as_view()),
    path('trendyol/log', integration.TrendyolLogView.as_view()),
    path('trendyol/transfer', integration.TrendyolTransfer.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
