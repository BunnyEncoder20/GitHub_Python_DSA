# Immutable and Mutable 
---
- When we search for mutable and immutable data types in python we can find something like this : 

![alt text](./Notes_Images/1679695596993.png)

- This can be confusing at first because me was like "But I can easily change integers and strings in python" cause 
  - Immutable = can't be changed
  - Mutable = can be changed
- However python works a little differently. Take the below example when we make a username = "hitesh"

![alt text](image.png)

- When the variable is made in python, it creates a object in memory which has a **immutable reference**. 
- When we make a change in the variable, the object in memory doesn't change. Python makes a another new object in memory with a **immutable reference** and makes the variable refer the new object.

![alt text](image-1.png)

- Python has it's own garbage collection so when it encounters such objects which none of the variables are referencing , it automatically removes them from memory.

> - This it the **TRUE** meaning of immutable. The variables reference can be changed but the object in memory can't be changed in case of Immutable data types.
> - When we are changing the value of a variable, we are actually just changing it's reference to a new object in memory.
---
- This can also be seen in the below example:
```
>>> x = 10
>>> y = x
>>> x, y
(10, 10)
>>> x = 15
>>> x,y
(15, 10)
>>>
```