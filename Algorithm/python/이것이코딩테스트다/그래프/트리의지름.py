#https://www.acmicpc.net/problem/1167
# 시작노드를 하나 정한뒤 노드를 하나하나 방문하면서 가중치를 더해가며 마지막노드까지의 거리중 최대값을 찾는다.
import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

V = int(input())

graph = [[] for _ in range(V+1)]
for v in range(V):
    visitedlist = list(map(int, input().split()))
    for i in range(1, len(visitedlist)- 2, 2):
        graph[visitedlist[0]].append([visitedlist[i], visitedlist[i+1]]) # 노드, 가중치


def dfs(v1, sum):
    for v2, cost in graph[v1]:
        newcost = sum + cost
        if visited[v2] == -1:
            visited[v2] = newcost
            dfs(v2, newcost)
        
        
visited = [-1 for _ in range(V+1)]
visited[1] = 0

dfs(1,0)

newstart = visited.index(max(visited))
visited = [-1 for _ in range(V+1)]
visited[newstart] = 0

dfs(newstart,0)
print(max(visited))