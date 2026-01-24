puts('The primitive data types in Ruby include:')
puts('- Integer: Represents whole numbers, e.g., 42, -7')
puts('- Float: Represents decimal numbers, e.g., 3.14, -0.001')
puts('- String: Represents sequences of characters, e.g., "Hello, World!"')
puts('- Boolean: Represents true or false values')

# NOTE: It’s important to keep in mind that when doing arithmetic with two integers in Ruby,
# the result will always be an integer #=> 3, not 3.4
# To obtain an accurate answer, just replace one of the integers in the expression with a float. #=> 3.4

# NOTE: As everything in Ruby is an object, primitive data types also have methods associated with them.
# Eg: Converting a number between integer and float (note that it just cuts off the numbers after decimal,
# it is not rounding them off)
13.to_f #=> 13.0

# To convert a float to an integer:
13.0.to_i #=> 13
13.9.to_i #=> 13  and NOT 14

# To check odd and even numbers:
6.even? #=> true
7.even? #=> false
6.odd? #=> false
7.odd? #=> true

# STRINGS
# NOTE: Strings can be formed with either double "" or single'' quotation marks, also known as string literals.
# They are pretty similar, but there are some differences.
# Specifically, string interpolation and the escape characters that we’ll discuss soon both only work inside
# double quotation marks, not single quotation marks.

# Concatenation of strings
# With the plus operator: #=> "Welcome to Odin!"

# With the shovel operator:
'Welcome ' << 'to ' << 'Odin!' #=> "Welcome to Odin!"

# With the concat method:
'Welcome '.concat('to ').concat('Odin!') #=> "Welcome to Odin!"

# SubStrings in Ruby:
'hello'[0] #=> "h"

'hello'[0..1] #=> "he"

'hello'[0, 4] #=> "hell"

'hello'[-1] #=> "o"

# Some commonly used escape charactrs in strings:
# \\  #=> Need a backslash in your string?
# \b  #=> Backspace
# \r  #=> Carriage return, for those of you that love typewriters
# \n  #=> Newline. You'll likely use this one the most.
# \s  #=> Space
# \t  #=> Tab
# \"  #=> Double quotation mark
# \'  #=> Single quotation mark

# String Interpolation
name = 'Bunny'

puts "Hello, #{name}" #=> "Hello, Odin"
puts 'Hello, #{name}' #=> "Hello, #{name}"

# Common built in functions for strings:
'hello'.capitalize #=> "Hello"
'hello'.include?('lo') #=> true
'hello'.include?('z') #=> false
'hello'.upcase #=> "HELLO"
'Hello'.downcase #=> "hello"
'hello'.empty? #=> false
''.empty? #=> true
'hello'.length #=> 5
'hello'.reverse #=> "olleh"
'hello world'.split #=> ["hello", "world"]
'hello'.split('') #=> ["h", "e", "l", "l", "o"]
' hello, world   '.strip #=> "hello, world"
