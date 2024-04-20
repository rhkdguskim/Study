# https://www.acmicpc.net/problem/8980
import sys
import heapq

input = sys.stdin.readline

N, C = map(int, input().split())
M = int(input())

edge = [[] for _ in range(N+1)]

for _ in range(M):
    src, dst, cost = map(int, input().split())
    edge[src].append((dst, cost))

for i in range(1, N+1):
    edge[i].sort(key=lambda x:(x[0], x[1]))

queue = []
truck_size = 0

cur = 1
ans = 0
while N >= cur:
    # 택배 하차.
    while queue and queue[0][0] <= cur:
        dst, cost = heapq.heappop(queue)
        #print(dst, cost)
        ans += cost
        truck_size -= cost
    
    # 택배 상차.
    for dst, cost in edge[cur]:
        if queue and queue[0][0] > dst and cost >= queue[0][1]:
            old_dst, old_cost = heapq.heappop(queue)
            truck_size -= old_cost
            
        if C > truck_size:
            if C >= cost + truck_size:
                heapq.heappush(queue, (dst, cost))
                truck_size += cost
            else:
                heapq.heappush(queue, (dst, C-truck_size))
                truck_size = C
            
            
    cur += 1
    
print(ans)