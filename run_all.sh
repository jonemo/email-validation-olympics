#!/usr/bin/env bash
#
# Run all email validation libraries against the address list.
# Results are saved to results/<library-name>.txt
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ADDRESSLIST="${1:-$SCRIPT_DIR/addresslist.txt}"
RESULTS_DIR="$SCRIPT_DIR/results"

if [[ ! -f "$ADDRESSLIST" ]]; then
    echo "Error: Address list not found: $ADDRESSLIST" >&2
    exit 1
fi

mkdir -p "$RESULTS_DIR"

# Create temp file for emails
EMAILS_FILE=$(mktemp)
trap "rm -f $EMAILS_FILE" EXIT

# Parse addresslist.txt: extract emails only
python3 -c "
import json

with open('$ADDRESSLIST', 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

i = 0
while i < len(lines):
    # Skip empty lines
    while i < len(lines) and lines[i].strip() == '':
        i += 1
    if i >= len(lines):
        break

    # Line 1: email
    email = lines[i]
    i += 1

    # Line 2: JSON metadata (skip it)
    if i < len(lines) and lines[i].strip():
        i += 1

    # Skip blank separator
    while i < len(lines) and lines[i].strip() == '':
        i += 1

    print(email)
" > "$EMAILS_FILE"

echo "Running validators against: $ADDRESSLIST"
echo "Results will be saved to: $RESULTS_DIR/"
echo

for dir in "$SCRIPT_DIR"/libraries/*/; do
    name="$(basename "$dir")"

    if [[ ! -f "$dir/Makefile" ]]; then
        echo "Skipping $name (no Makefile)"
        continue
    fi

    echo "Running $name..."
    ERROR_FILE=$(mktemp)
    if make -s -C "$dir" run ADDRESSLIST="$EMAILS_FILE" > "$RESULTS_DIR/$name.txt" 2>"$ERROR_FILE"; then
        echo "  -> $RESULTS_DIR/$name.txt"
    else
        echo "  -> FAILED"
        if [ -s "$ERROR_FILE" ]; then
            echo "     Error output:"
            sed 's/^/     /' "$ERROR_FILE"
        fi
        rm -f "$RESULTS_DIR/$name.txt"
    fi
    rm -f "$ERROR_FILE"
done

echo
echo "Done."
