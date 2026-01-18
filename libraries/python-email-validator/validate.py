#!/usr/bin/env python3
"""Validate email addresses using python-email-validator."""

import csv
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
        print("Usage: validate.py <addresslist.csv>", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]

    # Output CSV header
    print("email,expected,actual,match")

    with open(input_file, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row or not row[0].strip():
                continue

            email = row[0]
            expected = row[1].strip().lower() if len(row) > 1 else ""

            actual = "valid" if validate(email) else "invalid"
            match = "true" if actual == expected else "false"

            # Quote email if it contains comma
            email_out = f'"{email}"' if "," in email else email
            print(f"{email_out},{expected},{actual},{match}")


if __name__ == "__main__":
    main()
