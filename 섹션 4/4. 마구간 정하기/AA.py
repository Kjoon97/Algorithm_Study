import sys
#sys.stdin = open("input.txt","r")
n, c = map(int, input().split())
Line =[]
def Count(len):
    cnt=1         #말 개수
    ep = Line[0]  #맨 끝지점. ep =1
    for i in range(1,n):
         if Line[i] - ep >= len:
             cnt+=1
             ep=Line[i]
    return cnt
    
for _ in range(n):
    tmp = int(input())
    Line.append(tmp)
Line.sort()
lt=1
rt=Line[n-1]
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid) >=c:
        res = mid
        lt = mid+1
    else:
        rt = mid-1
print(res)
