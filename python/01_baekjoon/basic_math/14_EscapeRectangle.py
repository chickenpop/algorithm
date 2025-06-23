# 1085 직사각형에서 탈출

x, y, w, h = map(int, input().split())

lst = [0]*4

lst[0] = x
lst[1] = y
lst[2] = w-x
lst[3] = h-y

print(min(lst))
