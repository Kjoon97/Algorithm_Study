#import sys
#sys.stdin = open("input.txt","rt")
n = int(input())   #개수
a=list(map(int, input().split()))

def digit_sum(x):
    sum=0
    while x>0:
        sum+=x%10   #125를 10으로 나눈 나머지 5를 sum에 더하고
        x=x//10     #125를 10으로 나눈 몫 12를 저장하는식으로 반복
    return sum                # x가 0이되면 반복 중단.


max =-2147000000
for x in a:
    tot = digit_sum(x)
    if tot > max:
        max =tot
        res = x

print(res)




'''맞음 (내가 푼 답)
n = int(input())   #개수
a=list(map(int, input().split()))
max = -2147000000

def digit_sum(x):
    sum_ =0 
    for i in str(x):
        sum_ = sum_ + int(i)
    return sum_

for k, v in enumerate(a):
    if max < digit_sum(v):
        max= digit_sum(v)
        key = k
    

print(int(a[key]))
'''
