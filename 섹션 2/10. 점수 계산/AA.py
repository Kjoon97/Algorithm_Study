import sys
#sys.stdin = open("input.txt","rt")
n = input()
a = list(map(int, input().split()))
sum=0
cnt=0 #가중치
for x in a:
    if x==1:
        cnt+=1
        sum+=cnt
    else:
        cnt=0

print(sum)
