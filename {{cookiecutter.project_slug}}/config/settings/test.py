from .base import *  # noqa
from .base import env

# GENERAL
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="!!!SET DJANGO_SECRET_KEY!!!",
)
TEST_RUNNER = "django.test.runner.DiscoverRunner"
