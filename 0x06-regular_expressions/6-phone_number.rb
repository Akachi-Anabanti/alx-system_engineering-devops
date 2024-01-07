#!/usr/bin/env ruby
# This code finds pattern based on repetition
# should match 10 digit number
# should match "12345667890" but not " 1234567890" nor 
# "1234567890 " nor numbers with special characters in between

if ARGV.length == 1
  regex = /^\d{10,10}$/

  matches = ARGV[0].scan(regex)
  if matches.empty?
    puts "\n"
  else
    puts matches.join('')
  end
end
