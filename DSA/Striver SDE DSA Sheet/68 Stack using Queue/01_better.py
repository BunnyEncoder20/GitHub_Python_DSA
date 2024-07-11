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