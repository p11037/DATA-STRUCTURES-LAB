class Queue :
    def __init__(self) :
        self.item = []

    def De_QUEUE(self) :
        return self.item.pop(0)

    def En_QUEUE(self,i) :
        self.item.append(i)

    def size(self) :
        return len(self.item)


q = Queue()

inp = input("Enter Input : ").split(",")

for ele in inp :
    if ele[0] == "E" :
        n = (ele).split()
        q.En_QUEUE(int(n[1]))
        print(q.size())
    else :
        if not q.size() == 0 :
            print(q.De_QUEUE(),0)
        else :
            print(-1)
    

if not q.size() == 0 :
    for i in q.item :
        print(i,end=" ")
else :
    print("Empty")
        



