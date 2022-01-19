import sys
sys.stdin = open("input.txt","rt")

a, b = map(int, input().split())
print(a,b)
cnt =[0] * (a+b+3)
max=-2147000000
for i in range(1, a+1): #i - 1~4
    for j in range(1, b+1): #j - 1~6
        cnt[i+j] = cnt[i+j] +1

for i in range(a+b+1):
    if cnt[i]>max:
        max = cnt[i]
for i in range(a+b+1):
    if cnt[i] == max:
        print(i, end=" ")

#max값을 먼저 구하고 다시 for문과 max값을 이용해서 max값과 동일한 숫자의
#인덱스를 출력함.

