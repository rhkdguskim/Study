# https://www.acmicpc.net/problem/14003
import bisect
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
dp = dict()
dp[0] = [arr[0]]
prev = arr[0]
previdx = 0
for i in range(1, N):
    if prev > arr[i]:
        idx = bisect.bisect_left(dp[previdx], arr[i])
        dp[i] = dp[previdx][:idx+1]
        dp[i][-1] = arr[i]
        previdx = i
    else:
        for table in dp:
            if arr[i] > dp[table][-1]:
                dp[table].append(arr[i])
    prev = arr[i]

maxdp = max(dp)
print(maxdp)

for key in dp:
    if len(dp[key]) == maxdp:
        print(*dp[key])
        break
    
    