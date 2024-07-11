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