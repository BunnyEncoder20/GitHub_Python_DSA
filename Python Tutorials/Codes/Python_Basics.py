print("Hello World 👋")
print("I love Pizza 🍕")

# Varibles : 
variable_name = "bro"       # in python strings can be "" or ''
print("Hello "+variable_name);

# checking the type of variable
print(type(variable_name)) ;        

# Simple String Concat 
first_name = "Varun" ;
last_name = "Verma" ;
name = first_name+" "+last_name  ;
print("Name : " + name) ;


# Integers (int)
age = 22 ;
print("my age is ",age) #cannot concat int and str 
print("my age is " + str(age)) # converting the int into str using type casting

# Floating (float - can store a floating point number value)
height = 170.8
print("my height is "+str(height)+"cms")

# Booleans (Binary true or false values)
isHuman = False      # booleans start with caps in python
if(isHuman) :
    print("You are a Human 😃")
else : 
    print("You are a robot 🤖")

# Standard and Multi Assignment
name = "Soma"
age = 22
isBFF = True 

print(name)
print(age)
print(isBFF)

name, age , isBFF = "Varun", 22, True

print(name)
print(age)
print(isBFF)


# Taking in user input 
name = input("What is your name ? ")    # Note |> that input() always returns a string datatype (series of characters) 
print("Hello ",name)
age = int(input("How old are you ? "))
print("You are "+str(age)+"yrs old") ;
print("Next year you'll be "+str(age+1)+"yrs old") ;
height = float(input("How tall are you ? ")) ;
print("You are "+str(height)+"cms tall") ;