import sys
#sys.stdin = open("input.txt","r")

def DFS(x,y):
    
    if dy[x][y]>0:                   #메모이제이션 cut-edge
        return dy[x][y]
    
    if x==0: and y==0:
        return arr[0][0] 
    else:
        if y==0:
            dy[x][y] =  DFS(x-1, y)+arr[x][y]
        elif x==0:
            dy[x][y] = DFS(x,y-1)+arr[x][y]
        else:
            dy[x][y] = min(DFS(x-1,y), DFS(x,y-1)) + arr[x][y]

        return dy[x][y]
        
            
            


n= int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dy = [[0]*n for _ in rane(n)]   #메모이제이션하기 위해
print(DFS(n-1,n-1))
