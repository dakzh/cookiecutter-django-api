from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

User = get_user_model()


class EmailModelBackend(ModelBackend):

    def authenticate(self, request, username=None, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(email__iexact=username or email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
