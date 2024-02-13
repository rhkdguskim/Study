# https://www.acmicpc.net/problem/14226
import sys
from collections import deque
input = sys.stdin.readline

S = int(input())

queue = deque([(1, 0, 0)])
dp = [[False for _ in range(1001)] for _ in range(1001)]
dp[1][0] = True

while queue:
    screen, clipboard, time = queue.popleft()
    
    if S == screen:
        print(time)
        break
    
    if 1000 >= screen+clipboard and not dp[screen+clipboard][clipboard]:
        queue.append((screen+clipboard, clipboard, time + 1))
        dp[screen+clipboard][clipboard] = True
        
    if not dp[screen][screen]:
        queue.append((screen, screen, time + 1))
        dp[screen][screen] = True
    
    if screen -1 >= 0 and not dp[screen-1][clipboard]:
        queue.append((screen-1, clipboard, time + 1))
        dp[screen-1][clipboard] = True