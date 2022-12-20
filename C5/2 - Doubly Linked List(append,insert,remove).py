class Node :
    def __init__ (self,element) :
        self.element = element
        self.next = None 
        self.previous = None

class LinkList :
    def __init__(self) :
        self.head = None
        self.tail = None

    def append(self,data) :
        new = Node(data)
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
        
    def isEmpty(self):
        return self.head == None

    def size(self) :
        j = self.head
        count = 0
        while j != None :
            j = j.next
            count += 1
        return count

    def insert(self, index, data):
        new = Node(data)
        x = self.head
        id = 0
        if index < 0 :
            print("Data cannot be added")
        elif index == 0 :
            print("index = 0 and data =",data)
            self.add_head(data)
        elif self.isEmpty() and index != 0 :
            print("Data cannot be added")
        elif index > self.size() :
            print("Data cannot be added")
        elif index == self.size() :
            print("index =",index,"and data =",data)
            self.append(data)
        else :
            while id != index :
                x = x.next
                id+=1
            #print(x.element)
            x.previous = new
            new.next = x

            x = self.head
            id = 0

            while id != index-1 :
                x = x.next
                id+=1
            x.next = new
            new.previous = x
        
            print("index =",index,"and data =",data)

    def remove(self, data):
        count = 0
        x = self.head
        if x != None :
            if x.element == data :
                print("removed :",data,"from index :",0)
                if self.head == self.tail :
                    self.head = None
                    self.tail = None 
                    return
                else : 
                    self.head = x.next
                    x = x.next
                    x.previous = None
                    return
                

        while x != None :
            if x.element == data :
                break
            y = x
            x = x.next
            count += 1

        if x == None :
            print("Not Found!")
            return
        elif x.next == None :
            self.tail = x.previous
            y.next = x.next
        else :
            y.next = x.next
            x = x.next
            x.previous = y

        print("removed :",data,"from index :",count)

    def add_head(self,data) :
        new = Node(data)
        if self.head == None :
            self.head = new
            self.tail = new
        else :
            x = self.head
            new.next = x
            x.previous = new
            self.head = new
            
    def str_reverse(self) :
        x = self.tail
        while x != None :
            if x.previous != None :
                print(x.element,end="->")
            else :
                print(x.element,end=" ")
            x = x.previous
            
            
    def __str__(self) :
        x = self.head
        while x != None :
            if x.next != None :
                print(x.element,end="->")
            else :
                print(x.element,end=" ")
            x = x.next

list = LinkList()
inp = input("Enter Input : ").split(",")

for ele in inp :
    ele = ele.strip()
    if ele[0] == "A" and ele[1] == "b":
        ab = ele.split()
        list.add_head(int(ab[1]))
    elif ele[0] == "I" :
        i1 = ele.split()
        i2 = i1[1].split(":")
        list.insert(int(i2[0]),int(i2[1]))
    elif ele[0] == "A" :
        n = ele.split()
        list.append(int(n[1]))
    else :
        r = ele.split()
        list.remove(int(r[1]))

    print("linked list : ",end="")
    list.__str__()
    print()
    print("reverse : ",end="")
    list.str_reverse()
    print()