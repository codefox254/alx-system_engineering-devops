#!/usr/bin/env  ruby
#this scrips prints the match patterns
input_string = ARGV[0]

if input_string =~ /h+b?tn/
  puts "The string matches the pattern."
else
  puts "The string does not match the pattern."
end

