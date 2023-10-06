# https://www.acmicpc.net/problem/17136
from copy import deepcopy
from pprint import pprint
table = []
cnt = 0
for _ in range(10):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        if temp[j] == 1:
            cnt += 1

    table.append(temp)

# table에 (1x1, 2x2, 3x3, 4x4, 5x5) 순열로 반복해서 붙혀보면서 문제를 해결한다.
# 1의 개수를 카운팅한다. dfs로 모든 경우의수를 구하고 색종이를 붙혀볼때 1을 카운팅하여 1의 개수가 0이 완성이 된다면 최소값이 된다.
# dfs 종료조건 1의 개수가 0이 되었을때 혹은 가능한 모든 색종이를 다 붙혀보았을때
def dfs(table, visited, cnt):
    total = sumvisited(visited)

    global maxvalue
    if cnt == 0: # 모든 색종이를 붙혔을때
        maxvalue = max(total, maxvalue)
        return

    if total == 25: # 모든 색종이를 사용했음.
        return

    for i in range(10):
        for j in range(10):
            for s in range(1, 6): # 가능한 색종이 (1x1 ... 5x5)
                newtable = deepcopy(table)
                result = canattach(s, i, j, newtable)
                if table[i][j] == 1 and 5 > visited[s] and result > 0:
                    visited[s] += 1
                    dfs(newtable, visited, cnt - result)
                    visited[s] -= 1


def canattach(size, i, j, table):
    for y in range(i, i+size):
        for x in range(j, j+size):
            if y >= 10 or x >= 10 or table[y][x] == 0:
                return 0
    for y in range(i, i+size):
        for x in range(j, j+size):
            table[y][x] = 0
    return size * size

def sumvisited(visited):
    return sum(visited)

visited = [0] * 6
maxvalue = 0
dfs(table, visited, cnt)
print(maxvalue)