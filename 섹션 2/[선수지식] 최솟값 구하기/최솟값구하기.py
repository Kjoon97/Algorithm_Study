#최솟값 구하기

arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = float('inf')  #파이썬에서 가장 큰 값 float('inf')
for x in arr:
    if x < arrMin:
        arrMin = x
print(arrMin)
