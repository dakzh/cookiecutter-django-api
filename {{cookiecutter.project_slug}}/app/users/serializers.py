from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id',
                  'name',
                  'email',
                  'created_at',
                  'updated_at']


class UserEditSerializer(serializers.ModelSerializer):

    password = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['email',
                  'name',
                  'password']
