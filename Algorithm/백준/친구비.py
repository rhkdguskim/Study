# https://www.acmicpc.net/problem/16562
import sys
input = sys.stdin.readline

N, M, k = map(int, input().split())

parent = [i for i in range(N+1)]

def find(v1):
    if parent[v1] != v1:
        parent[v1] = find(parent[v1])
        return parent[v1]
    
    return parent[v1]

def union(v1, v2):
    p1 = parent[v1]
    p2 = parent[v2]
    if p1 != p2:
        if p1 > p2:
            parent[p1] = p2
        else:
            parent[p2] = p1

friends = []
for i, A in enumerate(list(map(int, input().split()))):
    friends.append((A, i+1))

friends.sort(key=lambda x:x[0])

for _ in range(M):
    v, w = map(int, input().split())
    p1 = find(v)
    p2 = find(w)
    
    if p1 != p2:
        union(p1, p2)

cost = 0
for friend_be, i in friends:
    p1 = find(0)
    p2 = find(i)
    if p1 != p2:
        union(p1, p2)
        cost += friend_be

if cost > k:
    print("Oh no")
else:
    print(cost)
