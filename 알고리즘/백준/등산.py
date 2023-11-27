# https://www.acmicpc.net/problem/16681
import heapq
import sys
input = sys.stdin.readline
INF = int(1e15)
# 주완이는 올라갈때 (얻은 성취감) - (소모한 체력)이 가장 높은 가치가 나오게 이동한다. ( 모든 경로까지 가치가 저장된다. )
# 모든 가치가 저장된 목적지로부터 다시 고려대학교까지 내려가는데 내려갈때는 거리가 가장 짧은 순으로 내려간다.


# 1. 집에서 고려대학교를 제외한 부분을 높이가 증가하는 방향으로, 꼭대기까지 방문한다. 방문할때 각각의 가중치를 각 위치에 저장한다.
# 각 위치에서부터 고려대학교로 내려와하는데 이건, 이동하기만하므로 가중치를 빼준다.
# 계산된값중에 가장 큰 값이 가장 높은 등산 경로이다.

N, M, D, E = map(int, input().split()) #지점의개수, 경로의개수, 비례 체력 소모량, 높이 비례 성취감
h = [0]+ list(map(int, input().split())) # i번째 지점의 높이를 의미
up = [[] for _ in range(N+1)] 
down = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, n = map(int, input().split())
    if h[b] > h[a]:
        up[a].append((b, n)) # 위치, 거리
        down[b].append((a, n)) # 위치, 거리
    else:
        up[b].append((a, n)) # 위치, 거리
        down[a].append((b, n)) # 위치, 거리

up_distance = [-INF for _ in range(N+1)]
queue = []

# 가장 짧은 거리를 이동해야 가치가 크다.
for new, d in up[1]:
    heapq.heappush(queue, (d, new)) # 거리, 위치
    up_distance[new] = (E*h[new] - D*d)

while queue:
    dis, target = heapq.heappop(queue)
    
    if up_distance[target] <= (E*h[target] - D*(dis)):
        for new_target, d in up[target]:
            new_distance = dis + d
            new_cost = (E*h[new_target] - D*(new_distance))
            if new_cost > up_distance[new_target]:
                up_distance[new_target] = new_cost
                heapq.heappush(queue, (new_distance, new_target))


down_distance = [-INF for _ in range(N+1)]

# 정상에 도달한 노드들
new_queue = []
for i in range(1, N+1):
    if up_distance[i] != -INF:
        heapq.heappush(new_queue, (-up_distance[i], i)) # 최대 힙으로 탐색한다.
        down_distance[i] = up_distance[i]
        
ans = -INF
while new_queue:
    dis, node = heapq.heappop(new_queue)
    if node == N:
        ans = max(ans, -dis)
    if down_distance[node] <= -dis:
        for new_node, d in down[node]:
            new_cost = -dis - d*D
            if down_distance[new_node] < new_cost:
                down_distance[new_node] = new_cost
                heapq.heappush(new_queue, (-new_cost, new_node)) # 최대 힙으로 탐색한다.
    
if ans == -INF:
    print('Impossible')
else:
    print(ans)
    