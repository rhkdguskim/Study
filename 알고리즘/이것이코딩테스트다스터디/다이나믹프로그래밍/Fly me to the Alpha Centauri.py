# https://www.acmicpc.net/problem/1011
from collections import deque
T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    dp = [y+1 for _ in range(y+1 - x)]
    queue = deque()
    queue.append([1, 1])
    dp[0] = 0
    dp[1] = 1
    while queue:
        distance, year = queue.popleft()
        if year > 0 and y+1 - x > distance + year + 1:
            cost = dp[distance] + 1
            
            if year - 1 > 0 and dp[distance + year-1] > cost: # K -1
                dp[distance + year-1] = cost 
                queue.append([distance + year-1, year-1])
            if dp[distance + year] > cost: # K
                dp[distance + year] = cost
                queue.append([distance + year, year])
            if dp[distance + year+1] > cost: # K+1
                dp[distance + year+1] = cost
                queue.append([distance + year+1, year+1])
    if y-x == 1:
        print(1)
    else:
        print(dp[y-1 - x]+1)