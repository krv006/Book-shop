from django.contrib.auth.backends import ModelBackend
from users.models import User


class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, email=None, password=None, **kwargs):

        if username is None:
            return None

        try:

            user = User.objects.get(email=username)
        except User.DoesNotExist:

            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return None
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None

# from django.contrib.auth import get_user_model
# from django.contrib.auth.backends import ModelBackend
#
#
# class EmailBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         UserModel = get_user_model()
#         try:
#             user = UserModel.objects.get(email=username)
#         except UserModel.DoesNotExist:
#             return None
#         else:
#             if user.check_password(password):
#                 return user
#         return None
