ADDRESSLIST ?= ../../addresslist.txt

build: node_modules

node_modules: package.json
	npm install --silent
	@touch node_modules

package.json:
	@echo '{"private":true,"dependencies":{"email-addresses":"*"}}' > package.json

run: build
	@node validate.js $(ADDRESSLIST)

check: build
	@echo "test@example.com" | node validate.js /dev/stdin | grep -q "valid" && echo "✓ Basic validation works"

version: build
	@node -e "console.log(require('email-addresses/package.json').version)"

clean:
	rm -rf node_modules package.json package-lock.json

.PHONY: build run check version clean
