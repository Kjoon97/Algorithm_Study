import sys
#sys.stdin = open("input.txt",'r')
#5개의 숫자 중 3개를 뽑아 합이 6의 배수인 조합의 경우의 수 구하기

def DFS(L,s,sum):
    global cnt
    if L==k:
        if sum%m==0:
            cnt+=1
    else:
        for i in range(s, n):
            DFS(L+1, i+1, sum+a[i])


if __name__ =="__main__":
    n, k = map(int, input().split())
    a=list(map(int, input().split()))
    m=int(input())
    cnt=0
    DFS(0,0,0)
    print(cnt)
