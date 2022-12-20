def findPalindrom(str,i,n,lenght) :
    if n <= lenght//2 :
        return " is palindrome"

    if str[i] == str[n-1] :
        return findPalindrom(str,i+1,n-1,lenght)
    else :
        return " is not palindrome"

inp = input("Enter Input : ")

print("\'"+inp+"\'" + findPalindrom(inp,0,len(inp),len(inp)))