# There is a loop loop in ruby for some reason
i = 0
loop do
  puts 'This will keep printing until you stop it!'
  break unless i < 10

  i += 1
end

# While loops
i = 0
while i < 10
  puts "i is #{i}"
  i += 1
end

puts 'Do you like Pizza ?'
puts 'Do you like Pizza ?' while gets.chomp.downcase != 'yes'

# Ranges
# 1..5 inclusive range
# 1...5 exclusive range
for i in 1..5
  puts "Inclusive range value: #{i}"
end

for i in 1...5
  puts "Exlcusive range value: #{i}"
end

# Times loops
# It uses a number to loop over that specific number of times
# As a bonus it also alows to access the current iteration number
# Remember that looping always starts from 0 unless specified otherwise
5.times do |i|
  puts "Times loop iteration: #{i}"
end

# .upto and downto loops: Similar to Times Loops, do exactly as the name says
5.upto(10) { |num| print "#{num} " }     #=> 5 6 7 8 9 10

10.downto(5) { |num| print "#{num} " }   #=> 10 9 8 7 6 5
