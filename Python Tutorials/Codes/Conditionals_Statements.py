# If elif else

age = int(input("enter your age : "))

if age >= 18 : 
    print("you are an adult 🧑")
elif age == 100 :           # notice how even though the age will be == 100, this section doesn't execute because the first if condition is fulfilled and skips the rest 
    print("You are a century old! 👴")
elif age < 0 : 
    print("You have not been born yet ! 🤨")
else : 
    print("You are a baby 👶")


# Logical Operators and, or, not

temp = int(input("Enter the Temperature : "))
isGoodDay = False ;

if temp>=0 and temp<=30 : 
    print("The Temp is good Today")
    print("Go outside 🏐")
    isGoodDay = True ;

elif temp<0 or temp>30 : 
    print("The temperature is bad today !")
    print("Don't go outside toady! 😅")
    isGoodDay = False ;

if not(isGoodDay) :
    print("Man this sucks 😠")
