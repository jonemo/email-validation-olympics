# Email Validator Compare

Benchmark suite for comparing email address validation libraries across languages.

## Key Files

- `addresslist.txt` - Test cases in email + JSON metadata format
- `libraries.md` - Catalog of validation libraries with metadata
- `run_all.sh` - Runs all validators, outputs to `results/`

## addresslist.txt Format

```
foo@bar.com
{"valid": true, "description": "simple test case"}

"hi@you"@stavros.io
{"valid": true, "description": "quoted at symbol in local part", "source": "https://..."}

```

- Line 1: Email address (literal, no escaping needed)
- Line 2: JSON with `valid` (bool), `description` (string), optional `source`
- Line 3: Blank separator

## Library Interface

Each library in `libraries/` has a Makefile. The critical target is:

```
make run ADDRESSLIST=<path>
```

Input: Plain text file with one email per line.
Output to stdout: `valid   <email>` or `invalid <email>` (8-char prefix + email)

## Important Distinction

**Validation** = syntax/format checking (what we test)
**Verification** = DNS/SMTP checking if address exists (disable this)

Always disable deliverability/DNS/SMTP checks in validation scripts.

## GitHub Pages

Results are published automatically when validators run. The `deploy-pages.yml` workflow generates an HTML comparison table at the repo's GitHub Pages URL.

## Adding Libraries

Use the skill: `/add-library` or see `.claude/skills/add-library/SKILL.md`
