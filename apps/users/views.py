from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView

from users.models import User
from users.serializers import UserModelSerializer


@extend_schema(tags=['user'])
class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
