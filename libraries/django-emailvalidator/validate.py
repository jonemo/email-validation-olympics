#!/usr/bin/env python3
"""Validate email addresses using Django's EmailValidator."""

import sys
import os

# Django requires settings to be configured before importing validators
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '__main__')
import django
from django.conf import settings

# Configure minimal Django settings
if not settings.configured:
    settings.configure(
        DEBUG=False,
        SECRET_KEY='dummy-key-for-email-validation',
        INSTALLED_APPS=[],
    )
    django.setup()

from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError


def validate(email: str) -> bool:
    """Return True if email is valid, False otherwise."""
    validator = EmailValidator()
    try:
        validator(email)
        return True
    except ValidationError:
        return False


def main():
    if len(sys.argv) < 2:
        print("Usage: validate.py <addresslist.txt>", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, encoding="utf-8") as f:
        for line in f:
            email = line.rstrip("\n")
            if not email:
                continue

            result = "valid   " if validate(email) else "invalid "
            print(f"{result}{email}")


if __name__ == "__main__":
    main()
