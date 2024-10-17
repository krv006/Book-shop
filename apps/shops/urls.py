from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shops.views import AddressListCreateAPIView, CountryListAPIView, AddressDestroyUpdateAPIView

router = DefaultRouter()
# router.register(r'wishlists', WishListViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('address', AddressListCreateAPIView.as_view(), name='address_list'),
    path('address/<int:pk>', AddressDestroyUpdateAPIView.as_view(), name='address_detail'),

    path('address', AddressListCreateAPIView.as_view()),
    path('country', CountryListAPIView.as_view()),
]
