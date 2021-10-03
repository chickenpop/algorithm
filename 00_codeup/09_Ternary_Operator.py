# 6063 x if C else y
num1, num2 = map(int, input().split())
print(num1 if num1>=num2 else num2)

# 6064 연산자 우선순위, 가장 작은 값 출력
num1, num2, num3 = map(int, input().split())
print(num3 if(num1 if(num1<=num2) else num2)>=num3 else num1 if(num1<=num2) else num2)
#or
num1, num2, num3 = map(int, input().split())
num4 = num1 if(num1<=num2) else num2
num5 = num3 if(num3<=num4) else num4
print(num5)