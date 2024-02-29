#!/usr/bin/env ruby
# Check if the argument is provided
if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

# Regular expression pattern
pattern = /School/

# Method to match the regular expression pattern
def match_pattern(string, pattern)
  string.match(pattern)
end

# Main script logic
input_string = ARGV[0]
match_result = match_pattern(input_string, pattern)

if match_result
  puts match_result[0] # Print the matched substring
else
  puts "" # No match found
end

