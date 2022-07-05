import sys
from collections import deque
#sys.stdin = open("input.txt","r")

MAX=10000
ch=[0]*(MAX+1)
dis=[0]*(MAX+1)

n,m = map(int, input().split())

ch[n]=1
dis[n]=0

dQ = deque()
dQ.append(n)

while dQ:
    now = dQ.popleft()  #큐에서 하나 꺼내서 now(현재 위치)에 반환.
    if now==m:         #목적지 탐색하면 바로 break
        break
    for next in(now-1, now+1, now+5):   #next가 now-1, now+1, now+5 각각 한번 씩 세번 돈다.
        if 0<next<=MAX:
            if ch[next]==0:   # 최초 방문일 때만 방문.
                dQ.append(next)
                ch[next]=1
                dis[next]=dis[now]+1
print(dis[m])
        
