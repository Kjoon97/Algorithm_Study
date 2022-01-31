#----------------모범답안----------------------

s= input()
res=0
for x in s:
    if x.isdecimal():
        res= res*10+int(x)   #숫자로 만들기
print(res)
cnt=0
for i in range(1, res+1):
    if res%i==0:
        cnt+=1
print(cnt)

# isdecimal()은 0~9까지만 확인해줌,
# isdigit()는 숫자 형태는 다 확인해줌.




'''내가 쓴답 success:100
import sys
#sys.stdin = open("input.txt","rt")
s = input()
result=[]

for i in s:
    if i.isdigit():
        result.append(i)

result=int("".join(result))
print(result)
cnt=1
for i in range(1, result//2+1):
    if result % i == 0:
        cnt+=1
print(cnt)
'''
