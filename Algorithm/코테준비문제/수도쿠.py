# https://www.acmicpc.net/problem/2239
def getavailable(i, j):
    h, w = getpos(i,j)
    temp = {1,2,3,4,5,6,7,8,9} # 놓을 수 있는 수.

    for k in range(h, h+3): # 3x3 정사각형
        for n in range(w, w+3):
            if table[k][n] in temp:
                temp.remove(table[k][n])

    for t in range(9): # 가로, 세로
        n1 = table[i][t]
        n2 = table[t][j]
        if n1 in temp:
            temp.remove(n1)

        if n2 in temp:
            temp.remove(n2)

    return temp # 현재 위치에서 놓을 수 있는 경우의 수

# 현재위치에서 정사각형을 찾기위한 함수
def getpos(i, j):
    h, w = 0, 0
    if 3 > i >= 0:
        h = 0
    elif 6 > i >= 3:
        h = 3
    elif 9 > i >= 6:
        h = 6

    if 3 > j >= 0:
        w = 0
    elif 6 > j >= 3:
        w = 3
    elif 9 > j >= 6:
        w = 6

    return h, w

table = [[0 for _ in range(9)] for _ in range(9)]

cnt = 0
for i in range(9):
    temp = list(input())
    for j in range(len(temp)):
        num = int(temp[j])
        if num == 0: # 놓을 수 있는 숫자의 수 ( 숫자를 다 놓았는지 놓지 않았는지 판별 )
            cnt += 1
        table[i][j] = num


def dfs(index, depth):
    global end
    if end: # 스토쿠를 찾은경우 모든 경우의수를 백트래킹 한다.
        return

    if depth == cnt: # 숫자를 모두 넣어본경우
        for result in table:
            char = ''
            for a in result:
                char += str(a)
            end = True
            print(char)
        return

    y = index // 9
    x = index % 9

    if table[y][x] == 0: # 숫자를 넣을 수 있는 후보라면
        nums = getavailable(y,x) # 후보의 경우의수를 구한다.
        if not nums: # 경우의 수가 없다면 백트래킹
            return

        for n in nums: # 경우를 하나씩 방문해간다. ( 조합 )
            table[y][x] = n
            dfs(index +1, depth+1)
            table[y][x] = 0
    else:
        dfs(index+1, depth) # 넣을 수 없는 후보라면 다음 후보를 탐색한다.

end = False
dfs(0,0)