# https://school.programmers.co.kr/learn/courses/30/lessons/12978
# 각 마을은 양방향으로 연결되어 있다.
# 1번마을에서 N개의 마을중에서 K시간 이하로 배달 가능한 마을을 찾는다.
# 데이크스트라 알고리즘으로 거리를 갱신한뒤 K이하인 마을만 결과에 추가하여 리턴한다.
import heapq
import sys

def solution(N, road, K):
    edge = [[] for _ in range(N+1)]

    # 양방향 간선
    for src, dst, cost in road:
        edge[src].append((dst, cost))
        edge[dst].append((src, cost))

    distance = [sys.maxsize for _ in range(N+1)]
    queue = []
    heapq.heappush(queue, (1, 0))
    distance[1] = 0

    while queue:
        node, cost = heapq.heappop(queue)

        if cost > distance[node]:
            continue

        for next, cost in edge[node]:
            new_cost = distance[node] + cost
            if distance[next] > new_cost:
                distance[next] = new_cost
                heapq.heappush(queue, (next, new_cost))

    return len([i for i in range(1, N+1) if distance[i] <= K])