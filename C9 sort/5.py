def selectionSort(list) :
    for last in range(len(list) -1, -1, -1) :
        max = list[0]
        maxIndex = 0
        for i in range(1, last + 1) :
            if list[i] > max :
                max = list[i]
                maxIndex = i
        list[last], list[maxIndex] = list[maxIndex], list[last]    
    return list

def sortLen(list) :
    for i in range(len(list) -1) :
        swap = False
        for j in range(len(list) - i - 1) :
            if len(list[j]) > len(list[j + 1]) :
                list[j], list[j + 1] = list[j + 1], list[j]
                swap = True
        if not swap:
            break
    return print('No Subset') if list == [] else print(*list, sep='\n')

def subset(l, s, i = 0, out = [], temp = []):  
    if i >= len(l) :
        return out
    temp.append(l[i])
    if sum(temp) == s:
        out.append(temp.copy())
    out = subset(l, s, i + 1, out, temp)
    temp.pop()
    out = subset(l, s, i + 1, out, temp)
    return out
    

inp = input('Enter Input : ').split('/')
lst = list(map(int, inp[1].split()))
sortLen(subset(selectionSort(lst), int(inp[0])))