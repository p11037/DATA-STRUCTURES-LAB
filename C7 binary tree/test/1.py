class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self.insertNode(self.root, data)
        return self.root
    
    def insertNode(self, current, data):
        if data < current.data:
            if current.left != None:
                self.insertNode(current.left, data)
            else:
                current.left = Node(data)
        else:
            if current.right != None:
                self.insertNode(current.right, data)
            else:
                current.right = Node(data)
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)