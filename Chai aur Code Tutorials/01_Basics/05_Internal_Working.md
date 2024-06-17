# Internal Working of Python (Copy, reference counts, slice)
---
- In previous lecture we saw how the internal memory management of the immutable and mutable data types works in python.
- But the internal working of python treats number types (because python is number precise language) and string types a little differently.
- In this md we'll take the look at this internal working of python.

---

## Reference Count

- This `ref count` keeps track of number of variables which are referencing to a particular object in memory.
- As we had seen, any object in memory with no references are removed from the memory. This is done by automatic `garbage collection` of python.
  
- We (easily at least) cannot look at the ref count in python because in python there is no mechanism to get so close to memory that we can get the exact ref count of a variable.

> **NOTE:** remember in python the data types are assigned **only in memory**. They are not assigned to the **variable**. So, variables (technically) do not have a data type. Only the object in memory has the data type with it.

- **Exception** in garbage collection when there is no ref for data types number and string. This is because python is optimized in a way so that it **doesn't immediately** removes these data types from memory as they are used a lot.

---

## Updating number types 

- Consider the following commands : 
```
>>> a,b = 5,2
>>> a
5   
>>> b
2   
>>> a = a+2
>>> a
7   
```
- As we have studies these lines will be executed as : 
    1. objects in memory are created of 5 & 2 and assigned to `a` & `b`
    2. In a = a + 2 first the a in the expression is replaced with it's reference value (5). The the new value is calculated for a (7).
    3. This causes python to create a new object in memory with value 7 and assigns the reference to `a`
    4. Note that the Garbage collection for 5 **will not** be done immediately. 

---

## Working of Mutable Types 

- Now we know that List is a mutable data type. 
- So, if we make changes to a common reference which multiple variables are pointing to, the changes will be reflected in all the variables.
- **Eg:**
```
>>> l1 = [1,2,3]
>>> l2 = l1
>>> l1[0] = 69  😏
>>> l1
[69, 2, 3]
>>> l2
[69, 2, 3]
```
This happened because `l1` and `l2` are pointing to the **same object in memory**. And Lists are `mutable` in nature (unlike strings).

---

## Copying items in Python

- when we use the `=` operator, we are actually making a binding of the object and variable. According to Python docs: 
> Assignment statements in Python do not copy objects, they create bindings between a target and an object. 
- There are 2 types of copies in python (only relevant when we are dealing with compound/nested objects) : 
    1. **Shallow Copy** (creates a new copy of object and stores the reference of the nested elements)
    2. **Deep Copy** (creates a new object and recursively adds the copies of nested objects present in the original elements)

- So when we `=` operator we make the variables point to the same reference object in memory.
- But sometimes want to make another object in memory which an copy of the original object. 
- A work around for this is to use `slicing` : 
```
>>> l1 = [1,2,3]
>>> l2 = l1[:]
>>> l1[0] = 69
>>> l1
[69, 2, 3]
>>> l2
[1, 2, 3]
```
- `slicing` creates a new object in memory which contains the elements (a copy) from the l1 reference object.
---
- This becomes more clear when we use the `is` keyword. 
- `is` keyword tells you if the variables have the reference for the **same object** in memory. 
- This is different from the working of `==` operator which just compares the **values** of the objects.
- **Eg:**
```
>>> l1 = [1,2,3]
>>> l2 = [1,2,3]
>>> l1 == l2
True
>>> l1 is l2
False
>>> p1 = [4,5,6]
>>> p2 = p1
>>> p1 == p2
True
>>> p1 is p2
True
```