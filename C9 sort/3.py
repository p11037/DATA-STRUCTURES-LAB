def insertion(l,sl=[],i=0):
    if len(sl)==0:sl=[l.pop(0)]
    if i==len(sl) or l[0]<=sl[i]:
        sl.insert(i,l.pop(0))
        print("insert",sl[i],"at index",i,":",sl,end="")
        if len(l)==0:
            return sl
        print("",l)
        return insertion(l,sl)
    else:
        return insertion(l,sl,i+1)

l = [int(i)for i in input("Enter Input : ").split()]
l = insertion(l)
print("\nsorted")
print(l)

# Enter Input : 1 2 3 4
# insert 2 at index 1 : [1, 2] [3, 4]
# insert 3 at index 2 : [1, 2, 3] [4]
# insert 4 at index 3 : [1, 2, 3, 4] 
# sorted
# [1, 2, 3, 4]
