# 6017
a = input()
print(a, a, a)

# 6018
hour, min = input().split(":")
print(hour, min, sep=":")

# 6019
year, month, days = input().split(".")
print(days, month, year, sep="-")

# 6020
human_num1, human_num2 = input().split("-")
print(human_num1, human_num2, sep="")

# 6021
str = input()

for i in range(5):
    print('{}'.format(str[i]))

# 6022
yymmdd = input()

for i in range(0, 6, 2):
    print(yymmdd[i]+yymmdd[i+1], end=" ")

# 6023
hour, min, sec = input().split(":")
print(min)

# 6024
str1, str2 = input().split()
print(str1+str2)