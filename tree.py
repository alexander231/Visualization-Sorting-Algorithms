class Node:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def leftTraverse(self, start):
        
        if start is None:
            return
        else:
            print(start.val)
        
        if start.left:
           
            self.leftTraverse(start.left)
        elif start.right:
            self.leftTraverse(start.right)
        else:
            return

        

tree = Tree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

tree.leftTraverse(tree.root)