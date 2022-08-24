import sys
sys.stdin = open("input.txt",'r')
input = sys.stdin.readline

n,m = map(int,input().split())
x,y,d = map(int,input().split())
map = [list(map(int,input().split()))for _ in range(n)]
cnt=0
dx=[-1,0,1,0]
dy=[0,1,0,-1]

while True:
    if map[x][y]==0:
        map[x][y]=2
        cnt+=1
        
    sw= False
    for i in range(1,5):
        nx=x+dx[d-i]
        ny=y+dy[d-i]
        if 0<=nx<n and 0<=ny<m:
            if map[nx][ny]==0:   #청소하지 않은 공간이 존재한다면.
                d=(d-i+4)%4
                x=nx
                y=ny
                sw = True
                break
            
    #4방향 모두 있지 않은 경우.
    if sw == False:
        nx = x-dx[d]
        ny = y-dy[d]
        if 0<=nx<n and 0<=ny<m:
            if map[nx][ny] ==1:
                break
            else:
                x=nx
                y=ny
        else:
            break
        
print(cnt)
