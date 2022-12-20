class Node :
    def __init__ (self,element) :
        self.element = element
        self.next = None 
        self.previous = None

class LinkList :
    def __init__(self) :
        self.head = Node("|")
        self.tail = Node("|")

    def append(self,data) :
        new = Node(data)
        x = self.head
        if x.element == "|" :
            new.next = x
            x.previous = new
            self.head = new

        else :
            while x.element != "|" :
                x = x.next
            before = x.previous
            x.previous = new
            new.next = x
            before.next = new
            new.previous = before

    def Left(self) :
        x = self.head
        if self.head == "|" :
            return
        while x.element != "|" :
            x = x.next
        if x.previous == None :
            return
        before = x.previous
        data_before = before.element
        before.element = x.element
        x.element = data_before

    def Right(self) :
        x = self.head
        while x.element != "|" :
            x = x.next
        if x.next == None :
            return
        after = x.next
        data_after = after.element
        after.element = x.element
        x.element = data_after

    def Backspace(self) :
        x = self.head
        while x.element != "|" :
            x = x.next
        if x.previous == None :
            return
        before = x.previous
        if before == self.head :
            self.head = x
            x.previous = None
        else :
            x.previous = before.previous
            before.previous.next = x

    
        

    def __str__(self) :
        x = self.head
        while x != None :
            print(x.element,end=" ")
            x = x.next

    def isEmpty(self):
        return self.head == None

    def size(self) :
        j = self.head
        count = 0
        while j != None :
            j = j.next
            count += 1
        return count

list = LinkList()
inp = input("Enter Input : ").split(",")

for ele in inp :
    if ele[0] == "I" :
        i = ele.split()
        list.append(i[1])
    elif ele[0] == "L" :
        list.Left()
    elif ele[0] == "R" :
        list.Right()
    elif ele[0] == "B" :
        list.Backspace()
    else :
        list.Delete()
list.__str__()