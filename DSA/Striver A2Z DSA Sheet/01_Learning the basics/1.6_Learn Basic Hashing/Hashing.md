# Hashing in DSA (Very Important)

- If you don't know about hashing, you wouldn't be able to solve a lot of DSA questions 
>- Hashing in naive way can be defined by **pre-storing** some data and then **fetching** it later when needed. 
- In python hash maps are the Container Data Structure : **`Dictionaries`**
- They are very useful for 2 main reasons 
  - Custom keys for retrieving values is easier for development 
  - HashMaps allow for searching/fetching of values in `O(1)` time whereas arrays and LinkedList are `O(n)`
- HashMap use a **Hash function** to map the values to unique keys which can be retrieved in `O(1)` time.
- In most modern day languages, Hash maps are already implemented and so we do not need to worry about making hash functions.
- But in python we can use **collections** module to make our own hash function.
- Dictionaries Keys needs to be an **immutable Type**. We cannot make something which is mutable (like Lists, make em into an tuple if you need to make the list as a key).
- Dictionaries Need all the Keys to be initialized before altering their values otherwise it will raise a `KeyError`.
- You can use something like **`Collections.defaultdict(Type)`** to make a Dictionary with all the keys already initialized.
- The 3 main methods associated with HashMaps (or Python Dictionaries) are : 
  - `dict.keys()` - returns all the keys of the dictionary (by default dictionary will loop through all the keys)
  - `dict.values()` - returns all the values in the dictionary 
  - `dict.items()` - returns all the keys and values in the dictionary in form of tuples


<br>

- Take a scenario where we need to find the number of occurrences of each element in a array
  - `Time Complexity`: **O(q x n)** (q = number of elements in the list which count we need)
- This is not a good `Time Complexity` and can very well go up to **O(n<sup>2</sup>)**
- This situation is where something like Hashing is useful.
- Instead of doing the calculations for the count when needed, we can do some pre-calculations by making a **Hashing** (or frequency) **array** and then using it to store the frequency of each element of the original array.
- This is done efficiently by 
    1. Make an Hashing array and initialize all the elements to 0 (length = number of unique numbers in the number array).   
    2. Loop through the number array and for each number 'n', increase the value of at the position HashArray[n].
- This way by a simple O(n) time we have created a pre-fetched Hash array which now has the number of occurrences of each and every element in the Number array.

<br>

- Generally we can declare array size up to 10<sup>6</sup> in main function without memory segmentation errors. (can declare bigger ones as globals 10<sup>7</sup> at max)
- Hashing can also be done for characters
```python
from math import sqrt
import collections
def hash(arr:list)->list:
    hashed = {}
    for char in arr:
        if char in hashed:
            hashed[char]+=1
        else :
            hashed[char] = 1
    return hashed

if __name__ == '__main__':
    hashedArray = hash(['a','g','a','d','r','y'])
    for key in hashedArray:
        print(f"{key} : {hashedArray[key]}")
```
- Python **Collections** module also have a function called **`Counter`** that can be used to count the number of occurrences of each element in an array.
- It returns back a dictionary like looking Counter object back which contains all the elements(as keys) and their number of occurrences(as values).
  
<br>


- Hashing Function were implemented earlier using the 3 methods : 
  - `Division Method` - element % (number of unique elements) would give the key
  - `Folding Method` - no one asks anymore
  - `Mid-square Method` - no one asks anymore

<br>

- **Collisions** in HashMaps is when the hash function is not an optimal one and so, for 2 different elements, it returned back the same key.
- In case of collisions, we need to use **Hash Chaining**. Where the collisions elements are stored in a **LinkedList** of the same key. 
- So in absolute worse case of Hash function could assign all the elements into the same key (probability of this happening is almost 0) and thus in that case, searching and fetching in the HashMap could theoretically be **`O(n)`**