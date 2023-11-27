# https://www.acmicpc.net/problem/2342
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

INF = int(1e9)
input_cmd = list(map(int, input().split()))
dp = [[[[INF for _ in range(5)] for _ in range(5)] for _ in range(5)] for _ in range(5)]

def dfs(s_left, s_right, t_left, t_right, idx):
    if input_cmd[idx] == 0: # 종료조건
        return 0
    
    if dp[s_left][s_right][t_left][t_right] != INF: # 이미 최소값이 존재한다면
        return dp[s_left][s_right][t_left][t_right] # 최소값을 리턴한다.
        
    # 왼쪽으로 갔을때
    if s_left == 0: # 0으로 시작한다면
        cost = 2
    elif s_left == input_cmd[idx]: # 동일 위치일때
        cost = 1
    elif abs(s_left - input_cmd[idx]) == 2: # 반대쪽 위치일때
        cost = 4
    else: # 다른 인접 위치로 이동할때
        cost = 3
    dp[t_left][t_right][input_cmd[idx]][t_right] = dfs(t_left, t_right, input_cmd[idx], t_right, idx+1) + cost
    
    # 오른쪽으로 갔을때
    if s_right == 0: # 0으로 시작한다면
        cost = 2
    elif s_right == input_cmd[idx]: # 동일 위치일때
        cost = 1
    elif abs(s_right - input_cmd[idx]) == 2: # 반대쪽 위치일때
        cost = 4
    else: # 다른 인접 위치로 이동할때
        cost = 3
    
    dp[t_left][t_right][t_left][input_cmd[idx]] = dfs(t_left, t_right, t_left, input_cmd[idx], idx+1) + cost
    
    dp[s_left][s_right][t_left][t_right] = min(dp[t_left][t_right][input_cmd[idx]][t_right], dp[t_left][t_right][t_left][input_cmd[idx]])
    return dp[s_left][s_right][t_left][t_right]

print(dfs(0,0,0,0,0))
#print(dp)