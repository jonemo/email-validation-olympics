CARGO := cargo
ADDRESSLIST ?= ../../addresslist.csv

.PHONY: build run clean check version

build: Cargo.toml
	$(CARGO) build --release --quiet

Cargo.toml:
	$(CARGO) init --name emailvalidator --quiet --vcs none
	$(CARGO) add email_address --quiet

run: build
	@$(CARGO) run --release --quiet -- $(ADDRESSLIST)

check: build
	@echo "Testing basic validation..."
	@$(CARGO) run --release --quiet -- --check
	@echo "OK"

version: Cargo.toml
	@$(CARGO) metadata --format-version 1 --no-deps 2>/dev/null | grep -o '"email_address","version":"[^"]*"' | cut -d'"' -f4 || grep email_address Cargo.lock | head -1 | grep -o '"[0-9.]*"' | tr -d '"'

clean:
	rm -rf target Cargo.toml Cargo.lock src .git
