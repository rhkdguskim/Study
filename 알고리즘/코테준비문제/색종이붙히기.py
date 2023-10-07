# https://www.acmicpc.net/problem/17136
import sys
sys.setrecursionlimit(10**6)

table = []
for _ in range(10):
    temp = list(map(int, input().split()))
    table.append(temp)

remain = [5 for _ in range(6)]
def check(i,j, size):
    for y in range(i, i+size):
        for x in range(j, j+size):
            if table[y][x] == 0: # 색종이를 붙힐 수 없음
                return False

    return True # 색종이를 붙힐 수 있음.
def visit(i,j, size):
    for y in range(i, i+size):
        for x in range(j, j+size):
            table[y][x] = 0

def unvisit(i,j, size):
    for y in range(i, i+size):
        for x in range(j, j+size):
            table[y][x] = 1

minvalue = 25
def dfs(i,j, cnt):
    global minvalue, remain, table
    if i >= 10: # 모든경우를 탐색했을경우
        minvalue = min(cnt, minvalue)
        return
    if j >= 10: # x의 범위가 10이상으로 넘어가면 다시 y를 +1 하여 탐색한다.
        dfs(i+1,0, cnt)
        return

    if table[i][j] == 1: # 색종이를 붙힐 수 있다면
        for s in range(1,6): # 1~5의 색종이 사이즈를 다 붙혀본다.
            if remain[s] == 0:
                continue
            if i+s > 10 or j+s > 10:
                continue

            if not check(i,j,s):
                break

            remain[s] -= 1
            visit(i, j, s)
            dfs(i, j+s, cnt+1)
            remain[s] += 1
            unvisit(i, j, s)
    else: # 색종이를 붙힐 수 없다면 다음칸을 탐색해본다.
        dfs(i ,j+1, cnt)

dfs(0,0,0)
print(-1 if minvalue == 25 else minvalue)