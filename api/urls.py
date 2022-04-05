from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="products")

urlpatterns = [
] + router.urls