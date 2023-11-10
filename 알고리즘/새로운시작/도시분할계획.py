# https://www.acmicpc.net/problem/1647
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

parent = [i for i in range(N+1)]

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
        return parent[a]
    else:
        return parent[a]

def union(a, b):
    n = find(a)
    n2 = find(b)
    
    if n > n2:
        parent[n] = n2
    else:
        parent[n2] = n
        
route = []
for _ in range(M):
    A, B, C = map(int, input().split())
    route.append((C, A, B)) # 유지비 ,노드1, 노드2

route.sort()
new_route = []
for cost, n1, n2 in route:
    a = find(n1)
    b = find(n2)
    
    if a != b:
        new_route.append((cost, a, b))
        union(a, b)

new_route.sort()
ans = 0

for cost ,_ ,_ in new_route:
    ans += cost
print(ans - new_route[-1][0])
    