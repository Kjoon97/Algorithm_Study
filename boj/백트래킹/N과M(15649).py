import sys
sys.stdin = open("input.txt",'r')
def dfs(idx):
    if idx == m:
        for x in res:
            print(x, end=' ')
        print()
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                res[idx]=i
                dfs(idx+1)
                res[idx]=0
                ch[i]=0


n, m = map(int, input().split())
nums = [range(1,n+1)]
ch =[0]*(n+1)
res =[0]*m
dfs(0)
