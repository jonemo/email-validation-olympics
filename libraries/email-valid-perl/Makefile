ADDRESSLIST ?= ../../addresslist.txt

.PHONY: build run clean check version

build: .cpan-installed

.cpan-installed:
	cpanm --quiet --notest Email::Valid
	@touch .cpan-installed

run: build
	@perl validate.pl $(ADDRESSLIST)

check: build
	@echo "Testing basic validation..."
	@perl -e 'use Email::Valid; print Email::Valid->address("test@example.com") ? "OK\n" : "FAIL\n"'

version: build
	@perl -MEmail::Valid -e 'print "Version: $$Email::Valid::VERSION\n"'

clean:
	rm -f .cpan-installed
