x = input("Enter Input : ").split(",")
list = []
for i in x:
    if i[0] == "A" :
        a,b = i.split()
        list.append(b)
        print("Add =" , b , "and Size =" , len(list))
    else :
        if list != [] :
            index = len(list)-1
            print("Pop =" , list.pop() , "and Index =" , index)
        else :
            print(-1)
if list == [] :
    print("Value in Stack = Empty")
else :
    print("Value in Stack =",end=" ")
    for i in list :
        print(i,end=" ")
