# https://www.acmicpc.net/problem/9663
from copy import deepcopy
N = int(input())
table = [[False for _ in range(N)] for _ in range(N)]
move = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
cnt = 0
def dfs(queue, col):
    global cnt

    if len(queue) == N: # N개의 퀸이 방문했다면 모두 방문한것
        cnt += 1
        return

    for j in range(N):
        if is_valid(queue, col, j):
            queue.append((col, j))
            dfs(queue, col + 1)
            queue.pop()
def is_valid(queue, i, j):
    for y, x in queue:
        # 세로가 같은경우
        if i == y:
            return False
        # 가로가 같은경우
        if j == x:
            return False

        # 대각선이 같은경우
        # 우상향, 좌상향
        if y - i == x - j or y - i == -(x - j):
            return False

    return True


dfs([], 0)
print(cnt)