import os
import sys
from pathlib import Path

from django.core.wsgi import get_wsgi_application

app_path = Path(__file__).parents[1].resolve()
sys.path.append(str(app_path / "app"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

application = get_wsgi_application()
