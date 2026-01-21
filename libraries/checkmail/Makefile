GO := go
BINARY := validate
ADDRESSLIST ?= ../../addresslist.txt

.PHONY: build run clean check version

build: $(BINARY)

$(BINARY): validate.go go.mod
	$(GO) build -o $(BINARY) validate.go

go.mod:
	$(GO) mod init emailvalidator
	$(GO) get github.com/badoux/checkmail@latest

run: build
	@./$(BINARY) $(ADDRESSLIST)

check: build
	@echo "Testing basic validation..."
	@./$(BINARY) --check
	@echo "OK"

version: go.mod
	@$(GO) list -m -f '{{.Version}}' github.com/badoux/checkmail

clean:
	rm -f $(BINARY) go.mod go.sum
