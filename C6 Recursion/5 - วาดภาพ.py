output = ''
def staircase(line,sharp):
    global output
    if line == 0:
        return 'Not Draw!'
    elif line > 0:
        output += '_'*(line-1) + '#'*(sharp+1) + '\n'
        if line-1 == 0:
            return output
        return staircase(line-1,sharp+1)
    elif line < 0:
        output += '_'*(sharp) + '#'*abs(line) + '\n'
        if line+1 == 0:
            return output
        return staircase(line+1,sharp+1)

print(staircase(int(input("Enter Input : ")),0))