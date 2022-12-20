def hbd(age):
    i=1
    while (i<=age/2) : 
        if age//i == 2 :
            if age%i == 0 :
                return "saimai is just 20, in base "+str(i)+"!"
            if age%i == 1 :
                return "saimai is just 21, in base "+str(i)+"!"
        i+=1

    
    

year = input("Enter year : ")

print(hbd(int(year)))