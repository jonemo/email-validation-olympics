#!/usr/bin/env python3
"""Generate Markdown report from validation results."""

import csv
from pathlib import Path


def load_addresslist(path: Path) -> list[dict]:
    """Load the expected results from addresslist.csv."""
    emails = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= 2:
                emails.append({
                    "email": row[0],
                    "expected": row[1],
                    "description": row[2] if len(row) > 2 else "",
                })
    return emails


def load_results(results_dir: Path) -> dict[str, dict[str, str]]:
    """Load all library results. Returns {library: {email: actual}}."""
    libraries = {}
    for result_file in sorted(results_dir.glob("*.csv")):
        library_name = result_file.stem
        results = {}
        with open(result_file, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 4:
                    email, expected, actual, match = row[:4]
                    results[email] = actual
        libraries[library_name] = results
    return libraries


def escape_markdown(text: str) -> str:
    """Escape special markdown characters in text."""
    # Escape pipe characters for table cells
    return text.replace("|", "\\|").replace("\n", " ")


def generate_report(addresslist: list[dict], libraries: dict[str, dict[str, str]]) -> str:
    """Generate the Markdown report."""
    lines = []
    library_names = sorted(libraries.keys())

    # Calculate stats for each library
    stats = {}
    for lib in library_names:
        correct = 0
        false_negatives = 0  # valid emails incorrectly rejected
        false_positives = 0  # invalid emails incorrectly accepted
        for addr in addresslist:
            email = addr["email"]
            expected = addr["expected"]
            actual = libraries[lib].get(email, "")
            if actual == expected:
                correct += 1
            elif expected == "valid" and actual == "invalid":
                false_negatives += 1
            elif expected == "invalid" and actual == "valid":
                false_positives += 1
        stats[lib] = {
            "correct": correct,
            "false_negatives": false_negatives,
            "false_positives": false_positives,
        }

    # Summary table
    lines.append("## Summary\n")
    lines.append("| Library | Correct | False Negatives | False Positives |")
    lines.append("|---------|---------|-----------------|-----------------|")
    for lib in library_names:
        s = stats[lib]
        lines.append(f"| {lib} | {s['correct']} | {s['false_negatives']} | {s['false_positives']} |")
    lines.append("")

    # Expected valid emails table
    valid_emails = [a for a in addresslist if a["expected"] == "valid"]
    if valid_emails:
        lines.append("## Expected Valid Emails\n")
        lines.append("- ✓ = correctly accepted")
        lines.append("- ✗ = false negative (incorrectly rejected)\n")
        header = "| Email |" + " | ".join(library_names) + " |"
        separator = "|-------|" + "|".join(["-----"] * len(library_names)) + "|"
        lines.append(header)
        lines.append(separator)
        for addr in valid_emails:
            email = escape_markdown(addr["email"])
            cells = []
            for lib in library_names:
                actual = libraries[lib].get(addr["email"], "")
                if actual == "valid":
                    cells.append("✓")
                else:
                    cells.append("✗")
            lines.append(f"| `{email}` | " + " | ".join(cells) + " |")
        lines.append("")

    # Expected invalid emails table
    invalid_emails = [a for a in addresslist if a["expected"] == "invalid"]
    if invalid_emails:
        lines.append("## Expected Invalid Emails\n")
        lines.append("- ✓ = correctly rejected")
        lines.append("- ✗ = false positive (incorrectly accepted)\n")
        header = "| Email |" + " | ".join(library_names) + " |"
        separator = "|-------|" + "|".join(["-----"] * len(library_names)) + "|"
        lines.append(header)
        lines.append(separator)
        for addr in invalid_emails:
            email = escape_markdown(addr["email"])
            cells = []
            for lib in library_names:
                actual = libraries[lib].get(addr["email"], "")
                if actual == "invalid":
                    cells.append("✓")
                else:
                    cells.append("✗")
            lines.append(f"| `{email}` | " + " | ".join(cells) + " |")
        lines.append("")

    return "\n".join(lines)


def main():
    root = Path(__file__).parent.parent
    addresslist_path = root / "addresslist.csv"
    results_dir = root / "results"
    site_dir = root / "site"

    site_dir.mkdir(exist_ok=True)

    addresslist = load_addresslist(addresslist_path)
    libraries = load_results(results_dir)

    if not libraries:
        print("Warning: No result files found in results/")
        report = "# Email Validator Comparison\n\nNo results available yet.\n"
    else:
        report = "# Email Validator Comparison\n\n" + generate_report(addresslist, libraries)

    output_path = site_dir / "report.md"
    output_path.write_text(report, encoding="utf-8")
    print(f"Generated {output_path}")


if __name__ == "__main__":
    main()
