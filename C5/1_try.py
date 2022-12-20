class Linklist :
    class Node :
        def __init__(self,ele = None) :
            self.ele = ele
            self.next = None
    def __init__(self) :
        self.head = None
        self.size = 0

    def append(self,n) :
        newNode = self.Node(n)
        x = self.head
        if self.head == None :
            self.head = newNode
        else :
            while x.next != None :
                x = x.next
            x.next = newNode

    def str(self):
        x = self.head
        while x != None :
            if x.next != None :
                print(x.ele,end=" <- ")
            else :
                print(x.ele,end="")
            x = x.next

    def search(self,data) :
        x = self.head.next

        while x != None :
            if x == data :
                return True
            x = x.next
        return False



list = Linklist()
inp = input("Enter Input : ").split()

for i in inp :
    list.append(i)

print("Before : ")
list.str()

while list.search("0") :
    list.append(list.head.ele)
    list.head = list.head.next

print("")
print("After : ")
list.str()
