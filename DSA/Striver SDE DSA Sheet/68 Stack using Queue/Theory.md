# Implement Stack using single Queue

- Problem Statement: Implement a Stack using a single Queue.
- **Note:** Stack is a data structure that follows the Last In First Out (LIFO) rule.
- **Note:** Queue is a data structure that follows the First In First Out (FIFO) rule.

## Brute Force Approach (Using 2 queues)

### Algorithm 

1. We gonna need 2 queues (one for push and one for pop)
2. When pushing into the Stack : 
   1. add x to q2
   2. put all elements of q1 into q2 (element by element)
   3. swap q1 and q2 (all the elements will not be in q1)
3. When doing top, return the top of q1
4. When popping
   1. remove the top of q1

### Code

```python 
class Stack():
    def __init__(self) -> None:
        self.q1 = []
        self.q2 = []
        self.top = 0

    def push(self,x:int)->None:
        # Step 1 : Push the element into q2
        self.q2.append(x)
        if len(self.q1)>0:
            # Step 2 : put q1 element by element into q2
            for i in range(len(self.q1)):
                self.q2.append(self.q1[i])
        # Step3 : Swap the contents of q1 and q2
        self.q1,self.q2 = self.q2,self.q1
        self.q2.clear()
        print(f"Pushed {x} into stack")
    
    def pop(self)->int:
        # Step : pop the top of q1
        return self.q1.pop(self.top)

    def get_top(self)->int:
        return self.q1[self.top]
    def get_size(self)->int:
        return len(self.q1)

if __name__ == "__main__":
    s = Stack()
    s.push(4)
    s.push(3)
    s.push(2)
    s.push(1)
    print(s.q1)
    print(s.q2)
    print("Top of the stack: ", s.get_top())
    print("Size of the stack before removing element: ", s.get_size())
    print("The deleted element is: ", s.pop())
    print("Top of the stack after removing element: ", s.get_top())
    print("Size of the stack after removing element: ", s.get_size())
```
- **Time complexity : O(n)**
  - Cause of the the transfering thing 
- **Space complexity : O(2n)**
  - Becuase there are 2 queues

<br>

## Better Approach (Using 1 Queue)

### Algorithm

- [Watch it here](https://youtu.be/jDZQKzEtbYQ?si=ZqTNf05dcxl_qm8_&t=433)
1. We going to use a single queue to implement stack
2. For pushing operations : 
   1. append the element into the queue
   2. for size-1 elements of the queue, pop(top) and append them back into the queue
3. This way the last added element will always be at top
4. For poping, we simply
   1. Pop the top from the queue

### Code 

```python 
class Stack:
    def __init__(self) -> None:
        self.top = -1
        self.queue = []
        
    def push(self,x:int) -> None:
        self.top+=1
        self.queue.append(x)
    
    def pop(self) -> None: 
        x = self.queue.pop(self.top)
        self.top-=1
        return x
    
    def get_top(self) -> int:
        return self.queue[self.top]
    def get_size(self) -> int:
        return len(self.queue)


if __name__ == "__main__":
    s = Stack()
    s.push(4)
    s.push(3)
    s.push(2)
    s.push(1)
    print(s.queue)
    print("Top of the stack: ", s.get_top())
    print("Size of the stack before removing element: ", s.get_size())
    print("The deleted element is: ", s.pop())
    print("Top of the stack after removing element: ", s.get_top())
    print("Size of the stack after removing element: ", s.get_size())
```
- **Time complexity : O(n)**
- **Space complexity : O(n)**
  - Cause now we are only using single queue

<br>

---
---