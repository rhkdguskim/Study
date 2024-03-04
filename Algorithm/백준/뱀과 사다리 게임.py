# https://www.acmicpc.net/problem/16928
import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N, M = map(int, input().split())

snake = defaultdict(int)
ladder = defaultdict(int)

for _ in range(N):
    x, y = map(int, input().split())
    snake[x] = y
    
for _ in range(M):
    u, v = map(int, input().split())
    ladder[u] = v
    

queue = deque()
queue.append((1, 0))

INF = sys.maxsize
dp = [INF for _ in range(101)]

while queue:
    cur, cost = queue.popleft()
    
    if cur == 100:
        print(cost)
        break
    
    if cost > dp[cur]:
        continue
    
    dp[cur] = cost
    
    if cur in snake.keys():
        cur = snake[cur]
    
    if cur in ladder.keys():
        cur = ladder[cur]
    
    for i in range(1, 7):
        next = cur + i
        if 100 >= next:
            queue.append((next, cost + 1))