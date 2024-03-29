#!/usr/bin/env ruby
# This code finds pattern based on repetition
# should match hbn, hbtn, hbttn ... hbtttttn

if ARGV.length == 1
  regex = /hbt?{1,}n/

  matches = ARGV[0].scan(regex)
  if matches.empty?
    puts "\n"
  else
    puts matches.join('')
  end
end
