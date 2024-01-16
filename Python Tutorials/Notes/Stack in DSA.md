# Stack in DSA (Python)
---

## Use cases of Stack DS
- a simple use case of stack example is storing the **history** of a browser. When user wants to go to the back page, stack will pop out the last entered website directly instead of having to traverse an entire DS (like array or LinkedList) 
- Other Examples of usage of stack include : 
  - **Function calling** in any programming language is managed using a stack
  - **Undo** (Ctrl+Z) functionality in any editor uses stack to track down last set of operations.
![Image](./Notes%20Assets/stack.png)
- Note that Stack uses LIFO

### Complexity :
- Push/Pop element: `0(1)`
- Search element by value: `O(n)`

### Stack implementation in other languages : 
![Image](./Notes%20Assets//stack%20in%20other%20languages.png)

---

## Implementing Stack DS in python 

- we can implement stack using a simple list : 
```
stack = []
# Inserting some links 
stack.append('https://www.soma.com')
stack.append('https://www.bunny.com')
stack.append('https://www.varun.com')
stack.append('https://www.senpai.com')
stack.append('https://www.somya.com')

# Getting the last element without changing the stack : 
print(stack[-1])            # https://www.somya.com


print(stack.pop())          # https://www.somya.com
print(stack.pop())          # https://www.senpai.com
print(stack.pop())          # https://www.varun.com
print(stack.pop())          # https://www.bunny.com
print(stack.pop())          # https://www.soma.com
print(stack.pop())          # IndexError: pop from empty list
```
- `.pop()` **removes** the last (top most) element of the stack.
- `.pop()` **returns** the popped out element 

Even though `stack` can be implemented like this, it still suffers from the overhead of dynamic arrays as at the end of the day `Lists` in python are implementation of _dynamic arrays_ only.
(That being when the array grows, it needs to allocate twice the memory space and copy all the elements to the new locations)
![Image](./Notes%20Assets/Lists%20increasing%20in%20size.png)
- Hence it is not advised to use `lists` as arrays in python
- Instead we use `collections.deque()` documentation can be found [here](https://docs.python.org/3/library/collections.html#collections.deque).
- `Collections` is a module which  implements specialized container datatypes providing alternatives to Python’s general purpose built-in containers like `dict`, `list`, `set`, and `tuple`.
- `deque` is a _list-like_ container with **fast appends and pops** on either end

---

## Implementing Stack using collections.deque()

1. from collections import deque 
```
from collections import deque 
Deque_stack = deque()
```
Read the [documentation](https://docs.python.org/3/library/collections.html#collections.deque) or use ```dir(stack)``` in above code to look at all of the functions available for the stack instance of deque

2. `.append()` will add data to the right side of the stack : 
```
Deque_stack.append('https://www.soma.com')
Deque_stack.append('https://www.bunny.com')
Deque_stack.append('https://www.varun.com')
Deque_stack.append('https://www.senpai.com')
Deque_stack.append('https://www.somya.com')
print(Deque_stack)              # deque(['https://www.soma.com', 'https://www.bunny.com', 'https://www.varun.com', 'https://www.senpai.com', 'https://www.somya.com'])
```
3. Removing elements from teh stack
```
print(Deque_stack.pop())        # https://www.somya.com
print(Deque_stack.pop())        # https://www.senpai.com
print(Deque_stack.pop())        # https://www.varun.com

print(Deque_stack)              # deque(['https://www.soma.com', 'https://www.bunny.com'])
```
---

## Implementing a stack class for the OG function calls

- Implementing a stack class using `deque` : 
```
class Stack :
    def __init__(self):
        self.container = deque()
    
    def peek(self):
        return self.container[-1]
    
    def push(self, data):
        self.container.append(data)
        print("pushed {} into stack".format(data))
    
    def pop(self): 
        poppedElement = self.container.pop()
        print("{} was popped out of stack".format(poppedElement))
        return poppedElement
    
    def isEmpty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
    def show(self):
        print(self.container)
```
