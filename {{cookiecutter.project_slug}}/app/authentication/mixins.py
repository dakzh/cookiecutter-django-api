from rest_framework.permissions import IsAuthenticated

from app.apis.mixins import TokenAuthentication


class JSONWebTokenAuthenticationMixin:
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
