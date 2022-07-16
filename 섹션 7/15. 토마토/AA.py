import sys
from collections import deque
#sys.stdin=open("input.txt","r")
dx=[-1,0,1,0]
dy=[0,1,0,-1]

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(m)]

Q=deque()

dis = [[0]*n for _ in range(m)]  #거리 기록 용 격자.

for i in range(m):
    for j in range(n):
        if board[i][j]==1:           #익은 토마토일 때.
            Q.append((i,j))

while Q:
    tmp = Q.popleft()
    for i in range(4):
        xx=tmp[0]+dx[i]
        yy=tmp[1]+dy[i]

        if 0<=xx<m and 0<=yy<n and board[xx][yy]==0:
            board[xx][yy]=1              #더 이상 방문 하지 않도록 익은 토마토로 변경
            dis[xx][yy]=dis[tmp[0]][tmp[1]]+1
            Q.append((xx,yy))


flag=1

for i in range(m):
    for j in range(n):
        if board[i][j]==0:           #익지 않은 토마토가 존재하면 flag를 0으로. 
            flag=0

result=0

if flag==1:                              #모두 익은 경우.
    for i in range(m):
        for j in range(n):
            if dis[i][j]>result:
                result=dis[i][j]          #날짜 중 최댓 값 구하는 것이 최종일자 구하는 것.
    print(result)
else:                                     #안익은 토마토가 있는 경우. 
    print(-1)


        
                
