import sys
from collections import deque
sys.stdin = open("input.txt",'r')
'''
1. 아이디어
- 2중 for문 => 값 1 && 방문x =>BFS
- BFS 돌면서 그림 개수+1, 최댓값을 갱신

2. 시간 복잡도
- BFS: O(V+E)
- V: 500*500
- E: 4*500*500
- V+E: 5*250000 = 100만 <2억 -->가능

3. 자료구조
-그래프 전체 지도: int[][]
-방문: bool[][]
-Queue(BFS)
'''

dx=[0,1,0,-1]
dy=[1,0,-1,0]
n, m = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]
ch = [[False]*m for _ in range(n)]

def bfs(x,y):
    rs=1
    q = [(x,y)]
    while q:
        ex,ey = q.pop()
        for i in range(4):
            nx = ex+dx[i]
            ny = ey+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny]==1 and ch[nx][ny]==False:
                    rs+=1
                    ch[nx][ny]=True
                    q.append((nx,ny))
    return rs

cnt=0
maxv=0
for i in range(n):
    for j in range(m):
        if board[i][j]==1 and ch[i][j]==False:
            ch[i][j]=True
            #전체 그림 개수
            cnt+=1
            #최대 그림 크기
            maxv = max(maxv, bfs(i,j))
print(cnt)
print(maxv)
