import sys
from collections import deque
#sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
deq = [(pos,val) for pos,val in enumerate(list(map(int, input().split())))]
deq = deque(deq)
cnt=0
while True:
    cur = deq.popleft()
    if any(cur[1]<x[1] for x in deq):
        deq.append(cur)
    else:
        cnt+=1
        if cur[0] == m :
            break
print(cnt)


# any() -> 하나라도 참이면 참 반환
# 리스트에서 enumerate를 감싸서 (인덱스, 값)인 튜플 리스트 만들기.
