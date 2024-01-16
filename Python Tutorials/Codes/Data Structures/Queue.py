simpleQ = []

# inserting elements 
simpleQ.insert(0, 132)
simpleQ.insert(0, 135)
simpleQ.insert(0, 140)

print(simpleQ)

# popping elements 
print(simpleQ.pop())
print(simpleQ.pop())


# Implementing Queue using collections.deque DS
from collections import deque
queue = deque()

queue.appendleft(132)
queue.appendleft(135)
queue.appendleft(140)

print(queue)

print(queue.pop())
print(queue.pop())


# Implementing Queue class for the OG function calls 
class Queue : 
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, data):
        self.buffer.appendleft(data)
        print("{} added into queue".format(data))
    
    def dequeue(self):
        popped = self.buffer.pop()
        print("{} exited queue".format(popped))
        return popped
    
    def nextInLine(self):
        return self.buffer[-1]
    
    def isEmpty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
    
    def show(self):
        print(self.buffer)

Q = Queue()

print(Q.isEmpty())

Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)

Q.show()

Q.dequeue()
Q.dequeue()

print("Next in line : ",Q.nextInLine())

Q.show()

    