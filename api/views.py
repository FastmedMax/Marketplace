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

    def retrieve(self, request, pk=None):
        product = self.get_object()
        serializer = self.serializer_class(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["get", "post"], url_name="rates", url_path="rates", serializer_class=ProductRateSerializer)
    def rates(self, request, pk=None):
        if request.method == "GET":
            product = self.queryset.get(id=pk)
            serializer = self.serializer_class(product.rates, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == "POST":
            data = request.data.copy()
            data["product"] = pk
            serializer = self.serializer_class(data=data)

            if serializer.is_valid(raise_exception=False):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
