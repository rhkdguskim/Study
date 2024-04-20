# https://www.acmicpc.net/problem/11722
import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = []
dp.append(-arr[0])

for i in range(1, N):
    if -dp[-1] > arr[i]:
        dp.append(-arr[i])
    else:
        idx = bisect_left(dp, -arr[i])
        dp[idx] = -arr[i]
        
print(len(dp))