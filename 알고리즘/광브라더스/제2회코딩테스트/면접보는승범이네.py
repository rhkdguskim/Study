# https://www.acmicpc.net/problem/17835
import sys
import heapq
from pprint import pprint
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    U, V, C = map(int, input().split())
    graph[V].append((C, U)) # 거꾸로 탐색하기위해 거꾸로 넣는다.

ic = list(map(int, input().split()))

maxidx = 0
maxdistance = 0
visited = [100000*500000 for _ in range(N+1)]
queue = []

for init in graph:
    init.sort()

for k in ic:
    heapq.heappush(queue, (0, k))
    visited[k] = 0

maxvalue = 0
maxidx = 0
while queue:
    cost, target = heapq.heappop(queue)

    if cost > visited[target]:
        continue

    if cost >= maxvalue:
        if maxvalue == cost and target > maxidx:
            pass
        else:
            maxidx = target

        maxvalue = cost

    for dis, newidx in graph[target]:
        if visited[newidx] > cost + dis:
            visited[newidx] = cost + dis
            heapq.heappush(queue, (dis + cost, newidx))

#pprint(visited)
print(maxidx)
print(maxvalue)






