import sys
#sys.stdin = open("input.txt", "r")
n = int(input())
a = list(map(int, input().split()))
lt=0
rt=n-1
last=0
res=""
tmp=[]
while lt<=rt:
    if a[lt]>last:
        tmp.append((a[lt],'L'))
    if a[rt]>last:
        tmp.append((a[rt],'R'))
    tmp.sort()
    if len(tmp)==0:
        break
    else:
        res=res+tmp[0][1]
        last=tmp[0][0]
        if tmp[0][1]=='L':
            lt+=1
        else:
            rt-=1
    tmp.clear()
print(len(res))
print(res)


'''
리스트 비우기: 리스트.clear()
리스트에 튜플 넣기: 리스트.append((a,b))
리스트 속 튜플 : 리스트[][]로 조회 가능.
'''
