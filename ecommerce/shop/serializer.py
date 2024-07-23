from rest_framework import serializers

from .models import Order, Product, User


class UserSerializes(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "is_admin"]


class ProductSerializes(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "stock"]


class OrderSerializes(serializers.ModelSerializer):
    class Meta:
        model = Order
        fiels = ["id", "user", "product", "quantity", "created_at"]
