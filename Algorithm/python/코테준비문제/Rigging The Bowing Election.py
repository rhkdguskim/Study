# https://www.acmicpc.net/problem/1941
from pprint import pprint
from collections import deque

moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
table = []
for _ in range(5):
    table.append(list(input()))

count = 0
visited = [[False for _ in range(5)] for _ in range(5)]  # 방문 표시
route = dict()
def dfs(jersey, holstein, people):
    global count
    if holstein >= 4:
        return

    if holstein + jersey >= 7:
        if jersey > holstein:
            temp = sorted(people, key=lambda c: (c[0] + c[1] * 5))
            key = ''
            for p in temp:
                key += str(p[0] + p[1]*5)
            if key not in route:
                #print(char, temp)
                count += 1
                route[key] = True
            return
        return

    for p in people:
        y = p[0]
        x = p[1]
        for dy, dx in moves:
            ny = dy + y
            nx = dx + x
            if 5 > ny >= 0 and 5 > nx >= 0 and not visited[ny][nx]:  # 배열범위에 들어있는 경우 탐색
                visited[ny][nx] = True
                people.append((ny, nx))
                if table[ny][nx] == 'S':
                    dfs(jersey + 1, holstein, people)
                else:
                    dfs(jersey, holstein + 1, people)
                visited[ny][nx] = False
                people.pop()


for i in range(5):
    for j in range(5):
        visited[i][j] = True
        people = []
        people.append((i, j))
        if table[i][j] == 'S':
            dfs(1, 0, people)
        else:
            dfs(0, 1, people)
        visited[i][j] = False

print(count)
