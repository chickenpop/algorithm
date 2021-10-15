# ~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor), <<(bitwise left shift), >>(bitwise right shift)
# 6059 2 > -3 | 0010 > 1101 | ~n = -n-1, -n = ~n+1
num = int(input())
print(~(num))

# 6060 &
num1, num2 = map(int, input().split())
print(num1&num2)

# 6061 |
num1, num2 = map(int, input().split())
print(num1|num2)

# 6062 xor(^)
num1, num2 = map(int, input().split())
print(num1^num2)