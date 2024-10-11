from django.urls import path

from users.views import UserListAPIView, UpdateUserView, RegisterCreateAPIView, LoginAPIView

urlpatterns = [
    path('user/', UserListAPIView.as_view()),
    path('update-user/', UpdateUserView.as_view(), name='update-user'),

    path('auth/register', RegisterCreateAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),

]
