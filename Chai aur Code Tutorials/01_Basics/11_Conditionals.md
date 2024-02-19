# Conditionals in Python

---

- `.input()` method is used to take input from user.
- **Remember** that input is always a string.
- So we will have to convert it into our preferred data type using methods like `int()` and `str()`.

---

## Problems 

### Q1. Age Group Categorization
- Classify a person into a group based on their age:
  - child( <13 )
  - Teenager (13-19)
  - Adult (20-59)
  - Senior (60+)
- **Solution**
```python
age = int(input("Enter Age:\n"))

if age < 13 : 
    print("Child")
elif age<20 : 
    print("Teenager")
elif age<60 : 
    print("Adult")
else : 
    print("Senior")
```
- Note how we have optimized the conditions by not checking the lower limits because they are been checked by the previous if statement

---

### Q2. Movie ticket problem 
- Movie Tickets are based on age. \$12 for adults (18 and over), \$8 for children. Everyone gets a \$2 discount on Wednesday
- **Solution**
```python
age = int(input("Enter age: \n"))
day = input("Enter day: \n")

price = 12 if age >= 18 else 12
if day.lower() == "wednesday" : 
    price = price-2 

print("Your Price is ${}".format(price))
```
---

### Q3. Grade Assignment 

- Assign a single Letter grade based on student score : 
  - A (90-100)
  - B (80-89)
  - C (70-79)
  - D (60-69)
  - F (below 60)
- **Solution**
```python
while True:
    try:
        score = int(input("Enter your score :\n"))
        if(0<=score<=100) : 
            break
        else : 
            print("Invalid Score : Please enter a valid score (0-100)")
    except ValueError:
        print("Invalid Score : Please enter a valid integer")
            

if score >= 90 : 
    grade = "A"
elif score >= 80 : 
    grade = "B"
elif score >= 70 : 
    grade = "C"
elif score >= 60 : 
    grade = "D"
else : 
    grade = "F"

print(f"Grade : {grade}")
```
- **NOTE** how we use the `try-except` block to validate user input. It also helps use to avoid edge cases like user not entering a number.
- ValueError is the kinda of error which we get for entering wrong input type data. (Eg: entering a string/char when asked for an int())
---

### Q4. Fruit Ripeness Calculator

- Determine the ripeness of the fruit based on the color : 
  - fruit: Banana
  - Green (unripe)
  - Yellow (ripe)
  - Brown (overripe)
- **Solution**
```python
while True : 
    fruit = input("Enter fruit : \n")
    color = input("Enter color : \n").lower()

    if color in ['green','yellow','brown']:
        break
    else : 
        print("unrecognized color, try again")

ripeness = ""

if color == 'green':
    ripeness = 'unripe'
elif color == 'yellow':
    ripeness = 'ripe'
else :
    ripeness = 'overripe'

print(f"{fruit} is {ripeness}")
```
---

### Q5. Weather Activity Suggestion 

- Suggest activity to do according to weather :
  - Sunny : walk
  - Rainy : read a book
  - Snowy : build a snowman
- **Solution**
```python
while True : 
    weather = input("Enter the weather : \n").lower()
    if weather in ['sunny','rainy','snowy'] : 
        break
    else :
        print("Invalid weather, try again")

activity = ""
if weather == "sunny":
    activity = "go for a walk"
elif weather == "rainy" : 
    activity = "read a book"
else : 
    activity = "build a snowman"

print(f"Today is {weather} so {activity}")
```
---

### Q6. Transport mode selection

- Chose a mode of transportation based on distance:
  - <3 : walk
  - 3-15 : bike
  - more than 15 : car
- **Solution**
```python 
while True : 
    try : 
        distance = int(input("Enter the distance (kms) :\n"))
        break
    except ValueError : 
        print("Please enter a valid integer")

if (distance < 3):
    transport = "walk"
elif distance < 15 : 
    transport = "bike" 
else : 
    transport = "car"

print(f"The distance is {distance} so take a {transport} to reach your destination")
```

---

### Q7. Coffee Customizations.

- Customize a coffee order
  - Large / medium / small
  - if customer wants an extra shot of expresso ?
- **Solution**  
```python
while True : 
    size = input("Enter the size of the Coffee : \n").lower()
    want_shot = input("Do you want extra shot of exprsso? (y/n)\n").lower()
    shot = True if want_shot=='y' else False
    
    if size in ['large','medium','small'] and want_shot in ['y','n'] : 
        break
    else : 
        print("Invalid Inputs, try again")

if shot : 
    print(f"Your order is 1 {size} coffee with extra shot of expresso")
else : 
    print(f"Your order is 1 {size} coffee without extra shot of expresso")
```
---

### Q8. Password Strength Checker

- Check the strength of a password from length : 
  - less than 6 characters : weak 
  - 6-10 characters : medium
  - more than 10 characters : strong
- **Solution**
```python
password = input("Enter your password :\n")
if len(password)<6 :
    print("Password is weak")
elif len(password)<10 : 
    print("Password is medium")
else : 
    print("Password is strong")
```

---

### Q9. Leap Year Checker

- Check if a year is a leap year or not
- **HINT:** leap years are divisible by 4 , but not by 100 unless they are also divisible by 400
- **Solution**
```python
while True : 
    try : 
        year = int(input("Enter the year :\n"))   
        break
    except ValueError : 
        print("Please enter a valid year integer")

if (year%4==0 and year%100!=0) or (year%400==0):
    print("Leap year")
else : 
    print("Not a leap year")
```

---

### Q10. Pet Food Recommendation 

- Give recommendation based on species and age of pet : 
  - Dogs : 
    - less than 2 years : puppy food
    - more than 2 years : adult dog food
  - cats : 
    - less than 5 years : cat food
    - more than 5 years : senior cat food
  - Fish 
    - fish food for all age groups
- **Solution**
```python
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
```
