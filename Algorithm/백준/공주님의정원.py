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

def month_day_to_num(month, day):
    return acc[month-1] + day

flower = []
end = []
visited = [False for _ in range(N)]

start_condition = month_day_to_num(3, 1)
end_condition = month_day_to_num(11, 30)
queue = deque()
for i in range(N):
    s_month, s_day, e_month, e_day = map(int, input().split())
    start_cost = month_day_to_num(s_month, s_day)
    end_cost = month_day_to_num(e_month, e_day)
    flower.append((start_cost, end_cost, i))
    if start_condition >= start_cost:
        queue.append((start_cost, end_cost, 1))
        visited[i] = True

flower.sort(key=lambda x:(x[0], x[1]))

def search(end_cost):
    start = 0
    end = N-1
    result = N 

    while start <= end:
        mid = (start + end) // 2
        
        if end_cost >= flower[mid][0]:
            result = min(result, mid)
            start = mid + 1
        else:
            end = mid - 1
    
    for i in range(result+1):
        if not visited[i]:
            return i
        
    return result

ans = N+1

while queue:
    start_cost, end_cost, cost = queue.popleft()
    
    if end_cost > end_condition:
        ans = min(ans, cost)
        
    idx = search(end_cost)
    
    if idx == N:
        continue
    
    if not visited[flower[idx][2]]:
        visited[flower[idx][2]] = True
        queue.append((flower[idx][0], flower[idx][1], cost + 1))

if ans == N+1:
    print(0)
else:
    print(ans)
    
