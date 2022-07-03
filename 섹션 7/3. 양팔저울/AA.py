import sys
#sys.stdin = open("input.txt","r")

def DFS(L,sum):
    global res
    if L==n:
        if 0<sum<=s:
            res.add(sum)

    else:
        DFS(L+1, sum+G[L]) #추를 왼쪽에 놓는다
        DFS(L+1, sum-G[L]) #추를 오른쪽에 놓는다.
        DFS(L+1, sum)      #L번째 추를 사용하지 않겠다. 

if __name__ == "__main__":
    n  = int(input())
    G = list(map(int, input().split()))
    s = sum(G)
    res = set()   #중복을 제거하면서 값을 추가하기 위해.
    DFS(0,0)   #추의종류, 측정할 수 있는 물의 무게
    print(s-len(res))
    
