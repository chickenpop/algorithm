#2884 알람시계
hour, min = map(int, input().split())

bef_hour = (hour*60 + min) // 60
bef_min = min - 45

if bef_min < 0:
    bef_min += 60
    bef_hour -= 1
if bef_hour < 0:
    bef_hour += 24

print(bef_hour, bef_min)