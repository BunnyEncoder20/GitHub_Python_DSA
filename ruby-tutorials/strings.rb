puts 'Hello World'
print 'Hello World'
p 'Hello World'

name = 'Soma'
puts('Hello ' + name)
age = 25
p('Soma is ' + age.to_s + ' years old')

puts "Varun\nVerma"

phrase = 'I am not the Common Wealth'
puts phrase
puts phrase.upcase
puts phrase.downcase
puts phrase.strip
puts phrase.length
puts phrase.include? 'common'
puts phrase.include? 'Common'

# Indexing of string
puts phrase[0]
puts phrase.index('C')
puts phrase.index('W')
puts phrase[13..18] # This uses the start and end index
puts phrase[13, 6] # The second parameter is length, not the ending index
