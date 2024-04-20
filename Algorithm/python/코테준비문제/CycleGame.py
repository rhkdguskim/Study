# https://www.acmicpc.net/problem/20040
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
parent = [i for i in range(N)]

def find(v1):
    if parent[v1] != v1:
        parent[v1] = find(parent[v1])
        return parent[v1]
    else:
        return v1

def union(v1, v2):
    p1 = find(v1)
    p2 = find(v2)

    if p1 > p2:
        parent[p1] = p2
    else:
        parent[p2] = p1

cnt = 0
iscycle = False
for _ in range(M):
    v1, v2 = map(int, input().split())
    p1 = find(v1)
    p2 = find(v2)
    cnt += 1
    if p1 == p2: # Cycle Made
        iscycle = True
        break
    else:
        union(v1, v2)

if cnt == M and not iscycle:
    print(0)
else:
    print(cnt)