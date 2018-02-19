from __future__ import absolute_import, unicode_literals

import os
from .base import *

DEBUG = os.getenv('DEBUG', False)
SECRET_KEY = os.getenv('SECRET_KEY')
ALLOWED_HOSTS = []

try:
    from .local import *
except ImportError:
    pass
