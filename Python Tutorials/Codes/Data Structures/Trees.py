class TreeNode:
    """Class for making TreeNodes."""

    def __init__(self, data):
        self.parent = None
        self.data = data
        self.children = []

    def add_child(self, child): 
        child.parent = self
        self.children.append(child)

    def getLevel(self):
        lvl = 0
        dad = self.parent
        while dad:
            lvl += 1
            dad = dad.parent

        return lvl

    def printTree(self):
        spaces = '    '*self.getLevel()
        prefix = spaces+'┕> ' if self.parent else ""

        print(prefix+self.data)
        if self.children :
            for child in self.children: 
                child.printTree();

def buildProductTree():
    root = TreeNode('Electronics')
    
    laptop = TreeNode('Laptop')
    laptop.add_child(TreeNode('Mac'))
    laptop.add_child(TreeNode('ThinkPad'))
    laptop.add_child(TreeNode('Surface'))

    mobile = TreeNode('Mobile')
    mobile.add_child(TreeNode('Samsung'))
    mobile.add_child(TreeNode('iPhone'))
    mobile.add_child(TreeNode('OnePlus'))

    tv = TreeNode('TV')
    tv.add_child(TreeNode('Sony'))
    tv.add_child(TreeNode('LG'))

    root.add_child(laptop)  
    root.add_child(mobile)
    root.add_child(tv)


    return root

if __name__ == "__main__":
    root = buildProductTree()
    root.printTree()
    
    countriesList = ["USA","India","USA","India","China"]
    print(countriesList)
    countriesSet = set(countriesList)
    print(countriesSet)