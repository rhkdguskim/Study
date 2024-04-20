# https://www.acmicpc.net/problem/15681
import sys

input = sys.stdin.readline

N, R, Q = map(int, input().split())
edge = [[] for _ in range(N+1)]
dp = [0 for _ in range(N+1)]

for _ in range(N-1):
    U, V = map(int, input().split())
    edge[U].append(V)
    edge[V].append(U)
    

stack = [R]
path = []

while stack:
    parent = stack.pop()
    dp[parent] = 1
    for child in edge[parent]:
        if not dp[child]:
            stack.append(child)
            path.append((parent, child))
            
while path:
    parent, child = path.pop()
    dp[parent] += dp[child]

for _ in range(Q):
    n = int(input())
    print(dp[n])