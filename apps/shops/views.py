from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

# from shops.models import WishList
# from shops.serializers import WishListSerializer

# @extend_schema(tags=['wish-list'])
# class WishListViewSet(ModelViewSet):
#     queryset = WishList.objects.all()
#     serializer_class = WishListSerializer
#     permission_classes = [IsAuthenticated]
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
