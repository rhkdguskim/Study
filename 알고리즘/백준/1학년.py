# https://www.acmicpc.net/problem/5557
# 현재위치의 숫자값이 있다면 그것에 가중치를 더하면 된다.

# 11
# 8 3 2 4 8 7 2 4 0 8 8

import sys
input = sys.stdin.readline
INF = pow(2, 63) -1
N = int(input())
nums = list(map(int, input().split()))

result = nums[-1]
nums.pop()
length = len(nums)
dp = [[-1 for _ in range(21)] for _ in range(length)]

def dfs(i, cur):
    if i == length-1:
        if cur == result:
            return 1
        else:
            return 0
    
    if dp[i][cur] != -1:
        return dp[i][cur]
    
    dp[i][cur] = 0
    if 20 >= cur + nums[i+1] >= 0:
        dp[i][cur] += dfs(i+1, cur + nums[i+1])
    if 20 >= cur - nums[i+1] >= 0:
        dp[i][cur] += dfs(i+1, cur - nums[i+1])
    
    return dp[i][cur] % INF

print(dfs(0, nums[0]))