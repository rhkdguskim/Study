# https://www.acmicpc.net/problem/10942
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N): # 길이가 1인 펠린드롬
    dp[i][i] = 1

for i in range(N - 1): # 길이가 2인 펠린드롬
    if arr[i] == arr[i + 1]:
        dp[i][i + 1] = 1
    else:
        dp[i][i + 1] = 0

for i in range(2, N): # 길이가 3이상인 펠린드롬 ( N펠린드롬을 구할때 N-1 펠린드롬을 참고하여 구한다.)
    for j in range(N - i):
        if arr[j] == arr[j+i]:
            dp[j][j+i] = dp[j+1][j+i-1]
        else:
            dp[j][j+i] = 0

for _ in range(M):
    left, right = map(int, input().split())
    print(dp[left - 1][right - 1])
