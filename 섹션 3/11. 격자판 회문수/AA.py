import sys
#sys.stdin = open("input.txt","r")
#모범답안
board= [list(map(int, input().split())) for _ in range(7)]
cnt=0

for i in range(3):
    for j in range(7):
        tmp = board[j][i:i+5]
        if tmp==tmp[::-1]:
            cnt+=1
        for k in range(2):
            if board[i+k][j]!=board[i+5-k-1][j]:
                break
        else:
            cnt+=1

print(cnt)


'''
#내가쓴답(success100)
a= [list(map(int, input().split())) for _ in range(7)]

cnt=0

for x in a:
    for i in range(3):
        x2 = x[i:i+5]
        for j in range(len(x2)//2):
            if x2[j]!=x2[-1-j]:
                break
        else:
            cnt+=1

for i in range(7):
    c=[]
    for j in range(7):
        c.append(a[j][i])
    for z in range(3):
        c2 = c[z:z+5]
        for e in range(len(c2)//2):
            if c2[e]!=c2[-1-e]:
                break
        else:
            cnt+=1
print(cnt)
'''
