CARGO := cargo
ADDRESSLIST ?= ../../addresslist.txt

.PHONY: build run clean check version

build: Cargo.toml
	$(CARGO) build --release --quiet

Cargo.toml:
	$(CARGO) init --name emailvalidator --quiet --vcs none
	$(CARGO) add validator --quiet

run: build
	@$(CARGO) run --release --quiet -- $(ADDRESSLIST)

check: build
	@echo "Testing basic validation..."
	@$(CARGO) run --release --quiet -- --check
	@echo "OK"

version: Cargo.toml
	@grep -A1 'name = "validator"' Cargo.lock | grep version | head -1 | sed 's/.*"\([0-9.]*\)".*/\1/'

clean:
	rm -rf target Cargo.toml Cargo.lock src
