def printNum(num,i,str) :
    if i >= pow(2,num) :
        return str

    str += bin(i)[2:].zfill(num)+"\n"
    return printNum(num,i+1,str)


inp = int(input("Enter Number : "))

if inp < 0 :
    print("Only Positive & Zero Number ! ! !")
else :
    str = ""
    print(printNum(inp,0,str))
