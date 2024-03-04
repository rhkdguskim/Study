# https://www.acmicpc.net/problem/12851
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque()
queue.append((N, 0))
INF = 100001
ans = 0

max_cost = sys.maxsize
while queue:
    cur, cost = queue.popleft()
    #print(cur, cost, max_cost)
    if cost > max_cost:
        continue
    
    if cur == K:
        max_cost = cost
        ans += 1
    
    queue.append((cur * 2, cost + 1))
    queue.append((cur + 1, cost + 1))
    
    if cur - 1 > 0:
        queue.append((cur - 1, cost + 1))    
    
    
    
print(max_cost)
print(ans)
        