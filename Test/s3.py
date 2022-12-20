class Stack():
    def __init__(self):
        self.elements = []

    def push(self,data) :
        self.elements.append(data)

    def pop(self) :
        return self.elements.pop()
    
    def isEmtyp(self) :
        return self.elements == []

    def size(self) :
        return len(self.elements)

def postFixeval(st):

    s = Stack()
    i = 0
    x = 0
    y = 0
    ans = 0

    while i < len(st) :
        n = st[i]
        is_num = True

        try :
            n = int(n)
            is_num = True
        except ValueError :
            is_num = False

        if is_num :
            s.push(n)
        else :
            op = st[i]
            if not s.isEmtyp() :
                y = s.pop()
            if not s.isEmtyp() :
                x = s.pop()
            if op == "+" :
                ans = x+y
            elif op == "-" :
                ans = x-y
            elif op == "*" :
                ans = x*y
            else :
                ans = x/y
            s.push(ans)
        i+=1

    return s.pop()
        

print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())



print("Answer : ",'{:.2f}'.format(postFixeval(token)))