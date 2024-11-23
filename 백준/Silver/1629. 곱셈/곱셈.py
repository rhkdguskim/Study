import sys
sys.setrecursionlimit(2147483647//2)
input = sys.stdin.readline

A, B, C = map(int, input().split())

def dfs(n):
    if n == 1:
        return A % C
    
    div = n // 2
    a = dfs(div)
    if n % 2 == 1:
        return (A * a * a) % C
    else:
        return (a * a) % C

print(dfs(B))