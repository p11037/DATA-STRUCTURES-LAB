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
        self.height = 0

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
    
    def heightTree(self,current, level = 0):
        if current != None:
            if level > self.height:
                self.height = level
            self.heightTree(current.right, level + 1)
            self.heightTree(current.left, level + 1)
        return self.height

    def printTree(self, current, level = 0):
        if current != None:
            self.printTree(current.right, level + 1)
            print('     ' * level, current)
            self.printTree(current.left, level + 1)

    def checkpos(self, data):
        self.search(self.root, data)
    
    def search(self, current, data):
        if current != None:
            if data == current.data:
                if current == self.root:
                    print('Root')
                elif current.left == None and current.right == None:
                    print("Leaf")
                else:
                    print("Inner")
                return
            elif data < current.data:
                self.search(current.left, data)
            else:
                self.search(current.right, data)
        else:
            print('Not exist')

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.insert(inp[i])
T.printTree(root)
T.checkpos(inp[0])