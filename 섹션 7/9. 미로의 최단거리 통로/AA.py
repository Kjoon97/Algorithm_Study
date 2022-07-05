import sys
from collections import deque
#sys.stdin = open("input.txt","r")

dx=[-1,0,1,0]
dy=[0,1,0,-1]

board = [list(map(int, input().split())) for _ in range(7)]
dis=[[0]*7 for _ in range(7)]
Q=deque()
Q.append((0,0))
board[0][0]=1       #출발점 - 한번 방문했으므로 다시 방문 안하게 1로 초기화함.

while Q:            #Q가 빌 때까지 반복
    tmp = Q.popleft()
    for i in range(4):
        x=tmp[0]+dx[i]
        y=tmp[1]+dy[i]
        if 0<=x<=6 and 0<=y<=6 and board[x][y]==0:     #이 조건을 세워야 경계선 밖으로 나가지 않고 0인 통로에만 갈 수 있음.
            board[x][y]=1                              #한번 방문한 곳은 다시 방문 안하게 벽(1)으로 만들기
            dis[x][y]= dis[tmp[0]][tmp[1]]+1
            Q.append((x,y))

if dis[6][6]==0:             #벽에 가로막혀서 도착점에 못 온 경우.
    print(-1)
else:
    print(dis[6][6])
    
