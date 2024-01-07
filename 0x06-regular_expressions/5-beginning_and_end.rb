#!/usr/bin/env ruby
# This code finds pattern based on repetition
# should match h and anything to n

if ARGV.length == 1
  regex = /h.+n/

  matches = ARGV[0].scan(regex)
  if matches.empty?
    puts "\n"
  else
    puts matches.join('')
  end
end
