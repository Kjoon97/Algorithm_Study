import sys
#sys.stdin = open("input.txt","r")

def DFS(L,P):
    global cnt
    if L==n:
        cnt+=1
        for j in range(P):
            print(chr(res[j]+64), end='')
        print()

    else:
        for i in range(1,27):
            if code[L]==i:
                res[P]=i
                DFS(L+1,P+1)
            elif i>=10 and code[L]==i//10 and code[L+1]==i%10:
                res[P]=i
                DFS(L+2, P+1)
                
                
    
            
if __name__ == "__main__":
    code= list(map(int, input()))
    n= len(code)    #n이 종착점.
    code.insert(n,-1)    #마지막 것을 십의 자리로 두고 볼 때 일의 자리는 없으므로 -1을 추가해줌.
    res=[0]*n
    cnt=0
    DFS(0,0)
    print(cnt)
    
