from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description']


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    is_in_stock = serializers.BooleanField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 
            'name', 
            'slug', 
            'description', 
            'price', 
            'category', 
            'category_name',
            'image', 
            'stock_quantity', 
            'is_in_stock',
            'is_active',
            'created_at'
        ]
        read_only_fields = ['created_at']


class ProductListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for product lists"""
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'price', 'category_name', 'image', 'is_in_stock']