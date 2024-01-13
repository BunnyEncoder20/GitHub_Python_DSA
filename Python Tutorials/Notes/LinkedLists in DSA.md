# LinkedLists in DSA (Python)
---
- There were some **issues** with traditional arrays, major one being their need to be in a **sequential block of memory**. 
- Hence when we want to **add** or **remove** an element from teh array, we get a complexity of `O(n)` because all the elements of the array need to be shifted
- also when using **dynamic array**, when the _pre-allocated_ space of memory is filled, the function will assign a new memory block with twice the space as previous **AND** copy all the elements to the new block. This causes `additional overhead`.
![Image](./Notes%20Assets/dynamicarrayallocation.png)

---

- LinkedList store elements in non sequential memory blocks. Each block has a pointer pointing to the next elements memory location. Looks something like this : 
![Image](./Notes%20Assets/llmemoryblock.png)
- Using these pointers or Links we can access the next element in the list. Also it is easier to add or remove an element , as we just have to change the links and do not need to always copy all the elements to new locations when the linkedlist grows in size. 
![Image](./Notes%20Assets/insertinginll.png)
- Insert/Delete Element **at beginning** = `0(1)`
- Insert/ Delete Element **at the end** = `O(n)`
- Traversing the LinkedList = `O(n)`
- Accessing element by value = `O(n)`
  
**Linked Lists** have 2 main benefits : 
1. Don't have to **pre-allocate** memory space
2. Insertion is easier
- LinkedList can be doubly linked also, called a **Doubly LinkedList** (pointer to both next and previous element)

###LinkedList VS Arrays
![Image](./Notes%20Assets/llvsarr.png)
- The one advantage array has over linkedlist is when we know the index of teh element we want. Then in array it is a constant time complexity of `O(1)`. Whereas in LinkedList it will be of `O(n)`
- Cause in LinkedList even if we know we want to access only the 5th element, we have to go though all the previous elements as well.
- Inserting/Deleting in arrays has addition 'amortized' cost due to expansion of the memory spaces when previous pre-allocated space runs out  

#### Implementing LinkedList in Python
```
# Class defining a node 
class Node : 
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

# Class defining LinkedList 
class LinkedList :
    def __init__(self) :
        self.head=None
    
    def insertAtBeginning(self,data):
        node = Node(data, self.head)
        self.head = node 
    
    def insertAtEnd(self,data):
        if self.head is None: 
            self.head = Node(data,None)
            return 
        
        iterator = self.head
        while iterator.next:
            iterator = iterator.next

        iterator.next = Node(data,None)
    
    def insertList(self,DataList) :
        self.head = None
        for data in DataList :
            self.insertAtEnd(data)

    def getLength(self) :
        count=0
        iterator = self.head 
        while iterator:
            count+=1
            iterator = iterator.next 
        return count

    def printLinkedList(self):
        if self.head is None:
            print("LinkedList is empty !")
            return 

        llStr = ''
        iterator = self.head
        while iterator : 
            llStr += str(iterator.data)+" --> "
            iterator = iterator.next 
        print(llStr)
    
    def removeAt(self,idx) : 
        if(idx<0 or idx>self.getLength()) :
            raise Exception("invalid idx")
        
        if idx==0 :
            self.head = self.head.next
            return 
        
        i = 0
        iterator = self.head 
        while iterator :
            if i == idx-1 :
                iterator.next = iterator.next.next
            i+=1
            iterator = iterator.next 

    def insertAt(self, data, idx) :
        if idx<0 or idx>=self.getLength() :
            raise Exception("invalid index for insertion")
        
        if idx==0 :
            self.insertAtBeginning(data)
        
        i = 0
        iterator = self.head 
        while iterator : 
            if i == idx-1 : 
                node = Node(data,iterator.next)
                iterator.next = node 
                return
            
            i+=1
            iterator = iterator.next  


    
    

# main function
if __name__ == '__main__' :
    # Making instance of LinkedList 
    ll = LinkedList()

    # inserting new values at beginning 
    ll.insertAtBeginning(1)
    ll.insertAtBeginning(2)
    ll.insertAtBeginning(3)
    ll.insertAtBeginning(4)
    ll.insertAtBeginning(5)
    ll.printLinkedList()

    # inserting at end
    ll.insertAtEnd(0)
    ll.insertAtEnd(-1)
    ll.printLinkedList()

    # Inserting an List to be made into a LinkedList 
    ll2 = LinkedList()
    ll2.insertList(['🍌','🍊','🍎','🍉','🥝'])
    ll2.printLinkedList()

    # Getting the length of LinkedList : 
    print("The length of ll is {}".format(ll.getLength()))
    print("The length of ll2 is {}".format(ll2.getLength()))

    # removing element from a specific index
    ll2.printLinkedList()
    ll2.removeAt(2)
    ll2.printLinkedList()
    ll2.insertAt('🍏',2)
    ll2.printLinkedList()

```