class LinkList:
    class _Node :
        def __init__(self, element) :
            self._element = element
            self._next = None
    def __init__(self) :
        self._head = None
        self._size = 0

    def __len__(self) :
        return self._size

    def is_empty(self) :
        return self._size == 0

    def push(self,e) :
        if self._head == None :
            self._head = self._Node(e)
        else :
            x = self._head
            while x._next != None :
                x = x._next
            x._next = self._Node(e)
        self._size += 1
    
    def print_ele(self) :
        x = self._head
        while x != None :
            if x._next != None :
                print(x._element,end=" <- ")
            else :
                print(x._element,end="")
            x = x._next

            
    def FindingZero(self) :
        x = self._head
        while x._next != None :
            x = x._next
        x._next = self._head 

        # print(x._next._element)
        # print("-------------")
        while x._next._element != "0" :
            x = x._next
            #print(x._element)
        self._head = x._next
        # print("*******")
        # print(self._head._element)
        x._next = None


            
list = LinkList()
print(" *** Locomotive ***")
inp = input("Enter Input : ").split()


for i in inp :
    list.push(i)

print("Before : ",end="")
list.print_ele()
print()
list.FindingZero()
print("After : ",end="")
list.print_ele()


#for j in range(list.__len__()) :
