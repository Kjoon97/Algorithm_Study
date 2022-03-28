import sys
#sys.stdin = open("input.txt",'r')

n = int(input())
p = dict()
for _ in range(n):
    word = input()
    p[word] =1
for _ in range(n-1):
    word = input()
    p[word] =0 
for key, val in p.items():
    if val == 1:
        print(key)
        break
    


#딕셔너리는 리스트와 다르게 키 값을 정수뿐만 아니라 단어도 할 수 있다. 
