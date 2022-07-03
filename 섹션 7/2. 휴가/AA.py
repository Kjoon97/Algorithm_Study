import sys
#sys.stdin = open("input.txt","r")

def DFS(L,sum):
    global res
    if L==n+1:
        if sum > res:
            res=sum
    else:
        if L+T[L]<=n+1:
            DFS(L+T[L],sum+P[L])  #상담을 하게 될 경우
        DFS(L+1,sum)              #상담 안 할 경우
             
        
        

if __name__ == "__main__":
    n  = int(input())
    T = list()
    P = list()
    for i in range(n):
        t, p = map(int, input().split())
        T.append(t)
        P.append(p)
    res=-2147000000
    T.insert(0,0)      #삽입하면 뒤로 미는 효과
    P.insert(0,0)
    DFS(1,0)     #날짜, 얻을 수 있는 수익 총합
    print(res)
