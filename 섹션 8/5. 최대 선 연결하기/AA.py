import sys
#sys.stdin = open("input.txt","r")

n=int(input())
arr= list(map(int,input().split()))

arr.insert(0,0)   #arr리스트를 0번이 아닌 1번 인덱스부터 시작하게하려고 0번 인덱스에 0을 넣어 뒤로 한칸 씩 미룸.
dy=[0]*(n+1)       #인덱스 1번부터하려고 길이 n+1만큼 생성.
dy[1]=1
res=0

for i in range(2, n+1):
    max=0
    for j in range(i-1, 0, -1):
        if arr[j]<arr[i] and dy[j]>max:               #arr[i]는 내가 만들고자하는 증가 수열의 마지막 항. arr[j]는 그 앞에 있는 숫자.
            max=dy[j]
    dy[i]=max+1
    if dy[i]>res:
        res=dy[i]
print(res)
