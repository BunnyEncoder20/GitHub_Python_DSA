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