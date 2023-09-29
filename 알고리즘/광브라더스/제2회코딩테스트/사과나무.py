from pprint import pprint
N = int(input())
table = []
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(N):
    table.append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + table[i-1][j-1] # 2차원 배열 구간 합 구하기

# 모든 경우의수를 탐색하여 최대값을 갱신한다.
maxvalue = -1000 * 300 * 300 - 1
for n in range(1, N+1):
    for i in range(n, N+1):
        for j in range(n, N+1):
            if N >= i-n >= 0 and N >= j-n >= 0: # 배열의 범위가 넘어가면 안됨
                temp = dp[i][j] - dp[i-n][j] - dp[i][j-n] + dp[i-n][j-n]
                maxvalue = max(maxvalue, temp)

print(maxvalue)