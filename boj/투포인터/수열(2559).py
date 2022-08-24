"""
1. 아이디어
- 투포인터를 활용
- for문으로 처음에 k 개 값을 저장
- 다음 인덱스 더해주고, 이전 인덱스 빼줌
- 이 때마다 최댓값 갱신

2. 시간 복잡도
- O(N) = 1e5 > 가능
"""

import sys
sys.stdin = open("input.txt",'r')
input = sys.stdin.readline

n , k = map(int,input().split())
nums= list(map(int,input().split()))
each=0
for i in range(k):
    each+=nums[i]
maxv=each

for i in range(k,n):
    each+=nums[i]
    each-=nums[i-k]
    maxv=max(each,maxv)
print(maxv)
