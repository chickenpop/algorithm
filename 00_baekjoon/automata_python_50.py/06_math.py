#2914
import math

song, song_avg = map(int, input().split())

melody = song*song_avg-song+1
print(melody)

5355
n = int(input())

for _ in range(n):
    mars = list(map(str, input().split()))
    result = float(mars[0])
    for i in range(1, len(mars)):
        if mars[i] == '@':
            result *= 3
        elif mars[i] == "%":
            result += 5
        elif mars[i] == '#':
            result -= 7    
        else:
            continue       
    
    print("%.2f"%result)