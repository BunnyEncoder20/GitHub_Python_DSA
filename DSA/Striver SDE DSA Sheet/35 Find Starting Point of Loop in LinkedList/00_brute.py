# Node class represents a node in a linked list
class Node:
    def __init__(self, data, next_node=None):
        self.data = data  
        self.next = next_node 

def detect_loop(head):
    node_map = {}
    temp = head

    while temp != None :
        if temp in node_map :
            return temp
        else :
            node_map[temp] = True
        temp = temp.next
    
    return None

if __name__ == "__main__":
    # Create a sample linked list with a loop
    node1 = Node(1)
    node2 = Node(2)
    node1.next = node2
    node3 = Node(3)
    node2.next = node3
    node4 = Node(4)
    node3.next = node4
    node5 = Node(5)
    node4.next = node5

    # Make a loop from node5 to node2
    node5.next = node2

    # Set the head of the linked list
    head = node1

    # Detect the loop in the linked list
    loop_start_node = detect_loop(head)

    if loop_start_node:
        print("Loop detected. Starting node of the loop is:", loop_start_node.data)
    else:
        print("No loop detected in the linked list.")