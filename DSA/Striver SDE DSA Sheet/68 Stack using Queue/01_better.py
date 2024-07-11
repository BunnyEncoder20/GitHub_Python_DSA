class Stack:
    def __init__(self) -> None:
        self.queue = []
        
    def push(self,x:int) -> None:
        self.queue.append(x)
        for i in range(len(self.queue)-1):
            self.queue.append(self.queue.pop(0))
    
    def pop(self) -> None: 
        x = self.queue.pop(0)
        return x
    
    def get_top(self) -> int:
        return self.queue[0]
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