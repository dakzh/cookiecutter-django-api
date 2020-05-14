from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import ObtainJSONWebToken

from app.apis.mixins import ServiceExceptionHandlerMixin
from app.authentication.serializers import RegistrationSerializer
from app.users.serializers import UserViewSerializer
from app.users.services import create_user_and_token

jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


class LoginApi(ObtainJSONWebToken):
    """
    User login API.
    """

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        token = data.get('token')
        user = data.get('user')
        return Response(status=status.HTTP_200_OK, data={
            "user": UserViewSerializer(instance=user).data,
            "token": token,
        })


class RegistrationApi(ServiceExceptionHandlerMixin, APIView):
    """
    User registration API.
    """

    def get_serializer(self):
        return RegistrationSerializer()

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = create_user_and_token(**serializer.validated_data)
        return Response(status=status.HTTP_200_OK, data={
            "user": UserViewSerializer(instance=user).data,
            "token": token
        })

