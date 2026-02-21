from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, ProductViewSet, SubcategoryViewSet

router = DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"subcategories", SubcategoryViewSet)
router.register(r"products", ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
