def my_func
  'Bunny & Soma'
end

puts my_func #=> Bunny & Soma

def my_best_friend(name1, name2)
  "#{name1} & #{name2} are best friends"
end
puts my_best_friend('Bunny', 'Some')

# Default parameters
def greet(name = 'stranger')
  'Hello, ' + name + '!'
end
puts greet('Soma')
puts greet

# WARN: Ruby is one of the few langs which has a implicit return.
# Ruby method will return the last expression that was evalutated even without the return keyword
# This may or may not be the last line of the func
def even_or_odd(number)
  if number.even?
    'This number is even'
  else
    'This number is odd'
  end
end
puts even_or_odd(4)
puts even_or_odd(7)

# Return keyword works almost the same as any other langs
def even_odd(number)
  return 'A number was not entered, aborting...' unless number.is_a? Numeric

  if number.even?
    'This number is even'
  else
    'This number is odd'
  end
end

puts even_odd(65)
puts even_odd('ola')

# Chaining methods together
phrase = %w[? want to of meaning the is what] # use %w to make a array of strings
puts phrase.reverse.join(' ').capitalize

# NOTE: You will sometimes encounter built-in Ruby methods names that have a ? mark at the end.
# These are predicate methods, which is a naming convention that Ruby uses to indicate
# that the method returns a boolean value (true or false).
puts 5.even? #=> false
puts 6.even? #=> true
puts 17.odd? #=> true

puts 12.between?(10, 15) #=> true

# NOTE: Similarly, methods that end with a ! are called "bang" methods.
# These mehtods, reassign the receiver object itself instead of returning a modified copy.
str = 'HELLO WORLD THIS SENTENCE WAS IN CAPS BEFORE'
puts str.downcase
puts str
puts str.downcase!
puts str
