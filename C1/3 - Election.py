import statistics as stats
print("*** Election ***")

# number of elements as input
n = int(input("Enter a number of voter(s) : "))

# iterating till the range
a = [int(x)for x in input().split() if 0<int(x)<21]

if len(a) > 0 :
    print(stats.mode(a))
else : print("*** No Candidate Wins ***")

#mode
"""mode = stats.mode(a)
if (mode>=1) and (mode<=20) :
    print(mode)
else : print("*** No Candidate Wins ***") """

