from django.urls import path

from users.views import UserListAPIView

urlpatterns = [
    path('user/', UserListAPIView.as_view())
]
