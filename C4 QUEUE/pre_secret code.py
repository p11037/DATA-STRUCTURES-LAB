class Queue:
    queue=[]
    size=0
    def __init__(self) :
        self.queue=[]
        self.size=0
    def Enqueue(self,x):
        self.queue.append(x)
        self.size+=1
    def Dequeue(self):
        self.size-=1
        return self.queue.pop(0)
    def size(self):
        return self.size
    def isEmpty(self):
        return self.queue==[]
code,hint=input("Enter code,hint : ").split(',')
key=ord(hint)-ord(code[0])
ans=Queue()
for i in code:
    ans.Enqueue(chr(ord(i)+key))
    print(ans.queue)