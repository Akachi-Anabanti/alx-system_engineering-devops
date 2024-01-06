#!/usr/bin/env ruby
# This code finds pattern based on repetition
# should match hbtn and htn

if ARGV.length == 1
  regex = /hb?tn/

  matches = ARGV[0].scan(regex)
  if matches.empty?
    puts "\n"
  else
    puts matches.join('')
  end
end
