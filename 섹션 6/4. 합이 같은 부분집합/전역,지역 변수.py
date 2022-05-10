import sys
#sys.stdin = open("input.txt",'r')
'''전역 변수와 지역 변수'''

def DFS1():
    cnt=3                          #지역 변수
    print(cnt)

def DFS2():
    global cnt                   # global로 전역 변수됨.              
    if cnt==5:
        cnt=cnt+1
        print(cnt)


if __name__=="__main__":
    cnt=5                           #전역 변수 생성, 5로 할당. cnt
    DFS1()
    DFS2()
    print(cnt) 
