import sys
#sys.stdin = open("input.txt","r")

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def DFS(x,y):
    global cnt
    
    #종료 지점
    if x==6 and y==6:
        cnt+=1
        
    #뻗어가는 지점
    else:
        for i in range(4):
            xx= x+dx[i]              #나아갈 방향
            yy= y+dy[i]

            if 0<=xx<=6 and 0<=yy<=6 and board[xx][yy]==0:  #경계선 밖으로 나가지 않고 0인 통로에만 갈 수 있음.
                board[xx][yy]=1
                DFS(xx,yy)          #아래 노드로 진입
                board[xx][yy]=0     #복귀 시 1 해제
                
                

if __name__=="__main__":
    board= [list(map(int, input().split())) for _ in range(7)]
    cnt=0
    board[0][0]=1  #출발점.
    DFS(0,0)
    print(cnt)
