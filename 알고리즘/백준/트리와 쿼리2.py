# https://www.acmicpc.net/problem/15681
import sys

input = sys.stdin.readline

N, R, Q = map(int, input().split())
edge = [[] for _ in range(N+1)]
cnt_node = [0 for _ in range(N+1)]

for _ in range(N-1):
    U, V = map(int, input().split())
    edge[U].append(V)
    edge[V].append(U)
    

stack = [R]
path = []

while stack:
    node = stack.pop()
    cnt_node[node] = 1
    for new_node in edge[node]:
        if not cnt_node[new_node]:
            stack.append(new_node)
            path.append((node, new_node))
            
while path:
    node1, node2 = path.pop()
    cnt_node[node1] += cnt_node[node2]

for _ in range(Q):
    n = int(input())
    print(cnt_node[n])