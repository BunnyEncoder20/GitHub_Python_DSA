class BinarySearchTreeNode:
    """Class for making BST Nodes."""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data: 
            return
        
        if data < self.data : 
            # add data in left subtree
            if self.left :
                self.left.add_child(data)
            else : 
                self.left = BinarySearchTreeNode(data)
        else :
            # add data in right subtree
            if self.right :
                self.right.add_child(data)
            else : 
                self.right = BinarySearchTreeNode(data)
    
    def search(self, val):
        if self.data == val : return True

        if val < self.data:
            if(self.left) : 
                return self.left.search(val)
            else :
                return False

        else :
            if(self.right) : 
                return self.right.search(val)
            else : 
                return False

    def inOrderTraversal(self):
        elements = []

        # Visit the left subtree
        if self.left :
            elements += self.left.inOrderTraversal()

        # Visit the root node 
        elements.append(self.data)

        # Visit the right subtree
        if self.right :
            elements += self.right.inOrderTraversal()
        
        return elements     # don't forget to return the elements array
    
    def find_min(self):
        node = self 

        while node.left: 
            node = node.left
        
        return node.data

    def find_max(self):
        node = self
        while node.right: 
            node = node.right
        return node.data 
    
    def sum(self):
        sum = 0 

        # Add the node on left 
        if self.left :
            sum += self.left.sum()
        # Add node value 
        sum += self.data 

        # add the node on right
        if self.right :
            sum += self.right.sum()

        return sum 

    def post_order(self):
        elements = []

        if(self.left):
            elements += self.left.post_order()
        if(self.right):
            elements += self.right.post_order()
        elements.append(self.data)

        return elements
    
    def pre_order(self):
        elements = [] 

        elements.append(self.data)
        if(self.left):
            elements += self.left.pre_order()
        if(self.right):
            elements += self.right.pre_order()
        
        return elements 

        


def buildTree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root 

if __name__ == "__main__":
    numbers = [15,12,7,14,27,20,88,23,12]
    numBST = buildTree(numbers)

    print("In Order Traversal : ",numBST.inOrderTraversal())   
    # notice that it doesn't print duplicates cause BT doesn't store duplicate values
    # Also notice that the values are sorted in ascending order none (one of the utilities of BT)

    # Searching in BST
    print("22 in numBST ? ",numBST.search(22))
    print("23 in numBST ? ",numBST.search(23))

    # Printing the minimum and maximum values
    print("Minimum in numBST : ",numBST.find_min())
    print("Maximum in numBST : ",numBST.find_max())

    # Calculating the sum of all teh elements
    print("Sum of numBST: ",numBST.sum())
    sum = 0
    for num in numbers:
        sum += num 
    print("Actual sum : ",sum)

    # Pre Order Traversal
    print("Pre Order Traversal : ",numBST.pre_order())

    # Post Order Traversal
    print("Post Order Traversal : ",numBST.post_order())
    
    