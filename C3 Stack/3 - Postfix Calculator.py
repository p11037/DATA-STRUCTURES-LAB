class Stack():

    def __init__(self):
        self.elements = []

    def push(self, data):
        self.elements.append(data)

    def pop(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)

    def isEmpty(self):
        return self.elements == []

def postFixeval(st):

    i=0
    x=0
    y=0
    answer = 1
    s = Stack()

    while i < len(st):
        n = st[i]
        is_num = True

        try:
            n = int(n)
            is_num = True
        except ValueError:
            is_num = False

        if is_num :
            s.push(n)
        else :
            op = st[i]
            if not s.isEmpty() :
                y = s.pop()
            if not s.isEmpty() :
                x = s.pop()
            if op == "+" :
                answer = x+y
            elif op == "-" :
                answer = x-y
            elif op == "*" :
                answer = x*y
            else :
                answer = x/y
            s.push(answer)
        i+=1
    return s.pop()

print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())

print("Answer : ",'{:.2f}'.format(postFixeval(token)))