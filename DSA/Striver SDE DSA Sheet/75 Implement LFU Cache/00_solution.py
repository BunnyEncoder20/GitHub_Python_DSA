from turtle import update


class Node:
    def __init__(self,key,value) -> None:
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        self.freq = 0

class LRUCache:
    def __init__(self) -> None:
        self.size = 0
        self.keymap = {}
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node(self,new_node):
        second_node = self.head.next 
        self.head.next = new_node
        new_node.next = second_node
        second_node.prev = new_node
        new_node.prev = self.head
        self.size+=1

    def remove_node(self,del_node):
        del_node_prev = del_node.prev
        del_node_next = del_node.next
        del_node_prev.next = del_node_next
        del_node_next.prev = del_node_prev
        self.size-=1


class LFUCache:
    def __init__(self,limit) -> None:
        self.freqmap = {}
        self.keymap = {}
        self.maxCacheLimit = limit
        self.LF = 1
        self.size = 0
    
    def get(self,key):
        if key in self.keymap:
            node = self.keymap[key]
            node_val = node.value

            # increase the frequency
            self.update_freq(node)

            return node_val
        else:
            return -1
        
    def update_freq(self,node):
        current_freq = node.freq

        if current_freq in self.freqmap : 
            old_dll = self.freqmap[current_freq]
            old_dll.remove_node(node)
            del self.keymap[node.key]

            if current_freq == self.LF and old_dll.size==0:
                self.LF += 1
        
        node.freq += 1

        if node.freq not in self.freqmap:
            self.freqmap[node.freq] = LRUCache()
        
        new_dll = self.freqmap[node.freq]
        new_dll.add_node(node)
        self.keymap[node.key] = node
    
    def put(self,key,val):
        if key in self.keymap:
            node = self.keymap[key]
            node.value = val
            self.update_freq(node)
            return

        if len(self.keymap)==self.maxCacheLimit:
            LFU_dll = self.freqmap[self.LF]
            LRU_node = LFU_dll.tail.prev
            LFU_dll.remove_node(LRU_node)
            del self.keymap[LRU_node.key]
        
        new_node = Node(key,val)
        self.keymap[key] = new_node
        self.update_freq(new_node)

if __name__ == "__main__":
    cache = LFUCache(2)
    print(cache.put(1,1))   # None
    print(cache.put(2,2))   # None
    print(cache.get(1))     # 1
    print(cache.put(3,3))   # None
    print(cache.get(2))     # -1
    print(cache.get(3))     # 3
    print(cache.put(4,4))   # None
    print(cache.get(1))     # -1 
    print(cache.get(3))     # 3 
    print(cache.get(4))     # 4
