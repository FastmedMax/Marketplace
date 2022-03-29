from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from .models import User, Product, ProductRate, UserProduct

from .serializers import UserSerializer, ProductSerializer, ProductRateSerializer, UserProductSerializer


# Create your views here.
class ProductViewSet(viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        products = self.queryset.values_list("title", "description", "short_description", "image", "downloads", "file")
        return Response(products, status=status.HTTP_200_OK)


class ProductRateViewSet(viewsets.GenericViewSet):
    queryset = ProductRate
    serializer_class = ProductRateSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
