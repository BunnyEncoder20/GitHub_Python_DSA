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