import sys
sys.stdin = open("input.txt","rt")

n = int(input())
a = list(map(int, input().split()))
avg = round(sum(a)/n)
min = 2147000000

for idx, x in enumerate(a):
    tmp = abs(x-avg)
    if tmp<min:
        min = tmp
        score = x
        res = idx+1         #0번 인덱스부터 시작이라 1을 더해줌.
    elif tmp == min:
        if x >score:
            score =x
            res = idx+1
print(avg,res)




## round()소숫점 반올림, sum(리스트) : 리스트 합, abs(): 절댓값
# enumerate(리스트) -> 인텍스, 값 추출.

