from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from ecommerce.shop.serializer import OrderSerializes, ProductSerializes

from .models import Order, Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializes

    def get_permissions(self):
        if self.request.method in ["POST", "PUT", "PATCH", "DELETE"]:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


class OderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializes

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
