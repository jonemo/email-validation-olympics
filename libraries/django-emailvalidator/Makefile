VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
ADDRESSLIST ?= ../../addresslist.txt

.PHONY: build run clean check version

build: $(VENV)
	$(PIP) install --quiet Django

$(VENV):
	python3 -m venv $(VENV)

run: build
	@$(PYTHON) validate.py $(ADDRESSLIST)

check: build
	@echo "Testing basic validation..."
	@$(PYTHON) -c "from django.core.validators import EmailValidator; EmailValidator()('foo@example.com'); print('OK')"

version: build
	@$(PIP) show Django | grep Version

clean:
	rm -rf $(VENV) __pycache__ *.pyc
