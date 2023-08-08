# https://www.acmicpc.net/problem/1068
# 1. 부모노드에서 자식노드로 갈 수 있는 graph를 생성한다.
# 2. 지운 노드를 기억하여 지운 노드는 방문하지 않는다.
# 3. 자식노드가 없을경우 Leaf노드로 카운트 증가한다.
from collections import deque
N = int(input())
nodeInput = list(map(int ,input().split()))
deletedNode = int(input())
graph = [[] for _ in range(N)]
rootnode = 0
for i in range(len(nodeInput)):
    if nodeInput[i] >= 0:
        graph[nodeInput[i]].append(i)
    else:
        rootnode = i
    
cnt = 0
def bfs():
    global cnt
    queue = deque()
    queue.append(rootnode) # 루트노드로 부터 출발
    
    while queue:
        node = queue.popleft()
        if node != deletedNode: # 지운노드인경우는 자식도 방문하지 않는다.
            if graph[node]: # 자식이 있는경우
                for newnode in graph[node]:
                    queue.append(newnode)
            else: # 자식이 없는경우 (Leaf 노드인경우)
                cnt += 1
                
bfs()
print(cnt)
            