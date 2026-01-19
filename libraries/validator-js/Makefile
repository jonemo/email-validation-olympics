NODE := node
NPM := npm
ADDRESSLIST ?= ../../addresslist.txt

.PHONY: build run clean check version

build: node_modules

node_modules: package.json
	$(NPM) install --silent
	@touch node_modules

package.json:
	@echo '{"private":true,"dependencies":{"validator":"*"}}' > package.json

run: build
	@$(NODE) validate.js $(ADDRESSLIST)

check: build
	@echo "Testing basic validation..."
	@$(NODE) -e "const v = require('validator'); if (!v.isEmail('foo@example.com')) process.exit(1); console.log('OK');"

version: build
	@$(NODE) -e "console.log('Version:', require('validator/package.json').version)"

clean:
	rm -rf node_modules package.json package-lock.json
