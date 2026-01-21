PHP := php
ADDRESSLIST ?= ../../addresslist.txt
WP_VERSION := 6.7.1
WP_FORMATTING_URL := https://raw.githubusercontent.com/WordPress/WordPress/$(WP_VERSION)/wp-includes/formatting.php

.PHONY: build run clean check version

build: formatting.php

formatting.php:
	@curl -sS -o formatting.php $(WP_FORMATTING_URL)

run: build
	@$(PHP) validate.php $(ADDRESSLIST)

check: build
	@echo "Testing basic validation..."
	@echo "foo@example.com" | $(PHP) validate.php /dev/stdin | grep -q "^valid" && echo "OK"

version:
	@echo "WordPress $(WP_VERSION)"

clean:
	rm -f formatting.php
