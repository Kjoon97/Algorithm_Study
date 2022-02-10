import sys
#sys.stdin = open("input.txt","rt")
n = int(input())
a= [list(map(int,input().split())) for _ in range(n)]

#문자열 회전하기.
m = int(input())
for i in range(m):
    h, t, k = map(int, input().split())
    if t==0:                               #왼쪽 회전
        for _ in range(k):
             a[h-1].append(a[h-1].pop(0))
    else:                                  #오른쪽 회전
        for _ in range(k):
             a[h-1].insert(0, a[h-1].pop())


#a[h-1].pop(0) : 앞에 원소는 빠지고 나머지 원소들이 앞으로 한칸씩 이동
#a[h-1].insert(0, a[h-1].pop()) : 마지막 원소를 빼서 0번째 자리에 삽입.

#정리: pop(), insert(), append() 활용하기

#모래시계모양만 더하기
s=0
e=n-1
res=0
for i in range(n):
    for j in range(s,e):
        res+=a[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1

print(res)
