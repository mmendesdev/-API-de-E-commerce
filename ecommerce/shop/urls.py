from django.db import router
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from ecommerce.shop.models import Order, Product

from .views import OderViewSet, ProductViewSet

router = DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"Order", OderViewSet)

urlpatterns = [path("", include(router.urls))]
