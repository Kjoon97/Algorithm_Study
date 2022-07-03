import sys
#sys.stdin = open("input.txt","r")

def DFS(L, sum, time):
    global res
    if time > m:
        return 
    if L==n:
        if sum > res:
            res= sum
    else:
        DFS(L+1,sum+pv[L],time+pt[L])
        DFS(L+1,sum,time)



if __name__ == "__main__":
    n, m = map(int, input().split())
    pv = list()         #문제 점수
    pt = list()         #걸리는 시간.

    for i in range(n):
        a,b = map(int, input().split())
        pv.append(a)
        pt.append(b)
    res = -2147000000
    DFS(0, 0, 0) #문제 번째,L번째의 총점,할애 시간
    print(res)
