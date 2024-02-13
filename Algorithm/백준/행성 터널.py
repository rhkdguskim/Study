# https://www.acmicpc.net/problem/2887
# 간선의 정보가 필요함.
# MST 알고리즘을 활용해야함.
# 정렬을 한다음에, 자기자신의 위와 아래의 diff 를 확인한다.
import sys

input = sys.stdin.readline

N = int(input())
parent = [i for i in range(N)]
planet = [[] for _ in range(3)]
for i in range(N):
    a, b, c = map(int, input().split())
    planet[0].append((a, i))
    planet[1].append((b, i))
    planet[2].append((c, i))

def find(a):
    if parent[a] != a:        
        return find(parent[a])
    else:
        return a

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def get_distance(n1, n2):
    return abs(n1 - n2)

distance = []

planet[0].sort(key=lambda x:x[0])
planet[1].sort(key=lambda x:x[0])
planet[2].sort(key=lambda x:x[0])

for node in range(N-1):
    for i in range(3):
        distance.append((get_distance(planet[i][node-1][0], planet[i][node][0]), planet[i][node-1][1], planet[i][node][1]))
        distance.append((get_distance(planet[i][node][0], planet[i][node+1][0]), planet[i][node][1], planet[i][node+1][1]))
        
distance.sort()
ans = 0
for dis, node, new_node in distance:
    v1 = find(node)
    v2 = find(new_node)
    if v1 != v2:
        ans += dis
        union(node, new_node)

print(ans)



