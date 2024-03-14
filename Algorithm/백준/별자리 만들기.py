# https://www.acmicpc.net/problem/4386
# 최소신장트리
import sys
from math import sqrt
input = sys.stdin.readline

def get_distance(y1, x1, y2, x2):
    y = pow(abs(int((y1*100 - y2*100)//100)), 2)
    x = pow(abs(int((x1*100 - x2*100)//100)), 2)
    return sqrt(y+x)


N = int(input())

node = []
for _ in range(N):
    a, b = map(float, input().split())
    node.append((a, b))
    
edge = []
for i in range(N):
    for j in range(i+1, N):
        y1, x1 = node[i]
        y2, x2 = node[j]
        cost = get_distance(y1, x1, y2, x2)
        edge.append((i, j, cost))

edge.sort(key=lambda x:x[2])

parent = [i for i in range(N)]

def find(v1):
    if v1 != parent[v1]:
        p1 = find(parent[v1])
        return p1
    else:
        return v1
    
def union(v1, v2):
    p1 = find(v1)
    p2 = find(v2)
    
    if p1 > p2:
        parent[p1] = p2
    else:
        parent[p2] = p1
        
ans = 0 
for n1, n2, cost in edge:
    p1 = find(n1)
    p2 = find(n2)
    if p1 != p2:
        union(p1, p2)
        ans += cost

print(round(ans, 2))