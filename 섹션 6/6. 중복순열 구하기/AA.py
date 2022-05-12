import sys
#sys.stdin = open("input.txt",'r')
input = sys.stdin.readline   #대량의 입력할 때 엄청 빨라짐.

def DFS(L):
    global cnt
    if L==m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1, n+1):
            res[L]=i
            DFS(L+1)
    

if __name__ == "__main__":
    n,m = map(int, input().split())
    res = [0]*m
    cnt=0
    DFS(0)
    print(cnt)
# 1~n까지의 구슬을 m번 중복으로 뽑아.

'''
input = sys.stdin.readline   #대량의 입력할 때 엄청 빨라짐.
                            문자열을 읽을 때는 문자열 끝의 줄바꿈 기호까지 읽힘.
s = input().rstrip();  -> 줄바꿈 기호 제거 (오른쪽 것을 strip)
'''
