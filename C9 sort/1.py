def bubbleSort(n:int,lis:list):

    if n < 0:
        return
    
    bubbleSort(n-1,lis)
    if lis[n] > lis[n+1]:
        lis[n] , lis[n+1] = lis[n+1] , lis[n]

    
    bubbleSort(n-1,lis)
    if lis[n] > lis[n+1]:
        lis[n] , lis[n+1] = lis[n+1] , lis[n]

    return lis
    


lis = [] or list(map(int,input("Enter Input : ").split()))
print(bubbleSort(len(lis)-2,lis))

