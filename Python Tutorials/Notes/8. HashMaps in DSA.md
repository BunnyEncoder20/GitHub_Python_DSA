# HashMaps in DSA Python 
---

- Imagine we are trying to store the data for stock prices and we want to search a day which has a specific value of stock :
 
| Date | Value |
|------|-------|
| 6-Mar | 310 |
| 7-Mar | 340 |
| 8-Mar | 380 |
| 9-Mar | 302 |
| 10-Mar | 297 |
| 11-Mar | 323 |

- Then we might do something like : 
```
stock_prices = [
    ['6-Mar',310],
    ['7-Mar',340],
    ['8-Mar',380],
    ['9-Mar',302],
    ['10-Mar',297],
    ['11-Mar',323],
]  

for element in stock_prices:
    if element[0] == '9-Mar' :
        print(element[1])               # O(n)

```
- This is a brute force approach and has a time complexity of order of n - `O(n)`
- Instead of using something like arrays or lists , python has another data structure called Dictionary which can do the same task in order of 1 time complexity - `O(1)`
```
stock_prices_dict = {
    '6-Mar':310,
    '7-Mar':340,
    '8-Mar':380,
    '9-Mar':302,
    '10-Mar':297,
    '11-Mar':323,
} 

print(stock_prices_dict['9-Mar'])       # O(1)
```
- Hence for this particular situation, using a dict makes more sense as it can get the same thing done in less time complexity
- Let's us look at internal working of a dictionary which uses hash table as the underlying data structure

---

## How Dictionary work under the hood

- when we were storing the above mentioned data in the form of a `list`, it was getting stored in the memory something like this : 
![Image](./Notes%20Assets/liststorage.png)
- These are **contiguous memory** locations on our ram.
- When the same data was being stored as a `dict` it looked something like this : 
![Image](./Notes%20Assets/dictstorage.png)
- The _Hash function_ is simply a function which is used to map the `key` of the dictionary to a specific `index` of the allocated memory
- Hash tables, hash maps are the same things. They are the **underlying data structure** and `Dictionary` is a _python specific implementation_ of **HashMap** 
![Image](./Notes%20Assets/arrvsdict.png)
- As seen above, the array `index` is a number but dictionary's `key` (can also be seen as an index) is a string. So these are similar in behavior
  
---

### Complexity 
 
For a dictionary / hashMap
- Look up by key is O(1) on average
- Insertion/ Deletion is 0(1) on average

Hash maps in various languages
![Image](./Notes%20Assets/hashmapinlangs.png)

---

### Implementing HashMap in Python 

1. We are going to need a hash function
```
def getHash(key) : 
        h = 0 
        for char in key : 
            h+=ord(char)        # ord just returns the ASCII value of the character
        return h%100
```
2. We implement an class for the hashmap : 
```
class HashTable :
    def __init__(self) :
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]  # adding 100 elements here using list comprehension
    
    def getHash(self, key) : 
        h = 0 
        for char in key : 
            h+=ord(char)        
        return h % self.MAX
```
3. Adding items into Hash Map and retrieving items from hash map
```
class HashTable :
    def __init__(self) :
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]  # adding 100 elements here using list comprehension
    
    def getHash(self, key) : 
        h = 0 
        for char in key : 
            h+=ord(char)        # ord just returns the ASCII value of the character
        return h % self.MAX

    def add(self,key,value) :
        idx = self.getHash(key)
        self.arr[idx] = value
        return 
    
    def get(self, key) :
        idx = self.getHash(key)
        if self.arr[idx] is not None:
            return self.arr[idx]
        else :
            print("No element on given index")


t = HashTable()
t.add('9-Mar',310)
print(t.get('9-Mar'))
```
- Right now we are adding and retrieving items like a regular function call. If we want make it feel more like a regular python dictionary, we can do it using Python operators, documentation can be found [here](https://docs.python.org/3/library/operator.html).
- Using the `.__getitem__(a,b)` will lets us get the value like a dict : 
```
t['9-Mar']
```
- Using the `.__setitem__(a,b,c)` we will be able to set values like a dict : 
```
t['9-Mar] = 330
```
- Think of a as the dictionary instance (`self`), b as the `key` and c is the `value` of the key
- Hence we can replace the `add()` & and `get()` & functions with `__setitem__()` & `__getitem__()` as : 
```
class HashTable :
    def __init__(self) :
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]  
    
    def getHash(self, key) : 
        h = 0 
        for char in key : 
            h+=ord(char)        
        return h % self.MAX

    def __setitem__(self,key,value) :
        idx = self.getHash(key)
        self.arr[idx] = value
        return 
    
    def __getitem__(self, key) :
        idx = self.getHash(key)
        if self.arr[idx] is not None:
            return self.arr[idx]
        else :
            print("No element on given index")

```
- and we can change the calling of these functions to : 
```
t['9-Mar'] = 310        # calls the __setitem__()
print( t['9-Mar'] )     # calls the __getitem__()
```
- To check out the entire array and how the values are been stored : 
```
print(t.arr)
```
- Outputs : 
```
[310, 350, 280, None, None, None, 330, None, None, None]
```
- We can remove elements using the `__delitem__(self,key)` operator. It's fucntion will look like : 
```
def __delitem__(self,key) :
        idx = self.getHash(key)
        self.arr[idx]=None
```
- and then we can delete elements like a dict using : 
```
del t['2-Apr']
```
- Outputs : 
```
[310, 350, 280, None, None, None, None, None, None, None]
```
- But we have yet to Handle Collisions. This is a very important feature for a hashmap
---

## Collisions Handling in HashMaps

**Collision** is when the hash function will give the same index for 2 different keys. A good hash function usually aims to give mostly unique idx for all but sometimes they are not always viable to have no collisions

1 **Chaining** 
- is a simple way to deal with collisions in `HashMaps`. Where a pre-allocated array elements are initialized as empty arrays (Lists).
- When an `key` is mapped to the same `idx` as a previous `key`, HashMap will now make a new node of linkedlist of that idx and store the new value in it.
- Usually, HashMap searching is of order `O(1)` 
- But in Chaining, in worse case it can go up to `O(n)` cause all the idx can have long linkedlist if the hashing function is not proper
- And then after going to the idx, it'll have to manually go through the linkedlist 
![Image](./Notes%20Assets/collisionchaining.png)

2. Linear Probing 
- In this method when collision happens, the HashMap linearly searches for the next empty memory block and stores the new value there
- If the spaces till the end are filled , it'll start from the top again 
![image](./Notes%20Assets/Linearprobing.png)

---

### Implementing Collision Chaining in HashMap

1. First we need to correctly initialize a empty list (array) as the elements of the Dict arr
```
def __init__(self) :
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
```
2. The `getHash` Function remains pretty much the same , but the other functions like `__getitem__()`,`__setitem__()`,`__delitem__()` need to be modified.
```
class HashMap :
    def __init__(self) :
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
    
    def getHash(self, key) : 
        h = 0 
        for char in key : 
            h+=ord(char)        
        return h % self.MAX
    
    def __setitem__(self, key, value) :
        idx = self.getHash(key)
        found = False 
        for i,element in enumerate(self.arr[idx]) :
            if(len(element)==2 and element[0]==key):
                element[1] = value
                found = True
                break 
        
        if not found : 
            self.arr[idx].append((key,value))
    
    def __delitem__(self,key) :
        idx = self.getHash(key)
        found = False 
        for i,element in enumerate(self.arr[idx]) :
            if(element[0]==key):
                del self.arr[idx][i] 
                found = True
                break 
        
        if not found : 
            print("Element with that key was not found in the HashMap")

    def __getitem__(self, key) : 
        idx = self.getHash(key)
        for i,element in enumerate(self.arr[idx]) :
            if(element[0]==key) :
                return element
```
3. We get to know that these 2 entries will give the same idx of 0: 
```
print("9-Mar : ",hm.getHash('9-Mar'))       # 0
print("10-Mar : ",hm.getHash('10-Mar'))     # 0
```
- So the Following should cause the data of _idx 0_ to get overridden 
```
hm['1-Mar'] = 100
hm['2-Mar'] = 200
hm['9-Mar'] = 300
hm['10-Mar'] = 400
```
- Hence this will cause a **collision**. But our `HasMap` is prepared to handle this and just inserts the value of the '10-Mar' into the new node (or idx) of the list 
```
# Seeing how the collision was handled
for element in hm.arr : 
    print(element)
```
- Outputs :-
```
[('9-Mar', 300), ('10-Mar', 400)]     
[]
[('1-Mar', 100)]
[('2-Mar', 200)]
[]
[]
[]
[]
[]
[]
```
- Seeing if the `get` function is working correctly : 
```
print(hm['9-Mar'])
print(hm['10-Mar'])
```
- Outputs : 
```
('9-Mar', 300)
('10-Mar', 400)
```
- Seeing if the `del` function is working correctly : 
```
del hm['10-Mar']
for element in hm.arr : 
    print(element)
```
- Outputs : 
```
[('9-Mar', 300)]
[]
[('1-Mar', 100)]
[('2-Mar', 200)]
[]
[]
[]
[]
[]
[]
```
### Hence everything is working as indented