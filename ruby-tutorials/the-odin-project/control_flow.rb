# If else block:
room_tidy = true

if room_tidy
  puts 'You can play video games!'
else
  puts 'Clean your room first!'
end

# elsif block for connecting values
attack_by_land = false
attack_by_sea = false
if attack_by_land == true
  puts 'release the goat'
elsif attack_by_sea == true # Notice that it is "elsif" and not "elif" from Python
  puts 'release the shark'
else
  puts 'release Kevin the flying octopus'
end

# Unless block: works opposite of if block (only runs if condition is false)
age = 25
unless age <= 20
  print 'Get a fooking job, '
  print "ya young'un!"
end

# can also put an else in there:
age = 19
puts 'Welcome to a life of debt.' unless age < 18

if age < 18
  puts 'Careful now!'
else
  puts 'Down with that sort of thing.'
end

# Different kinds of equivalence and comparison operators
# = checks for same value or simple true/false
puts "\nNormal = euqality checks:"
var1 = 5
var2 = 5
puts var1 == var2 #=> true
var2 = 7
puts var1 == var2 #=> false

# .eql?() checks both value type
puts "\n.eql() euqality checks:"
var1.eql?(var2) #=> false
var1 = 7.0
var1.eql?(var2) #=> false, although the values are the same
var2 = 7.0
var1.eql?(var2) #=> true

# .equal?() checks object identity. Basically if both the variables are pointing to the same object in memory
puts "\n.equal() euqality checks:"
var1 = 'hello'
var2 = 'hello'
puts var1.equal?(var2) #=> false, although the values are the same, they are different objects in memory
var2 = var1
puts var1.equal?(var2) #=> true, both are pointing to the same object in memory now

# Greater than and less than comparisons
# WARN: Only false and nil have falsey values in Ruby
# remaining everything is considered Truthy values (even 0 and empty strings)
puts var1 > var2 #=> false
puts var1 < var2 #=> true

# NOTE: Spaceship operator <=>
puts 5 <=> 10    #=> -1
puts 10 <=> 10   #=> 0
puts 10 <=> 5    #=> 1

# Logical operators
# or aka ||
# and aka &&
# not aka !

# Case statements (like switch case in other langs)
grade = 'D'

did_i_pass = case grade #=> create a variable `did_i_pass` and assign the result of a call to case with the variable grade passed in
             when 'A' then 'Hell yeah!'
             when 'D' then "Don't tell your mother."
             else "'YOU SHALL NOT PASS!' -Gandalf"
             end
puts did_i_pass

# Ternary operator: concise, one line if-else statement
age = 18
response = age < 18 ? 'You still have your entire life ahead of you.' : "You're all grown up."
puts response
