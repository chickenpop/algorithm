# 2447 별 찍기 - 10

n = int(input())  # 3 <= n은 3의 제곱근


def Star(num):
    if num == 1:
        return ["*"]

    rec = Star(num//3)
    star = []

    for i in rec:
        star.append(i*3)
    for i in rec:
        star.append(i+" "*(num//3)+i)
    for i in rec:
        star.append(i*3)

    return star


print("\n".join(Star(n)))
