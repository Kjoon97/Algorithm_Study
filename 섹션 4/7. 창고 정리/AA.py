import sys
#sys.stdin = open("input.txt", "r")
w = int(input())
a = list(map(int, input().split()))
n = int(input())
a.sort()
for _ in range(n):
    a[0] = a[0]+1
    a[-1] = a[-1]-1
    a.sort()
print(a[-1] - a[0])
    
