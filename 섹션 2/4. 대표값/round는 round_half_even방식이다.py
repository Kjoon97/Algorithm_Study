'''
대표값 문제 오류
round는 round_half_even방식을 택한다. - 딱 중간 x.5000일 경우 짝수로 근사한다.
a가 6.5일경우 7이어야하는데 round(a)는 6이된다.
'''
a = 66.5
print(round(a))
#0.5를 더하고 정수형으로 바꾸는 식으로 반올림하자.
a = a+0.5  
a = int(a)  
print(a)
