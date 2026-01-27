# Enumerables
friends = %w[Bunny Soma Bunnu Hoods Chaitanya Ammar Rihan imposter]

# Filtering out a single value using select or reject
actual_friends = friends.select { |friend| friend != 'imposter' }
puts 'friends: ', friends
puts 'Actual Friends:', actual_friends

actual_friends_through_reject = friends.reject { |friend| friend == 'imposter' }
puts 'Rejecting the imposter:', actual_friends_through_reject

# NOTE:  .each method. It is the granddaddy of all enumerable methods in Ruby.
# Can practically do anything.
# Calling each on an array will iterate through that array and will yield
# each element to a code block, where a task can be performed:
friends = %w[Bunny Soma Bunnu Hoods Chaitanya Ammar Rihan]
friends.each { |friend| puts 'Hello, ' + friend }

# WARN: If the logic is multi lines long, it is best practice to use the
# do...end block syntax instead of .each
my_arr = [1, 2, 3]
my_arr.each do |num|
  num *= 2
  puts "The new number is #{num}"
end

# .each on hashes, will give both key and value to the block
my_hash = { one: 1, two: 2, three: 3 }
my_hash.each { |key, value| puts "#{key} maps to #{value}" }

# WARN: whatever happens inside the block, is not going to change the original array or hash.
# The original array or hash remains unchanged after the .each method is called.

# NOTE: .each_with_index method gives additional functionality by providing the value and index
# Just like the normal .each method, this also returns the original array or hash.
fruits = %w[apple banana orange grape mango pineapple]
fruits.each_with_index { |fruit, index| puts fruit if index.even? }

# NOTE: .map method is used when we want to tranform an array or hash into a new array or hash.
friends = %w[Bunny Soma Bunnu Hoods Chaitanya Ammar Rihan]
friends = friends.map { |friend| friend.upcase }
# OR can use the ! operator for the same effect
friends.map! { |friend| friend.upcase }
puts friends.join(', ')

my_order = ['medium Big Mac', 'medium fries', 'medium milkshake']
my_order.map! { |item| item.gsub('medium', 'extra large') }
puts my_order.join(', ')

# NOTE: reduce method (aka inject) is possibly the most difficult to grasp enumerable for new coders.
# Takes values of a hash or array and 'reduces' it to a single value
my_numbers = [5, 10, 15]
sum = 0
my_numbers.each { |number| sum += number }
puts sum
# This above can be done better with the reduce method:
puts(my_numbers.reduce { |sum, number| sum + number })
# we can even provide the initial value for sum:
puts my_numbers.reduce(100) { |sum, number| sum + number }

# reduce given a new hash as a initial value and adding things
# to that hash along the iteration of the reduce and then return a single
# object still: the hash
votes = ["Bob's Dirty Burger Shack", "St. Mark's Bistro", "Bob's Dirty Burger Shack"]

results = votes.each_with_object(Hash.new(0)) do |vote, result|
  result[vote] += 1
end

puts results
