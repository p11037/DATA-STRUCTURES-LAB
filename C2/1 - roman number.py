from distutils.command.install_egg_info import safe_name


class translator:
    ans=""
    sum=0
    def __init__(self) :
        pass
    def deciToRoman(self, num):
        self.ans=""
        num=int(num)
        while num>=1000:
            num-=1000
            self.ans+='M'
        if num>=900:
            num-=900
            self.ans+='CM'
        if num>=500:
            num-=500
            self.ans+='D'
        if num>=400:
            num-=400
            self.ans+='CD'
        while num>=100:
            num-=100
            self.ans+='C'
        if num>=90:
            num-=90
            self.ans+='XC'
        if num>=50:
            num-=50
            self.ans+='L'
        if num>=40:
            num-=40
            self.ans+='XL'
        while num>=10:
            num-=10
            self.ans+='X'
        if num>=9:
            num-=9
            self.ans+='IX'
        if num>=5:
            num-=5
            self.ans+='V'
        if num>=4:
            num-=4
            self.ans+='IV'
        while num>=1:
            num-=1
            self.ans+='I'
        return self.ans 

    def romanToDeci(self, s):
        i=0
        while i <len(s):
            if s[i]=='M':
                self.sum+=1000
            elif s[i]=='D':
                self.sum+=500
            elif s[i]=='C':
                if i+1<len(s) and s[i+1]=='M':
                    self.sum+=900
                    i+=1
                elif i+1<len(s) and s[i+1]=='D':
                    self.sum+=400
                    i+=1
                else:
                    self.sum+=100
            elif s[i]=='L':
                self.sum+=50
            elif s[i]=='X':
                if i+1<len(s) and s[i+1]=='C':
                    self.sum+=90
                    i+=1
                elif i+1<len(s) and s[i+1]=='L':
                    self.sum+=40
                    i+=1
                else:
                    self.sum+=10
            elif s[i]=='V':
                self.sum+=5
            elif s[i]=='I':
                if i+1<len(s) and s[i+1]=='X':
                    self.sum+=9
                    i+=1
                elif i+1<len(s) and s[i+1]=='V':
                    self.sum+=4
                    i+=1
                else:
                    self.sum+=1
            i+=1
        return self.sum

num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))