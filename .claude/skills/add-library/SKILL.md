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
ADDRESSLIST ?= ../../addresslist.csv

build:    # Install dependencies, compile if needed
run:      # Run validation (must use @-prefix to suppress command echo)
check:    # Quick sanity test
version:  # Print library version
clean:    # Remove build artifacts
```

The `run` target must:
1. Accept `ADDRESSLIST` variable as path to CSV input
2. Output CSV to stdout: `email,expected,actual,match`
3. Be silent (use `@` prefix) so only CSV is output

## Validation Script Requirements

1. Read CSV from path given as command-line argument
2. For each row: validate email syntax only (disable DNS/SMTP checks)
3. Output CSV with header: `email,expected,actual,match`
   - `actual`: "valid" or "invalid"
   - `match`: "true" or "false"
4. Quote emails containing commas

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

## After Adding

1. Test: `make run` in the library directory
2. Run all: `./run_all.sh` from repo root
3. Update `libraries.md` if not already listed
4. Update `.github/workflows/run-validators.yml` if new language runtime needed
