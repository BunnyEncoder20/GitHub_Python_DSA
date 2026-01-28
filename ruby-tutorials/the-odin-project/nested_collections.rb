teacher_mailboxes = [
  %w[Adams Baker Clark Davis],
  %w[Jones Lewis Lopez Moore],
  %w[Perez Scott Smith Young]
]

test_scores = [
  [97, 76, 79, 93],
  [79, 84, 76, 79],
  [88, 67, 64, 76],
  [94, 55, 67, 81]
]

# Accessing elements in nested arrays
puts teacher_mailboxes[0][0]
#=> "Adams"
puts teacher_mailboxes[1][0]
#=> "Jones"
puts teacher_mailboxes[2][0]
#=> "Perez"

# traditional looping
for i in 0...test_scores.length
  for j in 0...test_scores[i].length
    puts "Score: #{test_scores[i][j]}"
  end
end

# Ruby looping
test_scores.each do |row|
  row.each do |score|
    puts "Score: #{score}"
  end
end

# can also use the negative indexing to access elements from the end
puts teacher_mailboxes[0][-1]
#=> "Davis"
puts teacher_mailboxes[-1][0]
#=> "Perez"
puts teacher_mailboxes[-1][-2]
#=> "Smith"

teacher_mailboxes.each_with_index do |row, row_index|
  puts "Row:#{row_index} = #{row}"
end

# WARN:
# one major “gotcha” that is important to point out. According to the Array class documentation,
# the second optional argument for Array.new (the default value), should only be used
# with an immutable (unable to be changed) object such as a number, boolean value,
# or symbol. Using a string, array, hash, or other mutable object may result in confusing
# behavior because each default value in the array will actually be a reference to the
# same default value. Therefore, any change to one of the elements will change all of
# the elements in the array.
mutable = Array.new(3, Array.new(2))
#=> [[nil, nil], [nil, nil], [nil, nil]]
puts mutable[0][0] = 1000
#=> 1000
puts mutable
#=> [[1000, nil], [1000, nil], [1000, nil]]

nested_array = Array.new(3) { Array.new(3) }
nested_array[0][0] = 1000
puts nested_array

# NOTE: Nested Hashes
puts 'Nested Hashes Examples:'
vehicles = {
  alice: { year: 2019, make: 'Toyota', model: 'Corolla' },
  blake: { year: 2020, make: 'Volkswagen', model: 'Beetle' },
  caleb: { year: 2020, make: 'Honda', model: 'Accord' }
}

# Accessing data
vehicles[:alice][:year]
#=> 2019
vehicles[:blake][:make]
#=> "Volkswagen"
vehicles[:caleb][:model]
#=> "Accord"

# vehicles[:zoe][:year]
#=> NoMethodError
vehicles.dig(:zoe, :year)
#=> nil
vehicles[:alice][:color]
#=> nil
vehicles.dig(:alice, :color)
#=> nil

# NOTE: The filter map method can be very useful when working with nested collections.
# especially in web development when dealing with JSON data for filtering and transforming data.
puts(vehicles.filter_map { |name, data| name if data[:year] >= 2020 })
#=> [:caleb, :dave]
