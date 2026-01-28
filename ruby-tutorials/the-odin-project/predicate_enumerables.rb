# NOTE: include? method works same as python's 'in' keyword
# each equvialent of python's 'include' function
def my_include?(arr, val)
  arr.each do |element|
    return true if element == val
  end
  false
end

puts 'include method examples:'
numbers = [1, 2, 3, 4, 5]
puts numbers.include?(3) #=> true
puts numbers.include?(6) #=> false

friends = %w[Bunny Soma Bunnu Hoods Chaitanya Ammar Rihan Darpan]
friends.include?('Soma') #=> true
friends.include?('Jonathan') #=> false

# NOTE: any? method:
# if any of the element of the enumerate match the condition, it returns true
puts 'any method examples:'
# each equvialent of 'any' function
result = false
numbers = [21, 42, 303, 499, 550, 811]
numbers.each do |num|
  if num > 500
    result = true
    break
  end
end
puts result #=> true

# using ruby's any? method
puts(numbers.any? { |num| num > 500 }) #=> true
puts(numbers.any? { |num| num < 20 }) #=> false

# NOTE: all? method
# fairy intuitive, returns true only if all elements match the condition
puts 'all method ecamples:'
fruits = %w[apple banana strawberry pineapple]
puts(fruits.all? { |fruit| fruit.length > 3 }) #=> true
puts(fruits.all? { |fruit| fruit.length > 6 }) #=> false

# NOTE: none? method
# opposite of the all method, returns true only if none of the elements match the condition
puts 'None methos ecamples:'
puts(fruits.none? { |fruit| fruit.length > 3 }) #=> false
puts(fruits.none? { |fruit| fruit.length < 3 }) #=> true

# NOTE: one? method
# Checks and returns true only when exactly one element matches the condition
puts 'One method ecamples:'
fruits = %w[apple banana strawberry pineapple]
puts(fruits.one? { |fruit| fruit.length > 9 }) #=> true
puts(fruits.one? { |fruit| fruit.length > 2 }) #=> false
