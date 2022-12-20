n=int(input("Enter Input : "))
for i in range(n+2):    
    for k in range(n+2):
        if(k<n+1-i):
            print(".",end="")
        else:
            print("#",end="")
    for k in range(n+2):
        if i==0 or k==0 or k==n+1 or i==n+1:
            print("+",end="")
        else:
            print("#",end="")
    print()
for i in range(n+2):    
    for k in range(n+2):
        if i==0 or k==0 or k==n+1 or i==n+1:
            print("#",end="")
        else:
            print("+",end="")
    for k in range(n+2):
        if(k<n+2-i):
            print("+",end="")
        else:
            print(".",end="")
    print()