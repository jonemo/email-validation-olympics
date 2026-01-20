ADDRESSLIST ?= ../../addresslist.txt

.PHONY: build run clean check version

build: .gems-installed

.gems-installed: Gemfile
	bundle install --quiet
	@touch .gems-installed

Gemfile:
	@echo "source 'https://rubygems.org'" > Gemfile
	@echo "gem 'valid_email2'" >> Gemfile

run: build
	@bundle exec ruby validate.rb $(ADDRESSLIST)

check: build
	@echo "Testing basic validation..."
	@bundle exec ruby -e "require 'valid_email2'; puts ValidEmail2::Address.new('test@example.com').valid? ? 'OK' : 'FAIL'"

version: build
	@bundle exec ruby -e "require 'valid_email2'; puts ValidEmail2::VERSION"

clean:
	rm -rf .gems-installed Gemfile Gemfile.lock .bundle vendor
