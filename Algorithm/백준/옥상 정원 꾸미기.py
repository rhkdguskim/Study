# https://www.acmicpc.net/problem/6198
import sys
input = sys.stdin.readline

N = int(input())

buildings = list(int(input()) for _ in range(N))

stack = []
ans = 0
for i in range(N-1, -1, -1):
    cnt = 1
    while stack and buildings[i] > stack[-1][0]:
        _, c = stack.pop()
        cnt += c
        ans += c
    
    stack.append((buildings[i], cnt))
    
print(ans)