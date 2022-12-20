class Stack :
    def __init__(self) :
        self.element = []
    
    def push(self,ele1) :
        ele = int(ele1)
        while self.size() != 0 and ele >= int(self.peek()) :
            self.element.pop()
        self.element.append(ele)
    
    def pop(self) :
        self.element.pop()

    def peek(self) :
        return self.element[-1]

    def size(self) :
        return len(self.element)

    def clear(self) :
        self.element = []

stack = Stack()
list = []
inp = input("Enter Input : ").split(",")

for ele in inp :
    if ele[0] == "A" :
        a = ele.split()
        stack.push(a[1])
    elif ele[0] == "B" :
        print(stack.size())
    else :
        for i in stack.element :
            list.append(int(i))
        
        for k in range(len(list)) :
            if list[k] % 2 == 0 :
                list[k]-=1
            else :
                list[k]+=2
        stack.clear()
        for j in list :
            stack.push(j)

