import sys
#sys.stdin = open("input.txt",'r')

firstw = input()
secondw = input()
sH = dict()

for x in firstw:
    sH[x] = sH.get(x,0)+1
    
for x in secondw:
    sH[x] = sH.get(x,0)-1
    
for x in firstw:
    if sH.get(x)>0:
        print("NO")
        break
else:
    print("YES")

#딕셔너리 내장 함수 - 딕셔너리.get('A',0) + 1 => 딕셔너리에 키 'A'의 value값을 가져와라, value가 없으면 0을 리턴해라. 
