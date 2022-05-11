import sys
#sys.stdin = open("input.txt",'r')
def DFS(indx, sum,tsum):
    global result
    if sum+(total-tsum)<result:
        return
    if sum >c:
        return 
    if indx==n:
        if sum>result:
            result=sum
    else:
        DFS(indx+1, sum+a[indx], tsum+a[indx])
        DFS(indx+1, sum, tsum+a[indx])
   

if __name__=="__main__":
    c, n = map(int, input().split())
    a = [0]*n
    result = -2174000000
    for i in range(n):
        a[i] = int(input())
    total=sum(a)
    DFS(0,0,0)
    print(result)
