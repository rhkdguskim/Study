from collections import deque
import sys
import math
input = sys.stdin.readline

# 기준은 연료통으로
def calc(c1, c2):
    return (c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2


def bfs(cur, cnt):
    q = deque([(cur, cnt)])  # 처음부터 시작, k = 0
    visited = [False] * (n + 2)
    visited[0] = True

    while q:
        idx, cnt = q.popleft()
        if idx == n + 1:
            return True
        if cnt > k:
            continue
        for i in range(1, n + 2):
            if cnt <= k and not visited[i]:
                if dist[idx][i] <= cost:
                    visited[i] = True
                    q.append((i, cnt + 1))

    return False


n, k = map(int, input().split())

graph = [[0, 0]] + [list(map(int, input().split()))
                    for _ in range(n)] + [[10000, 10000]]
ans = 0

dist = [[0] * (n + 2) for _ in range(n + 2)]

for i in range(n + 1):
    for j in range(i, n + 2):
        if i == j:
            dist[i][j] = float('inf')
        else:
            dist[i][j] = dist[j][i] = calc(graph[i], graph[j])

# 최소, 최대 연료통
pl, pr = 1, 1415

while pl <= pr:
    mid = (pl + pr) // 2
    cost = mid ** 2 * 100
    if bfs(0, 0):
        pr = mid - 1
        ans = mid
    else:
        pl = mid + 1

print(ans)