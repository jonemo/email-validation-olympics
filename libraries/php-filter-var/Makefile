PHP := php
ADDRESSLIST ?= ../../addresslist.txt

.PHONY: build run clean check version

build:
	@# No build step needed - filter_var is built into PHP

run: build
	@$(PHP) validate.php $(ADDRESSLIST)

check: build
	@echo "Testing basic validation..."
	@echo "foo@example.com" | $(PHP) validate.php /dev/stdin | grep -q "^valid" && echo "OK"

version:
	@$(PHP) -v | head -1

clean:
	@# Nothing to clean
