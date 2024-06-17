# Loops in Python (iterables)

---

- **`Loops`** in python are treated a _little differently_ **internally**. 
- It in important to understand the _inner working_ of the `loops` in python in order to get more comfortable with it.

---

## Internal working of loops

- Python looks at loops like `for`, `while`,comprehensions, etc as **iteration tools**. 
- Hence _iteration tools_ can only be used on **iterable objects**. Eg : 
  - Lists
  - Tuples
  - Set
  - Dictionaries
  - Strings
  - file (this one's iteration is a little different, but it is a iterable object nonetheless)
- Another item important to loops in python is the **`__next__`** which is a **response**

---

### Basics of looping in python ( iter(),next() )

- Any `Iterable tool` will loop over an `iterable object` in the following steps : 

1. `__iter__`  is called to check if the object is iterable or not
2. `__next__` is sent back as a _response_ (which is usually a memory location from where the list starts in memory) 
3. `__next__` is called again until `__next__` raises `StopIterationException` which tells the iteration tool when to stop iterating

---

### How iterating over a file is different 

- Consider the following `.py` file : 
```python 
import time 
print("Soma is my best friend")
username = "Bunny"
print(username)
```
- we can open a file in python using the `.open('filename.ext')` method
- we can then print one line at a time using the `.readline()` method : 
```python
>>> file = open('test.py')
>>> file.readline()
'import time \n'
>>> file.readline()
'print("Soma is my best friend")\n'
>>> file.readline()
'username = "Bunny"\n'
>>> file.readline()
'print(username)'
>>> file.readline()
''
>>> file.readline()
''
>>>
```
- Once it reached the end of file character (here ''), it doesn't move more ahead in memory - This is because there is no **`__next__`** response from the `file` object.
- we will have to import the file again to start over.
- We can see how the `.__next__` is used (it is the core syntax of `iterables` which makes them iterable)
```python
>>> file = open('test.py') 
>>> file.__next__()
'import time \n'
>>> file.__next__()
'print("Soma is my best friend")\n'
>>> file.__next__()
'username = "Bunny"\n'
>>> file.__next__()
'print(username)'
>>> file.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
```
- As we can see cause it is raw code, the exceptions are not handle in this method. 
- But do note that the final error is `StopIteration` exception.
- We can even print these lines in loops : 
```python
>>> file = open('test.py') 
>>> for line in file : 
...     print(line)
... 
import time 

print("Soma is my best friend")

username = "Bunny"

print(username)
>>>
```
- Notice hwo there is an extra line ('\n') after each line. This is cause there is a '\n' in the raw file lines and another which is made cause fo the `print()` function.
- We can avoid this by using the `end` parameter in `print()` function :
```python
>>> file = open('test.py') 
>>> for line in file : 
...     print(line, end="")
... 
import time
print("Soma is my best friend")
username = "Bunny"
print(username)
>>>
```
- now only the raw \n in the file lines will be read.
- We can do the same using while loop, but the syntax will change : 
```python 
>>> file = open('test.py'))
>>> while True :  
...     line = file.readline()
...     if not line : break
...     print(line, end='')
... 
import time 
print("Soma is my best friend")
username = "Bunny"
print(username)>>>
```
- **NOTE:** `not` keyword just checks to see if the variable is empty or not. 
- This happens as empty variables are false values and non-empty variables are true values by default (Read more about `Truthy` & `Falsy` [here](https://www.freecodecamp.org/news/truthy-and-falsy-values-in-python/)).
- **NOTE:** file comes with it's own iteration tool (unlike other data types like lists, dicts,etc)

---

### Iterating Over Lists in python

- Remember how we had mentioned that iter() returns the memory location of where the list starts.
- We can use `iter(iterable)` function to get that exact memory location like this : 
```python 
>>> l1 = [1,2,3,4,5]
>>> I = iter(l1)
>>> I
<list_iterator object at 0x000002255D37BBE0>
>>>
```
- We can go over the items of the list using the `__next__()` method : 
```python 
>>> I
<list_iterator object at 0x000002255D37BBE0>
>>> I.__next__() 
1
>>> I.__next__()
2
>>> I
<list_iterator object at 0x000002255D37BBE0>
>>> I.__next__()
3
>>> I.__next__()
4
>>> I.__next__()
5
>>> I.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> I
<list_iterator object at 0x000002255D37BBE0>
```
- **BUT** do note that the I (`iter()`) value doesn't change at all thought the looping process.
- It will always point to the starting memory location of the list 

<br>

- This `iter()` object is there in files by default.
- So we do not need to `iter(file_ref)` as this has already been done while opening the file. (this is just how the internal of python work)
- Hence both of them are the **same** thing.
- We can even verify this by using the `is` keyword : 
```python 
>>> file_ref = open('test.py')
>>> file_ref is iter(file_ref)
True
>>> file_ref is file_ref.__iter__()
True
```

<br>

- Do note that this is **only** true for file objects. This is **not** true for Lists and other iterable objects.
- Eg: 
```python
>>> l1 = [1,2,3]
>>> iter(l1) is l1
False
>>> l1.__iter__() is l1
False
```
---

### Playing with Iterables 

- we can iterate over dictionaries in many ways:
```python
>>> D = {'a':1,'b':2,'c':3}
>>> for keys in D.keys() : 
...     print(keys)          
... 
a
b
c
```
- We can also get it's `iter()` object and use the `next(iter_ref)` to loop over it.
```python
>>> I = iter(D)
>>> I
<dict_keyiterator object at 0x0000029869615AD0>
>>> next(I)
'a'
>>> next(I)
'b'
>>> next(I)
'c'
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
```

<br>


- Remember `range()` is also an iterable object.
- Eg: 
```python 
>>> range_ref = range(5)  
>>> range_ref
range(0, 5)
>>> I = iter(range_ref)
>>> I    
<range_iterator object at 0x000002986935BB70>
>>> next(I)
0
>>> next(I)
1
>>> next(I)
2
>>> next(I)
3
>>> next(I)
4
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
```

---

## Practice Problems 

### Q1. Positive numbers 
- given a list of numbers, determine count of positive numbers.
- **Solution**
```python
l1 = [1,-2,-3,4,-5,-6,7,-8,9,10]
count = 0
for num in l1 : 
    if num < 0 : 
        count += 1

print(f"Count : {count}/{len(l1)}")
```

---

### Q2. Sum of Even Numbers 
- given a list of numbers, determine sum of even numbers up to 'n' number.
- **Solution**
```python
while True : 
    try: 
        n = int(input("Enter n :\n"))
        break
    except ValueError:
        print("Invalid Input")
sum = 0
for i in range(n+1):
    if i%2 == 0: 
        sum+=i

print(f"The sum  even numbers up to {n} = {sum}")
```

### Q3. Multiplication Table printer

- Print the Multiplication table of given 'n'
- But skip the 5th iteration
- **Solution**
```python
while True : 
    try: 
        n = int(input("Enter n :\n"))
        break
    except ValueError:
        print("Invalid Input, try again...")

for i in range(1,11):
    if i == 5 :
        continue
    else : 
        print(f"{n} x {i} = {n*i}")
```
---

### Q4. Reverse a String using loops

- reverse the string given **using loops**
- **Solution**
```python
str = input("Enter your string : ")
rev_str = ""

for char in str:
    rev_str = char+rev_str
print("Reversed String : ",rev_str)
```
---

### Q5. Find the first non-repeated character

- given a string find the first non-repeated character
- **Solution**
```python
str = input("Enter your string : ")

for char in str : 
    if str.count(char)==1 :
        print(char)
        break
```
---

### Q6. Find Factorial

- find the factorial for a number using **while loop**
- **Solution**
```python
while True : 
    try: 
        n = int(input("Enter n :\n"))
        if n > 0 :
            break
        else : 
            raise ValueError
    except ValueError:
        print("Invalid Input, try again...")

factorial = 1
while n > 0 : 
    factorial *= n
    n -= 1
print(factorial)
```
- **NOTE:** `raise` keyword (is like `throw` in java) is used to throw an exception in python.

---

### Q7. Valid Input

- Keep asking user for input until they give an integer between 1 and 10.
- **Solution**
```python
while True : 
    try: 
        n = int(input("Enter n between (1,10):\n"))
        if 0 < n < 11 :
            break
        else : 
            raise ValueError
    except ValueError:
        print("Can't even follow basic instructions 😐? try again...")
print("Congratulations...you can follow basic instructions. 🙄")
```

### Q8. Prime Number Checker

- check if a number is prime 
- prime number is only divisible by itself & 1  
- **Solution**
```python
while True : 
    try: 
        n = int(input("Enter an number (greater than 1) :\n"))
        if n<=1 :
            raise ValueError
        else : 
            break
    except ValueError:
        print("Can't even follow basic instructions 😐? try again...")

is_prime = True
for i in range(2,n//2) : 
    if n%i == 0 : 
        is_prime = False
        break
if is_prime : 
    print("Prime number ✅")
else : 
    print("Not Prime number ❌")
```

### Q9. List Uniqueness Checker 

- check if all the elements in the list are unique.
- If a duplicate element is found, exit and print the duplicate element
- **Solution**
```python
l1 = ['apple','oranges','mango','banana','grapes','mango']
l2 = ['soma','bunnu','hoods']

flag1 = True
flag2 = True

for element in l1 : 
    if l1.count(element)>1:
        flag1 = False
        print(element)
        break
for element in l2 : 
    if l2.count(element)>1:
        flag2 = False
        print(element)
        break

if flag1 : 
    print("List 1 is Unique ✅")
else : 
    print("List1 is not Unique ❌")
    
if flag2 : 
    print("List 2 is Unique✅")
else : 
    print("List2 is not Unique ❌")
```
- another approach : 
```python 
l1 = ['apple','oranges','mango','banana','grapes','mango']
l2 = ['soma','bunnu','hoods']

unique_items = set()

for i in l1:
    if i in unique_items:
        print("Duplicate found : ",i)
        break
    else:
        unique_items.add(i)
for i in l2:
    if i in unique_items:
        print("Duplicate found : ",i)
        break
    else:
        unique_items.add(i)
```

---

### Q10. Exponential Backoff 

- Implement a exponential backoff algorithm
- Which doubles the wait time after each retry starting from 1 second, but stops after 5 retries
- **Solution**
```python 
import time 

wait_time = 1
attempts = 0
max_retries = 5

while attempts != max_retries :
    print(f"retrying {attempts} time...")    
    print(f"waiting for {wait_time} seconds")
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
print("Failed")
```