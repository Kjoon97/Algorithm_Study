import sys
#sys.stdin = open("input.txt","rt")

#----모범답안
n1 = int(input())
a = list(map(int,input().split()))
n2 = int(input())
b = list(map(int,input().split()))

p1=p2=0   #포인터
c=[]      
while p1<n1 and p2<n2:    #a,b리스트 중 하나가 조회가 다 끝나면 반복 끝
    if a[p1] <= b[p2]:    # a,b리스트 각 원소 비교해서 작은 것을 c리스트에 추가. 작은 원소가 있던 리스트의 포인터 +1
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1

if p1<n1:    #a리스트가 다 안끝나고 남은경우
    c = c+a[p1:]
if p2<n2:    #b리스트가 다 안끝나고 남은경우
    c = c+b[p2:]

for x in c:
    print(x, end=' ')
    




'''
n1 = int(input())
a = list(map(int,input().split()))
n2 = int(input())
b = list(map(int,input().split()))
c = a+b
c.sort()
for i in c:
    print(i, end=" ")

'''
'''
  1. sort()라는 함수를 사용하면 n개를 정렬할 때, nlogn번 시간이 걸린다.
     문제처럼 2리스트가 이미 정렬이 되어있는 경우에서는 n번만에 문제를 풀 수 있다.
     데이터가 많을 경우, nlogn과 n의 차이는 크다.
  2. list에 항목을 하나만 추가할 때는 +=보다는 append를 사용하고
     list들을 이을(concatenation) 때만 +=나 extend를 사용하자(list들을 이을 때는 +=가 extend보다 더 빠르다)
'''
