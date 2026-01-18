GO := go
BINARY := validate
ADDRESSLIST ?= ../../addresslist.csv

.PHONY: build run clean check version

build: $(BINARY)

$(BINARY): validate.go go.mod
	$(GO) build -o $(BINARY) validate.go

go.mod:
	$(GO) mod init emailvalidator
	$(GO) get github.com/AfterShip/email-verifier@latest

run: build
	@./$(BINARY) $(ADDRESSLIST)

check: build
	@echo "Testing basic validation..."
	@./$(BINARY) --check
	@echo "OK"

version: go.mod
	@$(GO) list -m -f '{{.Version}}' github.com/AfterShip/email-verifier

clean:
	rm -f $(BINARY) go.mod go.sum
