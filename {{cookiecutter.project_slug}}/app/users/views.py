from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from app.authentication.mixins import \
    JSONWebTokenAuthenticationMixin
from app.users.filters import UserFilter
from app.users.serializers import UserViewSerializer, UserEditSerializer

from django.contrib.auth import get_user_model

from rest_framework.viewsets import ModelViewSet

from app.users.services import create_user_and_token, update_user

User = get_user_model()


class UserViewSet(JSONWebTokenAuthenticationMixin, ModelViewSet):
    filterset_class = UserFilter
    queryset = User.objects.all()
    search_fields = ['email', 'name']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return UserViewSerializer
        return UserEditSerializer

    def get_permissions(self):
        return [p() for p in self.permission_classes + [IsAdminUser]]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, _ = create_user_and_token(**serializer.validated_data)
        return Response(UserViewSerializer(instance=user).data,
                        status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user,
                                         data=request.data,
                                         partial=True)
        serializer.is_valid(raise_exception=True)
        user = update_user(user=user, **serializer.validated_data)
        return Response(UserViewSerializer(instance=user).data,
                        status=status.HTTP_201_CREATED)
