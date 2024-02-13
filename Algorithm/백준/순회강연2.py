# https://www.acmicpc.net/problem/2109
import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input())
cost = []
for _ in range(N):
    p, d  = map(int, input().split())
    cost.append((p, d))
    
cost.sort(key=lambda x:(x[1]))
q = []
for p, d in cost:
    heappush(q, p)
    
    while len(q) > d:
        heappop(q)

print(sum(q))