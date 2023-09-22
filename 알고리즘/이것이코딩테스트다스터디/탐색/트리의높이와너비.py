# https://www.acmicpc.net/problem/2250
# 높이가 10001인 배열을 만든다.
# 각각의 높이에는 x 좌표와 노드번호가 들어간다.
# 10001의 높이를 순회하면서 정렬을 한뒤 0번째배열과 마지막배열을 길이를 구한뒤 최대값에 적용시킨다(노드번호도 적용)
import sys
sys.setrecursionlimit(10000000)
N = int(input())
rootgraph = [[] for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
graph2 = [[] for _ in range(N+1)]
for _ in range(N):
    root, left, right = map(int, input().split())
    # 자식노드 탐색 그래프
    graph[root].append(left)
    graph[root].append(right)
    
def findRoot():
    visited = [False for _ in range(N)]
    for i in range(1, N+1):
        for node in graph[i]:
            if node != -1 and not visited[node-1]:
                visited[node-1] = True
        
    return visited.index(False) + 1

distance = 1

def dfs(node, depth):
    global distance
    
    visited[node-1] = True
    leftnode = graph[node][0]
    rightnode = graph[node][1]
    
    if leftnode != -1 and not visited[leftnode-1]: #좌측 노드가 존재하면방문
        dfs(leftnode, depth + 1)
    
    graph2[depth].append((distance, node))
    distance += 1
        
    if rightnode != -1 and not visited[rightnode-1]: # 우측 노드가 존재하면 방문
        dfs(rightnode, depth + 1)

visited = [False for _ in range(N)]
dfs(findRoot(), 1)

maxvalue = 1
level = 1
for i in range(1, len(graph2)):
    graph2[i].sort()
    if len(graph2[i]) >= 2:
        cost = abs(graph2[i][0][0] - graph2[i][-1][0]) + 1
        if cost >= maxvalue:
            if cost == maxvalue:
                if level > i:
                    level = i
            else:
                maxvalue =  cost
                level = i
        
print(level, maxvalue)