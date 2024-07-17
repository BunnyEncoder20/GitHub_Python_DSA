class LRUCache:
    
    class Node:
        def __init__(self,key,value):
            self.key = key
            self.value = value
            self.next = None
            self.prev = None
    
    def __init__(self,size):
        self.size = size
        head = Node(-1,-1)
        tail = Node(-1,-1)

        head.next = tail
        tail.prev = head
        hashmap = {}
    
    def add_node(self, new_node):
        second_node = head.next
        new_node.next = second_node
        second_node.prev = new_node
        head.next = new_node
        new_node.prev = head
    
    def get(self,key):
        if key in hashmap:
            result_node = hashmap[key]
            result_value = result_node.value
            
            # del the key from the hashmap and remove the DLL node
            del hashmap[key]
            remove_node(result_node)
            
            # Add the node to the most recent used position and add it back into the hashmap
            add_node(result_node)
            hashmap[key] = head.next 
        else:
            return -1
    
    def put(self,key,value):
        if key in hashmap:
            existing_node = hashmap[key]
            del hashmap[key]
            remove_node(existing_node)
        if len(hashmap)==self.size:
            del hashmap[tail.prev.key]
            remove_node(tail.prev.mode)
        
        # Inserting the new node 
        new_node = Node(key,value)
        add_node(new_Node)
        hashmap[key] = head.next
        
