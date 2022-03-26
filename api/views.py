from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .models import User, Product, ProductRate, UserProduct

from .serializers import UserSerializer, ProductSerializer, ProductRateSerializer, UserProductSerializer


# Create your views here.
class ProductViewSet(viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        products = self.queryset.values_list("title", "description", "short_description", "image", "downloads", "file")
        return Response(products, status=status.HTTP_200_OK)

