import sys
#sys.stdin = open("input.txt","r")

n=int(input())          #벽돌 수 
bricks=[]               #벽돌 정보 리스트

for i in range(n):
    s, h, w = map(int, input().split())
    bricks.append((s,h,w))

bricks.sort(reverse=True)    #튜플을 정렬할 때는 첫번째 자료를 우선으로 한다.(첫번째 자료가 같으면 그 다음 자료로 정렬,,)
dy=[0]*n

dy[0] = bricks[0][1]      #0번 벽돌의 높이 저장. (bricks[벽돌 번호][0] -넓이,bricks[벽돌 번호][1]- 높이, bricks[벽돌 번호][2] - 넓이)
res = bricks[0][1]

for i in range(1,n):     #i번째 벽돌: 내가 만들고자하는 탑의 가장 상단 벽돌.
    max_h=0
    for j in range(i-1, -1, -1):                #j번째 벽돌: i번째 벽돌의 아래 벽돌.
        if bricks[j][2] > bricks[i][2] and dy[j]>max_h:       #j번째 벽돌의 무게가 i번째 벽돌의 무게보다 커야하고 dy[]에서 제일 높은 벽돌이어야함.
            max_h=dy[j]
    dy[i] = max_h+bricks[i][1]
    res=max(res, dy[i])


print(res)
    
