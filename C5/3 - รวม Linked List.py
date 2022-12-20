class Node :
    def __init__ (self,element) :
        self.element = element
        self.next = None 
        self.previous = None

class LinkList :
    def __init__(self) :
        self.head = None
        self.tail = None

    def push(self,e) :
        new = Node(e)
        if self.head == None :
            self.head = new
            self.tail = new
        else :
            x = self.head
            while x.next != None :
                x = x.next
            x.next = new
            new.previous = x
            self.tail = new

    def reverst(self, LL) :
        x = self.tail
        while x != None :
            LL.push(x.element)
            x = x.previous
               
    def print_ele(self) :
        x = self.head
        while x != None :
            if x.next != None :
                print(x.element,end=" ")
            else :
                print(x.element,end=" ")
            x = x.next        

list1 = LinkList()
list2 = LinkList()
inp = input("Enter Input (L1,L2) : ").split()
l1 = inp[0].split('->')
l2 = inp[1].split('->')

for i in l1 :
    list1.push(i)

for i in l2 :
    list2.push(i)

print("L1    :",end=" ")
list1.print_ele()
print()
print("L2    :",end=" ")
list2.print_ele()
print()
list2.reverst(list1)


print("Merge :",end=" ")
list1.print_ele()



#list1.print_ele()
