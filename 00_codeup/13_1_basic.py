# 6077
num = int(input())
sum = 0

for i in range(num+1):
    if i % 2 == 0:
        sum += i
        
print(sum)

# 6078
while True:
    a = input()
    if a == "q":
        print(a)
        break
    print(a)

# 6079
a = int(input())
sum = 0

for i in range(a):
    sum += i
    if a <= sum:
        print(i)
        break

# 6080
dice1, dice2 = map(int, input().split())

for i in range(dice1):
    for j in range(dice2):
        print(i+1, j+1)

# 6081
n = ord(input()) - 55

for i in range(1, 16):
  print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')
#or
n = int(input(), 16)

for i in range(1, 16):
  print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

# 6082
num = int(input())

for i in range(1, num+1):
    if (i%10) == 3 or (i%10) == 6 or (i%10)==  9:
        print("X", end=" ")
    else : print(i, end=" ")

# 6083
red, green, blue = map(int, input().split())
count = 0

for i in range(red):
    for j in range(green):
        for k in range(blue):
            print(i, j, k)
            count+=1
print(count)