class Stack :
    def __init__(self):
        self.elements = []

    def push(self,data) :
        self.elements.append(data)

    def pop(self) :
        return self.elements.pop()

    def peek(self) :
        return self.elements[-1]

    def size(self) :
        return len(self.elements)

    def isEmpty(self) :
        return self.elements == []

s = Stack()

inp = input("Enter Input : ").split(",")

for ele in inp :
    if ele[0] == "A" :
        n = ele.split()
        m = int(n[1])
        while not s.isEmpty() and s.peek() <= m :
            s.pop()
        s.push(m)
    else :
        print(s.size())
    