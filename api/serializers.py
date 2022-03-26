from rest_framework import serializers

from .models import User, Product, ProductRate, UserProduct


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRate
        fields = "__all__"


class UserProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProduct
        fields = "__all__"
