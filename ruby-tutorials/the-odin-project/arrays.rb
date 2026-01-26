# Basic arrays
num_array = [1, 2, 3, 4, 5]
str_array = %w[This is a small array]
puts num_array
puts str_array

# Creating arrays using the new() method #=> []
puts Array.new(3)            #=> [nil, nil, nil]
puts Array.new(3, 7)         #=> [7, 7, 7]
puts Array.new(3, true)      #=> [true, true, true]

# Accessing array elements is the same as python
str_array = %w[This is a small array]

str_array[0]            #=> "This"
str_array[1]            #=> "is"
str_array[4]            #=> "array"
str_array[-1]           #=> "array"
str_array[-2]           #=> "small"

num_array = [1, 2]

num_array.push(3, 4)      #=> [1, 2, 3, 4]   Adding muliple elements to the end of the array
num_array << 5            #=> [1, 2, 3, 4, 5] terminal style
num_array.pop             #=> 5
puts num_array #=> [1, 2, 3, 4]

# Adding 2 arrays together
a = [1, 2, 3]
b = [3, 4, 5]

puts a + b         #=> [1, 2, 3, 3, 4, 5]
puts a.concat(b)   #=> [1, 2, 3, 3, 4, 5]

# Substracting arrays: returns a copy of the first array, removing any items that also appear in the second array
puts [1, 1, 1, 2, 2, 3, 4] - [1, 4] #=> [2, 2, 3]

# Some basic methods:
[].empty?               #=> true
[[]].empty?             #=> false
[1, 2].empty?           #=> false

[1, 2, 3].length        #=> 3

[1, 2, 3].reverse       #=> [3, 2, 1]

[1, 2, 3].include?(3)   #=> true
[1, 2, 3].include?('3') #=> false

[1, 2, 3].join          #=> "123"
[1, 2, 3].join('-')     #=> "1-2-3"

# Matrixes:
# m x n matrix filled with 0
grid = [[10, 20], [30, 40]]
# print dist in matrix format
grid.each_with_index do |row, r|
  row.each_with_index do |val, c|
    puts "Val at [#{r}][#{c}] is #{val}"
  end
end
