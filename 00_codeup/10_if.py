# 6065
num1, num2, num3 = map(int, input().split())

if num1 % 2 == 0:
    print(num1)

if num2 % 2 == 0:
    print(num2)

if num3 % 2 == 0:
    print(num3)

# 6066
num1, num2, num3 = map(int, input().split())

if num1 % 2 == 0:
    print("even")
else: print("odd")

if num2 % 2 == 0:
    print("even")
else: print("odd")

if num3 % 2 == 0:
    print("even")
else: print("odd")

# 6067
num = int(input())

if num % 2 == 0 and num > 0:
    print("C")
elif num % 2 == 0 and num < 0:
    print("A")
elif num > 0:
    print("D")
else:
    print("B")

# 6068
num = int(input())

if 90 <= num:
    print("A")
elif 70 <= num:
    print("B")
elif 40 <= num:
    print("C")
else : print("D")

# 6069
score = input()
 
if score == "A":
    print("best!!!")
elif score == "B":
    print("good!!")
elif score == "C":
    print("run!")
elif score == "D":
    print("slowly~")
else : print("what?")

# 6070
num = int(input())

if 3 <= num <= 5:
    print("spring")
elif 6 <= num <= 8:
    print("summer")
elif 9 <= num <= 11:
    print("fall")
else : print("winter")