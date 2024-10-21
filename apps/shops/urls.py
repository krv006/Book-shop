from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shops.views import CountryListAPIView

router = DefaultRouter()
# router.register(r'wishlists', WishListViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('country', CountryListAPIView.as_view()),
]
