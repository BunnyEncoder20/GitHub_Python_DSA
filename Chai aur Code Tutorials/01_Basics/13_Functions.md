# Functions in Python 

---

- in python we should know 
1. **how to define** Functions : how will the function work internally 
2.  **how to use** the Functions : how will we call the function

- We will learn all about python functions by answering questions below.

- A function is a block of code which only runs when it is called.
- You can pass data, known as parameters, into a function.
- A function can return data as a result.
- A function can be declared using the **`def`** keyword (short for definition)

---
---


## Questions Section

---
### Q1. Basic Function Syntax 

- make a function to calculate square of a number .
- **Solution**
```python

```
- parameters are values passed into the function when it is called.

---

### Q2. Function with multiple parameters 

- Make a function to take 2 parameters and returns their sum
- **Solution**
```python
def summation(x, y) : 
    return x+y

result = summation(3,4)
print(result)
```

--- 

### Q3. Implement Polymorphism in function

- make a function which multiples 2 numbers but can also take and multiple strings 
- **Solution**
```python
def multi(x, y) : 
    return x*y 

print(multi("Soma",5))
print(multi(5,"Soma"))
print(multi(5,5))
```

--- 

### Q4. Function returning multiple values 

- function to return both area adn circumference of a circle given it's radius 
- **Solution**
```python
def area_circumference(x) : 
    area = round(3.14*x*x , 2)
    circumference = round(2*3.14*x , 2)
    return area, circumference
radius = 5
area,circum = area_circumference(radius)
print(f"Area of circle with {radius} is {area} and its circumference is {circum}")
```
> **NOTE:** 
> - how much easier it is to return multiple values from a function in python. (PTSD from C++ & Java)
> - Remember that the round(number, decimal_points) rounds the number passed to it to the desired decimal points and it doesn't require the math library

---

### Q5. Default params 

- Make a function to greet a user. 
- If no name is provided then use a default name
- **Soltion**
```python
def greeting(name='user') : 
    return "Hello "+name

print(greeting("Soma"))
print(greeting())
```
-**NOTE** how we assign a default value in the function.

---

### Q6. Lambda Functions

- aka _anonymous function_ are basically **functions without a name** 
- These are powerful when we are simple or one line functions. 
- These are mostly used more in frameworks (like Danjo and Flask)
- Create a Lambda function to compute the cube of a number 

- **Solution**
```python 
result = lambda x : x**3
print(result(3))
print(result(5))
print(result(7))
```

---

### Q7. Functions with *args

- variable number of arguments was a common problem in python, so they solved this issue using the keyword : `*args` (short for argument)

- Write a function which takes variable number of arguments and returns their sum
- **Solution**
```python 
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5))
print(sum_all(1, 2, 3, 4, 5, 6, 7))
```
> **NOTE:**
> - The * is important as it allows you to pass any number of arguments
> - The multiple elements are being passed as tuple (which itself is a iterable)
> - Hence we can manually also sum them up using an iterator tool. Eg : 
> ```python
> def sum_all(*args):
>    print('Type of args :',type(args))
>    sum = 0 
>    for num in args : 
>        sum+=num
>    return sum
>print("Sum of 1+2+3 = ",sum_all(1, 2, 3))
> ```
> - **Output:** 
> ```
> <class 'tuple'>
> 6
> ```
> ___

---

### Q8. Functions with **kwargs

- **`**kwargs`** is used when we are receiving unknown number of arguments in `key:value` format
- `**` are used and the handling is a little different from the normal `*args`.
- This is because instead of a `tuple`, this time the variable arguments are passed as a `dictionary`

<br>

- Write a function which takes variable number of keyword arguments and prints them in key:value format
- **Solution**
```python 
def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(key,value)

print_kwargs(name='Batman', powers='Rich')
print_kwargs(name='Superman', power1='Super strength', power2='Flight', power3='Super Speed')
```

---

### Q9. Generator Function with yield

- `Generator` functions example is the `range()` function in python. 
- They are called multiple times and they _remember_ **who called** them and **till what value/iteration** they have returned.
- So when the next time they are called, the send back the next item / next iteration
- `yield` is a keyword that function similar to return but it is used in Generator functions to return one iter at a time and return the next iteration when it called again.
- `yield` is used to keep the **function** and it's **current state** in the **`memory`**

<br>

- Write a `generator` function that `yields` even numbers up to a specified limit.
- **Solution**
```python 
def even_generator(limit):
    for i in range(2, limit+1, 2):
        yield i
        
for num in even_generator(10):
    print(num)
```

---

### Q10. Recursive Functions

- Write a recursive function to return the factorial of a number
- **Solution**
```python 
def factorial(num):
    if num == 0 : return 1
    return num * factorial(num-1)
print(factorial(5))
print(factorial(3))
```