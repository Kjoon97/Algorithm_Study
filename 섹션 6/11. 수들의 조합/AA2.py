import sys
import itertools as it
sys.stdin = open("input.txt", "rt")
#5(n)개의 정수에서 3(k)개를 뽑아서 6(m)의 배수가 되는 프로그램
n, k = map(int, input().split())
a= list(map(int, input().split()))
m=int(input())
cnt=0

for x in it.combinations(a,k):  # a리스트에서 k개를 뽑는 조합. - 각각의 경우가 x
    if sum(x)%m==0:
        cnt+=1
print(cnt)

        
#itertools - 순열이나 조합을 자동으로 구해주는 라이브러리,
#라이브러리 없이 하는 연습해야함.

