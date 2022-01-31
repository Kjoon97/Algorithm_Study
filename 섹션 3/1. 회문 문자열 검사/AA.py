import sys
#sys.stdin = open("input.txt","rt")

# --------------------모범 답안 1----------------
n = int(input())
    
for i in range(n):
    s= input()
    s=s.upper()
    size= len(s)
    for j in range(size//2):
        if s[j]!=s[-1-j]:    #첫 문자와 마지막 문자가 다르면 회문이 아님.
            print(f"#{i+1} NO")
            break
    else:
        print(f"#{i+1} YES")   #for else문.


# 문자열[-1] -> 제일 마지막 문자
#for else문 -> 중간에 break 안당하고 다 돌고 끝났다면
#면접시에는 모범답안 1로 풀어보라고 할 수 있음.

# --------------------모범 답안 2 (파이썬스러운 방법)----------------

n = int(input())
    
for i in range(n):
    s= input()
    s=s.upper()
    if s==s[::-1]:
        print(f"#{i+1} YES")
    else:
        print(f"#{i+1} NO")

#s[::-1] -> 문자열 s가 거꾸로 뒤집힘.









'''내가쓴 답 (100점) 
n = int(input())
    
def func(word, i):
    if len(word)%2==0:
        slice1 = word[0:int(len(word)/2)]
        slice2 = word[int(len(word)/2):int(len(word))]
        slice2.reverse()
        if slice1 == slice2:
            print(f"#{i} YES")
        elif slice1 != slice2:
            print(f"#{i} NO")
    else:
        slice1 = word[0:int(len(word)/2)]
        slice2 = word[int(len(word)/2+1):int(len(word))]
        slice2.reverse()
        if slice1 == slice2:
            print(f"#{i} YES")
        elif slice1 != slice2:
            print(f"#{i} NO")

        
for i in range(n):
    word = input()
    word = word.upper()
    word =list(word)
    func(word,i+1)
'''
