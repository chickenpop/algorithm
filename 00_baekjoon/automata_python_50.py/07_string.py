#2675
n = int(input())

for i in range(n):
    num, s = list(map(str, input().split()))
    for j in range(len(s)):
        print(s[j]*int(num), end="")
    print()
