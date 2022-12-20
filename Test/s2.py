from distutils.log import error


class Stack :
    def __init__(self):
        self.elements = []

    def push(self,data) :
        self.elements.append(data)

    def pop(self) :
        return self.elements.pop()

    def peek(self) :
        return self.elements[-1]

    def size(self) :
        return len(self.elements)

    def isEmpty(self) :
        return self.elements == []

def Match(op,cl) :
    open = "([{"
    close = ")]}"
    return open.index(op) == close.index(cl)

def parenMatching(str) :
    s = Stack()
    error = 0
    i = 0
    while i < len(str) and error == 0 :
        c = str[i]
        if c in "([{" :
            s.push(c)
        elif c in ")]}" :
            if s.size() > 0 :
                if not Match(s.pop(),c) :
                    error = 1 # Not Match
            else :
                error = 2 # close excess
        i+=1
    
    if s.size() > 0 and error == 0 :
        error = 3 
    
    return error,s

inp = input("Enter expresion : ")

error,s = parenMatching(inp)

if error == 1 :
    print(inp,"Unmatch open-close")
elif error == 2 :
    print(inp,"close paren excess")
elif error == 3 :
    print(inp,"open paren excess  ",s.size(),": ",end="")
    for j in s.elements :
        print(j,end="")
else :
    print(inp,"MATCH")
