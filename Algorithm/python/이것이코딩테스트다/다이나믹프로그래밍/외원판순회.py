#https://www.acmicpc.net/problem/2098
from itertools import permutations
from collections import deque
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int ,input().split())))

minvalue = int(10e9)

def bfs(i, queue):
    global minvalue
    distance = 0
    start = i
    while queue:
        end = queue.popleft()
        distance += graph[start][end]
        
        if distance > minvalue:
            return int(10e9)
        
        start = end
        
    return distance
        
    
for i in range(N):
    numlist = [x for x in range(N) if i != x]
    numlist.append(i)
    for queue in list(permutations(numlist)):
        newqueue = deque(queue)
        newqueue.append(i) # 자기자신으로 돌아오는경우
        minvalue = min(bfs(i, newqueue), minvalue)
        
        
print(minvalue)