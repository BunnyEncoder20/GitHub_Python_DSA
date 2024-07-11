class Queue():
    def __init__(self,size) -> None:
        self.start = 0
        self.end = 0
        self.count=0
        self.size = size
        self.q = [None]*size
    
    def push(self,x)->None:
        if self.count==self.size:
            print(f"Queue FULL. Size:{self.count}/{self.size}")
            return
        else:
            self.q[self.end] = x
            self.end = (self.end+1)%self.size
            self.count+=1
            print(f"Element pushed. Size:{self.count}/{self.size}")

    def pop(self)->int:
        if self.count==0:
            print(f"Queue EMPTY. Size:{self.count}/{self.size}")
            return 
        else:
            x = self.q[self.start] 
            self.start = (self.start+1)%self.size
            self.count-=1
            print(f"Element popped. Size:{self.count}/{self.size}")
            return x

    def top(self)->int:
        return self.q[self.start]
            
    def get_size(self)->int:
        return self.count
    

if __name__ == "__main__":
    q = Queue(5)
    q.push(4)
    q.push(14)
    q.push(24)
    q.push(34)
    q.push(54)
    q.push(64)
    print("The peek of the queue before deleting any element", q.top())
    print("The size of the queue before deletion", q.get_size())
    print("The first element to be deleted", q.pop())
    print("The peek of the queue after deleting an element", q.top())
    print("The size of the queue after deleting an element", q.get_size())
    print("Popped : ", q.pop())
    print("Popped : ", q.pop())
    print("Popped : ", q.pop())
    print("The peek of the queue after deleting an element", q.top())
    print("The size of the queue after deleting an element", q.get_size())