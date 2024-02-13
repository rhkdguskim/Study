import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

INF = int(1e9)
input_cmd = list(map(int, input().split()))
dp = [[[-1 for _ in range(5)] for _ in range(5)] for _ in range(len(input_cmd)+1)]

def move_cost(from_pos, to_pos):
    if from_pos == to_pos:  # 같은 위치
        return 1
    elif from_pos == 0:  # 중앙
        return 2
    elif abs(from_pos - to_pos) == 2:  # 반대쪽
        return 4
    else:  # 인접
        return 3

def dfs(s_left, s_right, idx):
    if input_cmd[idx] == 0:  # 종료 조건
        return 0
    
    if dp[idx][s_left][s_right] != -1:  # 이미 계산됨
        return dp[idx][s_left][s_right]
    
    to_pos = input_cmd[idx]
    left_move = dfs(to_pos, s_right, idx + 1) + move_cost(s_left, to_pos)
    right_move = dfs(s_left, to_pos, idx + 1) + move_cost(s_right, to_pos)
    
    dp[idx][s_left][s_right] = min(left_move, right_move)  # 최소값 저장
    return dp[idx][s_left][s_right]

print(dfs(0, 0, 0))