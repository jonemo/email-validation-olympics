#!/usr/bin/env bash
#
# Run all email validation libraries against the address list.
# Results are saved to results/<library-name>.csv
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ADDRESSLIST="${1:-$SCRIPT_DIR/addresslist.csv}"
RESULTS_DIR="$SCRIPT_DIR/results"

if [[ ! -f "$ADDRESSLIST" ]]; then
    echo "Error: Address list not found: $ADDRESSLIST" >&2
    exit 1
fi

mkdir -p "$RESULTS_DIR"

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
    if make -s -C "$dir" run ADDRESSLIST="$ADDRESSLIST" > "$RESULTS_DIR/$name.csv" 2>/dev/null; then
        echo "  -> $RESULTS_DIR/$name.csv"
    else
        echo "  -> FAILED"
        rm -f "$RESULTS_DIR/$name.csv"
    fi
done

echo
echo "Done."
