#병합 정렬

def Dsort(lt, rt):
    if lt<rt:
        mid=(lt+rt)//2          #중간 값을 기준으로 나눔.
        Dsort(lt,mid)           
        Dsort(mid+1,rt)
        p1=lt
        p2=mid+1
        tmp=[]

        while p1<=mid and p2<=rt:   
            if arr[p1]<arr[p2]:   
                tmp.append(arr[p1])
                p1+=1
            else:
                tmp.append(arr[p2])
                p2+=1
        if p1<=mid: tmp = tmp+arr[p1:mid+1]    #왼쪽부분이 남아있을 때, 왼쪽 부분을 모조리 tmp에 추가
        if p2<=rt: tmp = tmp+arr[p2:rt+1]      #오른쪽 부분이 남아있을 때, 오른 쪽 부분을 모조리 tmp에 추가.
        for i in range(len(tmp)):
            arr[lt+i] = tmp[i]



if __name__ == "__main__":
    arr = [23,11,45,36,15,67,33,21]
    print("Before sort : ", end='')
    print(arr)
    Dsort(0,7)    #0번부터 7번까지 전체 정렬해라.
    print()
    print("After sort: ", end=' ')
    print(arr)


'''
Dsort(lt,rt) : lt는 정렬하고자하는 리스트의 맨 왼쪽 인덱스
               rt는 정렬하고자하는 리스트의 맨 오른쪽 인덱스
'''
