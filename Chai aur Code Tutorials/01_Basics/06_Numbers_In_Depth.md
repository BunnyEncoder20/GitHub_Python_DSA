# Numbers in Python

---

- Python is a very number precise language. 
- Though strings are also very powerful in python, but it is especially good at handling numbers (very large numbers precisely & various types of number representations).

- Numbers in Python is a Group of data types : 
  - Int
  - Float
  - Decimal
  - Exponential 
  - Boolean
  - Sets (to some extend are treated like numbers only)

- Whenever we are trying to do multiple operations in a single expression, we must use **parenthesis** `()` to group which operations to perform first.
- This makes the operations fool-proof and also makes the code more readable and understandable.

- We should explicitly take care that when doing operations together (Eg: 40 + 2.25), both the operands should be of the same data type (though python can easily add float and int together).
- Better way to do this would be to convert the operands to the same data type and then do the operation.
```
float(40) + 40.25
```

- Do keep in mind that there is `overloading` in operators in python (like almost all programming languages)

- Note that when we type code lines like : 
```
>>> x,y,z
(1,2,3)
```
- The resultant will be a tuple. We can also update values in the same way. Just expect to get back a tuple when you write lines like this.
```
>>> x+2, y*2, 3**3
(3, 4, 21)
```

- One of Python's _super power_ is the capability to handle almost `infinite` number lengths. Eg: 
```
>>> 2**100
1267650600228229401496703205376
>>> 2**1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376 
```
- Most other programming languages will fail even at 2<sup>100</sup>, but python can handle even 2<sup>1000</sup> very easily.
  
- Python also handles even imaginary numbers operations like : 
```
>>> (1+2j) * 3
(3+6j)
```

---

## Booleans 

- Mostly Booleans in python are treated as numbers only 
  - 0 is `False`
  - 1 is `True`
```
>>> True == 1
True
>>> False == 0
True
```
- In fact many documentations suggest that Booleans are just number 0 and 1 with wrappers build on top of them.
- Hence we can see Jack shit like : 
```
>>> True + 4
5
>>> False * 10
0
```
- When we use the `is` operator , we can see that in memory they are treated differently: 
```
>>> True is 1
<stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
False
>>> False is 0
<stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
False
```


- We are familiar with the the `and` and `or` operators : 
  - `and`: returns true only when both operands are true
  - `or`: returns true when either of the operands is true
- Eg : 
```
>>> x < y < z
True
```
- The above line is equivalent to : `x < y and y < z`


---

# `math` library in Python

- can be imported using `import math`
- Is one of the in built packages which comes with python installation.
- It comes with many more numeric based operations. Eg: 
```
>>> import math
>>> math.floor(3.5)
3
>>> math.floor(-4.8)
-5
>>> math.floor(3.9)
3
```
- Do note that `math.floor` will always give you the number which is lower (on the number line).
- Hence when we floor a negative number, we get the next higher negative number.

- `math.trunc()` pushes the numbers towards 0 (on the number line). So it'll handle negative numbers in a different way
```
>>> math.trunc(2.9)
2
>>> math.trunc(-2.2)
-2
>>> math.floor(-2.2)
-3
```

---

## Different Base Numbers in Python

- Python can also handle numbers of other bases by default.
    - 0b : Binary
    - 0o : Octal
    - 0x : Hexadecimal
- Eg:
```
>>> 0b1000
8
>>> 0xFF
255
>>> 0o20
16
```
- You could also use the int() directly for converting the given base representation to an integer. 
```
>>> int('0b1000000', 2)
64
>>> int ('0o100', 8) 
64
>>> int('0x40',16)
64
```
- Practically irl applications, we will converting decimal numbers  into these other number bases (rather than the opposite).
- Python has functions for doing that:
```
>>> bin(64)
'0b1000000'
>>> oct(64)
'0o100'
>>> hex(64)
'0x40'
```
---

## `random` library in Python

- one of the most used functions of library 'random' is `.random()` 😏
```
>>> import random
>>> random.random()
0.9587324005445979
>>> random.random()
0.9540444378052784
```
- By default, random.random() will give you a decimal between 0 and 1. But we can specify the range (easier than JS) and also the Number type we would want 
- Eg:  if we want an integer between the range 0 and 10
```
>>> random.randint(0,10)
3
>>> random.randint(0,10)
5
>>> random.randint(0,10)
10
```
- `random.choice()` will give you a random element from the list
```
>>> l1 = ['Batman','Madara','Sukuna','Sasuke']
>>> random.choice(l1)
'Batman'
>>> random.choice(l1)
'Sukuna'
>>> random.choice(l1)
'Madara'
>>> random.choice(l1)
'Sasuke'
>>> random.choice(l1)
'Batman'
```
- `random.shuffle()`: shuffles the order of the elements in the list
```
>>> l1 = ['Batman','Madara','Sukuna','Sasuke']
>>> random.shuffle(l1)
>>> l1
['Sasuke', 'Sukuna', 'Madara', 'Batman']
>>> random.shuffle(l1)
>>> l1
['Sasuke', 'Madara', 'Sukuna', 'Batman']
```

---

## Handling Decimal Numbers in Python

- Python sometimes is not able to handle complex operations on simple decimal numbers
- And does Jack shit like : 
```
>>> 0.1+0.1+0.1      
0.30000000000000004
>>> 0.1+0.1+0.1 - 0.3
5.551115123125783e-17
>>> (0.1+0.1+0.1) - 0.3 
5.551115123125783e-17
```
- To make it much better, we can import the **Decimal Context Manager**
```      
>>> from decimal import Decimal   
>>> Decimal('0.1')+Decimal('0.1')+Decimal('0.1')   
Decimal('0.3')
>>> Decimal('0.1')+Decimal('0.1')+Decimal('0.1') - Decimal('0.3') 
Decimal('0.0')
```
- Similarly, there is a **Fraction context Manager** for handling fractions in a similar way.

---

# Sets (the Mathematical one) in Python

- defined by : `set1 = {1,2,3,4,5}`
- On these sets, we can do all the operations which we were doing on sets in mathematics
- Eg: 
```
>>> set1 = {1,2,3,4,5}
>>> set2 = {4,5,6,7,8}
>>> set1 & set2
{4, 5}
>>> set1 | set2
{1, 2, 3, 4, 5, 6, 7, 8}
>>> set1.union(set2)
{1, 2, 3, 4, 5, 6, 7, 8}
>>> set1.intersection(set2)
{4, 5}
>>> set1 - set2
{1, 2, 3}
>>> set2 - set1 
{8, 6, 7}
```
> **NOTE:** 
> - When we declare an empty set or when we get an empty set as a resultant, we do not get empty braces **{}** as a result. We get **set()**.
> - This is because **{}** denotes is a empty dictionary (dict)
> You can check the type of a object by using the **type()** function.
> Eg:
> ```
> >>> set1 - set2
> {1, 2, 3}
>>> set1 - set2 - {1,2,3} 
> set()
> >>> type(set1 - set2 - {1,2,3}) 
> <class 'set'>
> >>> type({})
> <class 'dict'>
> ```

