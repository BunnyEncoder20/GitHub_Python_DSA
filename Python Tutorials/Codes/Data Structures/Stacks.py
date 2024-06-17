stack = []
stack.append('https://www.soma.com')
stack.append('https://www.bunny.com')
stack.append('https://www.varun.com')
stack.append('https://www.senpai.com')
stack.append('https://www.somya.com')

# Getting the last element without changing the stack : 
print(stack[-1])

# Removing the last (top most) element of the stack.
# .pop() returns the popped out element
print(stack.pop())  # https://www.somya.com
print(stack.pop())  # https://www.senpai.com
print(stack.pop())  # https://www.varun.com
print(stack.pop())  # https://www.bunny.com
print(stack.pop())  # https://www.soma.com
#print(stack.pop())  # IndexError: pop from empty list



# Implementing Stack using collection.deque
from collections import deque 
Deque_stack = deque()
Deque_stack.append('https://www.soma.com')
Deque_stack.append('https://www.bunny.com')
Deque_stack.append('https://www.varun.com')
Deque_stack.append('https://www.senpai.com')
Deque_stack.append('https://www.somya.com')
print(Deque_stack)

# removing elements from the stack : 
print(Deque_stack.pop())        # https://www.somya.com
print(Deque_stack.pop())        # https://www.senpai.com
print(Deque_stack.pop())        # https://www.varun.com

print(Deque_stack)              # deque(['https://www.soma.com', 'https://www.bunny.com'])


# Implementing a Stack class of the OG function calls : 
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

print("\n\nImplementation of Stack class using Deque")

s = Stack()

print(s.isEmpty())

s.push('bunny')
s.push('soma')
s.push('senpai')

print(s.peek())

s.pop()
s.pop()

s.show()