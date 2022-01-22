import sys
#sys.stdin = open("input.txt","rt")
n = int(input())
a = list(map(int, input().split()))

def reverse(x):   # 숫자 뒤집기 함수(맨앞의 0은 제거 됨)
    res =0
    while x>0:
        t=x%10
        res = res*10+t
        x=x//10
    return res


def isPrime(x):   #소수인지 확인하는 함수
    if x ==1:
        return False
    for i in range(2, x//2+1):  #절반 까지만 돌면 됨.예) 16의 약수는 자기자신 제외하고 젤 큰 수가 절반임.
        if x %i ==0:
            return False
    else:                     #for else
        return True

for x in a:
    tmp = reverse(x)
    if (isPrime(tmp)):
        print(tmp, end=" ")

    

# for else문 알기: return은 함수까지 종료시키는 것임. for문이 중간에 리턴을 안 당하고 정상적으로 다 돌고 끝났다면 else문을 실행 시킴.
