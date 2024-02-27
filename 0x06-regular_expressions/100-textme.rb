#!/usr/bin/env ruby
#Your script should output: [SENDER],[RECEIVER],[FLAGS]
#The sender phone number or name (including country code if present)
#The receiver phone number or name (including country code if present)
#The flags that were used
from = ARGV[0].scan(/((?<=from:)[\w\+\d]+)/).join
to = ARGV[0].scan(/((?<=to:)[\w\+\d]+)/).join
flag = ARGV[0].scan(/((?<=flags:)[\-\d:]+)/).join
puts "#{from},#{to},#{flag}"
