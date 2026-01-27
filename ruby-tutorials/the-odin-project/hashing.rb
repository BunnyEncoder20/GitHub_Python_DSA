# Hashing is almost the same as python
my_hash = {
  'a random word' => 'ahoy',
  "Bunny's math test score" => 94,
  'an array' => [1, 2, 3, 4, 5],
  'an empty has within a hash' => {},
  9 => 'nine',
  6 => 'six'
}
puts my_hash

# Hash can also be made using the new methos (like arrays)
new_hash = {}
puts new_hash

# Accessing values in a hash
shoes = {
  'summer' => 'sandals',
  'winter' => 'boots'
}
puts shoes['summer'] # sandals
puts shoes['winter'] # boots
puts shoes['rainy'] # nil

# If you don't want a silent nil return, you can use fetch for key errors
# puts shoes.fetch('hiking') #=> KeyError: key not found: "hiking"
# Though, this method could also return a default value instead of raising an error
puts shoes.fetch('hiking', 'hiking boots') #=> hiking boots

# Adding key values pairs to hashes
shoes['rainy'] = 'rubber boots'
shoes['gaming'] = 'socks'

# chaning the values
shoes['summer'] = 'flip-flops'

# Removing key values pairs to hashes
puts shoes.delete('summer')
puts shoes

# Methods: couple of useful methods for hashes
books = {
  'Infinite Jest' => 'David Foster Wallance',
  'Into the Wild' => 'Jon Krajauer'
}

puts books.keys #=> ['Infinite Jest', 'Into the Wild']
puts books.values #=> ['David Foster Wallance', 'Jon Krajauer']

# Symbols as keys (symbols are immutable and hence much performant than plain strings)
american_cars = {
  chevrolet: 'Corvette',
  ford: 'Mustang',
  dodg: 'Ram'
}
japanese_cars = {
  honda: 'Accord',
  toyota: 'Corolla',
  nissan: 'Altima'
}
puts american_cars
puts japanese_cars
