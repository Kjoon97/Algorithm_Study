import sys
#sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
cnt=0
while a:                     #리스트가 빌 때까지 반복
    if len(a)==1:
        cnt+=1
        break
    if a[0]+a[-1] <= m:
        cnt+=1
        a.pop(0)
        a.pop()
    else:
        cnt+=1
        a.pop()
print(cnt)

'''
pop(0)을 하면 앞에 원소 제거되면서 뒤의 원소들이 한칸씩 앞으로 재정렬하는데
비효율적이다.
'''
