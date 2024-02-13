# https://www.acmicpc.net/problem/18222
import sys
input = sys.stdin.readline

k = int(input())

n = 1
while n <= k:
    n *= 2
    
def dfs(start, end, char):
    if start >= end:
        return char
    
    mid = (start + end) // 2
    if k <= mid: # 왼쪽
        return dfs(start, mid, char) # 왼쪽
    else:
        if char == 0:
            char = 1
        else:
            char = 0
            
        return dfs(mid+1, end, char) # 오른쪽
print(dfs(1, n, 0))