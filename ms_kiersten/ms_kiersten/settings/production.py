from .base import *
import dotenv
from os import environ

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

STATIC_ROOT = "/var/www/ms_kiersten/static"
MEDIA_ROOT = "/var/www/ms_kiersten/media"
ALLOWED_HOSTS = ["mskiersten.com"]

dotenv.load_dotenv("../msk.env")

SECRET_KEY = environ["DJANGO_SECRET_KEY"]
