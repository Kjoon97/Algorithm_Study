#퀵 정렬 - 전위 순회 방식.
#1. pivot 설정한다.
#2. pivot 기준으로 분할 작업한다=> pivot을 기준으로 작은 값 - 전부 왼 쪽으로/ 큰 값 - 전부 오른 쪽으로 이동.
#2번까지 마친 후에 Qsort()호출 시작.

#3. pivot값과 arr[i]를 비교한다. arr[i]가 pivot보다 크면 i가 증가, 작으면 arr[pos]와 arr[i]를 교환 & 교환 후 pos, i 증가. 
#3번 과정을 반복->반복이 끝나면 arr[pos]과 pivot 값을 교환.
# 결국 pivot 값을 중심으로 왼쪽은 pivot보다 작은 값, 오른쪽은 pivot보다 큰 값들이 있다.
# pos를 중심으로 분할하면 된다. Q(lt, pos-1), Q(pos+1, rt)

def Qsort(lt, rt):
    if lt<rt:
        pos=lt    #정렬하고자하는 분할 된 영역의 첫 지점.
        pivot= arr[rt]   #정렬하고자하는 분할 된 영역의 마지막 지점.
        for i in range(lt, rt):
            if arr[i]<=pivot:
                arr[i], arr[pos] = arr[pos], arr[i]
                pos+=1
        arr[rt], arr[pos] = arr[pos], arr[rt]            #반복이 끝나면 arr[pos]과 pivot 값을 교환.
        Qsort(lt,pos-1)
        Qsort(pos+1,rt)

if __name__ == "__main__":
    arr = [45, 21, 23, 36, 15, 67, 11, 60, 20, 33]
    print("Before sort : ", end='')
    print(arr)
    Qsort(0,9)    #0번부터 9번까지 전체 정렬해라.
    print()
    print("After sort: ", end=' ')
    print(arr)
