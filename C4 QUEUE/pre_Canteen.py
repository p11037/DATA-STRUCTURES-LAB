class CanteenQueue:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def push(self, i):
        self.items.append(i)
    def pop(self, i):
        return self.items.pop(i)
    def peek(self):
        return self.items[0]
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)


q = CanteenQueue()
qid = CanteenQueue()
ls1,ls2 = input("Enter Input : ").split('/')
ls1 = ls1.split(',')
ls2 = ls2.split(',')
pair = []

for e in ls1:
    num,id = e.split()
    pair.append((num,id))

for e in ls2:
    if e.startswith("E"):
        e = e.replace("E ","")
        for j in range(len(ls1)):
            # print("--------")
            # print(j)
            if e == pair[j][1]:
                # print("--------")
                # print((pair[j][0], e))
                q.push((pair[j][0], e))
                if qid.items.count(pair[j][0]) == 0:
                    qid.push(pair[j][0])
                else:
                    qid.items.insert(qid.items.index(pair[j][0]), pair[j][0])
    elif e.startswith("D"):
        count = 0
        if q.isEmpty() == True:
            print("Empty")
        else:
            for ele in q.items:
                if ele[0] == qid.peek():
                    print(q.items[count][1])
                    q.pop(count)
                    qid.pop(0)
                    break
                count+=1