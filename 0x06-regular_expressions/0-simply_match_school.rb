#!/usr/bin/env ruby
# This code matches the regex of Holberton and School


if ARGV.length == 1
  regex = /Holberton|School/

  matches = ARGV[0].scan(regex)
  if matches.empty?
    puts "\n"
  else
      puts matches.join('')
  end
end
