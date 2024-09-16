from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, UserViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)
router.register('users', UserViewSet)  # To'g'ri nom bilan

urlpatterns = [
    path('', include(router.urls)),
]
