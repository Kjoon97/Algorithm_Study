import sys
#sys.stdin = open("input.txt", "r")
a = input()
stack=[]
res =''
for x in a:
    if x.isdecimal():
        res+=x
    else:
        if x=='(':
            stack.append(x)
        elif x=='*' or x=='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                res+=stack.pop()
            stack.append(x)
        elif x=='+' or x=='-':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.append(x)
        elif x==')':
             while stack and stack[-1]!='(':
                  res+=stack.pop()
             stack.pop()

while stack:
    res+=stack.pop()

print(res)

'''
숫자는 그냥 문자열로 출력,
연산자,괄호는 스택에 넣기. 스택에 넣을 때, 현재 스택에 있는 연산자랑 비교,
기존 스택에 있는 연산자의 우선 순위가 더 높으면 pop, 그렇지 않으면 스택에 저장.
(는 무조건 스택에 넣기 -> )가 나오면 (이후의 연산자랑 같이 pop
--> 정리: 스택에 넣을 때 비교하고 우선 순위가 높은 걸 pop()하면 된다.
