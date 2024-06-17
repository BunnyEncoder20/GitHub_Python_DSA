# Tuples in Python 

- We know that `Lists` are `mutable` in python.
- But there was also the need for a similar data type which was `immutable` in python.
- **`Tuples`** are `immutable` types which have a behavior similar to `Lists`.
- **Eg:** `Tuples` are made using `()` and follow the same operations as a basic `list`.
```
>>> tup = ('Batman','Madara','Sasuke','Sukuna')
>>> tup[1]
'Madara'
>>> tup[-1] 
'Sukuna'
>>> tup[:]  
('Batman', 'Madara', 'Sasuke', 'Sukuna')
>>> tup[1:-1] 
('Madara', 'Sasuke')
>>> len(tup)
4
```
- But as mentioned before these are `immutable` types:
```
>>> tup[1] = 'Soma'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>>
```
- We can also concatenate 2 tups together, similar to list s concatenations:
```
>>> more_tup = ('Itachi','Indra','Kakashi','Might Guy') 
>>> all_tup = tup + more_tup
>>> all_tup
('Batman', 'Madara', 'Sasuke', 'Sukuna', 'Itachi', 'Indra', 'Kakashi', 'Might Guy')
>>>
```
- Conditional keywords like 
    - `if` &
    - `in`
- also work with `Tuples`:
```
>>> if 'Madara' in all_tup : 
...     print('Yay')
... 
Yay
>>> if 'Madara' in more_tup:
...     print('Yay')
... 
>>> 
```
- `.count()` returns the number of times that item appears in the tuple:
```
>>> all_tup.count('Sasuke')
1
```
<br>

- We also use tuples to unwrap tuple values into multiple variables : 
```
>>> tup = (1,2,3)
>>> (one,two,three) = tup
>>> one
1
>>> two
2
>>> three
3
>>>
```
> **NOTE:** how the variable names are not in '' casue they are variables and not keys or anything.

<br>

- Similar to `lists` and `dicts` there can be nested tuples:
```
>>> nested_tup = (1,2,(3,4))
>>> nested_tup
(1, 2, (3, 4))
```