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
            print(hq.heappop(a))
    else:
        hq.heappush(a,n)


# hq.heappop(a) = a리스트에서 힙 정렬을 이용해 최솟값(루트값)을 반환하는 것.
# hq.heappush(a,n) = a리스트에 n값을 넣고 힙 트리형태로 정렬해줌.
# 최소힙은 그려보면서 동작 원리 이해하는 것이 중요하다.(면접에도 중요)
