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
    
    def printTree(self, current, level = 0):
        if current != None:
            self.printTree(current.right, level + 1)
            print('     ' * level, current)
            self.printTree(current.left, level + 1)
    
    def moreThanK(self, current, k):
        if current != None:
            if current.data > k:
                current.data *= 3
                self.moreThanK(current.right, k)
                self.moreThanK(current.left, k)
            else:
                self.moreThanK(current.right, k)

T = BST()
inp = input('Enter Input : ').split('/')
num = inp[0].split()
for i in num:
    root = T.insert(int(i))
T.printTree(root)
print('--------------------------------------------------')
T.moreThanK(root, int(inp[1]))
T.printTree(root)