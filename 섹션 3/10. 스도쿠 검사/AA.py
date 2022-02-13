import sys
#sys.stdin = open("input.txt","r")

a= [list(map(int, input().split())) for _ in range(9)]

def check(a):
    for i in range(9):
        ch1=ch2=[0]*10
        for j in range(9):
            ch1[a[i][j]]=1
            ch2[a[j][i]]=1
        if sum(ch1)!=9 or sum(ch2)!=9:
            return False
    for i in range(3):
        for j in range(3):   #그룹 1개 지정 됨.
            ch3 =[0]*10
            for k in range(3):      #그룹 1개안에서 9개 숫자 살펴봄.
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]]=1
            if sum(ch3) != 9:
                return False
    return True

                

if check(a):
    print("YES")
else:
    print("NO")
