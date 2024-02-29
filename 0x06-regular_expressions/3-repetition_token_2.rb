#!/usr/bin/env ruby
# Check if the provided string matches the regular expression
def match_regex(test_string)
  regex = /hb+t+n/
  if test_string.match(regex)
    puts "The string matches the pattern."
  else
    puts "The string does not match the pattern."
  end
end

# Accept one argument from command line and pass it to match_regex method
if ARGV.length == 1
  match_regex(ARGV[0])
else
  puts "Please provide exactly one argument."
end

