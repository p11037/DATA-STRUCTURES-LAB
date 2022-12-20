class Queue :
    def __init__(self,list = None) :
        if list == None :
            self.item = []
        else :
            self.item = list

    def deQueue(self,index=0) :
        return self.item.pop(index)

    def enQueue(self,i) :
        self.item.append(i)

    def size(self) :
        return len(self.item)

x,y = list(input("Enter Input (Normal, Mirror) : ").split())
q1 = Queue()
q2 = Queue()
bomb = Queue()
check = 1
Expro_N = 0
Expro_M = 0
F_interrupt = 0
for i in x :
    q1.enQueue(i)


for j in y :
    q2.enQueue(j)
q2.item.reverse()

while q2.size() > 2 and check:
    for ele in range(2,q2.size()) :
        if q2.item[ele] == q2.item[ele-1] and q2.item[ele] == q2.item[ele-2] :
            bomb.enQueue(q2.item[ele])
            q2.deQueue(ele-2)
            q2.deQueue(ele-2)
            q2.deQueue(ele-2)
            Expro_M+=1
            break
        elif ele == q2.size()-1 :
            check = 0
check = 1
while q1.size() > 2 and check:
    for k in range(2,q1.size()) :
        if not bomb.size() == 0:
            if q1.item[k] == q1.item[k-1] == q1.item[k-2] and q1.item[k] != bomb.item[0] :
                q1.item.insert(k,bomb.deQueue())
            elif q1.item[k] == q1.item[k-1] == q1.item[k-2] == bomb.item[0]:
                q1.deQueue(k-2)
                q1.deQueue(k-2)
                bomb.deQueue()
                F_interrupt+=1
                break
        elif q1.item[k] == q1.item[k-1] == q1.item[k-2] :
            q1.deQueue(k-2)
            q1.deQueue(k-2)
            q1.deQueue(k-2)
            Expro_N+=1
            break
        if k == q1.size()-1 :
            check = 0

q1.item.reverse()


print("NORMAL :")
print(q1.size())
if not q1.size() == 0 :
    for ele2 in range(q1.size()) :
            print(q1.item[ele2],end="")

else :
    print("Empty",end="")
print()
print(Expro_N,"Explosive(s) ! ! ! (NORMAL)")
if not F_interrupt == 0 :
    print("Failed Interrupted",F_interrupt,"Bomb(s)")

print("------------MIRROR------------")
print(": RORRIM")
print(q2.size())
q2.item.reverse()
if not q2.size() == 0 :
    for ele3 in range(q2.size()) :
            print(q2.item[ele3],end="")

else :
    print("ytpmE",end="")
print()
print("(RORRIM) ! ! ! (s)evisolpxE",Expro_M)
#print(Expro_N , Expro_M , F_interrupt)