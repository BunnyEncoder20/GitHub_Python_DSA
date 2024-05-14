# Lists in Python 

---

- As we have seen, strings are treated almost as Lists and hence things like indexing, slicing, sorting, etc is possible.
- These all can also be done in Lists.
- **Eg:**
```
>>> lists = ['batman','sukuna','madara','sasuke']
>>> lists[2]
'madara'
>>> lists[-1] 
'sasuke'
>>> lists[::2] 
['batman', 'madara']
>>> lists[:3] 
['batman', 'sukuna', 'madara']
>>> lists[2:] 
['madara', 'sasuke']
>>>
```
- **BUT** unlike strings, Lists are mutable in nature. So it is possible to change the elements of Lists at particular indexes.
```
>>> lists[1] = 'Sung Jinwoo'
>>> lists
['batman', 'Sung Jinwoo', 'madara', 'sasuke']
>>>
```


- It is preffered that when you are updating/changing values within a List, that we do not use slicing. This may lead to some unwanted behaviors as slicing makes python take the assigning value as an array.
```
>>> lists[1:2]
['Sung Jinwoo']
>>> lists[1:2] = 'Sukuna'
>>> lists
['batman', 'S', 'u', 'k', 'u', 'n', 'a', 'madara', 'sasuke']
```
- Because python treated the string as a list (or array) so it added the individual elements of the string to the list. 
- A work around this could be to assign the single value as one element array: 
```
>>> lists[1:2]
['Sung Jinwoo']
>>> lists[1:2] = ['sukuna']
>>> lists
['batman', 'sukuna', 'madara', 'sasuke'] 
```
- Similarly we can also replace multiple elements in the same way:
```
>>> l1[1:3]
['sukuna', 'madara']
>>> l1[1:3] = ['Itachi' , 'Sung Jinwoo'] 
>>> l1
['batman', 'Itachi', 'Sung Jinwoo', 'sasuke']
```

---

## Avoiding doing dumb shit like : 

1. Inserting at a position using slicing: 
```
>>> l1
['batman', 'Itachi', 'Sung Jinwoo', 'sasuke']
>>> l1[1:1]
[]
>>> l1[1:1] = ['test1','test2']
>>> l1
['batman', 'test1', 'test2', 'Itachi', 'Sung Jinwoo', 'sasuke']
```
2. Inserting nothing (to delete elements)
```
>>> l1[1:3]                     
['test1', 'test2']
>>> l1[1:3] = []
>>> l1
['batman', 'Itachi', 'Sung Jinwoo', 'sasuke']
```
---

## Some Intro to Conditionals and Looping in Lists

- **`Looping`** over the list using for : 
```
['batman', 'Itachi', 'Sung Jinwoo', 'sasuke']
>>> for char in l1 : 
...     print(char)
... 
batman
Itachi
Sung Jinwoo
sasuke
```
- we can also specify the end character of a print() function using end=' ' : 
```
>>> for char in l1 : 
...     print(char, end=' ')
... 
batman Itachi Sung Jinwoo sasuke
```
- This way we can make all the characters in the list on the same line. (or can add other characters in between).


2. Finding a element in a list using `in` : 
```
>>> 'sasuke' in l1
True
```
- we can apply conditional statements to these also like : 
```
>>> if "sasuke" in l1 : 
...     print("We have this Character !")
... 
We have this Character !
```

3. `.append(element)` method we can add elements to the end of the list.
```
>>> l1.append('Madara Uchiha')
>>> l1
['batman', 'Itachi', 'Sung Jinwoo', 'sasuke', 'Madara Uchiha']
```
4. `.insert(index,element)` method we can add an element at a particular index in the list
```
>>> l1
['batman', 'Itachi', 'sasuke']

>>> l1.insert(1 , "Madara")
>>> l1
['batman', 'Madara', 'Itachi', 'sasuke']
```

5. `.pop()` method removes the last element in the list and returns back the popped element.
```
>>> l1
['batman', 'Itachi', 'Sung Jinwoo', 'sasuke', 'Madara Uchiha']
>>> l1.pop()
'Madara Uchiha'
>>> l1
['batman', 'Itachi', 'Sung Jinwoo', 'sasuke']
```

6. `.remove(element)` method removes a specified element from the list and doesn't return anything
```
>>> l1.remove('Sung Jinwoo')
>>> l1
['batman', 'Itachi', 'sasuke']
```

7. `.copy()` method is used to make a copy of the object in memory. As we know `=` will give the reference to the same object. 
```
>>> l1
['batman', 'Itachi', 'sasuke']
>>> l1_copy = l1.copy()
>>> l1.insert(1 , "Madara")
>>> l1
['batman', 'Madara', 'Itachi', 'sasuke']
>>> l1_copy
['batman', 'Itachi', 'sasuke']
```

---

## List Comprehension 

- Using List comprehension we can generate lists.
- **Eg:**
```
>>> ten_numbers = [x for x in range(10)]
>>> squares = [x**2 for x in range(10)]
>>> cubes = [x**3 for x in range(10)]
>>> ten_numbers
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> cubes
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
```