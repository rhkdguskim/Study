# https://www.acmicpc.net/problem/1509

import sys
input = sys.stdin.readline

word = str(input().strip())
L = len(word)

is_p = [[False for _ in range(L)] for _ in range(L)]
dp = [0 for _ in range(L+1)]

for i in range(L):
    is_p[i][i] = True

for i in range(L-1):
    if word[i] == word[i+1]:
        is_p[i][i+1] = True

for k in range(2, L):
    for i in range(L-k):
        start = i
        end = i+k
        if word[start] == word[end] and is_p[start+1][end-1]:
            is_p[start][end] = True

for end in range(L):
    dp[end+1] = float('inf')
    for start in range(end + 1):
        if is_p[start][end]:
            dp[end+1] = min(dp[end+1], dp[start] + 1)

print(dp[L])
