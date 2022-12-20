def maxIndex(list, i, j):
     if i == j:
          return i
     k = maxIndex(list, i + 1, j)
     return (k if list[i] < list[k] else i)

def straightSelectionSort(list, n):
     if n == 0:
          return
     k = maxIndex(list, 0, n)
     if k != n :
          temp = list[k]
          list[k] = list[n]
          list[n] = temp
          print(f'swap {list[k]} <-> {list[n]} : {list}')
     straightSelectionSort(list, n-1)

inp = [int(i) for i in input("Enter Input : ").split()]

straightSelectionSort(inp, len(inp)-1)

print(inp)

# Enter Input : 5 4 3 1 2
# swap 2 <-> 5 : [2, 4, 3, 1, 5]
# swap 1 <-> 4 : [2, 1, 3, 4, 5]
# swap 1 <-> 2 : [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]