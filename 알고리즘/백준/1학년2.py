# https://www.acmicpc.net/problem/5557

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
length = len(nums) - 1

dp = [[0 for _ in range(21)] for _ in range(length)]

dp[0][nums[0]] = 1

for i in range(1, length):
    for j in range(21):
        if dp[i-1][j]:
            if 20 >= j + nums[i]:
                dp[i][j+nums[i]] += dp[i-1][j]
            
            if j - nums[i] >= 0:
                dp[i][j-nums[i]] += dp[i-1][j]

print(dp[length-1][nums[-1]])