# Implement Queue using Stack

- Given a Stack having some elements stored in it. 
- Can you implement a Queue using the given Stack?

## Brute Force Approach 

### Algorithm 

- [Watch it here](https://youtu.be/3Et9MrMc02A?si=LuqIFumCSbCvX8g-&t=98)
1. When adding element into the queue : 
   1. Pop out elements from s1 and push them into s2
   2. push new element into s1
   3. pop out elements from s2 and push them into s1
2. When removing element from queue : 
   1. s1.pop() (the first element will be at the top of the utility stack)

### Code 

```python 
# using LifoQueue cause it is a stack in python
from queue import LifoQueue


class Queue:
    def __init__(self) -> None:
        self.stack1 = LifoQueue()
        self.stack2 = LifoQueue()

    def push(self,x) -> None:
        # Step 1 : popping out all the elements from stack1 and pushing them into stack2
        while not self.stack1.empty():
            self.stack2.put(self.stack1.get())

        # Step 2 : push new element into stack 1
        self.stack1.put(x)

        # Step 3 : returning all the elements from the stack2 back to stack1
        while not self.stack2.empty():
            self.stack1.put(self.stack2.get())
        
        print(f"Appended {x} into the Queue")
    
    def pop(self) -> int:
        if self.stack1.qsize==0:
            print("Stack is EMPTY")
        return self.stack1.get()

    def Top(self) -> None:
        # the LifoQueue.queue contains the underlying List which is acting like the stack
        # hence for the top element, we can just return this lists last element 
        return self.stack1.queue[-1]
    def size(self) -> None:
        return self.stack1.qsize()
    
if __name__ == "__main__":
    q = Queue()
    q.push(3)
    q.push(4)
    print("The element popped is", q.pop())
    q.push(5)
    print("The top of the queue is", q.Top())
    print("The size of the queue is", q.size())
```
- **Time complexity : O(n)**
- **Space complexity : O(2n)**

<br>

## Better Approach 

- We will get the complexity down to **O(1) amotized complexity** 
- It meeans that the complexity is not exactly O(1) (extreme cases when the output stack is empty for an operation) in only those cases, will the TC jump tp O(n)

### Algorithm 
- [Watch it here](https://youtu.be/3Et9MrMc02A?si=ga0UZHQZAZHkbYHd&t=310)
1. Taking 2 stacks again : input and output
2. When adding elements into the queue:
   1. append x to input
3. When removing element from the queue
   1. if the output stack is not empty : output.pop()
   2. else : transfer input stack to output stack and then : output.pop()
4. For operations like top : 
   1. if the output stack is not empty : output.top()
   2. else : transfer input stack to output stack and then : output.top() 
5. This way only when the output stack is completely empty, will the time complexity be O(n)
6. For all reminaing cases TC will be O(1)

### Code 

```python 
from queue import LifoQueue

class Queue:
    def __init__(self) -> None:
        self.input = LifoQueue()
        self.output = LifoQueue()
    
    def push(self,x) -> None:
        self.input.put(x)
        print(f"Appended {x} into the Queue")
    
    def pop(self) -> None:
        if not self.output.empty():
            return self.output.get()
        else:
            # If output stack is empty, transfer the elements into output stack
            while not self.input.empty():
                self.output.put(self.input.get())            
            return self.output.get()
    
    def Top(self) -> None:
        if not self.output.empty():
            return self.output.queue[-1]
        else:
            while not self.input.empty():
                self.output.put(self.input.get())
            return self.output.queue[-1]
    
    def size(self) -> None:
        return self.input.qsize() + self.output.qsize()

if __name__ == "__main__":
    q = Queue()
    q.push(3)
    q.push(4)
    print("The element poped is", q.pop())
    q.push(5)
    print("The top of the queue is", q.Top())
    print("The size of the queue is", q.size())
```
- **Time complexity : O(1) (amotized)**
  - In general the TC will be O(n), but as they are for only certain situations, 
  - The TC is O(1) for majority of cases
- **Spce complexity : O(2n)**

<br>

---
---

