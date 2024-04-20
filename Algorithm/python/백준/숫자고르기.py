# https://www.acmicpc.net/problem/2668
# 깊이우선탐색을 한다.
# 현재 위치에서 값이 있는지 확인한다.

import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

def dfs(idx):
    if visited[idx] == False:
        visited[idx] = True
        
        top.add(idx+1)
        bottom.add(nums[idx])
        
        if top == bottom:
            ans.extend(list(top))
            return
        
        dfs(nums[idx]-1)
        
    visited[idx] = False

ans = []
for i in range(N):
    visited = [False for _ in range(N)]
    top = set()
    bottom = set()
    dfs(i)
    
ans = list(set(ans))
ans.sort()

print(len(ans))

for n in ans:
    print(n)