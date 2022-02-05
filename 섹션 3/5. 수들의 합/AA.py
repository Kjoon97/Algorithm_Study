import sys
#sys.stdin = open("input.txt","rt")
n , m = map(int, input().split())
a = list(map(int, input().split()))
lt =0
rt =1
tot = a[0]   # 연속 부분의 합(lt부터 rt-1까지의 합)
cnt=0

while True:
    if tot<m:          #합이 3보다 작을 경우. 
        if rt<n:       #rt가 8보다 작은 경우 (rt가 8이면 순환 종료.)
            tot+=a[rt]  #tot는 a[0] + a[1] +.. 더해감.
            rt+=1
        else:
            break       #rt가 8인경우 반복문 종료
    elif tot ==m:
        cnt+=1
        tot-= a[lt]
        lt+=1
    else:
        tot-=a[lt]
        lt+=1


print(cnt)

#1. tot<m 이면 rt를 1올리고 tot+=a[rt](rt-1까지 더하는 것)를 함. 
#2. tot == m이면 cnt에 1올림.  tot에서 a[lt]를 빼고, lt를 1올림.
#3. tot>m이면 tot에서 a[lt]를 빼고, lt를 1올림.
#1번~3번까지 반복.
# tot<m이어서 rt를 1올려야되는데 rt가 (자료를 다 처리해서)n이어서 더 이상 못 올리면 반복 종료.(break)
