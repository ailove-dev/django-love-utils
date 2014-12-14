# -*- coding: utf-8 -*-

from django.core.exceptions import ImproperlyConfigured

try:
    import rest_framework
except ImportError:
    raise ImproperlyConfigured(
        "The 'rest_framework' package could not be imported. "
        "It is required for use module 'rest'."
    )