# https://www.acmicpc.net/problem/16681
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
# 주완이는 올라갈때 (얻은 성취감) - (소모한 체력)이 가장 높은 가치가 나오게 이동한다. ( 모든 경로까지 가치가 저장된다. )
# 모든 가치가 저장된 목적지로부터 다시 고려대학교까지 내려가는데 내려갈때는 거리가 가장 짧은 순으로 내려간다.
N, M, D, E = map(int, input().split())
h = [0]+ list(map(int, input().split()))
up = [[[] for _ in range(N+1)] for _ in range(N+1)]
down = [[[] for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    a, b, n = map(int, input().split())
    if h[b] > h[a]:
        up[a][b].append((n, h[b])) # 거리, 높이
    else:
        down[b][a].append((n, h[a])) # 거리, 높이

up_distance = [-INF for _ in range(N+1)]

queue = []

for i in range(2, N):
    for d, h in up[1][i]:
        heapq.heappush(queue, (-(E*h - D*d), i))
        up_distance[i] = (E*h - D*d)


while queue:
    cost, target = heapq.heappop(queue)
    
    if up_distance[target] < -cost:
        for new in range(N):
            for d, h in up[target][new]:
                new_cost = -cost + (E*h - D*d)
                if new_cost >= up_distance[new]:
                    heapq.heappush(queue, (-new_cost, new))
                
down_queue = []
down_distance = [-INF for _ in range(N+1)]

for i in range(2, len(up_distance) - 1):
    if up_distance[i] != -INF:
        heapq.heappush(down_queue, (-up_distance[i], i))
        down_distance[i] = up_distance[i]


while down_queue:
    cost, target = heapq.heappop(down_queue)
    
    if up_distance[i] > -cost:
        continue
    
    for new in range(target -1, 1, -1):
        for d, h in down[target][new]:
            new_cost = -cost + (E*h - D*d)
            if new_cost >= up_distance[new]:
                heapq.heappush(queue, (-new_cost, new))
    
    