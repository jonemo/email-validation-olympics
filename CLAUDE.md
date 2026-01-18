# Email Validator Compare

Benchmark suite for comparing email address validation libraries across languages.

## Key Files

- `addresslist.csv` - Test cases (email, expected validity, description)
- `libraries.md` - Catalog of validation libraries with metadata
- `run_all.sh` - Runs all validators, outputs to `results/`

## Library Interface

Each library in `libraries/` has a Makefile. The critical target is:

```
make run ADDRESSLIST=<path>
```

Must output CSV to stdout: `email,expected,actual,match`

## Important Distinction

**Validation** = syntax/format checking (what we test)
**Verification** = DNS/SMTP checking if address exists (disable this)

Always disable deliverability/DNS/SMTP checks in validation scripts.

## GitHub Pages

Results are published automatically when validators run. The `deploy-pages.yml` workflow generates an HTML comparison table at the repo's GitHub Pages URL.

## Adding Libraries

Use the skill: `/add-library` or see `.claude/skills/add-library/SKILL.md`
