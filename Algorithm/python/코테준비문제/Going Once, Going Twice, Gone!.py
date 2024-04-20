# https://www.acmicpc.net/problem/1246
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
P = []

for _ in range(M):
    P.append(int(input()))

P.sort()
ans = 0
maxcost = 0
for pr in P:
    cnt = 0
    for pr2 in reversed(P):
        if pr2 >= pr:
            cnt += 1

    if N >= cnt:
        if cnt * pr > maxcost:
            maxcost = cnt * pr
            ans = pr

print(ans, maxcost)