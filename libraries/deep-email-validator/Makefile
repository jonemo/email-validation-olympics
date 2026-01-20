NODE := node
NPM := npm
ADDRESSLIST ?= ../../addresslist.txt

.PHONY: build run clean check version

build: node_modules

node_modules: package.json
	$(NPM) install --silent
	@touch node_modules

package.json:
	@echo '{"private":true,"dependencies":{"deep-email-validator":"*"}}' > package.json

run: build
	@$(NODE) validate.js $(ADDRESSLIST)

check: build
	@echo "Testing basic validation..."
	@$(NODE) -e "const { validate } = require('deep-email-validator'); validate({ email: 'foo@example.com', validateMx: false, validateSMTP: false }).then(r => { if (!r.valid) process.exit(1); console.log('OK'); });"

version: build
	@$(NODE) -e "console.log('Version:', require('deep-email-validator/package.json').version)"

clean:
	rm -rf node_modules package.json package-lock.json
