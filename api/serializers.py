from rest_framework import serializers

from .models import User, Category, Product, ProductRate, UserProduct


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ProductRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRate
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field="title", queryset=Category.objects.all()
    )

    class Meta:
        model = Product
        fields = "__all__"


class ProductDetailSerializer(ProductSerializer):
    rates = ProductRateSerializer(read_only=True, many=True)


class UserProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProduct
        fields = "__all__"
