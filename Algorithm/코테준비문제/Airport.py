# https://www.acmicpc.net/problem/10775
import sys
input = sys.stdin.readline
G = int(input())
P = int(input())
parent = [i for i in range(G+1)]
def find(v1):
    if parent[v1] != v1:
        parent[v1] = find(parent[v1])
        return parent[v1]
    else:
        return parent[v1]

def union(v1, v2):
    p1 = find(v1)
    p2 = find(v2)
    if p1 > p2:
        parent[p1] = p2
    else:
        parent[p2] = p1

cnt = 0
for _ in range(P):
    g = int(input())
    p = find(g)

    if p == 0:
        break

    cnt += 1
    union(p, p-1)

print(cnt)