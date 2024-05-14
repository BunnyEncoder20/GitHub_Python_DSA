# Strings in Python

---

- Strings can be given in 
    - `Single quotes`: ('allows embedded "double" quotes')
    - `Double quotes`: ("allows embedded 'single' quotes")
    - `Triple quoted`: ('''Three single quotes''', """Three double quotes""")


- People tend to over complex slicing in strings. Basically
  - syntax : `string[start:stop:step]`
  - if you skip `start`,`stop` or `step`, the **default** values for them are taken (`start`=0, `stop`=last index, `step`=1)
  - Eg : 
```
>>> bff = "somasenpai"
>>> bff[0]
's'
>>> bff[0:4]
'soma'
>>> bff[-1]
'i'
>>> bff[4:]
'senpai'
```
- Slicing can be completely understood in a nutshell from this simple example:
```
>>> numlist = '0123456789'
>>> numlist[:]
'0123456789'
>>> numlist[:5] 
'01234'
>>> numlist[5:] 
'56789'
>>> numlist[3:8] 
'34567'
>>> numlist[::2] 
'02468'
>>> numlist[0:9:3] 
'036'
```
- If we put a **negative number** for `start` or `stop`, it'll take that index character from the _back_ of the list.
- If we put a **negative number** for step, it'll print the list counting (or printing) from the back. So we essentially get the reversed string.
- **Eg:**
```
>>> numlist[-5:-1] 
'5678'
>>> numlist[::-1]  
'9876543210'
```

--- 

# Methods of Strings

- Most of the strings in python are unicode strings 
- Python also supports other string encoding.

- Remember that when we use any method on a string, the original string remains unchanged cause strings in python are immutable types.

1. `lower()`
```
>>> bff = 'SomA SenpaI'
>>> bff.lower()
'soma senpai'
>>> bff
'SomA SenpaI'
```

2. `upper()`
```
>>> bff = 'SomA SenpaI'
>>> bff.upper()
'SOMA SENPAI'
>>> bff
'SomA SenpaI'
```

3. `strip()`
```
>>> bff = "  Soma  "
>>> bff.strip()
'Soma'
>>> bff
'  Soma  '
```


4. `.replace('replace this' , 'with this')`
```
>>> bff = 'soma senpai'
>>> bff.replace('s','t')
'toma tenpai'
>>> bff.replace('soma','bunny')
'bunny senpai'
>>> bff
'soma senpai'
```

5. `split('separator char')`: splits the string into seperate elements and returns there list
```
>>> friends = 'soma, bunnu, hoods'
>>> friends.split(', ')
['soma', 'bunnu', 'hoods']
```

6. `.join('char to put in between')`: used for joining the elements of a list into a string
```
>>> friends = ['soma','bunnu','hoods']
>>> char_in_between = ""
>>> char_in_between.join(friends)
'somabunnuhoods'
>>> char_in_between = " "
>>> char_in_between.join(friends)
'soma bunnu hoods'
>>> char_in_between = ", "
>>> char_in_between.join(friends)
'soma, bunnu, hoods'
>>> char_in_between = " -> " 
>>> char_in_between.join(friends)
'soma -> bunnu -> hoods'
```

7. `.find('char/string')`: finds a specific character and returns its index otherwise returns -1 if not there.
```
>>> bff = 'soma senpai'
>>> bff.find('senpai')
5
>>> bff.find('Senpai')
-1
```

8. `.count('char/string')`: counts the number of occurrences of a specified character / string
```
>>> bff = 'soma senpai'
>>> bff.count('s')
2
>>> bff.count('senpai')
1
```
---

1. `.format(list)`: used to insert variables into a string.
```
>>> bff,edible = 'soma','dessert'
>>> str = 'I want to eat {} for {}'
>>> str
'I want to eat {} for {}'
>>> print(str.format(bff,edible)) 
I want to eat soma for dessert  😏
```

2. `len(str)`: used for getting the length of the string
```
>>> bff = 'soma senpai'
>>> len(bff)
11
```
3. `for char in string:` : for loop for looping over each char in the string 
```
>>> for char in "soma" :     
...     print(char)
... 
s
o
m
a
```

> **NOTE:**
> - When making paths or any sting with forward slashes, it creates a lot of issues when dealing with windows paths (Fooking windows always).
> - This is cause forward slashes are unicode characters and so they will cause an error. Also the string cannot end with a \ , so there is a lot of issues 
> ```
>  >>> dir_path = 'C:\Users\gener\Coding\GitHub Python DSA\Chai aur Code Tutorials\01_Basics'
>   File "<stdin>", line 1
>     dir_path = 'C:\Users\gener\Coding\GitHub Python DSA\Chai aur Code Tutorials\01_Basics'
>                                                                                           ^
> SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
> ```
> - A solution is to use **raw strings** in the following manner : 
> ```
> >>> dir_path = r'C:\Users\gener\Coding\GitHub Python DSA\Chai aur Code Tutorials\01_Basics'
> >>> print(dir_path)
> C:\Users\gener\Coding\GitHub Python DSA\Chai aur Code Tutorials\01_Basics
> ```

4. `char in string`: the `in` keyword is used to check if a given char/string is present in the string or not
```
>>> bff = "Soma senpai is my best friend's pet name."
>>> "senpai" in bff
True
>>> "bunny" in bff  
False
```