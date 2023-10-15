# https://www.acmicpc.net/problem/10775
import sys
input = sys.stdin.readline
G = int(input())
P = int(input())
parent = [i for i in range(G+1)]
dock = [0]

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

for _ in range(P):
    g = int(input())
    p1 = find(0) # 가상의 0번 노드
    p2 = find(g)
    if p1 != p2:
        union(p1, p2)

    if g > dock[0]:
        dock[0] = g

    if dock[0] >= g:
        continue

    if dock[0] >= G-1:
        break

    dock[0] += 1

print(dock[0])

