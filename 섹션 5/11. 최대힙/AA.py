import sys
import heapq as hq
#sys.stdin = open("input.txt",'r')

a=[]
while True:
    n= int(input())
    if n==-1:
        break
    if n==0:
        if len(a)==0:
            print(-1)
        else:
            print(-hq.heappop(a))
    else:
        hq.heappush(a,-n)


# 최대 힙은 입력할 때 숫자를 음수화하고 pop할 때 다시 양수화시키면 된다. 
