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

q1 = Queue()
q2 = Queue()
Activity = ["Eat","Game","Learn","Movie"]
Place = ["Res.","ClassR.","SuperM.","Home"]
score = 0


inp = input("Enter Input : ").split(",")

for ele in inp :
    x = ele.split()
    q1.enQueue(x[0])
    q2.enQueue(x[1])
print("My   Queue =",end=" ")
for i in range(q1.size()) :
    if not i == q1.size()-1 :
        print(q1.item[i],end=", ")
    else :
        print(q1.item[i])

print("Your Queue =",end=" ")
for j in range(q2.size()) :
    if not j == q2.size()-1 :
        print(q2.item[j],end=", ")
    else :
        print(q2.item[j])

print("My   Activity:Location =",end=" ")
for i in range(q1.size()) :
    A,B = map(int,q1.item[i].split(":"))
    if not i == q1.size()-1 :
        print(Activity[A],":",Place[B],end=", ",sep="")
    else :
        print(Activity[A],":",Place[B],sep="")

print("Your Activity:Location =",end=" ")
for j in range(q2.size()) :
    A,B = map(int,q2.item[j].split(":"))
    if not j == q2.size()-1 :
        print(Activity[A],":",Place[B],end=", ",sep="")
    else :
        print(Activity[A],":",Place[B],sep="")

    X,Y = map(int,q1.item[j].split(":"))

    if A == X and B != Y:
        score+=1
    elif A != X and B == Y:
        score+=2
    elif A == X and B == Y:
        score+=4
    else :
        score-=5

if score >= 7 :
    print("Yes! You're my love! : Score is ",score,".",sep="")
elif score < 7 and score > 0 :
    print("Umm.. It's complicated relationship! : Score is ",score,".",sep="")
else :
    print("No! We're just friends. : Score is ",score,".",sep="")
