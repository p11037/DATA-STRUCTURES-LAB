def difference(num, n , inp, min):
    if n >= pow(2,num):
        return min
    
    bit = list(bin(n)[2:].zfill(num))
    sb = findOne(bit, inp, 1, 0)
    if sb < min:
        min = sb
    return difference(num, n+1, inp, min)

def findOne(bit, str, sour, bitter):
    if bit.count('1') == 0:
        return abs(sour-bitter)

    e = str[bit.index('1')].split()
    sour *= int(e[0])
    bitter += int(e[1])
    bit[bit.index('1')] = 0
    return findOne(bit, inp, sour, bitter)


inp = input("Enter Input : ").split(",")
print(difference(len(inp), 1, inp, 1000000000))

