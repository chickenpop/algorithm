#10988 팰린드롬인지 확인하기
lst = []
lst = list((input()))
palindrome = list(reversed(lst))

if lst == palindrome:
    print(1)
else:
    print(0)