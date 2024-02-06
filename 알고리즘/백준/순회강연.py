# https://www.acmicpc.net/problem/2109
import sys
input = sys.stdin.readline

N = int(input())
cost = []
for _ in range(N):
    p, d  = map(int, input().split())
    cost.append((p, d))

cost.sort(key=lambda x:(-x[0]))
parent = [i for i in range(10001)]

def find(p1):
    if p1 != parent[p1]:
        parent[p1] = find(parent[p1])
        return parent[p1]
    
    return p1
    
def union(p1, p2):
    v1 = find(p1)
    v2 = find(p2)
    if v1 != v2:
        if v1 > v2:
            parent[v1] = v2
        else:
            parent[v2] = v1

ans = 0
for p, d in cost:
    day = find(d)
    if day > 0:
        union(day, day-1)
        ans += p

print(ans)
