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


# **********************************************************************
# String Slicing in python 
# Slicing a string = making a substring from using elements from that (previous) string 
# indexing[] or slice()
# [] is called the indexing operator. [start idx : stop idx : step]
# **********************************************************************

name = "Soma Senpai"
first_name = name[0:3]      # note how this only returns 3 letters 
print(first_name)           # hence start idx is inclusive and the stop idx is exclusive

print(name[:4])             # if we do not mention the start idx, the default is taken as 0
last_name = name[5:]        # if the stop idx is left out, then it'll take till last character idx
print(last_name)

funky_name1 = name[::2]      # by default the step is = 1, but we can change it. 
print(funky_name1)           # note the absence of start and stop idx ==> it'll take the entire string

funky_name2 = name[::-1]     # step can seen as how the idx is updated. so when we take -1, it'll go in reverse 
print(funky_name2)


# Using slice(start idx , stop idx , step) 
# a string character has a +ve and -ve index (-ve index starts from the right end of the string with -1. Hence str[-2] => second last character)

website1 = "https://google.com" ;
website2 = "https://wikipedia.com" ;
website3 = "https://PandaExpress.com" ;

# slice to get the website name 
slice = slice(8,-4)

print("website1 : ",website1[slice])
print("website2 : ",website2[slice])
print("website3 : ",website3[slice])
