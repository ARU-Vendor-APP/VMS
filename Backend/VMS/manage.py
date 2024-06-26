#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from VMS.settings import base

from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())

def main():
    """Run administrative tasks."""

    if base.DEBUG:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "VMS.settings.local")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "VMS.settings.production")
        
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
