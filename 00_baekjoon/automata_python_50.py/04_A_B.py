# #11021 A+B-7
# def case_x(number, num1, num2):
#     print("Case #{}: {}".format(number, num1+num2))

# n = int(input())
# for i in range(n):
#     num1, num2 = map(int, input().split())
#     case_x(i+1, num1, num2)

#11022 A+B-8
def case_x(number, num1, num2):
    print("Case #{}: {} + {} = {}".format(number, num1, num2, num1+num2))

n = int(input())
for i in range(n):
    num1, num2 = map(int, input().split())
    case_x(i+1, num1, num2)