# Dictionary in Python

--- 

- `dict` are declares using `{}`
- They have a `key` and `value` pair which are together called a `item`.
- The `key` are like indexes of a list. Using the `key` we can fetch the `value`.
```
>>> dict = {'name':'soma','design':'bff','nickname':'senpai'}
>>> dict['name'] 
'soma'
```
- We can also make use of the `.get('key')` function of dict to fetch the value. 
- This is more useful because it doesn't throw an error if the key is not present in the dict 
```
>>> dict.get('name')
'soma'
>>> dict.get('nicknameS')
>>>
```
- We can also use the `in` operator to check if the `key` is present in the dict
```
>>> 'name' in dict
True
```

- Adding a new `item` (or `key:value` pair) into a `dict` : 
```
>>> dict['likes'] = 'bunny'
>>> dict                     
{'name': 'Somya', 'design': 'bff', 'nickname': 'senpai', 'likes': 'bunny'}
>>>
```

- Updating values of `dict` is also pretty straight forward: 
```
>>> dict['name'] = 'Somya'     
>>> dict
{'name': 'Somya', 'design': 'bff', 'nickname': 'senpai', 'likes': 'bunny'}
```
- **Remember** that `dict` are also mutable types. That's why we are to change the values in it even after declarations.

<br>

- `.pop('key')`: removes that `key:value` from the dict
- **NOTE** that this `.pop()` function requires a key (unlike a list)
- This also like the `pop()` function of list, returns the popped value back.
```
>>> dict.pop('likes')
'Somya'
>>> dict
{'name': 'Somya','design': 'bff', 'nickname': 'senpai'}
>>>
```
- But cause the essence of .pop() is to remove elements from the back, we can use...
- `.popitem()` function removes the item in the end of the dict and 
  - returns the `key:value` of the popped pair.
```
>>> dict.popitem()
('nickname', 'senpai')
>>> dict
{'name': 'Somya','design': 'bff'}
```
<br>

- `del dict['key']` : deletes that `key:value` from the `dict`.
  - unlike the above 2 methods, it doesn't return anything.
```
>>> dict
{'name': 'Somya','design': 'bff'}
>>> del dict['design']
>>> dict
{'name': 'Somya'}
```

- `.clear()` : removes all the `key:value` pairs from the dict
```
>>> dict
{'name': 'Somya'}
>>> dict.clear()
>>> dict
{}
```



---

# Looping in Dictionaries 

- by default , when we try to loop over an `dict`, we loop over the `keys` of the dictionary : 
```
>>> for field in dict : 
...     print(field)
... 
name
design
nickname
>>>
```
- We can also print the `values` of the dictionary 
```
>>> for key in dict : 
...     print(key, dict[key])
... 
name Somya
design bff
nickname senpai
>>>
```
- Using `.items()` is another way of doing the above
- It returns the key:value pair as a single item.
```
>>> for key, value in dict.items() : 
...     print(key, value)
... 
name Somya
design bff
nickname senpai
```

- Using the `len()` we can see how many items (or `key:value` pairs) are there in the `dict`.

---

# Making Copies of Dictionary 

- **Remember** when we use '=' we only pass the ref of the object in memory. 
- Thus to make a copy of the item we can use `copy()`
```
>>> dict1 = {'name':'soma','design':'bff','nickname':'senpai'}
>>> dict2 = dict1.copy()
>>> dict2
{'name': 'soma', 'design': 'bff', 'nickname': 'senpai'}
```

--- 

# Dictionary within Dictionary

- Similar to how we can have `lists` inside another `lists`, we can also have `dicts` inside another `dicts`.
- Eg:
```
>>> friends = {
... "Somya" : {'nickname':'soma senpai','doing':'job','met':'12th'},
... "Rishab" : {'nickname':'Hoods','doing':'IFS exam','met':'9th'},
... "Abhinav" : {'nickname':'Bunnu','doing':'Homeopathy','met':'9th'}
... }
```
- These internal `dicts` can be accessed using their respective keys
```
>>> friends.get('Somya') 
{'nickname': 'soma senpai', 'doing': 'job', 'met': '12th'}
>>> friends['Somya']['nickname']
'soma senpai'
>>>
```

---

## Dictionary comprehension

- Similar to `list` comprehension we can have comprehension statements in dictionaries also , which we can use to generate entire `dicts`
```
>>> squaredDict = {x:x**2 for x in range(1,11)}
>>> squaredDict
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
>>> cubeDict = {x:x**3 for x in range(1,11)}
>>> cubeDict
{1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}
>>>
```
<br>

- We should also be familiar with making `dicts` from given lists of keys and values
```
>>> keys = ['k1','k2','k3']
>>> default_value = ['value']
>>> newDict = dict.fromkeys(keys, defualt_value)
>>> newDict
{'k1': 'value', 'k2': 'value', 'k3': 'value'}
>>>
```
- We can also make a `dict` from two `lists` of keys and values with the help of the `.zip()` function
```
>>> keys = ['k1','k2','k3']
>>> values = ['v1','v2','v3']
>>> dictionary = {k:v for k,v in zip(keys,values)}
>>> dictionary
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
```
- `.zip()` method creates a iterable of pairs taking one value from each list making them into a tuple like : ('k1','v1'), ('k2','v2'), ('k3','v3'),... and so on.