from rest_framework import viewsets
from .models import Category, Product
from django.contrib.auth.models import User
from .serializers import CategorySerializer, ProductSerializer, UserSerializer
from django_filters.rest_framework import DjangoFilterBackend

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['price', 'category', 'name']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
