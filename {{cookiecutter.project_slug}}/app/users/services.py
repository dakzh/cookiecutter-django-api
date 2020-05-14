import uuid

from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

User = get_user_model()


@transaction.atomic
def create_user_and_token(*,
                          name: str,
                          email: str,
                          password: str,
                          type: int) -> (User, str):
    user = User.objects.create(email=email,
                               name=name,
                               password=password)
    user.is_active = True
    user.type = type
    user.save()

    payload = jwt_payload_handler(user)

    return user, jwt_encode_handler(payload)


@transaction.atomic
def update_user(*,
                user: User,
                name: str = None,
                password: str = None,
                type: int = None,
                email: str = None) -> User:
    if email:
        user.email = email
    if name:
        user.name = name
    if type:
        user.type = type
    if password:
        user.set_password(password)
        user.secret_key = uuid.uuid4()
    user.save()
    return user
