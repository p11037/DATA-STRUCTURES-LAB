class ManageStack :
    def __init__(self) -> None:
        self.element = []
    
    def add(self,data) :
        self.element.append(data)

    def pop(self) :
        self.element.pop()

    def delete(self,data) :
        temp3 = ManageStack()
        index = self.element.index(data)
        for i in range(len(self.element)) :
            if i != index :
                temp3.add(self.element[i])
        self.element = temp3.element
            

    def lessthanDelete(self,data) :
        temp = ManageStack()
        remove = ManageStack()
        for b in self.element :
            if int(b) >= int(data):
                temp.add(b)
            else :
                remove.add(b)
        self.element = temp.element
        
        while remove.size() != 0 :
            x = remove.peek()
            print("Delete =",x,"Because",x,"is less than",data)
            remove.pop()

    def morethanDelete(self,data) :
        temp1 = ManageStack()
        remove1 = ManageStack()
        for l in self.element :
            if int(l) <= int(data) :
                temp1.add(l)
            else :
                remove1.add(l)
        self.element = temp1.element

        while remove1.size() != 0 :
            y = remove1.peek()
            print("Delete =",y,"Because",y,"is more than",data)
            remove1.pop()

    def peek(self) :
        return self.element[-1]

    def size(self) :
        return len(self.element)

    def clear(self) :
        self.element = []

stack = ManageStack()
temp2 = ManageStack()
inp = input("Enter Input : ").split(",")

for ele in inp :
    if stack.size() != 0 or ele[0] == "A" :
        if ele[0] == "A" :
            a = ele.split()
            stack.add(a[1])
            print("Add =",a[1])
        elif ele[0] == "P" :
            print("Pop =",stack.peek())
            stack.pop()
        elif ele[0] == "D" :
            d = ele.split()
            remove = d[1]
            for k in stack.element :
                if k == remove :
                    temp2.add(k)
            for f in temp2.element :
                stack.delete(f)
                print("Delete =",f)
        elif ele[:2] == "LD" :
            Ld = ele.split()
            stack.lessthanDelete(Ld[1])
        elif ele[:2] == "MD" :
            Md = ele.split()
            print(Md[1])
            stack.morethanDelete(Md[1])
    else :
        print(-1)

print("Value in Stack = [",end="")

for o in stack.element :

    if o != stack.peek() :
        print(o,end=", ")
    else :
         print(o,end="")
    
print("]")

