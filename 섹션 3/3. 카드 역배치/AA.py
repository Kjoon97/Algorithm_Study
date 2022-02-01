import sys
#sys.stdin = open("input.txt","rt")

#-----------------모범 답안----------------------------
a = list(range(21))   # 0~20까지 리스트
for _ in range(10):   # i가 있으면 변수에 대입하는 것도 시간이 들어가므로 변수가 필요 없으면 _로 하는게 좋다
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]

a.pop(0)             #0번 인덱스의 것을 제거. a.pop()은 마지막 것을 제거.
for x in a:
    print(x, end=' ')
    




#----------------나의 답 (100)--------------------------
a= list(range(1,21))

for _ in range(10):
    n1, n2 = map(int, input().split())
    temp = a[n1-1:n2]
    temp.reverse()

    for i in range(n1-1, n2):  #i 4~7
        a[i]= temp[i-(n1-1)]

        
for i in a:
    print(i, end=" ")


'''
   a = list(range(21))   # 0~20까지 리스트
   a.pop(0)             #0번 인덱스의 것을 제거. a.pop()은 마지막 것을 제거.
   변수 필요 없을 때 반복 할 때는 _로 하는 것이 더 빠르다.
   
'''
