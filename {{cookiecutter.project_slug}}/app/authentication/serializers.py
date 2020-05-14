from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
import django.contrib.auth.password_validation as validators

from rest_framework import serializers

User = get_user_model()


class RegistrationSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = User(email=email)
        errors = dict()
        try:
            validators.validate_password(password=password, user=user)
        except ValidationError as e:
            errors['password'] = list(e.messages)
        if errors:
            raise serializers.ValidationError(errors)
        return super(RegistrationSerializer, self).validate(attrs)
