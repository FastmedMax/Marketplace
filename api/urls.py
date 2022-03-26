from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, ProductRateViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r"product", ProductViewSet, basename="product")
router.register(r"rate", ProductRateViewSet, basename="product_rate")

urlpatterns = [
] + router.urls