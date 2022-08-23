import sys
#sys.stdin = open("input.txt",'r')
input = sys.stdin.readline
each=0
dx=[0,1,0,-1]
dy=[1,0,-1,0]

n = int(input())
m = [list(map(int, input().strip())) for _ in range(n)]
ch= [[False]*n for _ in range(n)]
result=[]

def dfs(x,y):
    global each
    each+=1
    for i in range(4):
        nx= x+dx[i]
        ny= y+dy[i]

        if 0<=nx<n and 0<=ny<n:
            if m[nx][ny]==1 and ch[nx][ny]==False:
                ch[nx][ny]=True
                dfs(nx,ny)
                

for i in range(n):
    for j in range(n):
        if m[i][j]==1 and ch[i][j]==False:
            ch[i][j]=True
            each=0
            dfs(i,j)
            result.append(each)

result.sort()
print(len(result))
for x in result:
    print(x)
