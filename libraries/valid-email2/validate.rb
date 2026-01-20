#!/usr/bin/env ruby
require 'valid_email2'

if ARGV.length < 1
  STDERR.puts "Usage: validate.rb <addresslist.txt>"
  exit 1
end

File.readlines(ARGV[0]).each do |line|
  email = line.chomp
  next if email.empty?

  result = ValidEmail2::Address.new(email).valid? ? "valid   " : "invalid "
  puts "#{result}#{email}"
end
