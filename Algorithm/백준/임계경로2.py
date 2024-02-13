# https://www.acmicpc.net/problem/1948
import sys
from collections import deque, defaultdict

input = sys.stdin.readline


n = int(input())
m = int(input())

edge = [[] for _ in range(n+1)]
degree = [0 for _ in range(n+1)]
distance = [0 for _ in range(n+1)]
visited = [defaultdict(int) for _ in range (n+1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    edge[start].append((end, cost))
    degree[end] += 1

start, end = map(int, input().split())

def dfs(node, cost):
    
    for new_node, new_cost in edge[node]:
        degree[new_node] -= 1
        visited[new_node][new_cost + cost] += visited[node][cost] + 1
        distance[new_node] = max(distance[new_node], new_cost + cost)
        if degree[new_node] == 0:
            dfs(new_node, distance[new_node])
            
dfs(start, 0)
print(distance[end], visited[end][distance[end]])