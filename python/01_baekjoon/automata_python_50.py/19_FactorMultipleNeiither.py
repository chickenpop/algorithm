#5086 배수와 약수
num1 = 1
num2 = 1

while True:
    num1, num2 = map(int, input().split())

    if num1 == 0 and num2 == 0:
        break

    if num1%num2 == 0 and num2//num1 == 0 :
        print("multiple")
    elif num2%num1 == 0 and num1//num2 == 0 :
        print("factor")
    else:
        print("neither")