# https://www.acmicpc.net/problem/1162
import sys
import heapq
input = sys.stdin.readline
INF = int(98765432109876543210)

N, M, K = map(int, input().split())

dp = [[INF for _ in range(K+1)] for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for _ in range(M):
    P1, P2, T = map(int, input().split())
    graph[P1].append([T, P2])
    graph[P2].append([T, P1])

for i in range(K+1):
    dp[1][i] = 0

def dijikstra(i, j):
    queue = [(0,0,i)]
    while queue:
        time, cnt, n = heapq.heappop(queue)
        if dp[n][cnt] < time:
            continue

        if n == j:
            break

        if cnt + 1 <= K:
            for t, new_n in graph[n]:
                if dp[new_n][cnt+1] > time:
                    dp[new_n][cnt+1] = time
                    heapq.heappush(queue, (time, cnt+1, new_n))

        for t, new_n in graph[n]:
            if dp[new_n][cnt] > time + t:
                dp[new_n][cnt] = time + t
                heapq.heappush(queue, (time+t, cnt, new_n))

    return min(dp[j])

print(dijikstra(1,N))