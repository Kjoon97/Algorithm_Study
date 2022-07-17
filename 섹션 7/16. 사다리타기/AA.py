import sys
from collections import deque
#sys.stdin=open("input.txt","r")

def DFS(x,y):
    ch[x][y]=1
    if x==0:                #종착 지점 행이 0일 때 열 출력.
        print(y)
    else:
        if y-1>=0 and board[x][y-1]==1 and ch[x][y-1]==0:    #경계선 안이어야하고, 왼쪽이 1이고, 한번도 방문하지 않은 경우.
            DFS(x,y-1)
        elif y+1<10 and board[x][y+1]==1 and ch[x][y+1]==0:  #경계선 안이어야하고, 오른쪽이 1이고, 한번도 방문하지 않은 경우.
            DFS(x,y+1)
        else:                                                # 오른쪽 왼쪽 모두 1이 아닌 경우, 위로 올라가기.
            DFS(x-1,y)
            


if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(10)]
    ch = [[0]*10 for _ in range(10)]
    for y in range(10):
        if board[9][y]==2:
            DFS(9,y)
