VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
ADDRESSLIST ?= ../../addresslist.txt

.PHONY: build run clean check version

build: $(VENV)
	$(PIP) install --quiet pyIsEmail

$(VENV):
	python3 -m venv $(VENV)

run: build
	@$(PYTHON) validate.py $(ADDRESSLIST)

check: build
	@echo "Testing basic validation..."
	@$(PYTHON) -c "from pyisemail import is_email; print('OK' if is_email('foo@example.com') else 'FAIL')"

version: build
	@$(PIP) show pyIsEmail | grep Version

clean:
	rm -rf $(VENV) __pycache__ *.pyc
