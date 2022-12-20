class Stack:
    def __init__(self):
        self.elements = []
    
    def push(self, data):
        self.elements.append(data)

    def pop(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)

    def isEmpty(self):
        return self.elements == []
    
    def peek(self):
        return self.elements[-1]



s = Stack()

inp = input('Enter Input : ').split(',')

for ele in inp :
    if ele[0] == "A" :
        x = (ele).split(" ")
        n = int(x[1])
        while(not s.isEmpty() and s.peek()<=n):
            s.pop()
        s.push(n)
    if ele[0] == "B" :
        print(s.size()) 

        