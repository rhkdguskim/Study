# https://www.acmicpc.net/problem/2887
# 간선의 정보가 필요함.
# MST 알고리즘을 활용해야함.
# 정렬을 한다음에, 자기자신의 위와 아래의 diff 를 확인한다.
import sys

input = sys.stdin.readline

N = int(input())
parent = [i for i in range(N)]
planet = [list(map(int, input().split())) for _ in range(N)]

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
    return min(abs(n1[0]-n2[0]), abs(n1[1]-n2[1]), abs(n1[2]-n2[2]))

distance = []
for node in range(N):
    for new_node in range(node + 1, N):
        distance.append((get_distance(planet[node], planet[new_node]), node, new_node))
        
distance.sort()
ans = 0
for dis, node, new_node in distance:
    v1 = find(node)
    v2 = find(new_node)
    if v1 != v2:
        ans += dis
        union(node, new_node)
        

print(ans)



