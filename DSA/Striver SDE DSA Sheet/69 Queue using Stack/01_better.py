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