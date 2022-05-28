import sys
import itertools as it
sys.stdin = open("input.txt", "rt")
n,f = map(int, input().split())
b=[1]*n

for i in range(1,n):
    b[i]=b[i-1]*(n-i)/i
    
a=list(range(1,n+1))
for tmp in it.permutations(a):   #tmp - 순열.
    sum=0
    for L, x in enumerate(tmp):
        sum+= x*b[L]
    if sum==f:
        for x in tmp:
            print(x, end=' ')
        break                  # for tmp in it.permutations(a):를 break하는 것.
        
#itertools - 순열이나 조합을 자동으로 구해주는 라이브러리,
#라이브러리 없이 하는 연습해야함.

