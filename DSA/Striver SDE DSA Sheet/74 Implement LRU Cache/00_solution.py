class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    
    def __init__(self,size):
        self.size = size
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)

        self.head.next = self.tail
        self.tail.prev = self.head
        self.hashmap = {}
    
    def add_node(self, new_node):
        second_node = self.head.next
        new_node.next = second_node
        second_node.prev = new_node
        self.head.next = new_node
        new_node.prev = self.head
    
    def remove_node(self,del_node):
        del_prev = del_node.prev
        del_next = del_node.next
        del_prev.next = del_next
        del_next.prev = del_prev 
    
    def get(self,key):
        if key in self.hashmap:
            result_node = self.hashmap[key]
            result_value = result_node.value
            
            # del the key from the hashmap and remove the DLL node
            del self.hashmap[key]
            self.remove_node(result_node)
            
            # Add the node to the most recent used position and add it back into the hashmap
            self.add_node(result_node)
            self.hashmap[key] = self.head.next 

            # Return the value 
            return result_value
        else:
            return -1
    
    def put(self,key,value):
        if key in self.hashmap:
            existing_node = self.hashmap[key]
            del self.hashmap[key]
            self.remove_node(existing_node)
        if len(self.hashmap)==self.size:
            del self.hashmap[self.tail.prev.key]
            self.remove_node(self.tail.prev)
        
        # Inserting the new node 
        new_node = Node(key,value)
        self.add_node(new_node)
        self.hashmap[key] = self.head.next

if __name__ == "__main__":
    l = LRUCache(2)
    print(l.put(1,1))
    print(l.put(2,2))
    print(l.get(1))
    print(l.put(3,3))
    print(l.get(2))
    print(l.put(4,4))
    print(l.get(1))
    print(l.get(3))
    print(l.get(4))
# [null, null, 1, null, -1, null, -1, 3, 4]
