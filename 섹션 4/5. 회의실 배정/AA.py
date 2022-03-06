import sys
#sys.stdin = open("input.txt","r")
n = int(input())
meeting=[]
for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s,e))
meeting.sort(key=lambda x : (x[1],x[0]))   #튜플 중 x[1]로 정렬, x[1]이 같으면 x[0]으로 정렬
et=0
cnt=0
for s, e in meeting:
    if s>=et:
        et=e
        cnt+=1
print(cnt)



#meeting.sort() 하면 튜플 중 앞 자료를 보고 정렬한다.
