#!/usr/bin/env ruby
require 'truemail'

if ARGV.length < 1
  STDERR.puts "Usage: validate.rb <addresslist.txt>"
  exit 1
end

Truemail.configure do |config|
  config.verifier_email = 'verifier@example.com'
  config.default_validation_type = :regex
end

File.readlines(ARGV[0]).each do |line|
  email = line.chomp
  next if email.empty?

  result = Truemail.valid?(email) ? "valid   " : "invalid "
  puts "#{result}#{email}"
end
