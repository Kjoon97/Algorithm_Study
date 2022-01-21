import sys
#sys.stdin = open("input.txt","rt")

n = int(input())
ch = [0]*(n+1)
cnt=0

for i in range(2,n+1):
    if ch[i]==0:
        cnt =cnt+1
        for j in range(i,n+1,i):    ##step을 i로 줘서 i배수만 돌기.
                ch[j]=1

print(cnt)


#리스트 전체를 0으로 초기화하고, 소수아닌 것들을 1로 채워나가기. 
