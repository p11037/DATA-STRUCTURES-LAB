class Stack():
    def __init__(self):
        self.elements = []

    def push(self,data) :
        self.elements.append(data)

    def pop(self) :
        return self.elements.pop()
    
    def isEmtyp(self) :
        return self.elements == []

    def size(self) :
        return len(self.elements)

s = Stack()


inp = input("Enter Input : ").split(",")

for ele in inp :
    if ele[0] == "A" :
        n = ele.split()
        s.push(n[1])
        print("Add =",n[1],"and Size =",s.size())
    elif not s.isEmtyp() :
        index = s.size()-1
        print("Pop =",s.pop(),"and Index =",index)
    else :
        print("-1")

if not s.isEmtyp() :
    print("Value in Stack =",end=" ")

    for j in s.elements :
        print(j,end=" ")

else :
    print("Value in Stack = Empty")



#print(s.elements)