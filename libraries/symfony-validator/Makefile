PHP := php
COMPOSER := composer
ADDRESSLIST ?= ../../addresslist.txt

.PHONY: build run clean check version

build: vendor

vendor: composer.json
	$(COMPOSER) install --quiet
	@touch vendor

composer.json:
	@echo '{"require":{"symfony/validator":"^7.0","egulias/email-validator":"^4.0"}}' > composer.json

run: build
	@$(PHP) validate.php $(ADDRESSLIST)

check: build
	@echo "Testing basic validation..."
	@echo "foo@example.com" | $(PHP) validate.php /dev/stdin | grep -q "^valid" && echo "OK"

version: build
	@$(COMPOSER) show symfony/validator | grep -E "^versions" | head -1

clean:
	rm -rf vendor composer.json composer.lock
