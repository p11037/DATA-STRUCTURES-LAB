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

    def preorder(self, current):
        if current != None:
            print(current, end=' ')
            self.preorder(current.left)
            self.preorder(current.right)

    def inorder(self, current):
        if current != None:
            self.inorder(current.left)
            print(current, end=' ')
            self.inorder(current.right)
    
    def postorder(self, current):
        if current != None:
            self.postorder(current.left)
            self.postorder(current.right)
            print(current, end=' ')
    
    def bfs(self, current):
        q = []
        q.append(current)

        while len(q) > 0:
            current = q.pop(0)

            if current.left != None:
                q.append(current.left)
            if current.right != None:
                q.append(current.right)
            
            print(current, end=' ')

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)

print('Preorder : ',end='')
T.preorder(root)
print()

print('Inorder : ',end='')
T.inorder(root)
print()

print('Postorder : ',end='')
T.postorder(root)
print()

print('Breadth : ',end='')
T.bfs(root)
print()