VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
ADDRESSLIST ?= ../../addresslist.csv

.PHONY: build run clean check version

build: $(VENV)
	$(PIP) install --quiet email-validator

$(VENV):
	python3 -m venv $(VENV)

run: build
	@$(PYTHON) validate.py $(ADDRESSLIST)

check: build
	@echo "Testing basic validation..."
	@$(PYTHON) -c "from email_validator import validate_email; validate_email('foo@example.com', check_deliverability=False); print('OK')"

version: build
	@$(PIP) show email-validator | grep Version

clean:
	rm -rf $(VENV) __pycache__ *.pyc
