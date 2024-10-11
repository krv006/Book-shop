from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import WishListViewSet

router = DefaultRouter()
# router.register(r'wishlists', WishListViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
