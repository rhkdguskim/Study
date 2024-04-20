# https://www.acmicpc.net/problem/16947
# 사이클까지의 최소거리를 구한다.
# 사이클이 존재한다면 0, 주변에 사이클이 있는 가장 가까운 노드를 찾는다.
# 사이클이 생기는 조건은 DFS 탐색했을때 방문한 배열이 있다면 사이클이 생기고 그 방문 배열들은 모두 사이클 처리를 한다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e4))
N = int(input())
edge = [[] for _ in range(N+1)]

for _ in range(N):
    start, end = map(int, input().split())
    edge[end].append(start)
    edge[start].append(end)

cycled = [False for _ in range(N+1)]

def dfs(start, node, visited:set):
    for next in edge[node]:
        if next not in visited:
            visited.add(next)
            dfs(start, next, visited)
            visited.remove(next)
        elif len(visited) >= 3 and start == next:
            for v in visited:
                cycled[v] = True
            return
    

for i in range(1, N+1):
    if not cycled[i]:
        dfs(i, i, set([i]))

def find(node, visited:set):
    if cycled[node]:
        return len(visited) - 1
            
    min_result = N+1
    for next in edge[node]:
        if next not in visited:
            visited.add(next)
            min_result = min(find(next, visited), min_result)
            visited.remove(next)
            
    return min_result        

ans = []
for node in range(1, len(cycled)):
    if cycled[node]:
        ans.append(0)
    else:
        ans.append(find(node, set([node])))
        
print(*ans)