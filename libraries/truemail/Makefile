ADDRESSLIST ?= ../../addresslist.txt

.PHONY: build run clean check version

build: .gems-installed

.gems-installed: Gemfile
	BUNDLE_PATH=vendor/bundle bundle install --quiet
	@touch .gems-installed

Gemfile:
	@echo "source 'https://rubygems.org'" > Gemfile
	@echo "gem 'truemail'" >> Gemfile
	@echo "gem 'net-smtp'" >> Gemfile

run: build
	@BUNDLE_PATH=vendor/bundle bundle exec ruby validate.rb $(ADDRESSLIST)

check: build
	@echo "Testing basic validation..."
	@bundle exec ruby -e "require 'truemail'; Truemail.configure { |c| c.verifier_email = 'test@example.com'; c.default_validation_type = :regex }; puts Truemail.valid?('test@example.com') ? 'OK' : 'FAIL'"

version: build
	@bundle exec ruby -e "require 'truemail'; puts Truemail::VERSION"

clean:
	rm -rf .gems-installed Gemfile Gemfile.lock .bundle vendor
