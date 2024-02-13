# https://www.acmicpc.net/problem/13904
import sys
input = sys.stdin.readline
N = int(input())

works = []
for _ in range(N):
    day, cost = map(int, input().split())
    works.append((day, cost))
    
works.sort(key=lambda x:-x[1])

parent = [i for i in range(10001)]

def find(v1):
    if v1 != parent[v1]:
        parent[v1] = find(parent[v1])
        return parent[v1]
    
    return v1

def union(v1, v2):
    p1 = find(v1)
    p2 = find(v2)
    
    if p1 != p2:
        if p1 > p2:
            parent[p1] = p2
        else:
            parent[p2] = p1

ans = 0
for day, cost in works:
    d = find(day)
    if d > 0:
        union(d, d-1)
        ans += cost

print(ans)
