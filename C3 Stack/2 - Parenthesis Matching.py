class Stack:
    def __init__(self):
        self.elements = []

    def push(self, data):
        self.elements.append(data)

    def pop(self):
        return self.elements.pop()
    def size(self):
        return len(self.elements)

def match(op,cl) :
    return (op=="(" and cl==")") or \
        (op=="[" and cl=="]") or \
        (op=="{" and cl=="}")

def parenMatching(str):
    s = Stack()
    i = 0
    error = 0
    while i < len(str) and error == 0 :
        c = str[i]
        if c in "{[(" :
            s.push(c)
        else :
            if c in "}])" :
                if s.size() > 0 :
                    if not match(s.pop(),c) :
                        error = 1
                else :
                    error = 2
        i+=1
    if s.size() > 0 and error == 0 :
        error = 3
    return error,c,i,s

str = input("Enter expresion : ")

err,c,i,s = parenMatching(str)

if err == 1 :
    print(str,"Unmatch open-close")
elif err == 2 :
    print(str,"close paren excess")
elif err == 3 :
    print(str,"open paren excess  ",s.size(),": ",end="")
    for i in s.elements :
        print(i,end="")
    print()
else :
    print(str,"MATCH")
