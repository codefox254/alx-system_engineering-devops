#!/usr/bin/env ruby

if ARGV.length != 1
  puts "Usage: script.rb <string>"
  exit(1)
end

pattern = /^hbn(t*)$/
input_string = ARGV[0]

if input_string.match(pattern)
  puts "The string matches the pattern."
else
  puts "The string does not match the pattern."
end

