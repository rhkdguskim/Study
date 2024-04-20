# https://www.acmicpc.net/problem/1647
# 최소신장트리문제 최소신장트리에서 간선하나를 연결하지않는 상태

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

parent = [i for i in range(N+1)]

def find(v1):
    if parent[v1] != v1:
        parent[v1] = find(parent[v1])
        return parent[v1]

    return parent[v1]

def union(v1, v2):
    p1 = find(v1)
    p2 = find(v2)
    if p1 >= p2:
        parent[p1] = p2
    else:
        parent[p2] = p1

edge = []
for _ in range(M):
    A, B, C = map(int, input().split())
    edge.append((A, B, C))
    
edge.sort(key=lambda x:x[2])

cnt = 0
ans = 0
for A, B, C in edge:
    if cnt == N-2:
        break
    
    p1 = find(A)
    p2 = find(B)
    if p1 != p2:
        ans += C
        cnt += 1
        union(p1, p2)
    
print(ans)
        
           