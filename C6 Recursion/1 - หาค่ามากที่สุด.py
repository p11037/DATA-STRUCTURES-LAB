def findMax(str,n) :
    if n == 1 :
        return int(str[0])

    if int(str[0]) < int(str[n-1]) :
        str[0] = str[n-1]
    return findMax(str[:n-1],n-1)


inp = input("Enter Input : ").split()

#print(inp[:2])
print("Max :",findMax(inp,len(inp)))