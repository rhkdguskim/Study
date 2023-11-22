# https://www.acmicpc.net/problem/2565
# LIS 문제 ( 최장 증가하는 부분수열 )

N = int(input())

queue = []
for _ in range(N):
    a, b = map(int ,input().split())
    
    queue.append((a,b))
    
queue.sort()

dp = [0 for _ in range(N)]
dp[0] = 1
for i in range(1,len(queue)):
    dp[i] = 1
    for j in range(i):
        if queue[j][1] < queue[i][1]:
            dp[i] = max(dp[j] + 1, dp[i])
                
print(N - max(dp))

# 이분탐색으로 코드를 개선한다.
from bisect import bisect_left
N = int(input())

queue = []
for _ in range(N):
    a, b = map(int ,input().split())
    
    queue.append((a,b))
    
queue.sort()

temp = []
temp.append(queue[0][1]) # 첫번째 인자를 넣는다.
for i in range(1,len(queue)):
    if queue[i][1] > temp[-1]:
        temp.append(queue[i][1])
    else:
        idx = bisect_left(temp, queue[i][1])
        temp[idx] = queue[i][1]

print(N - len(temp))