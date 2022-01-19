'''내가쓴 답 결과 100점.
import sys
#sys.stdin= open("input.txt","rt")
a,b = map(int, input().split(' '))
nums =[]
count = 0
for i in range(a):
    if(a%(i+1)==0):
        nums.append(i+1)

if len(nums)<b:
    print(-1)
else:
    print(nums[b-1])

'''

'''
모범답안
'''
n, k = map(int, input().split())
cnt =0
for i in range(1,n+1):
    if n%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break
else:
    print(-1)


# 내가 쓴 답은 약수를 다 만들고 나서 그걸로 찾기 때문에 for문을 굳이 다 돈다.
# 모범답안은 for문을 다 돌지 않아 효율적이다. 
    
    
