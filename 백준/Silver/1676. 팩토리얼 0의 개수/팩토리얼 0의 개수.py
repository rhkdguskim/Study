import sys

input = sys.stdin.readline
N = int(input())

def dfs(n, v, cnt):
    if n > N:
        return cnt
    
    v = v * n
    while v % 10 == 0:
        v //= 10
        cnt += 1
    
    return dfs(n+1, v, cnt)

print(dfs(1, 1, 0))