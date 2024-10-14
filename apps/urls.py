from django.urls import path, include

urlpatterns = [
    path('shops/', include('users.urls')),
    path('shops/', include('shops.urls')),
]
