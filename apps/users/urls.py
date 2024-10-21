from django.urls import path

from users.views import UserUpdateAPIView, RegisterCreateAPIView, LoginAPIView, \
    UserWishlistCreateAPIViewDestroyAPIView, ActivateUserView, AddressListCreateAPIView, AddressDestroyUpdateAPIView

urlpatterns = [
    path('address', AddressListCreateAPIView.as_view(), name='address_list'),
    path('address/<int:pk>', AddressDestroyUpdateAPIView.as_view(), name='address_detail'),

    path('update-user', UserUpdateAPIView.as_view(), name='update-user'),
    path('user-wishlist', UserWishlistCreateAPIViewDestroyAPIView.as_view(), name='wishlist-user'),

    path('register', RegisterCreateAPIView.as_view(), name='register'),
    path('login', LoginAPIView.as_view(), name='login'),
    # path('customtoken', CustomTokenObtainPairView, name='custom-token'),
    path('activate/<uidb64>/<token>', ActivateUserView.as_view(), name='activate'),

]
