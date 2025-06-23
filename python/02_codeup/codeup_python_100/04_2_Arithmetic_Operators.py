# 6039
float1, float2 = map(float, input().split())
print(float1**float2)

# 6040
num1, num2 = map(int, input().split())
print(num1//num2)

# 6041
num1, num2 = map(int, input().split())
print(num1%num2)

# 6042
float1 = float(input())
print("%.2f" % float1)

# 6043
float1, float2 = map(float, input().split())
print("%.3f" % (float1/float2))

# 6044
num1, num2 = map(int, input().split())
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1//num2)
print(num1%num2)
print("{0:.2f}".format(num1/num2)) #print(round(a/b,2))

# 6045
num1, num2, num3 = map(int, input().split())
print(num1+num2+num3, end=" ")
print("{:.2f}".format(round((num1+num2+num3)/3, 2)))