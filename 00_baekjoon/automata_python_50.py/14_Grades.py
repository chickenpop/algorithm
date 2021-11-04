#2754 학점 계산
#직접한것
def grades(a):
    if a == 'A+':
        return 4.3
    elif a == 'A0':
        return 4.0
    elif a == 'A-':
        return 3.7
    elif a == 'B+':
        return 3.3
    elif a == 'B0':
        return 3.0
    elif a == 'B-':
        return 2.7
    elif a == 'C+':
        return 2.3
    elif a == 'C0':
        return 2.0
    elif a == 'C-':
        return 1.7
    elif a == 'D+':
        return 1.3
    elif a == 'D0':
        return 1.0
    elif a == 'D-':
        return 0.7
    else:
        return 0.0

score = str(input())
print(grades(score))
# or 딕셔너리(Dictionary)를 이용하는 다른 방법
grades = { 
     'A+': 4.3, 'A0': 4.0, 'A-': 3.7, 'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
     'C+': 2.3, 'C0': 2.0, 'C-': 1.7, 'D+': 1.3, 'D0': 1.0, 'D-': 0.7, 
     'F':0.0}

print(grades[str(input())])
