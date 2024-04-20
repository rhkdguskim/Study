# https://www.acmicpc.net/problem/1189
import sys
si = sys.stdin.readline
R, C, K = map(int, si().split())
move = ((0, 1), (0, -1), (1, 0), (-1, 0))
graph = [ si().strip() for _ in range(R)]

s_y = R-1
s_x = 0

e_y = 0
e_x = C-1

visit = dict()

ans = 0
def dfs(i,j, visited):
    global ans
    if i == e_y and j == e_x:
        if len(visited) == K:
            char = ''
            for y, x in sorted(visited):
                temp = y * R + x
                char += str(temp)

            if char not in visit:
                ans += 1
                visit[char] = True

        return

    for dy, dx in move:
        ny, nx = dy + i, dx + j
        if R > ny >=0 and C >nx >=0 and (ny, nx) not in visited and graph[ny][nx] != 'T':
            visited.append((ny, nx))
            dfs(ny, nx, visited)
            visited.pop()

dfs(s_y, s_x, [(s_y, s_x)])
print(ans)