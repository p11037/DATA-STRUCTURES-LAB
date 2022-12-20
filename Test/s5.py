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

def dec2bin(decnum) :
    s = Stack()
    binary = ""
    while decnum > 0 :
        n = decnum%2
        s.push(n)
        decnum = decnum // 2
    while not s.isEmpty() :
        binary += str(s.pop())
    return binary

print(" ***Decimal to Binary use Stack***")

token = input("Enter decimal number : ")

print("Binary number : ",end='')

print(dec2bin(int(token)))