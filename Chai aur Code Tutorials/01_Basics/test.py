while True : 
    try : 
        pet = input("Enter your pet species (cat,dog,fish) :\n ").lower()
        age = float(input("Enter your pet's age:"))

        if (pet in ['dog','cat','fish']) : 
            break
        else : 
            print("This species is not available, try one of the given species")
    except ValueError : 
        print("Enter a valid age for your pet")

if pet=='dog' : 
    food = 'puppy food' if age<2.0 else 'adult dog food'
elif pet =='cat' : 
    food = 'cat food' if age<5.0 else 'senior cat food'
else :
    food = 'fish food'
    
print(f"Your pet {pet} is recommended to eat {food}")

        

