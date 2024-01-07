#!/usr/bin/env ruby
#
# This code selects the [FROM] [TO] and [FLAG] 
# from a log file and displays it on a single line

if ARGV.length == 1
  regex = /\[from:(.*?)\]|\[to:(.*?)\]|\[flags:(.*?)\]/

  matches = ARGV[0].scan(regex)

  if matches.empty?
    puts "\n"
  else
    puts matches.map {|from, to, flags|[from, to, flags].compact.join(',')}.join(',')
  end
end
