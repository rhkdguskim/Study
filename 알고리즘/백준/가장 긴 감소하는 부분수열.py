# https://www.acmicpc.net/problem/11722
import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = []
dp.append(arr[0])

for i in range(1, N):
    if dp[-1] > arr[i]:
        dp.append(arr[i])
    else:
        for j in range(len(dp)):
            if arr[i] >= dp[j]:
                dp[j] = arr[i]
                break
        
print(len(dp))