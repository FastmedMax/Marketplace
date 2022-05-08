from django.utils.decorators import method_decorator

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import permissions

from drf_yasg.utils import swagger_auto_schema

from djoser.views import UserViewSet as DjoserUserViewSet

from .models import Product

from .serializers import ProductSerializer, ProductRateSerializer, UserProductSerializer


# Create your views here.
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_id="GetUser",
        operation_description="Получение пользователя с указанным `id`",
    ),
)
@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_id="GetUsersList",
        operation_description="Получение списка пользователей",
    ),
)
@method_decorator(
    name="create",
    decorator=swagger_auto_schema(
        operation_id="CreateUser", operation_description="Создание пользователя"
    ),
)
@method_decorator(name="destroy", decorator=swagger_auto_schema(auto_schema=None))
@method_decorator(name="update", decorator=swagger_auto_schema(auto_schema=None))
@method_decorator(
    name="partial_update", decorator=swagger_auto_schema(auto_schema=None)
)
@method_decorator(name="set_password", decorator=swagger_auto_schema(auto_schema=None))
@method_decorator(name="set_username", decorator=swagger_auto_schema(auto_schema=None))
@method_decorator(name="activation", decorator=swagger_auto_schema(auto_schema=None))
@method_decorator(
    name="resend_activation", decorator=swagger_auto_schema(auto_schema=None)
)
@method_decorator(
    name="reset_username", decorator=swagger_auto_schema(auto_schema=None)
)
@method_decorator(
    name="reset_password", decorator=swagger_auto_schema(auto_schema=None)
)
@method_decorator(
    name="reset_password_confirm", decorator=swagger_auto_schema(auto_schema=None)
)
@method_decorator(
    name="reset_username_confirm", decorator=swagger_auto_schema(auto_schema=None)
)
class UserViewSet(DjoserUserViewSet):
    pass


class ProductViewSet(viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classe = (permissions.IsAuthenticated)

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
            product = self.get_object()
            serializer = self.serializer_class(product.rates, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == "POST":
            data = request.data.copy()
            data["user"] = request.user.id
            data["product"] = pk
            serializer = self.serializer_class(data=data)

            if serializer.is_valid(raise_exception=False):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["post"], url_name="buy", url_path="buy", serializer_class=UserProductSerializer)
    def buy(self, request, pk=None):
        product = self.get_object()
        data = request.data.copy()
        data["user"] = request.user.id
        data["product"] = product.id

        serializer = self.serializer_class(data=data)

        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
