def odd_even(type, data, mode):
    start = 0
    if mode == "Odd" :
        start = 0
    else : 
        start = 1

    if type == "S" :
        a = ""
        for n in range (start,len(data),2):
            a += data[n]
        return a
    else :
        list = []
        list_data = [m for m in data.split()]
        for n in range (start,len(list_data),2):
            list.append(list_data[n])
        return list


print("*** Odd Even ***")
x,y,z = input("Enter Input : ").split(",")
print(odd_even(x,y,z))