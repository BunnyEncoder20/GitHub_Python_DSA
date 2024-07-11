# Implementing Stack Using Array 

- Implement a stack using an array.

### Algorithm 

- Stack is LIFO 
- Common functions include : 
  - PUSH : put element into the array
  - POP : remove the last added element,
  - TOP : returns the top most element in the stack
  - SIZE : returns the number/size of th stack

### Code 

```python 
class Stack:
    def __init__(self) -> None:
        self.top = -1 
        self.stk  = [0]*100
    
    def push(self,n:int)->None:
        self.top+=1
        self.stk[self.top] = n

    def pop(self)->int:
        x = self.stk[self.top]
        self.top-=1
        return x

    def Top(self)->int:
        return self.stk[self.top]
    
    def Size(self)->int:
        return self.top+1

if __name__ == "__main__":
    s = Stack()
    s.push(6)
    s.push(3)
    s.push(7)
    print("Top of stack is before deleting any element", s.Top())
    print("Size of stack before deleting any element", s.Size())
    print("The element deleted is", s.pop())
    print("Size of stack after deleting an element", s.Size())
    print("Top of stack after deleting an element", s.Top())
```
- Time complexity : O(n)
- Space complexity : O(n)

<br>

---
---