import sys
#sys.stdin = open("input.txt", 'r')


def DFS(len):
    if dy[len]>0:           #dy[]에 값이 있을 경우 그냥 바로 리턴. - (메모이제이션을 이용해 가지 컷해버리) ->효율성 증가. 
        return dy[len]
    if len==1 or len==2:    # 종착점
        return len
    else:
        dy[len] = DFS(len-1)+DFS(len-2)        #메모이제이션 = 기록하는 것.
        return dy[len]

if __name_ == "__main__":
    n=int(input())
    dy=[0]*(n+1)
    print(DFS(n))
