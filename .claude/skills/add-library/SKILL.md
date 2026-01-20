---
name: add-library
description: Add a new email validation library to the benchmark suite. Use when adding support for a new validator library.
---

# Adding a New Email Validation Library

## Directory Structure

Create `libraries/<library-name>/` with:
- `Makefile` - build and run commands
- `validate.{ext}` or `main.{ext}` - validation script
- `.gitignore` - language-specific ignores

## Makefile Requirements

Must implement these targets:

```makefile
ADDRESSLIST ?= ../../addresslist.txt

build:    # Install dependencies, compile if needed
run:      # Run validation (must use @-prefix to suppress command echo)
check:    # Quick sanity test
version:  # Print library version
clean:    # Remove build artifacts
```

The `run` target must:
1. Accept `ADDRESSLIST` variable as path to input file (plain text, one email per line)
2. Output to stdout: `valid   <email>` or `invalid <email>` (8-char prefix + email)
3. Be silent (use `@` prefix) so only results are output

## Validation Script Requirements

1. Read plain text file from path given as command-line argument (one email per line)
2. For each line: validate email syntax only (disable DNS/SMTP checks)
3. Output one line per email: `valid   <email>` or `invalid <email>`
   - "valid   " and "invalid " are both exactly 8 characters (padded with spaces)

## Language-Specific Patterns

### Python
```makefile
VENV := .venv
PYTHON := $(VENV)/bin/python
build: $(VENV)
	$(VENV)/bin/pip install --quiet <package>
$(VENV):
	python3 -m venv $(VENV)
run: build
	@$(PYTHON) validate.py $(ADDRESSLIST)
```
`.gitignore`: `.venv/`, `__pycache__/`, `*.pyc`

```python
#!/usr/bin/env python3
import sys

def validate(email: str) -> bool:
    # Your validation logic here
    pass

def main():
    with open(sys.argv[1], encoding="utf-8") as f:
        for line in f:
            email = line.rstrip("\n")
            if not email:
                continue
            result = "valid   " if validate(email) else "invalid "
            print(f"{result}{email}")

if __name__ == "__main__":
    main()
```

### Node.js
```makefile
build: node_modules
node_modules: package.json
	npm install --silent
	@touch node_modules
package.json:
	@echo '{"private":true,"dependencies":{"<package>":"*"}}' > package.json
run: build
	@node validate.js $(ADDRESSLIST)
```
`.gitignore`: `node_modules/`, `package.json`, `package-lock.json`

```javascript
#!/usr/bin/env node
const fs = require('fs');

function validate(email) {
    // Your validation logic here
}

const content = fs.readFileSync(process.argv[2], 'utf-8');
for (const line of content.split('\n')) {
    const email = line.replace(/\r$/, '');
    if (!email) continue;
    const result = validate(email) ? 'valid   ' : 'invalid ';
    console.log(`${result}${email}`);
}
```

### Go
```makefile
build: $(BINARY)
$(BINARY): validate.go go.mod
	go build -o $(BINARY) validate.go
go.mod:
	go mod init emailvalidator
	go get <package>@latest
run: build
	@./$(BINARY) $(ADDRESSLIST)
```
`.gitignore`: `validate`, `go.mod`, `go.sum`

### Rust
```makefile
build: Cargo.toml
	cargo build --release --quiet
Cargo.toml:
	cargo init --name emailvalidator --quiet --vcs none
	cargo add <crate> --quiet
run: build
	@cargo run --release --quiet -- $(ADDRESSLIST)
```
`.gitignore`: `target/`, `Cargo.toml`, `Cargo.lock`

**Note:** Use `--vcs none` to prevent `cargo init` from creating a nested `.git` folder.

## Testing

**Important:** The repo's `addresslist.txt` contains email + JSON metadata (alternating lines), NOT plain text. Don't test validators by running `make run` with the default `ADDRESSLIST` - this will process JSON lines as emails.

To test a new validator:

```bash
# Option 1: Use run_all.sh (extracts emails to temp file automatically)
./run_all.sh

# Option 2: Create a simple test file for quick checks
echo -e "test@example.com\ninvalid-email\nfoo@bar.baz" > /tmp/test-emails.txt
make run ADDRESSLIST=/tmp/test-emails.txt
```

## After Adding

1. Test using `./run_all.sh` from repo root (preferred)
2. Update `libraries.md` if not already listed
3. Update `.github/workflows/run-validators.yml` if new language runtime needed
