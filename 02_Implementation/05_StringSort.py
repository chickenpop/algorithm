# 문자열 재정렬

lst = list(map(str, input()))
ord_lst = []
sum = 0
for i in lst:
    if i.isdigit() == False:  # isdigit 문자열 False 숫자 True
        ord_lst.append(ord(i))
    else:
        sum += int(i)

ord_lst.sort()

for i in ord_lst:
    print(chr(i), end="")
print(sum)

# 다른 방법 비슷하지만 마지막 추가하는 방식과 문자열 판단 방법이 다름
data = input()
result = []
value = 0

for x in data:
    if x.isalpha():  # isdigit 문자열 True 숫자 False
        result.append(x)
    else:
        value += int(x)

result.sort()
# 숫자가 존재하는 경우 가장뒤에 삽입
if value != 0:
    result.append(str(value))

print(''.join(result))
