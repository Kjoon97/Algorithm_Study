import sys
#sys.stdin = open("input.txt","r")

dx=[-1,0,1,0]
dy=[0,1,0,-1]

n= int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.insert(0,[0]*n)
a.append([0]*n)
for x in a:
    x.insert(0,0)
    x.append(0)

cnt=0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):   #상하좌우 모두 보다 커야 봉우리.
            cnt+=1

print(cnt)
# all() -> 모든 경우가 다 참일 때 True 반환.
# all()안에서 네 방향 탐색 => all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
# 상하좌우 dx,dy 배열 초기화. 
