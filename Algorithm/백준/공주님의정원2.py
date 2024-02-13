# https://www.acmicpc.net/problem/2457
import sys
input = sys.stdin.readline
START_CONDITION = 301
END_CONDITION = 1201

N = int(input())
flower = []

for i in range(N):
    s_month, s_day, e_month, e_day = map(int, input().split())
    flower.append((s_month*100 + s_day, e_month*100 + e_day))

flower.sort()
end_date = START_CONDITION
count = 0

while flower:
    if flower[0][0] > end_date or end_date >= END_CONDITION:
        break
    
    max_end_date = -1
    
    for _ in range(len(flower)):
        if (flower[0][0] <= end_date):
            if (max_end_date <= flower[0][1]):
                max_end_date = flower[0][1]

            flower.remove(flower[0])
        else:
            break
        
    end_date = max_end_date
    count += 1
    
if end_date < END_CONDITION:
    print(0)
else:
    print(count)