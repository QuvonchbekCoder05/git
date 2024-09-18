from rest_framework import serializers
from .models import Category, Product
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name']

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')  # Kategoriya nomi
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'category', 'created_by']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        validated_data['created_by'] = user
        return super().create(validated_data)


class UserSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()  # Mahsulotlarni dinamik boshqarish

    class Meta:
        model = User
        fields = ['username', 'products']

    # Mahsulot serializerini tanlash
    def get_products(self, obj):
        request = self.context.get('request')

       
        if request.resolver_match.url_name == 'user-list':
            return SimpleProductSerializer(obj.products.all(), many=True).data

        
        return ProductSerializer(obj.products.all(), many=True).data
