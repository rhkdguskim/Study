# https://www.acmicpc.net/problem/1766
import heapq
N ,M = map(int, input().split())
table = [0 for _ in range(N)]
graph = [[] for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    
    graph[A-1].append(B)
    table[B-1] += 1
    
queue = []

for i in range(N):
    if table[i] == 0:
        heapq.heappush(queue, i+1)
        
while queue:
    num = heapq.heappop(queue)
    print(num, end = ' ')
    for newnum in graph[num-1]:
        table[newnum-1] -= 1
        if table[newnum-1] == 0:
            heapq.heappush(queue, newnum)