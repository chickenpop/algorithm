# 1151 10보다 작은수
n = int(input())

if n < 10 : print("small")

# 1152 10보다 작은수(else)
n = int(input())

if n < 10 : print("small")
else : print("big")

# 1153 두 수의 대소 비교
a, b = map(int, input().split())

if a > b : print(">")
elif a == b : print("=")
else : print("<")

# 1154 큰수 - 작은수
a, b = map(int, input().split())

if a > b : print(a-b)
else : print(b-a)

# 1155 7의 배수
num = int(input())

if num % 7 == 0: print("multiple")
else : print("not multiple")

# 1156 홀수 짝수 구별
num = int(input())

if num % 2 == 0: print("even")
else : print("odd")

# 1157 특별한 공 던지기 1
num = float(input())

if num >= 50 and num <= 60: print("win")
else : print("lose")

# 1158 특별한 공 던지기 2
num = float(input())

if (num >= 30 and num <= 40) or (num >= 60 and num <= 70): print("win")
else : print("lose")

# 1158 특별한 공 던지기 3
num = float(input())

if (num >= 50 and num <= 70) or (num % 6 == 0): print("win")
else : print("lose")

# 1160 아르바이트 가는 날
num = int(input())

if (num % 2 == 1): print("oh my god")
else : print("enjoy")

#1161 홀수와 짝수 그리고 더하기
num1, num2 = map(int, input().split())

if num1