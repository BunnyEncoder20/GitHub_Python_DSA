# Few useful String methods

# 1. Length of string 
name = "Soma Senpai" 
print("Length of name : ",len(name))

# 2. Find the first index of a character 
print(name.find("S"))
print(name.find("a"))

# Capitalize 
print("Capitalize : ", "varun".capitalize())

# Upper() & Lower()
print("Upper : ",name.upper())
print("Lower : ",name.lower())

# isDigit() - checks if the string is a string of digits 
print("name is digit ? ",name.isdigit())   
print("'12345' is digit ? ","12345".isdigit())

# isalpha() - is it a string of alphabetically characters ONLY 
print("All alphabets name? ",name.isalpha())       # prints false cause "Soma Senpai" has a space in between
print("All alphabets 'bunny'? ","bunny".isalpha())

# count() - returns the number od occurrences of a character in the string 
print("Count of S in name : ",name.count("S"))

# replace( "1st arg" , "2nd arg" ) - replaces first arg character with the 2nd arg character 
print("Replace S with T in name : ",name.replace("S" , "T"));

# Display a string multiple times: 
print("Bunny"*3)