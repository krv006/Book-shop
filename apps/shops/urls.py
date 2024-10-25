from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shops.views import CountryListAPIView, BookListAPIView, BookDetailAPIView

router = DefaultRouter()
# router.register(r'wishlists', WishListViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('country', CountryListAPIView.as_view()),

    path('books', BookListAPIView.as_view(), name='book-list'),
    path('books/<str:slug>', BookDetailAPIView.as_view(), name='book-detail'),

]
