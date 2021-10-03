# 6052 num == 0 False, != True, Use bool 
num = int(input())
print(bool(num))

# 6053 bool = True > False, bool = False > True
num = bool(int(input()))
print(not num)

# 6054 and
num1, num2 = map(int, input().split())
print(bool(num1&num2))
#or
num1, num2 = map(int, input().split())
print(bool(num1 and num2))

# 6055 or
num1, num2 = map(int, input().split())
print(bool(num1 | num2))
#or
num1, num2 = map(int, input().split())
print(bool(num1 or num2))

# 6056 num1 xor num2
num1, num2 = map(int, input().split())
print(bool(not(num1) and num2)or bool(num1 and not(num2)))

# 6057 num1 = 0, num2 = 0 True / num1 = 1, num2 = 1 True
num1, num2 = map(int, input().split())
print(bool(not(num1) and not(num2)) or bool(num1 and num2))

# 6058 num1 = 0, num2 = 0 True
num1, num2 = map(int, input().split())
print(bool(not(num1) and not(num2)))
#or
num1, num2 = map(int, input().split())
print(bool(num1 == False and num2 == False))