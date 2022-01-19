import sys
#sys.stdin = open("input.txt","rt")   #파일 이름, 모드는 rt(readtext)
n,k = map(int, input().split())
a = list(map(int,input().split()))
res = set()
for i in range(n):
    for j in range(i+1,n):
        for m in range(j+1,n):
            res.add(a[i]+a[j]+a[m])
res = list(res)
res.sort(reverse=True)
print(res[k-1])



#중복을 없애기 위해 set자료구조 이용
#3개를 뽑아야되기때문에 3번 for문 
#set 자료구조는 append로 추가하는게 아니라 add로 추가.(리스트는 append)
#set 자료구조는 sort기능이 없기때문에 정렬하려면 리스트화시켜야함.
