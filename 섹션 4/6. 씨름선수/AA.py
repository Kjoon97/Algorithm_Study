import sys
#sys.stdin = open("input.txt","r")
n = int(input())
body=[]
for _ in range(n):
    h, w = map(int, input().split())
    body.append((h,w))
body.sort(reverse=True)
largest=0
cnt=0
for x, y in body:
    if largest < y:
        largest=y
        cnt+=1
print(cnt)

#내림차순 정렬: 리스트.sort(reverse=True)
#키순으로 먼저 정렬, 내려가면서 무게로 비교, 무게가 큰 선수 카운트
