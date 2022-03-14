import sys
#sys.stdin = open("input.txt", "r")
s = input()
stack=[]
sum=0
for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1]=='(':
            sum+=len(stack)
        elif s[i-1]==')':
            sum+=1

print(sum)

