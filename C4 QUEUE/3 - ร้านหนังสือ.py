class Queue :
    def __init__(self,list = None) :
        if list == None :
            self.item = []
        else :
            self.item = list

    def deQueue(self) :
        return self.item.pop(0)

    def enQueue(self,i) :
        self.item.append(i)

    def size(self) :
        return len(self.item)
v = Queue()
ans = Queue()
inp = Queue()
n = Queue()
g = 0
x,y = list(input("Enter Input : ").split("/"))

for ele in x.split() :
    
    n.enQueue(ele)

inp = (y).split(",")

for i in inp :
    if i[0] == "E" :
        m = (i).split()
        n.enQueue(m[1])
    else :
        n.deQueue()

check = 1
for ele2 in n.item :
    if ele2 not in v.item :
        v.enQueue(ele2)
    else :
        check = 0


if check :
    print("NO Duplicate")
else :
    print("Duplicate")
