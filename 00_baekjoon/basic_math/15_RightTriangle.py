# 4153 직각삼각형
# 정답 코드
tri = list(map(int, input().split()))

while sum(tri) != 0:
    if tri[0]*tri[0] + tri[1]*tri[1] == tri[2]*tri[2]:
        print("right")
    elif tri[1]*tri[1] + tri[2]*tri[2] == tri[0]*tri[0]:
        print("right")
    elif tri[0]*tri[0] + tri[2]*tri[2] == tri[1]*tri[1]:
        print("right")
    else:
        print("wrong")
    tri = list(map(int, input().split()))

# 변형 코드
tri = list(map(int, input().split()))

while sum(tri) != 0:
    tri_max = max(tri)
    tri.remove(max(tri))
    if tri[0]**2+tri[1]**2 == tri_max**2:
        print("right")
    else:
        print("wrong")
    tri = list(map(int, input().split()))
