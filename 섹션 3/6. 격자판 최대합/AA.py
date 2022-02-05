import sys
#sys.stdin = open("input.txt","rt")
#---------------모범답안------------------------------
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
largest=-2147000000
for i in range(n):
    sum1 = sum2 =0
    for j in range(n):
        sum1+=a[i][j]
        sum2+=a[j][i]
    if sum1>largest:
        largest=sum1
    if sum2>largest:
        largest=sum2
sum1=sum2=0
for i in range(n):
    sum1+=a[i][i]
    sum2+=a[i][n-i-1]
    if sum1>largest:
        largest=sum1
    if sum2>largest:
        largest=sum2

print(largest)
        
'''
#------------------나의 답(success100)------------------
a = []
small=0
sum1=0
sum2=0
sum3=0
sum4=0

n = int(input())
for _ in range(n):
    a.append(list(map(int, input().split())))
    
#행끼리 비교.
for i in range(n):
    if sum1 < sum(a[i]):
        sum1 = sum(a[i])
    sum2=0
    for j in range(n):
        sum2 += a[j][i]
    if small < sum2:
        small=sum2
    sum3 +=a[i][i]
    sum4 +=a[i][n-1-i]

result = [sum1,small,sum3,sum4]
print(max(result))
'''
# a = [list(map(int,input().split())) for _ in range(n)] 이렇게 리스트를 한꺼번에 받을 수 있다.
