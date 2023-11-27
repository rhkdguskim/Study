# https://www.acmicpc.net/problem/11066
import sys
input = sys.stdin.readline


def prefix_sum(p_sum, start, end):
    return p_sum[start] - p_sum[end]

def solve():
    N = int(input())
    file = list(map(int, input().split()))
    p_sum = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        p_sum[i] = p_sum[i-1] + file[i-1]
    
    dp = [[int(1e9) for _ in range(N)] for _ in range(N)] # (i, j) 까지의 최소 합
    
    for i in range(N):
        dp[i][i] = 0
        
    for s in range(2, N+1): # 길이가 N이면 N-1 사이즈를 확인하면 된다. (0, 1,2, 3)
        for start in range(N-s + 1):
            end = start + s - 1
                
            for mid in range(start, end):
                dp[start][end] = min(dp[start][end], dp[start][mid] + dp[mid+1][end] + prefix_sum(p_sum, end+1, start))

    print(dp)
    print(dp[0][N-1])
T = int(input())
for _ in range(T):
    solve()
