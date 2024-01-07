#!/usr/bin/env ruby
# This code finds pattern based on repetition
# should match only Capital letters

if ARGV.length == 1
  regex = /[A-Z]/

  matches = ARGV[0].scan(regex)
  if matches.empty?
    puts "\n"
  else
    puts matches.join('')
  end
end
