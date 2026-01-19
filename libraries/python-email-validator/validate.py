#!/usr/bin/env python3
"""Validate email addresses using python-email-validator."""

import sys
from email_validator import validate_email, EmailNotValidError


def validate(email: str) -> bool:
    """Return True if email is valid, False otherwise."""
    try:
        validate_email(email, check_deliverability=False)
        return True
    except EmailNotValidError:
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
