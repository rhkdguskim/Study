# https://www.acmicpc.net/problem/1991
# 12
# 7 3 8 1 9 4 10 0 11 5 2 6
# 7 8 3 9 10 4 1 11 5 6 2 0
import sys
sys.setrecursionlimit(100001 * 3)

input = sys.stdin.readline
n = int(input())

in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

dp = [0 for _ in range(n+1)]
for i in range(n):
    dp[in_order[i]] = i
    
def dfs(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return
    
    root = post_order[post_end] # 포스트 오더의 마지막 인덱스는 항상 루트이다.
    print(root, end=' ') # 루트 노드 출력
    
    idx = dp[root]
    # 왼쪽노드 탐색
    dfs(in_start, idx-1, post_start, post_start - in_start + idx-1)
    # 오른쪽 노드 탐색
    dfs(idx+1, in_end, post_end - in_end + idx, post_end-1)
    
dfs(0,n-1, 0, n-1)
print()