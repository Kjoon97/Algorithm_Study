import sys
#sys.stdin = open("in1.txt",'r')
#==================================c++처럼 풀어보기 리스트 해시 방법 =============
a= input()
b= input()
str1= [0]*52   #알파벳이 소문자, 대문자 합해서 총 52개
str2= [0]*52

for x in a:
    if x.isupper():
        str1[ord(x)-65]+=1
    else:
        str1[ord(x)-71]+=1
        
for x in b:
    if x.isupper():
        str2[ord(x)-65]+=1
    else:
        str2[ord(x)-71]+=1

for i in range(52):             #파이썬은 if str1==str2 이렇게 직접 비교해도됨.
    if str1[i]!=str2[i]:
        print("NO")
        break
else:
    print("YES")


#문자를 아스키 넘버로 변환해주는 함수 ord(x)
#대문자 아스키 번호 : 65~90 (A~Z)-> str1,str2에 넣게 되면 -65해서 인덱스0~25에 넣기.
#소문자 아스키 번호 : 97~122 (a~z)-> str1,str2에 넣게 되면 -71해서 인덱스26~51에 넣기. 
        




'''
===========================딕셔너리 해시 방법=================================
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
'''
