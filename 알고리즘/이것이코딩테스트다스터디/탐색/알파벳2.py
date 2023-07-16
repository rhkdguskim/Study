R, C = map(int, input().split())

board = [input() for _ in range(R)]
max_count = 0

def dfs(i, j, count, visited):
    global max_count
    max_count = max(max_count, count)

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dx, dy in directions:
        nx, ny = i + dx, j + dy
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in visited:
            dfs(nx, ny, count + 1, visited + board[nx][ny])

dfs(0, 0, 1, board[0][0])
print(max_count)