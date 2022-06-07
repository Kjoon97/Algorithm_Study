import sys
sys.stdin = open("input.txt","r")

def DFS(v):
    global cnt
    if v == n:
        cnt+=1
        for x in path:
            print(x, end=' ')
        print()
    else:
        for i in range(1,n+1):
            if g[v][i]==1 and ch[i]==0:   #그래프에서 볼 때 1이 존재하냐(경로가 존재하냐) and 아직 그 경로를 가지 않아야.
                ch[i]=1
                path.append(i)
                DFS(i)
                path.pop()
                ch[i]=0 # 해당 레벨에서 나오면 체크 해


if __name__ == "__main__":
    n, m = map(int, input().split())
    g=[[0]*(n+1) for _ in range(n+1)]   #그래프 - 인덱스 0은 사용 x, 1~n 인덱스 사용하기 위해 n+1개로 함.
    ch=[0]*(n+1)                        #체크리스트.  - 인덱스 0은 사용 x, 1~n 인덱스
    for i in range(m):
        a, b = map(int, input().split())
        g[a][b]=1
    cnt=0
    path=[]             #경로 추적.
    path.append(1)
    ch[1]=1
    DFS(1)
    print(cnt)

'''
n= 노드 개수, m = 간선 수 
한번 방문한 노드는 방문하지 말아야함. -> 체크 리스트 활용.
DFS(1)노드 방문하면 체크리스트에 1번 체크.
DFS(1)에서 5가닥으로 for문으로 1,2,3,4,5 각각 연결 유무 확인. (1은 자기 자신이므로 패스)
연결된 노드 있으면 그쪽에서 다시 DFS(2)로 1,2,3,4,5 각각 연결유무 확인.
자기 자신 패스, 체크리스트에 있는 숫자 패스.
그러다가 종착점이 n이면 종료+ cnt 1추가.
상위 레벨의 DFS()로 이동 + 체크리스트에서 이동한만큼 체크 삭제.
'''
