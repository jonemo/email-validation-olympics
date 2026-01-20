NODE := node
NPM := npm
ADDRESSLIST ?= ../../addresslist.txt

.PHONY: build run clean check version

build: node_modules

node_modules: package.json
	$(NPM) install --silent
	@touch node_modules

package.json:
	@echo '{"private":true,"dependencies":{"joi":"*"}}' > package.json

run: build
	@$(NODE) validate.js $(ADDRESSLIST)

check: build
	@echo "Testing basic validation..."
	@$(NODE) -e "const Joi = require('joi'); if (Joi.string().email().validate('foo@example.com').error) process.exit(1); console.log('OK');"

version: build
	@$(NODE) -e "console.log(require('joi/package.json').version)"

clean:
	rm -rf node_modules package.json package-lock.json
