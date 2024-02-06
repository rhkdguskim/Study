# https://www.acmicpc.net/problem/2457
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
flower = []
queue = deque()
visited = [False for _ in range(N)]
month_in_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
acc = [0 for _ in range(13)]
for i in range(1, 13):
    acc[i] += acc[i-1] + month_in_day[i]

def day_month_to_num(month, day):
    return acc[month-1] + day

flower = []
end = []
visited = [False for _ in range(N)]

start_condition = day_month_to_num(3, 1)
end_condition = day_month_to_num(11, 30)
queue = deque()
for i in range(N):
    s_month, s_day, e_month, e_day = map(int, input().split())
    flower.append((s_month, s_day, e_month, e_day, i))
    cost = day_month_to_num(s_month, s_day)
    if start_condition >= cost:
        queue.append((s_month, s_day, e_month, e_day, 1))
        visited[i] = True

flower.sort(key=lambda x:(x[0], x[1], -x[2], -x[3]))
ans = N+1

def find_longest_end(cost):
    global flower
    s = 0
    e = N-1
    idx = -1
    new_end_month, new_end_day = -1, -1
    max_value = -1
    while e >= s:
        mid = (s + e) // 2
        comp = day_month_to_num(flower[mid][0], flower[mid][1])
        if comp > cost:
            e = mid - 1
        else:
            longest_day = day_month_to_num(flower[mid][2], flower[mid][3])
            if longest_day > max_value and not visited[flower[mid][4]]:
                max_value = longest_day
                new_end_month = flower[mid][2]
                new_end_day = flower[mid][3]
                idx = flower[mid][4]
            s = mid + 1
            
    return new_end_month, new_end_day, idx
            
        

while queue:
    s_m, s_d, e_m, e_d, cost = queue.popleft()
    
    day_cost = day_month_to_num(e_m, e_d)
    
    if day_cost >= end_condition:
        ans = min(ans, cost)
    
    new_end_month, new_end_day, idx = find_longest_end(day_cost)
    
    if idx == -1:
        continue
    
    #print(e_m, e_d, '->', new_end_month, new_end_day)
    if not visited[idx]:
        visited[idx] = True
        queue.append((new_end_month, new_end_day, cost + 1))

if ans == N+1:
    print(0)
else:
    print(ans)