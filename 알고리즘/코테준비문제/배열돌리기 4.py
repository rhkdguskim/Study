# https://www.acmicpc.net/problem/17406
from itertools import permutations
from copy import deepcopy
from pprint import pprint
def rotate(x1, y1, x2, y2, table):
    #pprint(table)
    temp1 = table[y1][x1]  # 왼위
    temp2 = table[y1][x2]  # 오른위
    temp3 = table[y2][x1]  # 왼아래
    temp4 = table[y2][x2]  # 오른아래

    # 오른쪽으로 움직임
    for t in range(x2-1, x1-1, -1):
        table[y1][t+1] = table[y1][t]

    # 아래로 움직임
    for t in range(y2-1, y1-1, -1):
        if t == y1:
            table[t+1][x2] = temp2
        else:
            table[t+1][x2] = table[t][x2]

    # 왼쪽으로 움직임
    for t in range(x1+1, x2+1):
        if x2 == t:
            table[y2][t-1] = temp4
        else:
            table[y2][t-1] = table[y2][t]

    # 위로 움직임
    for t in range(y1+1, y2+1):
        if t == y2:
            table[t-1][x1] = temp3
        else:
            table[t-1][x1] = table[t][x1]


    #pprint(table)
    return table

def total(table):
    ans = 1000000000
    for i in range(1, len(table)):
        total = sum(table[i])
        ans = min(total, ans)

    return ans

N, M, K = map(int, input().split()) # 행, 열, 연산수
table = [[0 for _ in range(M+1)] for _ in range(N+1)]
for i in range(1, N+1):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        table[i][j+1] = temp[j]

ops = []
for _ in range(K):
    r, c, s = map(int, input().split())
    ops.append([r,c,s])

minresult = 100 * 50
def dfs(table, visited):
    global minresult
    if all(visited):
        #print(visited)
        minresult = min(total(table), minresult)
        #print(minresult)
        return

    for i in range(len(ops)):
        newtable = deepcopy(table)
        if not visited[i]:
            temp = ops[i][2]
            while temp >= 1:
                y1, x1 = ops[i][0] - temp, ops[i][1] - temp
                y2, x2 = ops[i][0] + temp, ops[i][1] + temp
                newtable = rotate(x1, y1, x2, y2, newtable)
                temp -= 1

            visited[i] = True
            dfs(newtable, visited)
            visited[i] = False

visited = [False for _ in range(len(ops))]
dfs(table, visited)

print(minresult)