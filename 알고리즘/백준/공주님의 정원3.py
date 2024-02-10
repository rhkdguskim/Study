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

flower.sort(key=lambda x:(-x[0], -x[1]))
end_date = START_CONDITION
count = 0

while flower:
    if flower[-1][0] > end_date or end_date >= END_CONDITION:
        break
    
    max_end_date = -1
    while flower and flower[-1][0] <= end_date:
        max_end_date = max(flower[-1][1], max_end_date)
        flower.pop()
    
    count += 1
    end_date = max_end_date

if end_date < END_CONDITION:
    print(0)
else:
    print(count)