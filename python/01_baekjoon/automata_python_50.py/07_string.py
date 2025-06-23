#2675
n = int(input())

for i in range(n):
    num, s = list(map(str, input().split()))
    for j in range(len(s)):
        print(s[j]*int(num), end="")
    print()

#2935
a = int(input())
operator = str(input())
b = int(input())

if operator == '*':
    print(a*b)
elif operator == '+':
    print(a+b)
else:
    print("error")