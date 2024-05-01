# https://school.programmers.co.kr/learn/courses/30/lessons/87694

# 태두리의 그래프를 구한다.
# 1. 사각형 내의 좌표를 모두 방문처리 한다.
# 2. 방문하는데 상하좌우가 모두 방문처리된 곳이면 테두리 안쪽임으로 무시한다.
# 3. 테두리를 BFS 방문해가면서 최단 경로를 구한다.
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[False]*101 for _ in range(101)]

    for x1, y1, x2, y2 in rectangle:
        for y in range(y1*2, y2*2 + 1):
            for x in range(x1*2, x2*2 + 1):
                graph[y][x] = True

    def is_border(y, x):
        # 8개 주변에 칸이 모두 차있다면 테두리가 아니다.
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        visited = [False] * len(moves)
        for i, m in enumerate(moves):
            ny, nx = m[0] + y, m[1] + x
            if 101 > ny >= 0 and 101 > nx >= 0 and graph[ny][nx]:
                visited[i] = True

        return not all(visited)

    def bfs():
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False] * 101 for _ in range(101)]
        visited[characterY*2][characterX*2] = True
        queue = deque()
        queue.append((characterY*2, characterX*2, 0))
        while queue:
            i, j, cost = queue.popleft()
            print(i, j, cost)
            if itemY*2 == i and itemX*2 == j:
                return cost//2

            for dy, dx in moves:
                ny, nx = dy + i, dx + j
                if 0 <= ny < 101 and 0 <= nx < 101 and graph[ny][nx] and is_border(ny, nx) and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny, nx, cost + 1))

        return -1

    return bfs()

solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8)