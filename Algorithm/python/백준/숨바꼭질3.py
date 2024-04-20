# https://www.acmicpc.net/problem/13549
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque()
queue.append((N, 0))
dp = [100000 for _ in range(100001)]

while queue:
    dis, time = queue.popleft()
    
    if dis > 100000 or dis < 0:
        continue
    
    if time > dp[dis]:
        continue
    
    dp[dis] = time
    if dis == K:
        print(time)
        break
    
    queue.append((dis*2, time))
    queue.append((dis-1, time + 1))
    queue.append((dis+1, time + 1))