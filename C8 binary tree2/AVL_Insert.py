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

    def insert(self,node,data):
        if node == None:
            return Node(data)
        if data < node.data :
            node.left = self.insert(node.left,data)
        if data >= node.data :
            node.right = self.insert(node.right,data)
        
        balance = self.height(node.left)-self.height(node.right)

        if balance > 1 and data < node.left.data:
            return self.rightRotate(node)
        if balance < -1 and data >= node.right.data:
            return self.leftRotate(node)
        if balance > 1 and data >= node.left.data:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        if balance < -1 and data < node.right.data:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)
        return node
    def height(self,node):
        if node == None :
            return 0
        node_right = self.height(node.right)
        node_left = self.height(node.left)
        if node_left > node_right :
            return node_left + 1
        else :
            return node_right + 1
        
    def leftRotate(self,px):
        py = px.right
        px.right = py.left
        py.left = px
        return py

    def rightRotate(self,px):
        py = px.left
        px.left = py.right
        py.right = px
        return py    

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

avl = BST()
lists = list(map(int,input("Enter Input : ").split(" ")))
for i in lists:
    print("Insert : "+"( "+str(i)+" )")
    avl.root = avl.insert(avl.root,i)
    avl.printTree(avl.root)
    print("--------------------------------------------------")