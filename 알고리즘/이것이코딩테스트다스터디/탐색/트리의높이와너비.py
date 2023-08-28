# https://www.acmicpc.net/problem/2250
# 높이가 10001인 배열을 만든다.
# 각각의 높이에는 x 좌표와 노드번호가 들어간다.
# 10001의 높이를 순회하면서 정렬을 한뒤 0번째배열과 마지막배열을 길이를 구한뒤 최대값에 적용시킨다(노드번호도 적용)
from pprint import pprint
import sys
sys.setrecursionlimit(10000000)
N = int(input())
rootgraph = [[] for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
graph2 = [[] for _ in range(N+1)]
rootnode = 0
for _ in range(N):
    root, left, right = map(int, input().split())
    # 자식노드 탐색 그래프
    graph[root].append(left)
    graph[root].append(right)
    # 루트 노드를 찾기위한 그래프
    rootgraph[left].append(root)
    rootgraph[right].append(root)
    
def findRoot():
    rootnode = 0
    for i in range(1, N+1):
        if len(rootgraph[i]) == 0:
            rootnode = i
            return rootnode
        
    return rootnode

distance = 1
graph[0].append(-1)
graph[0].append(-1)
def dfs(node, depth):
    global distance
    
    leftnode = graph[node][0]
    rightnode = graph[node][1]
    
    if leftnode != -1: #좌측 노드가 존재하면방문
        dfs(leftnode, depth + 1)
    
    graph2[depth].append((distance, node))
    distance += 1
        
    if rightnode != -1: # 우측 노드가 존재하면 방문
        dfs(rightnode, depth + 1)

dfs(findRoot(), 1)

maxvalue = 0
level = 1
for i in range(len(graph2)):
    list = sorted(graph2[i])
    if len(list) >= 2:
        cost = abs(list[0][0] - list[-1][0]) + 1
        if cost >= maxvalue:
            if cost == maxvalue:
                if level > i:
                    level = i
            else:
                maxvalue =  cost
                level = i

print(level, maxvalue)