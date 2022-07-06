import sys
#sys.stdin = open("input.txt","r")

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def DFS(x,y):
    global cnt
    
    #종료 지점
    if x==ex and y==ey:
        cnt+=1
        
    #뻗어가는 지점
    else:
        for i in range(4):
            xx= x+dx[i]              #나아갈 방향
            yy= y+dy[i]

            if 0<=xx<=n-1 and 0<=yy<=n-1 and ch[xx][yy]==0 and board[xx][yy]>board[x][y]:  #경계선 밖으로 나가지 않고 0인 통로에만 갈 수 있고 값이 더 큰 곳으로만 이동.
                ch[xx][yy]=1
                DFS(xx,yy)          #아래 노드로 진입
                ch[xx][yy]=0     #복귀 시 1 해제
                
                

if __name__=="__main__":
    n= int(input())
    board= [[0]*n for _ in range(n)]
    ch=[[0]*n for _ in range(n)]
    max=-2147000000
    min=2147000000
    for i in range(n):
        tmp = list(map(int, input().split()))   #격자 한 줄 읽기
        for j in range(n):                      #한 줄에서 최솟값, 최댓값  탐색
            if tmp[j]<min:                     
                min = tmp[j]
                sx=i                            #start 지점. 
                sy=j
            if tmp[j]>max:
                max = tmp[j]
                ex=i                            #end 지점
                ey=j
            board[i][j]= tmp[j]
    ch[sx][sy]=1                               #start 지점 체크
    cnt=0
    DFS(sx,sy)
    print(cnt)
                
