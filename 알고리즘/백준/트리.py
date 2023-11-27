# https://www.acmicpc.net/problem/4256
import sys
sys.setrecursionlimit(10**6)


def dfs(pre_s, pre_e, in_s, in_e):
    # 범위를 벗어난경우
    if pre_e < pre_s or in_e < in_s:
        return
    
    root = pre_order[pre_s]
    idx = dp[root]
    left = idx - in_s
    right = in_e - idx
    
    dfs(pre_s+1, pre_s + left, in_s, idx-1) # 왼쪽노드
    dfs(pre_e - right+1, pre_e, idx+1, in_e) # 오른쪽노드
    print(root, end= ' ')
    
T = int(input())

for _ in range(T):
    n = int(input())
    pre_order = list(map(int, input().split()))
    in_order = list(map(int, input().split()))
    dp = [0 for _ in range(n+1)]
    for i in range(n):
        dp[in_order[i]] = i
    
    dfs(0, n-1, 0, n-1)
    print()


    