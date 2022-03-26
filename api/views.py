from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .models import User, Product, ProductRate, UserProduct

from .serializers import UserSerializer, ProductSerializer, ProductRateSerializer, UserProductSerializer


# Create your views here.
