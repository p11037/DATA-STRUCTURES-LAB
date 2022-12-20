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


c1 = Queue()
c2 = Queue()
main = Queue()
n = 1
n_c2 = 1

inp = input("Enter people : ")

for i in inp :
    main.enQueue(i)

while main.size() != 0 :

    if c1.size() == 5 :
        c2.enQueue(main.deQueue())
    else :
        c1.enQueue(main.deQueue())

    

    print(n ,main.item ,c1.item ,c2.item)

    if(n_c2%2 == 0) :
        c2.deQueue()

    if c2.size() != 0 :
        n_c2+=1
        
    if(n%3 == 0) :
        c1.deQueue()

    n+=1

