import sys
sys.stdin = open("input.txt","r")

#가지고 있는 4개의 랜선을 각각 지정한 길이만큼 나눠서 개수 구하는 함수
def Count(mid):
    cnt=0
    for x in line:
        cnt+=(x//mid)
    return cnt

k, n = map(int,input().split())
line = []
res=0
largest=0
for i in range(k):
    tmp = int(input())
    line.append(tmp)
    largest= max(largest,tmp)
lt=1
rt=largest

#이분 탐색
while lt<=rt:
    mid = (lt+rt)//2
    if Count(mid)>=n:
        res = mid
        lt = mid+1
    else:
        rt = mid-1

print(res)

# max(a,b) -> a와b를 비교해서 큰 값을 리턴.
